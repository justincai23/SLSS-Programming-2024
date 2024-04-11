while True:
    user_input = input("please enter a number（enter 'exit' to exit ）: ")
    

    if user_input == 'exit':
        print("see you next time")
        break  

    power_input = input("please enter the power of the number（enter 'exit' to exit ）: ")
    if power_input == 'exit':
        print("see you next time")
        break  

    else:
        try:
            number = float(user_input)
            power = float(power_input)
            print("this is your result:", number ** power)
        except ValueError:
            print("ERROR, please enter a valuable number")
