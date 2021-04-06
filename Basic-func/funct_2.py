#two arguments
def area(a, b):
    return a * b

print(area(4,5))

#multiple argument
def mean(*args):
    return sum(args) / len(args)

print(mean(2,4,5))