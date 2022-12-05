assignment_total = 0

def clean_line(line):
    x = line.split(',')
    first = x[0].split('-')
    second = x[1].split('-')
    a = int(first[0])
    b = int(first[1])
    c = int(second[0])
    d = int(second[1])
    return [list(range(a, b +1)), list(range(c, d + 1))]

def calculate_assignment(assig_t):
    with open ('puzzle_input.txt') as f:
        for i in f:
            a = clean_line(i)[0]
            b = clean_line(i)[1]
            if any(i in a for i in b):
                assig_t += 1
    return assig_t

if __name__ == '__main__':
    print(calculate_assignment(assignment_total)) 