import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import sqlite3
import os

import pandas as pd
import numpy as np


class StudentResultAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Student Result Analyzer")
        self.root.geometry("1100x650")

        self.df = None
        self.analyzed_df = None
        self.db_path = "results.db"

        self._build_ui()
        self._init_db()

    # -------------------- UI --------------------
    def _build_ui(self):
        # Top frame (Buttons)
        top = tk.Frame(self.root, padx=10, pady=10)
        top.pack(fill="x")

        tk.Button(top, text="Import CSV/Excel", width=18, command=self.import_file).pack(side="left", padx=5)
        tk.Button(top, text="Analyze", width=12, command=self.analyze_threaded).pack(side="left", padx=5)
        tk.Button(top, text="Save to DB", width=12, command=self.save_to_db).pack(side="left", padx=5)
        tk.Button(top, text="Export Report", width=14, command=self.export_report).pack(side="left", padx=5)

        # Search section
        tk.Label(top, text="Search (Roll/Name):").pack(side="left", padx=(20, 5))
        self.search_var = tk.StringVar()
        tk.Entry(top, textvariable=self.search_var, width=25).pack(side="left")
        tk.Button(top, text="Search DB", width=10, command=self.search_db).pack(side="left", padx=5)
        tk.Button(top, text="Show All DB", width=12, command=self.show_all_db).pack(side="left", padx=5)

        # Status label
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(self.root, textvariable=self.status_var, anchor="w", fg="blue", padx=10).pack(fill="x")

        # Table frame
        table_frame = tk.Frame(self.root, padx=10, pady=10)
        table_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(table_frame, show="headings")
        self.tree.pack(side="left", fill="both", expand=True)

        scroll_y = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scroll_y.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scroll_y.set)

        # Summary frame
        summary = tk.LabelFrame(self.root, text="Summary", padx=10, pady=10)
        summary.pack(fill="x", padx=10, pady=(0, 10))

        self.summary_var = tk.StringVar(value="Import a file to see summary.")
        tk.Label(summary, textvariable=self.summary_var, anchor="w").pack(fill="x")

    # -------------------- DB --------------------
    def _init_db(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS student_result (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_no TEXT,
                    name TEXT,
                    total REAL,
                    percentage REAL,
                    grade TEXT
                )
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    # -------------------- Import --------------------
    def import_file(self):
        file_path = filedialog.askopenfilename(
            title="Select CSV/Excel File",
            filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        try:
            self.status_var.set("Loading file...")
            self.root.update_idletasks()

            ext = os.path.splitext(file_path)[1].lower()

            if ext == ".csv":
                self.df = pd.read_csv(file_path)
            elif ext in [".xlsx", ".xls"]:
                self.df = pd.read_excel(file_path)  # requires openpyxl for .xlsx
            else:
                messagebox.showwarning("Invalid File", "Please select a CSV or Excel file.")
                return

            # Basic validation
            required_cols = {"RollNo", "Name"}
            if not required_cols.issubset(set(self.df.columns)):
                messagebox.showerror(
                    "Wrong Format",
                    "File must contain columns: RollNo, Name and subject columns like Python, DBMS, CN etc."
                )
                return

            self.analyzed_df = None
            self._show_dataframe(self.df.head(30))
            self.summary_var.set("File imported successfully. Click Analyze.")
            self.status_var.set("File imported: " + os.path.basename(file_path))

        except Exception as e:
            messagebox.showerror("Import Error", str(e))
            self.status_var.set("Ready")

    # -------------------- Analyze (Threaded) --------------------
    def analyze_threaded(self):
        if self.df is None or self.df.empty:
            messagebox.showwarning("No Data", "Please import a CSV/Excel file first.")
            return

        t = threading.Thread(target=self.analyze_data, daemon=True)
        t.start()

    def analyze_data(self):
        try:
            self.status_var.set("Analyzing data (thread running)...")
            self.root.update_idletasks()

            df = self.df.copy()

            # Identify subject columns (everything except RollNo and Name)
            subject_cols = [c for c in df.columns if c not in ["RollNo", "Name"]]

            if len(subject_cols) == 0:
                messagebox.showerror("Error", "No subject columns found. Add subject marks columns.")
                self.status_var.set("Ready")
                return

            # Convert marks to numeric safely
            for c in subject_cols:
                df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

            marks_matrix = df[subject_cols].to_numpy(dtype=float)  # NumPy array

            totals = np.sum(marks_matrix, axis=1)
            avg = np.mean(marks_matrix, axis=1)
            percentage = (totals / (len(subject_cols) * 100.0)) * 100.0

            # Grade function
            def grade(p):
                if p >= 85:
                    return "A"
                elif p >= 70:
                    return "B"
                elif p >= 55:
                    return "C"
                elif p >= 40:
                    return "D"
                else:
                    return "Fail"

            grades = [grade(p) for p in percentage]

            df["Total"] = np.round(totals, 2)
            df["Average"] = np.round(avg, 2)
            df["Percentage"] = np.round(percentage, 2)
            df["Grade"] = grades

            self.analyzed_df = df

            # Update GUI from main thread
            self.root.after(0, lambda: self._show_dataframe(self.analyzed_df.head(50)))
            self.root.after(0, lambda: self._update_summary(self.analyzed_df))

            self.status_var.set("Analysis completed successfully.")

        except Exception as e:
            self.status_var.set("Ready")
            messagebox.showerror("Analyze Error", str(e))

    def _update_summary(self, df):
        try:
            class_avg = df["Percentage"].mean()
            highest = df["Percentage"].max()
            pass_count = (df["Grade"] != "Fail").sum()
            fail_count = (df["Grade"] == "Fail").sum()

            topper_row = df.loc[df["Percentage"].idxmax()]
            topper_name = topper_row["Name"]
            topper_roll = topper_row["RollNo"]

            self.summary_var.set(
                f"Class Avg %: {class_avg:.2f} | Highest %: {highest:.2f} | Pass: {pass_count} | Fail: {fail_count} "
                f"| Topper: {topper_name} (Roll: {topper_roll})"
            )
        except Exception:
            self.summary_var.set("Summary not available.")

    # -------------------- Show DataFrame in Treeview --------------------
    def _show_dataframe(self, df):
        # clear
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        # insert rows
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row.values))

    # -------------------- Save to DB --------------------
    def save_to_db(self):
        if self.analyzed_df is None:
            messagebox.showwarning("Not Analyzed", "Please analyze data before saving to DB.")
            return

        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()

            # Insert each row
            for _, r in self.analyzed_df.iterrows():
                cur.execute("""
                    INSERT INTO student_result (roll_no, name, total, percentage, grade)
                    VALUES (?, ?, ?, ?, ?)
                """, (str(r["RollNo"]), str(r["Name"]), float(r["Total"]), float(r["Percentage"]), str(r["Grade"])))

            conn.commit()
            conn.close()

            messagebox.showinfo("Saved", "Results saved to database successfully!")
            self.status_var.set("Saved to DB.")

        except Exception as e:
            messagebox.showerror("DB Save Error", str(e))

    # -------------------- Search / Show All --------------------
    def search_db(self):
        key = self.search_var.get().strip()
        if not key:
            messagebox.showwarning("Empty", "Enter RollNo or Name to search.")
            return

        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute("""
                SELECT roll_no, name, total, percentage, grade
                FROM student_result
                WHERE roll_no LIKE ? OR name LIKE ?
                ORDER BY percentage DESC
            """, (f"%{key}%", f"%{key}%"))

            rows = cur.fetchall()
            conn.close()

            if not rows:
                messagebox.showinfo("No Results", "No matching student found in DB.")
                return

            df = pd.DataFrame(rows, columns=["RollNo", "Name", "Total", "Percentage", "Grade"])
            self._show_dataframe(df)
            self.summary_var.set(f"Found {len(df)} record(s) from DB for '{key}'.")
            self.status_var.set("Search completed.")

        except Exception as e:
            messagebox.showerror("Search Error", str(e))

    def show_all_db(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute("""
                SELECT roll_no, name, total, percentage, grade
                FROM student_result
                ORDER BY percentage DESC
            """)
            rows = cur.fetchall()
            conn.close()

            if not rows:
                messagebox.showinfo("Empty DB", "No records in database yet.")
                return

            df = pd.DataFrame(rows, columns=["RollNo", "Name", "Total", "Percentage", "Grade"])
            self._show_dataframe(df)
            self.summary_var.set(f"Total DB records: {len(df)} (sorted by Percentage).")
            self.status_var.set("Showing all DB records.")

        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    # -------------------- Export --------------------
    def export_report(self):
        if self.analyzed_df is None:
            messagebox.showwarning("Not Analyzed", "Analyze data first, then export.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            title="Save Report As"
        )
        if not save_path:
            return

        try:
            self.analyzed_df.to_csv(save_path, index=False)
            messagebox.showinfo("Exported", f"Report exported successfully:\n{save_path}")
            self.status_var.set("Report exported.")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentResultAnalyzer(root)
    root.mainloop()
