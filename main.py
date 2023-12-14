import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.money=100
        self.alive=True
    def to_study(self):
        print('time to study')
        self.progress+=0.12
        self.gladness-=3
    def to_sleep(self):
        print('I will sleep')
        self.gladness+=3
    def to_chill(self):
        print('Rest time')
        self.progress-=0.1
        self.gladness+=5
        self.money-=20
    def to_work(self):
        print('Work time')
        self.money+=30
        self.gladness-=3
        self.progress+=0.025
    def is_alive(self):
        if self.progress<-0.5:
            print('Cast out')
            self.alive=False
        elif self.gladness<=0:
            print('Depresion...')
            self.alive=False
        elif self.progress>5:
            print('Passed externaly')
            self.alive=False
        elif self.money<0:
            print('bankrupt')
            self.alive=False
    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {round(self.progress)}')
        print(f'Money - {round(self.money)}')
    def live(self,day):
        day='Day ' + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        life_cube=random.randint(1,4)
        if life_cube==1:
            self.to_study()
        elif life_cube==2:
            self.to_sleep()
        elif life_cube==3:
            self.to_chill()
        elif life_cube==4:
            self.to_work()
        self.end_of_day()
        self.is_alive()
mavpich=Student(name='mavpich')
for day in range(365):
    if mavpich.alive==False:
        break
    mavpich.live(day)




