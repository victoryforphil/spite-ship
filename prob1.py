
import random
import numpy as np
import matplotlib.pyplot as plt
probMap = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

ships = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# test

# 1x 4 Wide - 1
# 2x 3 wide - 2
# 3x 2 wide - 3
# 4x 1 wide - 4
# Blocked Space - 5
print("east")

def check_place(start_x, start_y, end_x, end_y):

    if end_y >= 10 or end_x >= 10:
        return False

    for y in range((end_y-start_y) + 1):
        for x in range((end_x - start_x) + 1):
            true_x = start_x + x
            true_y = start_y + y

            if ships[max(0, true_y - 1)][max(0, true_x - 1)] is not 0 and ships[max(0, true_y - 1)][max(0, true_x - 1)] is not 5:
                return False
            if ships[true_y][true_x] is not 0:
                return False
            if ships[min(9, true_y + 1)][min(9, true_x + 1)] is not 0 and ships[min(9, true_y + 1)][min(9, true_x + 1)] is not 5:
                return ships[min(9, true_y + 1)][min(9, true_x + 1)] is not 5
    return True


def add_ship(width, val):

    ran_x = random.randrange(-1, 11)
    ran_y = random.randrange(-1, 11)
    orient = random.randrange(0, 11)

    start_x = ran_x
    start_y = ran_y
    end_x = ran_x + width
    end_y = ran_y
    if orient < 6:
        end_x = ran_x
        end_y = ran_y + width

    valid = check_place(start_x, start_y, end_x, end_y)
    if valid:
        for y in range((end_y - start_y) + 1):
            for x in range((end_x - start_x) + 1):
                true_x = start_x + x
                true_y = start_y + y
                if true_x >= 0 and true_y >= 0:
                    ships[true_y][true_x] = val
                    probMap[true_y][true_x] += 1
       

        return 1
    else:
        return 0

runs = 55000
for i in range(runs):
    


    ships = [
    [5, 5, 0, 0, 5, 0, 0, 0, 0, 5],
    [5, 5, 0, 0, 5, 0, 0, 0, 5, 0],
    [5, 5, 5, 0, 0, 0, 5, 0, 0, 0],
    [5, 5, 0, 5, 0, 0, 0, 5, 0, 0],
    [5, 0, 5, 0, 5, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 5, 5, 5, 0, 0],
    [0, 0, 0, 0, 5, 5, 5, 5, 0, 0],
    [5, 5, 5, 0, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 0, 0, 0, 0, 0, 5, 0],
    [5, 5, 5, 0, 0, 5, 0, 5, 0, 0]]

    
    four_wide_count = 0
    while four_wide_count < 1:
        four_wide_count += add_ship(3, 4)

    three_wide_count = 0
    while three_wide_count < 2:
        three_wide_count += add_ship(2, 3)

    two_wide_count = 0
    while two_wide_count < 1:
        two_wide_count += add_ship(1, 2)

    one_wide_count = 0
    while one_wide_count < 3:
        one_wide_count += add_ship(0, 1)

probMap = probMap / runs
#probMap = probMap - probMap.mean(axis=0)
#probMap = probMap / np.abs(probMap).max(axis=0)
plt.imshow(probMap, cmap='jet')
plt.show()
