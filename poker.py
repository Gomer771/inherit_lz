#родительский класс Texas_holdem
class Texas_holdem:
    def __init__(self, first_card_value, first_card_suit, second_card_value, second_card_suit):
        self.first_card_value = first_card_value
        self.first_card_suit = first_card_suit
        self.second_card_value = second_card_value
        self.second_card_suit = second_card_suit

    def pocket_info(self):
        return f"Карты на руках: {self.first_card_value}{self.first_card_suit}, {self.second_card_value}{self.second_card_suit}"

    def win_chance(self):
        #проверяем параметры комбинаций
        if self.first_card_value == "A" and self.second_card_value == "A":
            return "Шансы на выигрыш: 0.45%"
        elif (self.first_card_value == "A" and self.second_card_value == "K") or \
             (self.first_card_value == "K" and self.second_card_value == "A"):
            if self.first_card_suit == self.second_card_suit:
                return "Шансы на выигрыш: 0.3%"  #одномастные A-K
            else:
                return "Шансы на выигрыш: 0.9%"  #разномастные A-K
        elif (self.first_card_value == "A" or self.first_card_value == "K") and \
             (self.second_card_value == "A" or self.second_card_value == "K"):
            return "Шансы на выигрыш: 1.2%"  #любые A-K
        elif self.first_card_value == self.second_card_value:
            if self.first_card_value in {"A", "K"}:
                return "Шансы на выигрыш: 0.9%"  #A-A или K-K
            else:
                return "Шансы на выигрыш: 5.9%"  #любая другая пара
        elif self.first_card_suit == self.second_card_suit:
            return "Шансы на выигрыш: 24%"  #две карты одной масти
        elif (self.first_card_value == "A" and self.second_card_value in {"K", "Q", "J"}) or \
             (self.second_card_value == "A" and self.first_card_value in {"K", "Q", "J"}):
            return "Шансы на выигрыш: 2.1%"  #A-K или топ пара
        else:
            return "Шансы на выигрыш: (меньше 1%)"


#дочерний класс Omaha_holdem
class Omaha_holdem(Texas_holdem):
    def __init__(self, first_card_value, first_card_suit, second_card_value, second_card_suit,third_card_value, third_card_suit, forth_card_value, forth_card_suit):
        super().__init__(first_card_value, first_card_suit, second_card_value, second_card_suit)
        self.third_card_value = third_card_value
        self.third_card_suit = third_card_suit
        self.forth_card_value = forth_card_value
        self.forth_card_suit = forth_card_suit

    def pocket_info(self):
        return f"Карты на руках: {self.first_card_value} {self.first_card_suit}, {self.second_card_value} {self.second_card_suit}, {self.third_card_value} {self.third_card_suit}, {self.forth_card_value} {self.forth_card_suit}"

    