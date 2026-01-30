from datetime import datetime

from numpy.f2py.auxfuncs import flatlist
from sqlalchemy.event import remove


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Student(Person):
    count=0
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,gender)
        self.stu_id=f'{datetime.now().year}{Student.count:03d}'
        self.scores={}

    #add score for student
    def add_score(self,subject,score):
        self.scores[subject]=score

    #caculate avg score
    def calcu_avg(self):
        if self.scores:
            return sum(self.scores.values())/len(self.scores)
        else:
            return 0

    #magic methods
    def __str__(self):
        return f'{self.name}-{self.age}-{self.scores}-{self.stu_id},the avg score is {self.calcu_avg():.2f}'

class Manager:
    def __init__(self):
        self.stu_list=[]

    def add_stu(self):
        name=input('text name:')
        age=input('text age')
        gender=input('text gender')
        stu=Student(name,age,gender)
        self.stu_list.append(stu)
        print(f'add stu successful,the stu-id is {stu.stu_id}')

    def del_stu(self,):
        sid=input('text stu id')
        target=None
        for stu in self.stu_list:
            if stu.stu_id==sid:
                target=stu
        if target:
            self.stu_list.remove(target)
            print('delete target seccessful')
        else:
            print('fail to find target stu')

    def show_all_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('there is no student in stu list')

    def set_score(self):
        sid=input('text stu id')
        for stu in self.stu_list:
            if sid==stu.stu_id:
                score_str=input('please text the format score with subject-score')
                score_list=score_str.replace(',','，').split('，')
                for item in score_list:
                    subject,score=item.split('-')
                    subject=subject.strip()
                    score=float(score.strip())
                    stu.add_score(subject,score)
                print('set score suceessfully')
                return
        print('stu id is mistake')

    def run(self):
        while True:
            print('___stu_manage___')
            print('1.add stu')
            print('2.del stu')
            print('3.show all stu')
            print('4.set score')
            print('5.exit')

            choice = input('text operation number')
            if choice == '1':
                self.add_stu()
            elif choice == '2':
                self.del_stu()
            elif choice == '3':
                self.show_all_stu()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('exit the system')
                break
            else:
                print('input wrong info')



s1=Student('andy',19,'men')
s1.add_score('math',120)
s1.add_score('english',99)

M1=Manager()
M1.run()
