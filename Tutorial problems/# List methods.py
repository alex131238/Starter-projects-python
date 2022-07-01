# List methods

from ast import Num
import numbers
from tokenize import Number


Numbers = [4, 3, 5, 12, 19, 20-3, 5, 8, 2020, 8, 3]
# Numbers.remove(2020)

# Numbers.append(20)
# LISTS ARE NOT IMMUTABLE THROUGH METHODS
# Numbers.pop()
# index = Numbers.index(5)
# print(Numbers)
# print(index)
# print(12 in Numbers)
# print(Numbers.count(5))
# Numbers.sort()
# Numbers.reverse()
# print(Numbers)
# Nubmers2 = numbers.copy()

for i in Numbers:
    duplicates = Numbers.count(i)
    if duplicates > 1:
        index = Numbers.index(i)
        Numbers.remove(Numbers[index])
print(Numbers)

# or 
no_duplicates = []
for number in Numbers:
    if number not in no_duplicates:
        no_duplicates.append(number)
print(no_duplicates)