import random
from english_words import get_english_words_set

def main_game():
    wap = "0"
    vap = "2"
    
    choice1 = int(input(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Select any one of this:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n1.To do list\n2.wordle\n3.rock,paper,scissors\nEnter your choice:"))
    
    tasks = []
    while True:
        if choice1 == 1:
            choice2 = int(input("1.Add tasks\n2.view tasks\n3.remove tasks\n4.to exit the list manager\nEnter your choice:"))
            if choice2 == 1:
                task = input("Enter the task to be added:")
                tasks.append(task)
                print(f"task {task} added successfully")
            elif choice2 == 2:
                if not tasks:
                    print("No entry found.")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}--->{task}")
            elif choice2 == 3:
                if not tasks:
                    print("No task to be removed in the list")
                    continue
                
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}--->{task}")
                ta = int(input("Enter the index of the word to be removed from the list:"))
                if 1 <= ta <= len(tasks):
                    removed = tasks.pop(ta - 1)
                    print(f"Removed: {removed}")
                    print(tasks)
                else:
                    print("Invalid index.")
            else:
                print("thank you")
                break
                
        elif choice1 == 2:
            all_words = get_english_words_set(['web2'], lower=True)
            three_letter_words = [word for word in all_words if len(word) == 3]
            four_letter_words = [word for word in all_words if len(word) == 4]
            five_letter_words = [word for word in all_words if len(word) == 5]
            six_letter_words = [word for word in all_words if len(word) == 6]
            
            choice2 = int(input("difficulty level:\n1.Easy\n2.Medium\n3.hard\n4.master\nSelect difficulty :"))
            if choice2 == 1:
                captcha_word = random.choice(list(three_letter_words))
            elif choice2 == 2:
                captcha_word = random.choice(list(four_letter_words))
            elif choice2 == 3:
                captcha_word = random.choice(list(five_letter_words))
            elif choice2 == 4:
                captcha_word = random.choice(list(six_letter_words))
            else:
                captcha_word = random.choice(list(four_letter_words))
                
            print(captcha_word)
            
            while wap == "0":
                user_input = input(f"Enter a {len(captcha_word)} letter word: ").lower()
                if len(user_input) != len(captcha_word):
                    print("error: invalid length")
                elif captcha_word == user_input:
                    print("You win")
                    cont = input("Do you want to continue (y/n): ").lower()
                    if cont == "y":
                        break
                    else:
                        wap = "1"
                        print("Thank you")
                        return wap
                else:
                    for i in range(len(captcha_word)):
                        if i < len(user_input) and captcha_word[i] == user_input[i]:
                            print(f"position matches for '{user_input[i]}' at index {i+1}")
            break
            
        elif choice1 == 3:
            user_score = 0
            comp_score = 0
            round_no = 0
            options = ["r", "p", "s"]
            opts = {"r": "rock", "p": "paper", "s": "scissors"}
            
            while vap == "2":
                comp_choice = random.choice(options)
                user_input = input("Enter r for rock, p for paper or s for scissors: ").lower()
                
                if user_input not in opts:
                    print("Invalid choice, try again.")
                    continue
                    
                print(f"computer's choice is {opts[comp_choice]}\nuser's choice is {opts[user_input]}")
                
                if (user_input == "r" and comp_choice == "p") or (user_input == "p" and comp_choice == "s") or (user_input == "s" and comp_choice == "r"):
                    print("Computer wins!")
                    comp_score += 1
                elif user_input == comp_choice:
                    print("Tie!")
                else:
                    print("You win this round!")
                    user_score += 1
                    
                print(f"user score = {user_score} <---> computer score = {comp_score}")
                round_no += 1
                print(f"round no ::::: {round_no}")
                
                cont = input("Do you want to continue (y/n): ").lower()
                if cont == "y":
                    continue
                else:
                    vap = "1"
                    print("Thank you")
                    return vap
            break

if __name__ == "__main__":
    main_game()