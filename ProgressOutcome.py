def progressOutcome(passCredit,deferCredit,failCredit):
    if passCredit == 120:
        return "Progress"

    elif passCredit == 100:
        if deferCredit == 20:
            return "Progress (module trailer)"
        elif failCredit == 20:
            return "Progress (module trailer)"
        else:
            return "Total incorrect"
    
    elif passCredit == 80:
        if deferCredit == 40:
            return "Do not Progress – module retriever"
        elif deferCredit == 20 and failCredit == 20:
            return "Do not Progress – module retriever"
        elif failCredit == 40:
            return "Do not Progress – module retriever"
        else:
            return "Total incorrect"

    elif passCredit == 60:
        if deferCredit == 60:
            return "Do not progress - module retriever"
        # Find a way to reduce the codelines, I think an XOR implementation could help
        elif  deferCredit == 40 and failCredit == 20:
            return "Do not progress - module retriever"
        elif  deferCredit == 20 and failCredit == 40:
            return "Do not progress - module retriever"
        elif failCredit == 60:
            return "Do not progress - module retriever"
        else:
            return "Total incorrect"

    elif passCredit == 40:
        if deferCredit == 80:
            return "Do not progress - module retriever"
        elif deferCredit == 60 and failCredit == 20:
            return "Do not progress - module retriever"
        elif deferCredit == 40 and failCredit == 40:
            return "Do not progress - module retriever"
        elif deferCredit == 20 and failCredit == 60:
            return "Do not progress - module retriever"
        elif failCredit == 80:
            return "Exclude"
        else:
            return "Total incorrect"

    elif passCredit == 20:
        if deferCredit == 100:
            return "Do not progress - module retriever"
        elif deferCredit == 80 and failCredit == 20:
            return "Do not progress - module retriever"
        elif deferCredit == 60 and failCredit == 40:
            return "Do not progress - module retriever"
        elif deferCredit == 40 and failCredit == 60:
            return "Do not progress - module retriever"
        elif deferCredit == 20 and failCredit == 80:
            return "Exclude"
        elif failCredit == 100:
            return "Exclude"
        else:
            return "Total incorrect"

    else:
        if deferCredit == 120:
            return "Do not progress - module retriever"
        elif deferCredit == 100 and failCredit == 20:
            return "Do not progress - module retriever"
        elif deferCredit == 80 and failCredit == 40:
            return "Do not progress - module retriever"
        elif deferCredit == 60 and failCredit == 60:
            return "Do not progress - module retriever"
        elif deferCredit == 40 and failCredit == 80:
            return "Exclude"
        elif deferCredit == 20 and failCredit == 100:
            return "Exclude"
        elif failCredit == 120:
            return "Exclude"
        else:
            return "Total incorrect"
        
def validateCreditRange(credit):
     creditRange = [0,20,40,60,80,100,120]
     if credit in creditRange:
        return credit
     else:
        raise Exception("Out of range.")
     
def validateTotalCredit(passCredit,deferCredit,failCredit):
    if passCredit + deferCredit + failCredit == 120:
        return "Valid"
    else:
        raise Exception("Total incorrect.")
     
progressOutcomes = []
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludeCount = 0

reEnter = True
while reEnter:    

    isExeption = True
    while isExeption:   

        try:
            passCredit = validateCreditRange(int(input("Enter your pass credits: ")))
            deferCredit = validateCreditRange(int(input("Enter your defer credits: ")))
            failCredit = validateCreditRange(int(input("Enter your fail credits: ")))

            validateTotalCredit(passCredit,deferCredit,failCredit)

        except ValueError:
            print("Integers only")
            print()

        except Exception as ex:
            print(ex)
            print()

        else:
            print()
            isExeption = False

    currentProgressOutcome = progressOutcome(passCredit,deferCredit,failCredit)
    
    print(currentProgressOutcome)

    progressOutcomes.append(currentProgressOutcome)

    if currentProgressOutcome == "Progress":
        progressCount += 1
    elif currentProgressOutcome == "Progress (module trailer)":
        trailerCount += 1
    elif currentProgressOutcome == "Do not progress - module retriever":
        retrieverCount += 1
    elif currentProgressOutcome == "Exclude":
        excludeCount += 1
    else:
        raise Exception("Invalid progress outcome.")
    print()

    rePrompt = True
    while rePrompt:
        print("Would you like to enter another set of data?")
        print("Enter 'y' for yes or 'q' to quit and view results: ")
        reEnterInput = input()
        if reEnterInput.lower() == "q":
            print()
            print(progressOutcomes)
            print()
            print("""Progress outcomes: {} \n
Progress (module trailer): {} \n
Do not progress - module retriever: {} \n
Exclude: {}""".format(progressCount,trailerCount,retrieverCount,excludeCount))
            print()
            print("Program quit successfully.")
            print()
            reEnter = False
            rePrompt = False
        elif reEnterInput.lower() == "y":
            print()
            reEnter = True
            rePrompt = False
        else:
            print("Invalid input. Please try again.")
            print()
            reEnter = True





