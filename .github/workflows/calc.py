#Calculator project.

while True:
    num1 = float(input("Enter number: "))
    user_input = input(":")
    num2 = float(input("Enter number: "))
    if user_input == "+":
        result = str(num1 + num2)
        print("The result is:" + result)
        break
    elif user_input =="-":
        result = str(num1 - num2)
        print("The result is:" + result)
        break
    elif user_input == "*":
        result = str(num1 * num2)
        print("The result is:" + result)
        break
    elif user_input == "/":
        result = str(num1 / num2)
        print("The reult is:" + result)
        break
    elif user_input == "//":
        result = str(num1 // num2)
        print("The result is" + result)
        break
    elif user_input == "%":
        result = str(num1 % num2 )
        print("The result is" + result)
        break
    else:
        print("Error")


####Created with love by JosephTheCode aka VesselKreative##########


