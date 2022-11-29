class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name

    def setmoney(self, money):
        self.__money = money

    def getmoney(self):
        return self.__money

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def moneyX(self):
        customer = input("Введите сумму:")
        return f'Вы добавили средства на свой счет \nНа вашем счету: {self.getmoney() + int(customer)}'

    def _kill(self):
        return f'Вы обнулили свой баланс \nНа вашем счету осталось:{self.getmoney() - self.getmoney()} '

    def __jackpot(self):
        return f'ВЫ БЫЛИ ВЫБРАНЫ В НАШЕЙ ЛОТЕРЕЕ! ВАШ СЧЕТ УВЕЛИЧИЛСЯ В 10 РАЗ\nНа вашем счету:{self.__money * 10}'


switz = Bank(0, 'Gus')
switz.setname('Gus')
switz.setmoney(2000)
print(f'Ваше имя:{switz.getmoney()} \nНа вашем счету:{switz.getmoney()}')
print(switz.moneyX())
print(switz._kill())
print(switz._Bank__jackpot())