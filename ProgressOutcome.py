passCredit = int(input("Enter your pass credits: "))
deferCredit = int(input("Enter your defer credits: "))
failCredit = int(input("Enter your fail credits: "))

def progressOutcome(passCredit,deferCredit,failCredit):
    if passCredit == 120:
        return "Progress"

    elif passCredit == 100:
        if deferCredit == 20:
            return "Progress (module trailer)"
        elif failCredit == 20:
            return "Do not progress - module retriever"
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

print(progressOutcome(passCredit,deferCredit,failCredit))
