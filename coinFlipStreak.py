import random

numberOfStreaks = 0
streak = 1

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinValues = []
    for i in range(100):
        coinValues.append(random.randint(0,1))

    # Code that check if there is a streak of 6 heads or tails in a row. 
    for i in range(1, len(coinValues)):
        if coinValues[i] == coinValues[i - 1]:
            streak += 1
        else:
            streak = 1
        
        if streak == 6:
            numberOfStreaks += 1
            break # Do not want to double count in the same series of 100 flips
print('Chance of streak: ' + str(numberOfStreaks / 100) + '%')