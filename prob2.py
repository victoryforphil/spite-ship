
import random
import numpy as np
import matplotlib.pyplot as plt
probMap = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]])

ships = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
# test

# 1x 4 Wide - 1
# 2x 3 wide - 2
# 3x 2 wide - 3
# 4x 1 wide - 4
# Blocked Space - 5
print("east")

def check_place(start_x, start_y, end_x, end_y):

    
    start_y = max(0, start_y)
    start_x = max(0, start_x)
    for y in range((end_y-start_y) + 1):
        for x in range((end_x - start_x) + 1):
            true_x = start_x + x
            true_y = start_y + y

            true_y = min([7, true_y])
            true_x = min([7, true_x])

            if ships[max(0, true_y - 1)][max(0, true_x - 1)] is not 0 and ships[max(0, true_y - 1)][max(0, true_x - 1)] < 5:
                return False
            if ships[true_y][true_x] is not 0:
                return False
            if ships[min(7, true_y + 1)][min(7, true_x + 1)] is not 0 and ships[min(7, true_y + 1)][min(7, true_x + 1)] < 5:
                return False
    return True


def add_ship(width, val):

    ran_x = random.randrange(-2, 9)
    ran_y = random.randrange(-2, 9)
    orient = random.randrange(0, 16)

    start_x = ran_x
    start_y = ran_y
    
    end_x = ran_x + width
    end_y = ran_y
    if orient < 6:
        end_x = ran_x
        end_y = ran_y + width

    start_y = max(0, start_y)
    start_x = max(0, start_x)
    end_x   = min(7, end_x)
    end_y   = min(7, end_y)
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
runs = 100000

def scan_hit(width):
    for y in range(8):
        for x in range(8):
            if ships[y][x] is 6:
                probMap[y][x] = 10

                for w in range(width + 1):
                    hit_x = x
                    hit_y = y - (width /2) + w

                    hit_y = min(7,hit_y)
                    hit_y = max(0, hit_y)

                    probMap[hit_y][hit_x] = ((runs / width) * -(abs(hit_y - y))) / width + 1


                for w in range(width):
                    hit_y = y
                    hit_x = x - (width /2 - 1) + w

                    hit_x = min(7,hit_x)
                    hit_x = max(0, hit_x)

                    probMap[hit_y][hit_x] = ((runs / width) * -(abs(hit_x - x))) / width + 1




from tqdm import tqdm
for i in tqdm(range(runs)):
    
   

    ships = [
    [0, 5, 5, 5, 0, 0, 5, 5],
    [5, 5, 5, 5, 0, 0, 5, 5],
    [0, 5, 5, 5, 0, 0, 5, 5],
    [0, 5, 5, 5, 0, 0, 5, 5],
    [0, 5, 5, 5, 0, 5, 5, 5],
    [0, 0, 0, 0, 0, 5, 5, 5],
    [0, 5, 0, 0, 0, 5, 5, 5],
    [5, 0, 0, 0, 0, 5, 5, 5]]

    
    four_wide_count = 0
    while four_wide_count < 1:
       four_wide_count += add_ship(3, 4)

    three_wide_count = 0
    while three_wide_count < 2:
        three_wide_count += add_ship(2, 3)

    two_wide_count = 0
    while two_wide_count < 2:
        two_wide_count += add_ship(1, 2)

    one_wide_count = 0
    while one_wide_count < 0:
        one_wide_count += add_ship(0, 1)
    #scan_hit(4)


#robMap = probMap / runs
#probMap = probMap - probMap.mean(axis=0)
#probMap = probMap / np.abs(probMap).max(axis=0)
i,j = np.unravel_index(probMap.argmax(), probMap.shape)
print("X/Y: " + str(j+1) + str(i+1))
plt.imshow(probMap, cmap='jet')
plt.show()
