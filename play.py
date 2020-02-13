import gym

from stable_baselines import DQN
from stable_baselines.common.evaluation import evaluate_policy


# Create environment
env = gym.make('gym_ship:ship-v0')

model = DQN.load("dqn_ship")

obs = env.reset()
for i in range(55):
    action, _states = model.predict(obs)
    print(action)
    obs, rewards, dones, info = env.step(action)
    env.render()

    # Taylor's Game
    
    ships = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [5, 0, 0, 0, 0, 0, 0, 0, 5, 0],
    [5, 5, 5, 0, 0, 0, 5, 0, 0, 0],
    [5, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [5, 0, 5, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 5, 5, 0, 0],
    [0, 0, 0, 0, 5, 5, 5, 5, 0, 0],
    [5, 5, 5, 0, 0, 5, 5, 5, 0, 5],
    [5, 5, 5, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 0, 0, 5, 0, 5, 0, 0]]

    

    
    

        ships = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]