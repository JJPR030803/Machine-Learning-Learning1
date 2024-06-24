import csv
with open("Dataset\Online Sales Data.csv","r") as file:
    listaDatos = []
    reader = csv.reader(file)
    for row in reader:
        listaDatos.append(row)
    first_column = [columna[0] for columna in listaDatos]
    
    for value in first_column:
        print(value)
        
        
    #for index,value in enumerate(listaDatos):
     #   print(listaDatos[index][0])    newRow = row.split(",")
        

        