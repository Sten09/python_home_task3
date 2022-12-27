# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#in
#4

#out
#[2, 5, 8, 10]
#[20, 40]

#in
#5

#out
#[2, 2, 4, 8, 8]
#[16, 16, 4]

from random import sample

def list_rand_nums(count):
    if count < 0:
        print('отрицательное значение количества чисел ')
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prob_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k -1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list

all_list = list_rand_nums(int(input('number of numbers: ')))
print(all_list)
print(prob_pairs(all_list))

#def mult_lst(
#lst):
#    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#    print(new_lst)
#
#
#lst = [2, 5, 8, 10]
#mult_lst(lst)
#lst = list(map(int, input("Введите числа через пробел:\n").split()))
#mult_lst(lst)