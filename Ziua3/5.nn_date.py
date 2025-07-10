

date = {
    "Alina" : [60, 165, True],
    "Bogdan" : [72, 183, False],
    "Ciprian" : [69, 178, False],
    "Diana" : [55, 152, True]
}

print(date.values())

inputs = [((i[0] - 61), (i[0] - 168)) for i in date.values()]
print(inputs)

outputs = [int(i[2]) for i in date.values()]
print(outputs)