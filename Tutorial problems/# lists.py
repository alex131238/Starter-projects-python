# lists
Names = ['Alex', 'Tanya', 'Artemis', 'Dragonborn', 'Bingus', 'Floppa']
Numbers = [2, 3, 5, 19 ,2100, 12, 43, 80, 900]
# using indexing

# print(Names[1])
# print(Names[2:])

# using index to modify

# Names[0] = 'L' 
# print(Names)

# Largest_number = len(Names)
# print(Names[Largest_number - 1])

Max = Numbers[0]

for number in Numbers:
    if number > Max:
        Max = number
print(Max)
