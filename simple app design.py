#portfolio prompts

#username checker, you have to enter the correct username in 3 tries or your kicked out
def user_name_checker():
    user_attempts = 3
    correct_username = "Agsim"

    while user_attempts > 0:
        login_user = input("What is the user name: ")

        if login_user == correct_username:
            print("Username accepted.")
            return True
        else:
            user_attempts -= 1
            print(f"Incorrect username. Attempts left: {user_attempts}")

    print("Too many failed username attempts.")
    return False

#password checker, you have to enter the correct password in 3 tries or you get kicked out
def password_checker():
    password_attempts = 3
    correct_password = "Weekend#1"

    while password_attempts > 0:
        login_password = input("What is the password: ")

        if login_password == correct_password:
            print("Password accepted.")
            return True
        else:
            password_attempts -= 1
            print(f"Incorrect password. Attempts left: {password_attempts}")

    print("Too many failed password attempts.")
    return False
# simple money calculator, after its used will exit the program
def money_calculator():
    while True:
        try:
            pennies = int(input("Enter the number of pennies: "))
            nickels = int(input("Enter the number of nickels: "))
            dimes = int(input("Enter the number of dimes: "))
            quarters = int(input("Enter the number of quarters: "))
            one_dollar_bills = int(input("Enter the number of $1.00 bills: "))
            five_dollar_bills = int(input("Enter the number of $5.00 bills: "))
            ten_dollar_bills = int(input("Enter the number of $10.00 bills: "))
            twenty_dollar_bills = int(input("Enter the number of $20.00 bills: "))
            fifty_dollar_bills = int(input("Enter the number of $50.00 bills: "))
            one_hundred_dollar_bills = int(input("Enter the number of $100.00 bills: "))

            total_amount = (
                pennies * 0.01 +
                nickels * 0.05 +
                dimes * 0.10 +
                quarters * 0.25 +
                one_dollar_bills * 1 +
                five_dollar_bills * 5 +
                ten_dollar_bills * 10 +
                twenty_dollar_bills * 20 +
                fifty_dollar_bills * 50 +
                one_hundred_dollar_bills * 100
            )

            print(f"\nThe total amount of money you entered was ${total_amount:,.2f}")
            break

        except ValueError:
            print("Please enter valid whole numbers only.\n")

# simple calculator, only allows 2 numbers, choose between addition, subtraction, multiplication, or division, you have the option to keep using or exit the program
History = []

def math_calculator():

    def addition(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return None
        return a / b

    while True:
        try:
            print("\n1 - Addition")
            print("2 - Subtraction")
            print("3 - Multiplication")
            print("4 - Division")
            print("5 - Show history")
            print("6 - Exit")

            choice = int(input("Choose an option: "))

            if choice == 5:
                print("History:", History)
                continue

            if choice == 6:
                print("Goodbye!")
                break

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == 1:
                result = addition(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
                if result is None:
                    print("Cannot divide by zero.")
                    continue
            else:
                print("Invalid option.")
                continue

            print(f"Result: {result}")
            History.append(result)

        except ValueError:
            print("Please enter valid whole numbers only.")

#enter the number of how many quizzes, labs, and exams, than ask for the total on each quiiz, lab, and exam, averages each quiz amount, lab amount, and exam amount than gives an overall average
def grade_calculator():

    def labs():
        total = 0
        lab_amount = int(input("How many labs are you going to enter? "))

        for lab_num in range(1, lab_amount + 1):
            score = int(input(f"Enter score for lab {lab_num}: "))
            total += score

        average_lab = total / lab_amount
        print(f"Lab average: {average_lab}")
        return average_lab

    def quizzes():
        total = 0
        quiz_amount = int(input("How many quizzes are you going to enter? "))

        for quiz_num in range(1, quiz_amount + 1):
            score = int(input(f"Enter score for quiz {quiz_num}: "))
            total += score

        average_quiz = total / quiz_amount
        print(f"Quiz average: {average_quiz}")
        return average_quiz

    def exams():
        total = 0
        exam_amount = int(input("How many exams are you going to enter? "))

        for exam_num in range(1, exam_amount + 1):
            score = int(input(f"Enter score for exam {exam_num}: "))
            total += score

        average_exam = total / exam_amount
        print(f"Exam average: {average_exam}")
        return average_exam

    lab_avg = labs()
    quiz_avg = quizzes()
    exam_avg = exams()

    overall_average = (lab_avg + quiz_avg + exam_avg) / 3
    print(f"\nOverall average: {overall_average}")


# Main program flow
if user_name_checker() and password_checker():
    while True:
        print("\nChoose from the menu options listed below")
        print("1 - Basic money calculator")
        print("2 - Basic math utility")
        print("3 - Grade calculator")
        print("4 - Exit")

        try:
            menu_choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number from 1-4.")
            continue

        if menu_choice == 1:
            money_calculator()
        elif menu_choice == 2:
            math_calculator()
        elif menu_choice == 3:
            grade_calculator()
        elif menu_choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
else:
    print("Access denied.")

