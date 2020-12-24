class Critter(object):   
 
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name=name  
        self.hunger=hunger
        self.boredom=boredom
 
    def __pass_time(self):
        self.hunger+=1
        self.boredom+=1
 
    @property
    def mood(self):
        unhappy = self.hunger+self.boredom
        if unhappy<5:
            m = 'прекрасно'
        elif 5<=unhappy<=10:
            m = 'неплохо'
        elif 11<=unhappy<=15:
            m = 'не очень хорошо'
        else:
            m = 'ужасно'
        return m
    
    def talk(self):
        print('Привет. Меня зовут ', self.name,' и сейчас я чувствую себя ', self.mood, ' сейчас.\n')
        self.__pass_time()
    
    def eat(self, food=4):
        print('Мрр... Спасибо!')
        self.hunger = food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()
 
    def play(self, fun = 0 ):
        print('Юххууу!!!')
        self.boredom = fun
        if self.boredom<0:
            self.boredom=0
        self.__pass_time()
 
def main():
    crit = Critter('Мурзик')
    choice = None   
    while choice != '0':
        print('''
    Моя зверюшка:
0 - Выход
1 - Узнать о самочувствии зверюшки
2 - Покормить зверюшку
3 - Поиграть со зверюшкой
''')
        print('Ваш выбор: ', end=' ')
        choice = input()
        if choice =='0':
            print('До свидания!')
        elif choice == '1':
             crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        else:
            print('Извините, в меню нет пункта ',choice)
            print('\nДля вызова меню жмите Enter.')
main()
