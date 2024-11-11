from processingTables.processingTable import ProcessingTable

table = ProcessingTable()
table.processCallback(lambda x: print(x))

size = 85
result = table.processTable(size)

print(result)
