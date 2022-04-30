import random
# a simple list comprehension to create a sequence with 13 empty set
dice = [set() for x in range(13)]
# a nested for loops for generating all possible 36 dice rolls
for i in range(1, 7):
    for j in range(1, 7):
        dice[i+j].add((i, j))  # to assign their sum to a set of the dice sequence
# 3 sets for possible dice rolls sum and what does the sum refer to
lose = [2, 3, 12]
win = [7, 11]
point = [4, 5, 6, 8, 9, 10]
# a variable to decide if we have to continue the game or not
game_over = False
# a loop for generating 2 random integers and check to which one of previous sets they belong to

# PART I

while True:
    a = random.randint(1, 7)
    b = random.randint(1, 7)
    Sum = a+b
    if Sum in lose:  # the condition explains itself
        print("You lost the game! the roll u got is : (%s,%s)" % (a, b))
        game_over = True  # change variable so the program won't continue the game
        break
    if Sum in win:  # the condition explains itself
        print("You won the game! the roll u got is : (%s,%s)" % (a, b))
        game_over = True  # change variable so the program won't continue the game
        break
    if Sum in point:
        break  # it will break this loop so we continue the game

# PART II

tries = 0
if game_over == False:  # this will only happen if the Sum of the dice roll is in point set
    while True:
        c = random.randint(1, 7)  # generate 2 other random integers
        d = random.randint(1, 7)
        tries = tries + 1
        total = c + d  # the new sum
        if total == Sum:  # the game continues until we got either 7 or the same Sum we got in part I
            print("U won the game! the roll u got is : (%s,%s)" % (c, d))
            print("Number of tries : %(tries)s" % locals())
            break
        elif total == 7:
            print("U lost the game! the roll u got is : (%s,%s)" % (c, d))
            print("Number of tries : %(tries)s" % locals())
            break
        else:
            continue
