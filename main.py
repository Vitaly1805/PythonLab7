import random
import os
from multiprocessing import Pool
import time
import threading
from functools import reduce
import re
def randomGrade():
    return random.randint(2, 5)

def init():
    return {'математика': [], 'русский язык': [], 'литература': [], 'инфоматика': []} #создаёт словарь с пустыми списками

def fun(i, j):
    files = os.listdir('D:/Учеба/Python/Labs/7Labs/school')

    for k in range(i, j):
        f = open('D:/Учеба/Python/Labs/7Labs/school/'+files[k])

        arr = []

        for s in f:
            arr = re.findall(r'"[а-яА-Я ]+": (\d)[, ]*', s) #региксом делим строку на результаты по школе на каждый предмет и вписываем в массив значнеия по порядку
            if arr:
                d['математика'].append(int(arr[0]))
                d['русский язык'].append(int(arr[1]))
                d['литература'].append(int(arr[2]))
                d['инфоматика'].append(int(arr[3]))

def avgGradesForLesson(str):
    return reduce(lambda x, y: x + y, d[str]) / len(d[str])

d = init()

for i in range(1, 501):
    f = open(f'D:/Учеба/Python/Labs/7Labs/school/{i}.txt', 'w+')
    counter = 0
    for j in range(random.randint(20, 30)):
        letter = chr(ord("а") + counter)
        f.write(f'{{"class_name": "11-{letter}", "marks": {{"математика": {randomGrade()}, "русский язык": {randomGrade()}, "литература": {randomGrade()}, "информатика": {randomGrade()}}}}},\n')
        counter += 1
    f.close()

if __name__ == '__main__':  # проверяем имя текущего модуля
    count = 1
    start_time = time.time()
    for i in range(count):
        my_thread = threading.Thread(target=fun, args=(500 // count * i, 500 // count * (i + 1)))
        my_thread.start()  # запуск потока
        my_thread.join()  # ждем завершение потока
    print(f'Количество потоков: {count}, Время вычислений: {time.time() - start_time}')
    print(f'Математика: {avgGradesForLesson("математика")}')
    print(f'Русский язык: {avgGradesForLesson("русский язык")}')
    print(f'Литература: {avgGradesForLesson("литература")}')
    print(f'Информатика: {avgGradesForLesson("инфоматика")}')


    d = init()
    start_time = time.time()
    count = 2
    p = Pool(count)
    p.starmap(fun, map(lambda x:(500//count*x, 500//count*(x+1)),range(count)))
    p.close()
    print(f'Количество процессов: {count}, Время вычислений: {time.time() - start_time}')