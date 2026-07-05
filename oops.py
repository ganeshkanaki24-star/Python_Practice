# inherintance 
class Bank:                                                                                                                                 
    def interest(self):
        print("Bank interest is 4%")

class SBI(Bank):
    def interest(self):
        print("SBI interest is 6%")

class HDFC(Bank):
    def interest(self):
        print("HDFC interest is 7%")

b1 = SBI()
b2 = HDFC()

# call methods to see output
if __name__ == "__main__":
    b1.interest()
    b2.interest()

