import random
class Dog:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.satiety=50
        self.go_to_the_toilet=0
    def to_eat(self):
        print('Lets go eat')
        self.gladness+=5
        self.go_to_the_toilet+=20
        self.satiety+=70
    def to_play(self):
        print('Lets go play')
        self.gladness+=10
        self.satiety-=10
        self.go_to_the_toilet+=20
    def to_sleep(self):
        print('Lets go sleep')
        self.gladness+=5
        self.satiety-=5
        self.go_to_the_toilet+=20
    def go_out(self):
        print('Lets go out!!!!:)')
        self.gladness+=15
        self.satiety-=5
        self.go_to_the_toilet=0
    def alive(self):
        if self.satiety<=-10:
            print(self.name + ' died from hunger')
            self.alive=False
        elif self.go_to_the_toilet==100:
            self.go_out()
        elif self.satiety>=100:
            self.satiety=100
        elif self.gladness<=0:
            print(self.name + 'got bored')

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Satiety - {round(self.satiety)}')
        print(f'Toilet - {round(self.go_to_the_toilet)}')
    def live(self,day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        life_cube = random.randint(1, 4)
        if life_cube==1:
            self.go_out()
        elif life_cube==2:
            self.to_play()
        elif life_cube==3:
            self.to_sleep()
        elif life_cube==4:
            self.to_eat()
        self.end_of_day()
        self.alive()
sharik=Dog(name='Sharik')
for day in range(365):
    if sharik.alive==False:
        break
    sharik.live(day)
