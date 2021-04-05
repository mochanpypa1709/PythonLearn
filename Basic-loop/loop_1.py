monday_temperatures = [9.1, 8.8, 7.6]
colors = [11, 34, 98, 43, 45, 54, 54]

for temp in monday_temperatures:
    print(round(temp))

for letter in 'hello':
    print(letter.title())

for warna in colors:
    if warna > 50:
        print(warna)

colors2 = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for warna in colors2:
    if type(warna) == int:
        print(warna)
