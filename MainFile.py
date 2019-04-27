# todo посчитать квадрат суммы
# todo посчитать сумму квадратов
# todo посчитать разность


import datetime

print("Программа вычисляет разность квадрата суммы и сумм квадратов чисел от 1 до 100")

start = datetime.datetime.now()

sum1 = 0
sum2 = 0

for i in range(1, 101):
    sum1 = sum1 + i*i
    sum2 = sum2 + i

result = sum2**2 - sum1

stop = datetime.datetime.now()
estimate_time = stop - start

print("Вычисления заняли ", estimate_time.microseconds, 'микросекунд.')
print('Разность сумм = ', result)