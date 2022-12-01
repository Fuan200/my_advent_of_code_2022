"""list_total = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

for i in range(len(list_total)):
    uwu = sum(list_total[i])
    list_total[i] = uwu

total_calories = max(list_total)
print(total_calories)

"""

def calorie():

    list_of_calorie = []
    aux = []
    with open('part_one.txt', 'r') as uwu:
        for i in uwu.readlines():
            if i != '\n':
                aux.append(int(i.strip('n')))
            else:
                list_of_calorie.append(sum(aux))
                aux = []
    return max(list_of_calorie)

print(calorie())