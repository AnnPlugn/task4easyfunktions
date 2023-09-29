#TASK3
def stroki(strok, isk_sim):
    arr_sim = [str(sim) for sim in strok]
    if isk_sim in arr_sim:
            return True
    else:
        return False


def cicles(n_numb):

    arrslov_ch = [n_numb[chislo] for chislo in range(len(n_numb)) if chislo % 2 == 0]
    arrslov_nech = [n_numb[chislo] for chislo in range(len(n_numb)) if chislo % 2 != 0]
    min_nech = min(arrslov_nech)
    Res = {"Четные числа:": arrslov_ch,"Нечетные числа:": arrslov_nech,"Минимальное нечетное:": min_nech}

    return Res


def dicts():
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    num_months = [int(num_month) for num_month in range(1,13)]
    months_list = {num_months: months for num_months, months in zip(num_months, months)}

    return months_list


#test1
#string = input("Введите строку: ")
#isk_sim = input("Введите символ: ")
#result = stroki(string)
#print(result)

#test2
#col_n = int(input("Введите количество чисел: "))
#i = 0
    #n_numb = []
    #while i < col_n:
        #n_numb.append(int(input("Введите число: ")))
        #i+=1
#print(cicles(col_n))

#test3
#print(dicts())

#TASK4
def lists(keys, values):
    if len(keys) == len(values):
        list = {keys: values for keys, values in zip(keys, values)}
    else:
        return False
    return list

#print("Длина списков одинакова")
#keys = (list(map(int,input().split("Через пробел введите список ключей"))))
#values = (list(map(int,input().split("Через пробел введите список значений"))))
#print(list(keys,values))

#TASK5
def lists2(listA, listB):
    listA.append(input("Выберите какой элемент хотите добавить"))
    listA.extend(listB)
    return reversed(listA)

#listA = (list(map(str,input().split("Через пробел введите список А"))))
#listB = (list(map(str,input().split("Через пробел введите список B"))))
#print(list2(listA, listB))


#TASK6
def lists3():
    my_list = []
    for i in range(120):
        my_list.append(i)

    length = len(my_list)

    total_sum = sum(my_list)

    avg = total_sum / length

    Res = {"Длина списка": length,"Сумма всех элементов:": total_sum,"Среднее арифметическое:": avg}
    return Res

#print(lists3())
