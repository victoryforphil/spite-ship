import gym
import random
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

# Map Def
# 0 - Empty
# 1 - Ship
# -1 - Miss


class ShipEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ai']}

    def __init__(self):

        self.action_space = spaces.Discrete(100)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(10, 10))

        self.reward_range = (0, 1.0)

      # test

    def step(self, action):
        self.current_step += 1

        delay_modifier = (self.current_step / 50)

        highest_y = 0
        highest_x = 0
        found_valid_hit = False

        reward = 0

        while found_valid_hit is False:
            x = 0
            y = 0
            for i in range(100):
                
                if x >= 10:
                    x = 0
                    y += 1

                if i == action:
                    highest_y = y
                    highest_x = x
                    found_valid_hit = True
                x += 1

        if self.ships[highest_y][highest_x] is not 0:
            self.hits += 1
            #reward = 1 * delay_modifier
            self.map[highest_y][highest_x] = 1
            # hit
        else:
            # miss

            self.map[highest_y][highest_x] = -1

        done = self.current_step > 51 or self.hits >= 16

        reward = (self.hits / 16)

        return np.array(self.map), reward, done, {}

    def reset(self):
        self.current_step = 0
        self.hits = 0
        self.map = [
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

        self.ships = [
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

        def check_place(start_x, start_y, end_x, end_y):

            if end_y >= 10 or end_x >= 10:

                return False

            for y in range((end_y-start_y) + 1):
                for x in range((end_x - start_x) + 1):
                    true_x = start_x + x
                    true_y = start_y + y

                    if self.ships[max(0, true_y - 1)][max(0, true_x - 1)] is not 0:
                        return False
                    if self.ships[true_y][true_x] is not 0:
                        return False
                    if self.ships[min(9, true_y + 1)][min(9, true_x + 1)] is not 0:
                        return False

            return True

        def add_ship(width, val):

            ran_x = random.randrange(-1, 10)
            ran_y = random.randrange(-1, 10)
            orient = random.randrange(0, 10)

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
                            self.ships[true_y][true_x] = val

                return 1
            else:

                return 0

        four_wide_count = 0
        while four_wide_count < 1:
            four_wide_count += add_ship(3, 4)

        three_wide_count = 0
        while three_wide_count < 2:
            three_wide_count += add_ship(2, 3)

        two_wide_count = 0
        while two_wide_count < 3:
            two_wide_count += add_ship(1, 2)

        one_wide_count = 0
        while one_wide_count < 4:
            one_wide_count += add_ship(0, 1)
        return np.array(self.map)

    def render(self, mode='human'):
        dismap = []
        for i in range(10):
            dismap.append(["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "])
        
        hits = 0
        for i in range(10):
            for j in range(10):

                if self.ships[i][j] is not 0:
                    dismap[i][j] = "■ "

                if self.map[i][j] is 1:
                    dismap[i][j] = "* "
                    hits += 1
                if self.map[i][j] is -1:
                    dismap[i][j] = "o "

        for i in range(10):
            for j in range(10):
                print(dismap[i][j] , end="")
            print("")
        print("------ HITS: " + str(hits))

        # test

    def close(self):
        print("")
        # test
