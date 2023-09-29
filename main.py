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