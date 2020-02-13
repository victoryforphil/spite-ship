import gym

from stable_baselines import DQN
from stable_baselines.common.evaluation import evaluate_policy


# Create environment
env = gym.make('gym_ship:ship-v0')

# Instantiate the agent
model = DQN('MlpPolicy', env, learning_rate=2e-3, prioritized_replay=True, verbose=1)
# Train the agent
model.learn(total_timesteps=int(2e5))
# Save the agent
model.save("dqn_ship")
#del model  # delete trained model to demonstrate loading

# Load the trained agent
#model = DQN.load("dqn_ship")

# Evaluate the agent
#mean_reward, n_steps = evaluate_policy(model,env, n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
for i in range(55):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()