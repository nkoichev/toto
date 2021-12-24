import random

my_list = [1, 2, 3, 4, 5, 6]
# my_li = list(input('enter 6 numbers: ').split(','))
# my_list = [int(i) for i in my_li]


winners = []
counter = 1
random_list = []


def winners_func(x, y, z):
    for i in x:
        if i in y:
            if i not in z:
                z.append(i)
    print(winners)


def rndm_func():
    while len(random_list) < 6:
        rndm = random.choice(range(1, 50))

        if rndm not in random_list:
            random_list.append(rndm)
    print('--------------------------')
    print(random_list)
    print(f'counter: {counter}')
    print('--------------------------')

target = 4

while True:
    rndm_func()
    counter += 1
    winners_func(my_list, random_list, winners)

    if len(winners) < target:

        random_list.clear()
        winners.clear()

    else:
        break

print('==========================')
print(f'Имате съвпадение на {target} числа в този тираж: {random_list}')
print(f'Печеливши числа: {winners}')
print(f'Брой на тиражите: {counter}')
print(f'Брой месеци {int(round(counter/4,0))}')
print(f'Брой години: {int(round(counter/4/12,0))}')