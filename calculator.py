Sign = input("Select a sign, Addition = 1, Subtraction = 2, Multiplication = 3, Division = 4. " )
if Sign == "1":
    AddNo1 = input("1st Number: ")
    AddNo2 = input("2nd Number: ")
    print("The sum is: " + str(float(AddNo1) + float(AddNo2)))
if Sign == "2":
    SubNo1 = input("1st Number: ")
    SubNo2 = input("2nd Number: ")
    print("The difference is: " + str(float(SubNo1) - float(SubNo2)))
if Sign == "3":
    MultNo1 = input("1st Number: ")
    MultNo2 = input("2nd Number: ")
    print("The product is: " + str(float(MultNo1) * float(MultNo2)))
if Sign == "4":
    DivNo1 = input("1st Number: ")
    DivNo2 = input("2nd Number: ")
    print("The quotient is: " + str(float(DivNo1) / float(DivNo2)))