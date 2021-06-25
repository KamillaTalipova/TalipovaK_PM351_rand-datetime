import random
import string
import datetime as dt
import calendar
from random import sample

def bingo():
    data=sample(range(1,76),25)
    res=[data[i:i+5]for i in range(0,25,5)]
    res[2][2]=0
    return list(map(list,res))
def rus_bingo():
    pass
def generate_password(m):
    str=string.ascii_letters
    numb=string.digits
    pasw=''.join(random.choice(str)+random.choice(numb) for i in range(m))
    return pasw
def generate_list_of_paswords(m,n):
    str = string.ascii_letters
    numb = string.digits
    pasw=list()
    for i in range(n):
        pasw.append(''.join(random.choice(str) + random.choice(numb) for i in range(m)))
    return pasw
def weekend(Y,M,D):
    date=calendar.weekday(Y,M,D)
    if date==5:
        return('Sunday')
    else: return ('Saturday')
def spring(Y,M,D):
    date=dt.date(Y,M,D)
    if M>3:
        spr=dt.date(Y+1, 3, 1)
    elif M<=3:
        spr=dt.date(Y,3,1)
    return abs(date - spr)
def lecture():
    pass

def main():
    print('_______________RANDOM______________')
    print('_______________TASK1_______________')
    [print(bingo()[i]) for i in range(len(bingo()))]

    print('_______________TASK3_______________')
    print(generate_password(5))

    print('_______________TASK4________________')
    print(generate_list_of_paswords(3, 4))

    print('-------------DATETIME----------------')
    print('_____________TASK1___________________')
    print(weekend(2021, 7, 26))

    print('_______________TASK2________________')
    print(spring(2019,2,1))
    print(spring(2019,3,1))
    print(spring(2019,4,1))


if __name__=='__main__':
    main()