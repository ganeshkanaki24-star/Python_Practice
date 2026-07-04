# generator 
def squares(n):
    for i in range(1 , n + 1):
        yield i * i

gen = squares(5)
print(next(gen))
print(next(gen))
print(next(gen))

# factorial using generator
def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

fact_gen = factorial_generator(5)
for value in fact_gen:
    print(value)


# prime number using generator 
