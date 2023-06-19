file=open("C:/Users/geete/OneDrive/Desktop/CU/22112308_Ananya_Geetey_BEA372/LAB_1/bank.csv",'r')
header=file.readline()
data=file.readlines()
print(header.replace('"',''))
#Find the count of customers in each category 'marital'.

def marital():
    married=0
    single=0

    for item in data:
        count=item.split(";")
        marital=count[2].strip('"')
        if marital=="married":
            married+=1
        else:
            single+=1
    print("count of married people is",married)
    print("count of single people is",single)

marital()
def age():
    age=0

    for item in data:
        count=item.split(";")
        age=int(count[0].strip('"'))
        age+=1
    print("count of age is",age)
age()

def categorize():
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    for item in data:
        count=item.split(";")
        age=int(count[0].strip('"'))
        if age<25:
            count1+=1
        elif age<35:
            count2+=1
        elif age<45:
            count3+=1
        elif age<55:
            count4+=1
        elif age<65:
            count5+=1
        else:
            count6+=1
    print(count1, count2, count3, count4,count5,count6)
    print("(0 to 25)","*"*count1,count1)
    print("(25 to 35)","*"*count2,count2)
    print("(35 to 45)","*"*count3,count3)
    print("(45 to 55)","*"*count4,count4)
    print("(55 to 65)","*"*count5,count5)
    print("(65 to 80)","*"*count6,count6)
categorize()
            





