import random

def determine_winner(user_choice, computer_choice):
    """
    Визначає переможця гри.
    :param user_choice: Вибір користувача.
    :param computer_choice: Вибір комп'ютера.
    :return: Результат (перемога, поразка чи нічия).
    """
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "Ви перемогли!"
    else:
        return "Ви програли!"

def rock_paper_scissors():
    """
    Основна функція для запуску гри.
    """
    print("Вітаємо у грі 'Камінь, ножиці, папір'!")
    print("Для виходу з гри введіть 'exit'.\n")

    choices = ["stone", "scissor", "paper"]

    while True:
        user_choice = input("Зробіть ваш вибір (stone, scissor, paper): ").lower()

        if user_choice == "exit":
            print("Дякуємо за гру! До зустрічі!")
            break

        if user_choice not in choices:
            print("Некоректний вибір. Будь ласка, оберіть 'stone', 'scissor' або 'paper'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Вибір комп'ютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

# Запуск гри
rock_paper_scissors()
