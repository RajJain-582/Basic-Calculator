import math
while (True):
    Sign = input("Select a sign, +, -, *, /, ^, SqrRt, CbRt. " )
    if Sign == "+":
        AddNo1 = input("1st Number: ")
        AddNo2 = input("2nd Number: ")
        if AddNo1 == "Ans":
            AddNo1 = Ans
        if AddNo2 == "Ans":
            AddNo2 = Ans
        print("The sum is: " + str(float(AddNo1) + float(AddNo2)))
        Ans = float(AddNo1) + float(AddNo2)
    if Sign == "-":
        SubNo1 = input("1st Number: ")
        SubNo2 = input("2nd Number: ")
        if SubNo1 == "Ans":
            SubNo1 = Ans
        if SubNo2 == "Ans":
            SubNo2 = Ans
        print("The difference is: " + str(float(SubNo1) - float(SubNo2)))
        Ans = float(SubNo1) - float(SubNo2)
    if Sign == "*":
        MultNo1 = input("1st Number: ")
        MultNo2 = input("2nd Number: ")
        if MultNo1 == "Ans":
            MultNo1 = Ans
        if MultNo2 == "Ans":
            MultNo2 = Ans
        print("The product is: " + str(float(MultNo1) * float(MultNo2)))
        Ans = float(MultNo1) * float(MultNo2)
    if Sign == "/":
        DivNo1 = input("1st Number: ")
        DivNo2 = input("2nd Number: ")
        if DivNo1 == "Ans":
            DivNo1 = Ans
        if DivNo2 == "Ans":
            DivNo2 = Ans
        print("The quotient is: " + str(float(DivNo1) / float(DivNo2)))
        Ans = float(DivNo1) / float(DivNo2)
    if Sign == "^":
        SqrNo1 = input("Number: ")
        SqrNo2 = input("power: ")
        if SqrNo1 == "Ans":
            SqrNo1 = Ans
        if SqrNo2 == "Ans":
            SqrNo2 = Ans
        print("The product is: " + str(float(SqrNo1) ** float(SqrNo2)))
        Ans = float(SqrNo1) ** float(SqrNo2)
    if Sign == "SqrRt":
        SqrRtNo1 = input("Number: ")
        if SqrRtNo1 == "Ans":
            SqrRtNo1 = Ans
        print("The square root is: " + str(math.sqrt(float(SqrRtNo1))))
        Ans = math.sqrt(float(SqrRtNo1))
    if Sign == "CbRt":
        CbRtNo1 = input("Number: ")
        if CbRtNo1 == "Ans":
            CbRtNo1 = Ans
        print("The cube root is: " + str(math.cbrt(float(CbRtNo1))))
        Ans = math.cbrt(float(CbRtNo1))
    


