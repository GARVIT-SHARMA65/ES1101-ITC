#ASSIGNMENT2

#QUES1
STRING="python is a case sensitive language"
#a
length=len(STRING)
print("length is:",length)
#b
print(STRING[::-1])
#c
print(STRING[10:27])
#d
string1=STRING.replace("a case sensitive","object oriented")
print(string1)
#e
string2=STRING.index("a")
print(string2)
#f
string3=STRING.replace(" ","")
print(string3)

#QUES2
name="GARVIT SHARMA"
Sid=22104065
department="electrical"
cgpa=9.9
string="Hey,{} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}".format(name,Sid,department,cgpa)
print(string)

#QUES3
a=56
b=10
#a
x=a&b
print(x)

#b
y=a|b
print(y)

#c
z=a^b
print(z)

#d
m=a<<2
n=b<<2
print(m)
print(n)

#e
o=a>>2
p=b>>4
print(o)
print(p)


#QUES4
A=int(input("enter 1st number:"))
B=int(input("enter 2nd number:"))
C=int(input("enter 3rd number:"))
greatest=max(A,B,C)
print("THE GREATEST OF THE THREE NUMBERS IS",greatest)

#QUES5
string=input("enter any string:")
if "name" in string:
    print("yes")
else:
    print("no")

#QUES6
s1=int(input("enter length of side1 :"))
s2=int(input("enter length of side2 :"))
s3=int(input("enter length of side3 :"))
if (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
          print(" ARE THE input lengths are the sides of triangle","YES")
else:
    print("ARE THE INPUT LENGTHS ARE THE SIDES OF TRIANGLE","NO")



