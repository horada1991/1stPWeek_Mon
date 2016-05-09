doors = [0]*100
j = 1
while j <= 100:
    i = 0
    while i < len(doors):
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0
        i += j
    j += 1

OpenedDoors = []
for i in range(len(doors)):
    if doors[i] == 1:
        OpenedDoors.append(i)

print(", ".join(map(str, OpenedDoors)))
