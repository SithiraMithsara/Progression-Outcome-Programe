print("Student's progression outcome prediction programme")

progress=0
trailing=0
retriever=0
excluded=0
total_count=0

while True:             #used to run the programme until the user wants to quit
    total_count=total_count+1
    while True:          
        while True:     #Pass_credit
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

        while True:     #Deffer_credit
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

        while True:
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
            progress=progress+1

        elif pass_credit==100 and deff_credit<=20 and fail_credit<=20:
            print("Progress - module trailer")
            trailing=trailing+1

        elif pass_credit<=80 and deff_credit<=120 and fail_credit<=60:
            print("Do not progress - module retriever")
            retriever=retriever+1

        elif pass_credit<=40 and deff_credit<=40 and fail_credit<=120:
            print("Exclude")
            excluded=excluded+1


        option = input("If you want to quit, press 'q' and if you want to continue the programme, press any key: \n")

        if option=='q':
            break
    print("Progress", "", progress, ":", progress* '*')
    print("Trailing", "", trailing, ":", trailing* '*')
    print("Retriever", "", retriever, ":", retriever* '*')
    print("Exclude", "", excluded, ":", excluded* '*')
    print(total_count, "outcomes in total.")
    break
