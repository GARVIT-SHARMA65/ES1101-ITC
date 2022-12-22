#ASSIGNMENT1
#QUES1
print("QUES1")
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
average=(n1+n2+n3)/3
print("average of 3 nos is",average)

#QUES2
print("QUES2")
gross_income=int(input("gross income is:"))
no_of_dependents=int(input("number of dependents are:"))
rate=0.20
standard_deduction=10000
additional_deduction=3000
taxable_income=gross_income-standard_deduction-(additional_deduction*no_of_dependents)
TAX=taxable_income*rate
print("total tax is:",TAX)

#QUES3
print("QUES3")
second=int(input("the total seconds are"))
minutes=second//60
seconds=second%60
print("the number of minutes are:",minutes)
print("the number of seconds are :",seconds)

#QUES4
print("QUES4")
num1=int(input("enter num1:"))
num2=float(input("enter num2:"))
num3=input("enter num3:")
num4=num1+num2+int(num3)
print("the sum of the nos is:",num4)


#QUES5
print("QUES5")
import math
a=0
while a<=345:
    print(math.sin(math.radians(a)),math.cos(math.radians(a)))
    a=a+15
