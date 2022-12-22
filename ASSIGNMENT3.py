#QUES4
# grade=float(input("Enter grade points"))
x=0
if grade==10:
        x="A+"
elif grade>=9:
        x="A"
elif grade>=8:
        x="B+"
elif grade>=7:
        x="B"
elif grade>=6:
        x="c+"
elif grade>=5:
        x="c"
elif grade>=4:
        x="D"
else:
        x="Very Poor Performance"
print(x)

#QUES1
count=0
word=str(input("Enter the line"))
letter=str(input("Enter the alphabet "))
for i in word:
    if i == letter:
        count=count+1
print(count)
