
import random


questions_list = [
    {"question 1":"question 1", "answer 1": "1"},
    {"question 2":"question 2", "answer 2": "2"},
    {"question 3":"question 3", "answer 3": "3"},
    {"question 4":"question 4", "answer 4": "4"},
]


def user_quit():
    
    print("Thank you. Farewell")


def random_question(questions_list):
    random_card = random.choice(questions_list)
    return random_card

    #random_question = questions_list[random.randint(0, 3)]



def show_question(card):
    question = card["questions_list"]
    print("questions_list", question)


    #print(random_question)



def show_answer(card):
    answer = card["questions_list"]
    print("questions_list", answer)



def main():

    while True:
        chosen_card = random_question(questions_list)
        show_question(chosen_card)

        user_choice = input("Enter Q to quit, type anything else to continue")

        if user_choice == "Q":
            quit()
            break

        else:
            show_answer(chosen_card)




'''    

while True:
        quit_answer = input("Would you like to quit the program? ")
        if quit_answer == "yes" or quit_answer == "Yes":
            break
        else:
            card = random_question(questions_list)
            show_question(card)
            ask_user = input("Would you like to see the answer? ")
            if ask_user == "yes" or ask_user == "Yes":
                show_answer(card)

'''



main()