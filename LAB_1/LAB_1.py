file=open("C:/Users/geete/OneDrive/Desktop/CU/22112308_Ananya_Geetey_BEA372/LAB_1/bank.csv",'r')
header=file.readline()
data=file.readlines()
print(header)
#Find the count of customers in each category 'marital'.
married=0
single=0
for item in data:
    count=item.split(";")
    marital=count[2].strip('"')
    if marital=="married":
        married+=1
    else:
        single+=1

print(married)
print(single)