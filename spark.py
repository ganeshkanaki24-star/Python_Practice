from pyspark.sql import SparkSession

# 1. Create SparkSession
spark = SparkSession.builder \
    .appName("EmployeeAnalysis") \
    .getOrCreate()

# 2. Create SQLContext ( not necessary)
#sqlContext = spark.sqlContext

# 3. Read CSV
#df = sqlContext.read.csv(
df = spark.read.csv(
    "employees.csv",
    header=True,
    inferSchema=True
)

# 4. Display DataFrame
df.show()

# 5. Display schema
df.printSchema()

# 6. DataFrame operation
df.select("name", "salary").show()

# 7. Filter
df.filter(df.salary > 45000).show()

# 8. Create temporary SQL view
df.createOrReplaceTempView("employees")

# 9. SQL query
result = spark.sql("""
    SELECT name, department, salary
    FROM employees
    WHERE salary > 45000
""")

result.show()

# 10. Aggregation
summary = spark.sql("""
    SELECT department,
           COUNT(*) AS employee_count,
           AVG(salary) AS average_salary,
           MAX(salary) AS maximum_salary
    FROM employees
    GROUP BY department
""")

summary.show()

# 11. Save result
summary.toPandas().to_csv(
    "employee_summary.csv",
    index=False
)
