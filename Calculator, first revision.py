import math
while (True):
    Sign = input("Select a sign, +, -, *, /, ^, SqrRt, CbRt. " )
    if Sign == "+":
        AddNo1 = input("1st Number: ")
        AddNo2 = input("2nd Number: ")
        print("The sum is: " + str(float(AddNo1) + float(AddNo2)))
        Ans = float(AddNo1) + float(AddNo2)
    if Sign == "-":
        SubNo1 = input("1st Number: ")
        SubNo2 = input("2nd Number: ")
        print("The difference is: " + str(float(SubNo1) - float(SubNo2)))
        Ans = float(SubNo1) - float(SubNo2)
    if Sign == "*":
        MultNo1 = input("1st Number: ")
        MultNo2 = input("2nd Number: ")
        print("The product is: " + str(float(MultNo1) * float(MultNo2)))
        Ans = float(MultNo1) * float(MultNo2)
    if Sign == "/":
        DivNo1 = input("1st Number: ")
        DivNo2 = input("2nd Number: ")
        print("The quotient is: " + str(float(DivNo1) / float(DivNo2)))
        Ans = float(DivNo1) / float(DivNo2)
    if Sign == "^":
            SqrNo1 = input("Number: ")
            SqrNo2 = input("power: ")
            print("The product is: " + str(float(SqrNo1) ** float(SqrNo2)))
            Ans = float(SqrNo1) ** float(SqrNo2)
    if Sign == "SqrRt":
            SqrRtNo1 = input("Number: ")
            print("The square root is: " + str(math.sqrt(float(SqrRtNo1))))
            Ans = math.sqrt(float(SqrRtNo1))
    if Sign == "CbRt":
                CbRtNo1 = input("Number: ")
                print("The cube root is: " + str(math.cbrt(float(CbRtNo1))))
                Ans = math.cbrt(float(CbRtNo1))
    


