doors = [0]*100
j = 1
#Loop for increase steps
while j <= 100:
    i = j - 1
    #Loop for check doors and close or open them (closed = 0, opened = 1)
    while i < len(doors):
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0
        i += j
    j += 1

print(doors)
#Printing out the opened doors's numbers
OpenedDoors = []
for i in range(len(doors)):
    if doors[i] == 1:
        OpenedDoors.append(i+1)
print(", ".join(map(str, OpenedDoors)))
