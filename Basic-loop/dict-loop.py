phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for value in phone_numbers.keys():
    print(value)

for value in phone_numbers.values():
    print(value)

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

for value in phone_numbers.values():
    print(value.replace("+", "00"))