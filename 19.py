import csv
lista=[]
f1=open("Holidays_2024.csv","r")
info1=csv.reader(f1)
for line in info1:
    lista.append(line)

date1=[]
day1=[]
holiday1=[]
state1=[]
len1=len(lista)
for i in range (0,len1,1):
    
    date1.append(lista[i][0])
    day1.append(lista[i][1])
    holiday1.append(lista[i][2])
    state1.append(lista[i][3].replace("\n","").replace("&",","))
for i in range(0,len1,1):
    if(state1[i]=="KA"):
        print(date1[i],day1[i],holiday1[i],"is a holiday for Karnataka")

    
