

with open("day2.txt", "r") as t:
    data = t.read()

data = data.split('\n')

rank = {'X': 1, 'Y': 2, 'Z': 3}

score = 0

for round in data:
    hands = round.split(' ')
    
    if (hands[0] == 'A' and hands[1] == 'X') or (hands[0] == 'B' and hands[1] == 'Y') or (hands[0] == 'C' and hands[1] == 'Z'):
        score += (rank[hands[1]] + 3)
    
    elif hands[1] == 'X':
        if hands[0] == 'C':
            score += (rank[hands[1]] + 6)
        else:
            score += (rank[hands[1]])
            
    elif hands[1] == 'Y':
        if hands[0] == 'A':
            score += (rank[hands[1]] + 6)
        else:
            score += (rank[hands[1]])
    
    elif hands[1] == 'Z':
        if hands[0] == 'B':
            score += (rank[hands[1]] + 6)
        else:
            score += (rank[hands[1]])
            
print(score)
    