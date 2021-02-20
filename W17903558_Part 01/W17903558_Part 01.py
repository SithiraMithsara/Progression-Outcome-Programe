print("Student's progression outcome prediction programme")

while True: #Pass_credit
        try:
            while True:
                pass_credit=int(input("Please enter your pass credit: \n"))
                if pass_credit%20!=0 or pass_credit<0 or pass_credit>=121:
                    print("Range Error")
                else:
                    break
        except ValueError:
            print("Integers required")
        else:
            break

while True:  #Deffer_credit
        try:
            while True:
                deff_credit=int(input("Please enter your deffer credit: \n"))
                if deff_credit%20!=0 or deff_credit<0 or deff_credit>=121:
                    print("Range Error")
                else:
                    break
        except ValueError:
            print("Integers required")
        else:
            break

while True:  #Fail_credit
        try:
            while True:
                fail_credit=int(input("Please enter your fail credit: \n"))
                if fail_credit%20!=0 or fail_credit<0 or fail_credit>=121:
                    print("Range Error")
                else:
                    break
        except ValueError:
            print("Integers required")
        else:
            break

#Progression_outcomes
if pass_credit+deff_credit+fail_credit != 120:
    print("Your total is incorrect...")

elif pass_credit==120 and deff_credit==0 and fail_credit==0:
        print("Progress")

elif pass_credit==100 and deff_credit<=20 and fail_credit<=20:
        print("Progress - module trailer")

elif pass_credit<=80 and deff_credit<=120 and fail_credit<=60:
        print("Do not Progress - module retriever")

elif pass_credit<=40 and deff_credit<=40 and fail_credit<=120:
        print("Exclude")
