


with open("day2.txt", "r") as t:
    data = t.read()

data = data.split('\n')

rank = {'A': 1, 'B': 2, 'C': 3}

loss = {'A': 'C', 'B': 'A', 'C': 'B'}

win = {'A': 'B', 'B': 'C', 'C': 'A'}

score = 0

for round in data:
    hands = round.split(' ')
    
    if hands[1] == 'Y': #draw
        score += (rank[hands[0]] + 3)
    
    elif hands[1] == 'X': #loss
        score += (rank[loss[hands[0]]] + 0)
        
    elif hands[1] == 'Z': #win
        score += (rank[win[hands[0]]] + 6)
       
            
print(score)
    