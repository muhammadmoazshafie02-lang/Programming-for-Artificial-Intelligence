marks=int(input("Enter your Marks in PAI between 0 and 100: "))
if 0<= marks <=100:
    if marks>=90:
        print("Grade A")
    elif marks>=80:
        print("Grade B")
    elif marks>=70:
        print("Grade C")
    else:
        print("Fail")
else:
    print("Invalid Marks")