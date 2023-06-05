set1 = {11, 20, 3, 21,23}
set2 = {11, 21}

print("set1: ",set1)
print("set2: ",set2)

set1.add(4)
print("set1 after add:",set1)

set1.discard(21)
print("set1 after discard:",set1)


print("union:", set1 | set2)
print("intersection:", set1 & set2)
print("difference:", set1 - set2)
print("symmetric difference:", set1 ^ set2)

print("set1 after clear opration:")
set1.clear()
print(set1)