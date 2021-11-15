def printTable(tableData):
    columnWidth = [0]*len(tableData)
    num_entries = len(tableData[0])
    temp_length = [0]*num_entries
    for i in range(len(columnWidth)):
        for j in range(num_entries):
            temp_length[j] = len(tableData[i][j])
        columnWidth[i] = max(temp_length)
    #print(columnWidth)

    for word in range(num_entries):
        for item in range(len(columnWidth)):
            print(tableData[item][word].rjust(columnWidth[item]), end=' ')
        print()
        
tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]
printTable(tableData)