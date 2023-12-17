from random import randint


number_of_Sixes_Rolled = 0


for x in range(4):
    roll = randint(1, 6)
    print(f"You rolled: {roll}")

    if roll == 6:
        number_of_Sixes_Rolled += 1


print(f"Number of sixes rolled: {number_of_Sixes_Rolled}")

if number_of_Sixes_Rolled > 0:
    print('You win!')
else:
    print('You lose')