password = "mulualem03"
trials = 0
while password != "password":
    # if the values of the two operands are not equal
    if trials == 5:
        print("Terminate")
        break;
    else:
        password = input("Enter password: ")
        trials += 1
if password == "password":
    print("Welcome In")


    

