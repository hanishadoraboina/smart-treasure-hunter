# smart-treasure-hunter
A beginner Reinforcement Learning environment built using Python and Markov Decision Process (MDP) concepts.
# smart-treasure-hunter

# 🤖 Smart Treasure Hunter

A beginner-friendly Reinforcement Learning (RL) project built in Python to understand the fundamentals of Markov Decision Processes (MDPs).

The project simulates an agent navigating a GridWorld environment to reach a treasure while avoiding dangerous states. It demonstrates the core concepts of Reinforcement Learning, including states, actions, rewards, transitions, and terminal states.

---

## 🎯 Project Objective

The goal of the agent is to:

* Reach the treasure 💎
* Avoid the fire 🔥
* Maximize total reward
* Interact with the environment through actions

This project focuses on understanding the environment design used in Reinforcement Learning before implementing learning algorithms such as Q-Learning and Deep Q-Networks (DQN).

---

## 🧠 MDP Components

### State Space

The environment consists of the following states:

```text
(0,0)  (0,1)  (0,2)

(1,0)  (1,1)  (1,2)
```

### Action Space

The agent can perform four actions:

* UP
* DOWN
* LEFT
* RIGHT

### Reward Function

| Event             | Reward |
| ----------------- | ------ |
| Reach Treasure 💎 | +10    |
| Enter Fire 🔥     | -10    |
| Normal Move       | -1     |

### Terminal States

* Treasure State 💎 → Success
* Fire State 🔥 → Failure

---

## 🌍 Environment

```text
+-----+-----+-----+
| 🤖  |     |     |
+-----+-----+-----+
|     | 🔥  | 💎  |
+-----+-----+-----+
```

Legend:

* 🤖 Agent Start State
* 🔥 Fire State
* 💎 Goal State

---

## ⚙️ How It Works

1. Agent starts at the initial state.
2. Agent selects a random action.
3. Environment updates the state.
4. Reward is assigned.
5. Process continues until:

   * Treasure is reached, or
   * Fire is reached.

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/hanishadoraboina/smart-treasure-hunter.git
```

Navigate to the project directory:

```bash
cd smart-treasure-hunter
```

Run the program:

```bash
python treasure.py
```

---

## 📊 Sample Output

```text
Current State : (0,1)

Action Chosen : RIGHT

New State : (0,2)

Reward : -1

Current State : (0,2)

Action Chosen : DOWN

New State : (1,2)

Reward : 10

💎 TREASURE FOUND!
🎉 Mission Successful!
```

---

## 🚀 Future Improvements

* Implement Q-Learning
* Add obstacles and walls
* Add larger GridWorld environments
* Implement epsilon-greedy exploration
* Visualize learning progress
* Upgrade to Deep Q Networks (DQN)

---

## 📚 Concepts Learned

* Reinforcement Learning
* Markov Decision Process (MDP)
* State Space
* Action Space
* Reward Function
* Transition Function
* Terminal States
* Agent-Environment Interaction

---

## 👩‍💻 Author

Hanisha Doraboina

B.Tech Artificial Intelligence | MITS

Currently learning Reinforcement Learning, Machine Learning, and AI Engineering.

