def progressOutcome(passCredit, deferCredit, failCredit):
    ## NOTE: This function does not use an if, elif chain. As a function terminates when a return is called, the function will terminate when the first true if statement return is called. This also helps to make future changes without worrying about the order of the if statement conditions.

    # Progress outcome
    if passCredit == 120 and deferCredit == 0 and failCredit == 0:
        return "Progress"
    
    # Progress (module trailer) outcomes
    if passCredit == 100 and (deferCredit == 20 or failCredit == 20):
        return "Progress (module trailer)"
    
    # Exclude outcomes - when fail credits are too high
    if failCredit >= 80:
        return "Exclude"
    
    # Do not Progress – module retriever for all other valid combinations
    if passCredit + deferCredit + failCredit == 120:
        return "Do not Progress – module retriever"
        
    raise Exception("Something went wrong. In the progressOutcome function.")

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





