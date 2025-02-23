a=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]]
maps={}
for column in range(len(a[0])):
    for row in range(len(a)):
        if (row_column:=row+column) not in maps:
            maps[row_column]=[a[row][column]]
        else:
            maps[row_column].append(a[row][column])
print(maps)
