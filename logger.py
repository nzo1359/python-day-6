




def ask_name():
    name = input("Please input your name: ")
    with open("visitors.txt", "a") as file:
        file.write(name + "\n")


def main():
    ask_name()


main()