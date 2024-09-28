"""
Задача "Потоковая запись в файлы"
"""

from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    f = open(file_name, 'w')
    f.close()
    for i in range(1, word_count + 1):
        with open(file_name, 'a') as file:
            file.write('Какое-то слово №' + str(i) + '\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end1 = datetime.now()
print(f'Работа потоков {time_end1 - time_start1}')

time_start2 = datetime.now()
a = Thread(target=write_words, args=(10, 'example5.txt'))
b = Thread(target=write_words, args=(30, 'example6.txt'))
c = Thread(target=write_words, args=(200, 'example7.txt'))
d = Thread(target=write_words, args=(100, 'example8.txt'))

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()
time_end2 = datetime.now()
print(f'Работа потоков {time_end2 - time_start2}')
