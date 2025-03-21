from poker import Texas_holdem, Omaha_holdem

def main():
    #ввод данных для Texas Holdem
    print("Введите карты для Texas Holdem:")
    first_card_value = input("Введите значение первой карты: ")
    first_card_suit = input("Введите масть первой карты (например, ♠, ♥, ♦, ♣): ")
    second_card_value = input("Введите значение второй карты: ")
    second_card_suit = input("Введите масть второй карты (например, ♠, ♥, ♦, ♣): ")

    #создание объекта Texas_holdem
    texas_game = Texas_holdem(first_card_value, first_card_suit, second_card_value, second_card_suit)
    print(texas_game.pocket_info())
    print(texas_game.win_chance())

    #ввод данных для Omaha Hold'em
    print("Введите карты для Omaha Hold'em:")
    first_card_value = input("Значение первой карты: ")
    first_card_suit = input("Масть первой карты: ")
    second_card_value = input("Значение второй карты: ")
    second_card_suit = input("Масть второй карты: ")
    third_card_value = input("Значение третьей карты: ")
    third_card_suit = input("Масть третьей карты: ")
    forth_card_value = input("Значение четвертой карты: ")
    forth_card_suit = input("Масть четвертой карты: ")

    #создание объекта Omaha_holdem
    omaha_game = Omaha_holdem(first_card_value, first_card_suit, second_card_value, second_card_suit, third_card_value, third_card_suit, forth_card_value, forth_card_suit)
    print(omaha_game.pocket_info())
    print(omaha_game.win_chance())

if __name__ == '__main__':
    main()
