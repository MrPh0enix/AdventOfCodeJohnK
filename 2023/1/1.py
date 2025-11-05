

with open('input.txt', 'r') as file:
    calibDoc = file.read()
    
calibLis = calibDoc.split('\n')

total = 0

for line in calibLis:
    firstNum = '0'
    lastNum = '0'
    firstNumFound = False
    lastNumFound = False
    
    for i in line:
        if i.isdigit():
            if firstNumFound == False:
                firstNum = i
                firstNumFound = True
            else:
                lastNum = i
                lastNumFound = True
    
    if lastNumFound == False:
        lastNum = firstNum
    
    number = firstNum+lastNum
    print(number)
    total += int(number)

print(total)




            