import threading
class NumberThread(threading.Thread):
    def run(self):
        for i in range(1, 6):
            print(i)

t1 = NumberThread()
t1.start()
print("Thread Run")