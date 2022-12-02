def rock_paper_scissors(a):
    choice_scoring = {'X': 0, 'Y': 3, 'Z': 6}
    options = {
        'A X': 3, 'A Y': 1, 'A Z': 2,
        'B X': 1, 'B Y': 2, 'B Z': 3,
        'C X': 2, 'C Y': 3, 'C Z': 1
    }
    with open (a, 'r') as f:
        text = f.read()
    uwu = text.split("\n")
    total_score = 0

    for i in uwu:
        total_score += choice_scoring[i.split(" ")[1]] + options[i]
    return total_score

if __name__ == '__main__':
    print(rock_paper_scissors("puzzle_input.txt"))