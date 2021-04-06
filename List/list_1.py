temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

#function list comprehensive
def foo(lst):
    return [i for i in lst if  isinstance(i, int)]

print(foo([99, 'no data', 95, 94, 'no data']))


