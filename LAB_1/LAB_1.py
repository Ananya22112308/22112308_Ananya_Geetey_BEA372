file=open("C:/Users/geete/OneDrive/Desktop/CU/22112308_Ananya_Geetey_BEA372/LAB_1/bank.csv",'r')
header=file.readline()
data=file.readlines()
print(header)
#Find the count of customers in each category 'marital'.
marital=[]
count=0
for items in data:
    for lines in items:
        count=count+lines
print(count)