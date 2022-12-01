def calorie():
    
    list_of_calories = []
    aux = []
    with open('part_two.txt', 'r') as uwu:
        for i in uwu.readlines():
            if i != '\n':
                aux.append(int(i.strip('\n')))
            else:
                list_of_calories.append(sum(aux))
                aux = []
    return list_of_calories

x = calorie()
print(max(x))
x.sort()
print(sum(x[-3:]))