import random
class Parents:
    def __init__(self):
        self.gladness2=50
        self.money1=100000
class Study:
    def __init__(self):
        self.progress=0
class Dog:
    def __init__(self,name1='Dog'):
        self.name=name1
        self.gladness1=50
        self.satiety1=50
class Nazarij:
    def __init__(self,name='Human', school=None, dog=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.school=school
        self.dog=dog

    def get_school(self):
        self.school=Study()
    def ask_parents_money(self):
        self.money+=50
        self.parent.money1-=50
    def eat(self):
        self.satiety+=50
    def get_dog(self):
        self.dog=Dog()
    def parents(self):
        self.parent=Parents()
    def go_to_academy(self):
        self.school.progress+=0.4
        self.satiety-=4
        self.money-=12
        self.parent.gladness2+=10
        self.parent.money1-=100
    def chill(self):
        self.gladness+=30
        self.school.progress-=1
        self.satiety+=5
        self.parent.gladness2-=30
    def do_homework(self):
        self.gladness-=15
        self.school.progress+=0.3
        self.dog.gladness1-=40
    def go_for_a_walk_with_dog(self):
        self.gladness+=40
        self.dog.gladness1+=100
    def give_food_for_dog(self):
        self.dog.satiety+=50
    def go_to_school(self):
        self.school.progress=0.5
        self.gladness-=10
        self.money+=50
        self.parent.gladness2+=40
        dice=random.randint(1,4)
        if dice==1:
            self.money-=50
        if dice==2:
            self.money-=25
        if dice==3:
            self.money-=10
        if dice==4:
            self.money-=0
    def day_indexes(self,day):
        day = f'Today the {day} of {self.name}`s life'
        print(f'{day:=^50}', '\n')
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:^50}', '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print((f'Gladness - {self.gladness}'))
        dog_indexes = 'Dog indexes'
        print(f'{dog_indexes:^50}', '\n')
        print(f'Satiety - {self.dog.satiety1}')
        print(f'Gladness - {self.dog.gladness1}')
        study_indexes = ' study indexes'
        print(f'{study_indexes:^50}', '\n')
        print(f'Progress - {self.school.progress}')
        parent_indexes = 'parents indexes'
        print(f'Money - {self.parent.money1}')
        print(f'Gladnesss - {self.parent.gladness2}')
    def is_alive(self):
        if self.gladness < 0:
            print('Дипресія...')
            return False
        elif self.satiety < 0:
            print('Голод...')
            return False
        elif self.money < -100:
            print("Банкрот...")
            return False
        if self.dog.gladness1 < 0:
            print('Собачка заскучала...')
            return False
        if self.parent.gladness2 < 0:
            print('Дипресія...')
            return False
        if self.school.progress < 3:
            print('سيسشيشسشسيشسي...')
            return False
        if self.dog.satiety1 < 0:
            print('Собачка голодна...')
            return False
    def live(self,day):
        if self.is_alive()==False:
            return False
        if self.school is None:
            print('Записують в школу')
            self.get_school()
        if self.dog is None:
            print('Хочу собачку')
            self.get_dog()
        dice = random.randint(1, 6)
        if self.dog.satiety1 < 15:
            print('Дам собаці їсти')
            self.give_food_for_dog()
        if self.satiety < 20:
            print('Я буду Їсти')
            self.eat()
        elif self.gladness < 20:
            if self.dog.gladness1 < 15:
                print('Хочеться відпочити, але собаку потрібно вигуляти')
                self.go_for_a_walk_with_dog()
            else:
                print('Я відпочину')
                self.chill()
        elif self.money < 0:
            print('Потрібно попросити в батьків гроші')
            self.ask_parents_money()
        elif self.school.progress < 0:
            print('Зараз батьки побачать двойку і всьо капець мені. Нада перездати')
            self.do_homework()
        elif dice == 1:
            print('Я відпочину')
            self.chill()
        elif dice == 2:
            print('Йду в школу')
            self.go_to_school()
        elif dice == 3:
            print('СОбачка хоче гуляти!!!')
            self.go_for_a_walk_with_dog()
        elif dice == 4:
            print('Йду в академію')
            self.go_to_academy()
        elif dice == 5:
            print('Хочу їсти')
            self.eat()
        elif dice==6:
            print('Дам собаці їсти')
            self.give_food_for_dog()



name1=Dog(name1='Sharik')
nazarij=Nazarij(name='Nazarij')
for day in range(30):
    if nazarij.live(day)==False:
        break