def rock_paper_scissors(a):
    choice_scoring = {'X': 1, 'Y': 2, 'Z': 3}
    options = {
        'A X': 3, 'A Y': 6, 'A Z': 0,
        'B X': 0, 'B Y': 3, 'B Z': 6,
        'C X': 6,'C Y': 0, 'C Z': 3
    }
    with open (a, 'r') as f:
        text = f.read()
    uwu = text.split("\n")
    total_score = 0

    for i in uwu:
        total_score += options[i] + choice_scoring[i.split(" ")[1]]
    return total_score

if __name__ == '__main__':
    print(rock_paper_scissors("puzzle_input.txt"))