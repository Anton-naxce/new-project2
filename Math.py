import math
# среднее значение солнечных дней
average = 1.72
# функция для вычисления вероятности события
def probability(k):
    return (math.exp(-average) * (average ** k)) / math.factorial(k)
# вероятность того, что будет 1 солнечный день
day_1_probability = probability(1)
print("Вероятность того, что будет 1 солнечный день: ", day_1_probability)
# вероятность того, что будет 2 солнечных дня
day_2_probability = probability(2)
print("Вероятность того, что будет 2 солнечных дня: ", day_2_probability)
# вероятность того, что будет 3 солнечных дня
day_3_probability = probability(3)
print("Вероятность того, что будет 3 солнечных дня: ", day_3_probability)
# вероятность того, что будет 4 солнечных дня
day_4_probability = probability(4)
print("Вероятность того, что будет 4 солнечных дня: ", day_4_probability)
# вероятность того, что будет 5 солнечных дней
day_5_probability = probability(5)
print("Вероятность того, что будет 5 солнечных дней: ", day_5_probability)
# вероятность того, что будет 6 солнечных дней
day_6_probability = probability(6)
print("Вероятность того, что будет 6 солнечных дней: ", day_6_probability)