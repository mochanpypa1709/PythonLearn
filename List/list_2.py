#if else condition
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

#if else condition 2
def foo(lst):
    return [i if isinstance(i, int) else 0 for i in lst]

print(foo([99, 'no data', 95, 94, 'no data']))

#convert and sum up
def foo(lst):
    return sum([float(i) for i in lst])

print(foo(['1.2', '2.6', '3.3']))