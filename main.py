# error handling

print("\n== Basic Math Operation ==")
print("1. Addition")
print("2. Subtraction")
print("E. Exit")
choice = input("choice: ")

while choice != 'E' and choice != 'e':
    if choice == '1':
        try:
            print("\n> Addition")
            print("input first number: ")
            first_num = int(input())
            print("input second number: ")
            second_num = int(input())
            result = first_num + second_num
        except ValueError:                           # invalid input
            print("\n[ invalid type input ]")
        except Exception:                            # something else wrong happen
            print("\n[ Something wrong occurred ]")
        else:                                        # if nothing wrong happen
            print("The result: ", result)
    elif choice == '2':
        try:
            print("\n> Subtraction")
            print("input first number: ")
            first_num = int(input())
            print("input second number: ")
            second_num = int(input())
            result = first_num - second_num
        except ValueError:
            print("\n[ Invalid type input ]")
        except Exception:
            print("\n[ Something wrong occurred ]")
        else:
            print("The result: ", result)

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Math Operation ==")
    print("1. Addition")
    print("2. Subtraction")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")



