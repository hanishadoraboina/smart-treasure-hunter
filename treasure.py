import random

# ==========================
# Grid Configuration
# ==========================

ROWS = 2
COLS = 3

start_state = (0, 0)
goal_state = (1, 2)
fire_state = (1, 1)

actions = ["UP", "DOWN", "LEFT", "RIGHT"]


# ==========================
# Display Grid
# ==========================

def print_grid(agent_state):

    print("\nGrid World")

    for row in range(ROWS):

        print("+-----+-----+-----+")

        for col in range(COLS):

            if (row, col) == agent_state:
                cell = " 🤖 "

            elif (row, col) == fire_state:
                cell = " 🔥 "

            elif (row, col) == goal_state:
                cell = " 💎 "

            else:
                cell = "     "

            print("|" + cell, end="")

        print("|")

    print("+-----+-----+-----+")


# ==========================
# Reward Function
# ==========================

def get_reward(state):

    if state == goal_state:
        return 10

    elif state == fire_state:
        return -10

    return -1


# ==========================
# Transition Function
# ==========================

def next_state(state, action):

    row, col = state

    if action == "UP":
        row = max(0, row - 1)

    elif action == "DOWN":
        row = min(ROWS - 1, row + 1)

    elif action == "LEFT":
        col = max(0, col - 1)

    elif action == "RIGHT":
        col = min(COLS - 1, col + 1)

    return (row, col)


# ==========================
# Start Simulation
# ==========================

current_state = start_state

steps = 0
total_reward = 0

print("\n🤖 Treasure Hunter Started")

print("\nLegend")
print("🤖 = Agent")
print("🔥 = Fire")
print("💎 = Treasure")

print_grid(current_state)


# ==========================
# Agent Loop
# ==========================

while current_state != goal_state and current_state != fire_state:

    print("\n--------------------------")

    print("Current State :", current_state)

    action = random.choice(actions)

    print("Action Chosen :", action)

    new_state = next_state(current_state, action)

    reward = get_reward(new_state)

    print("New State     :", new_state)
    print("Reward        :", reward)

    current_state = new_state

    total_reward += reward
    steps += 1

    print_grid(current_state)


# ==========================
# Final Result
# ==========================

print("\n==========================")

if current_state == goal_state:

    print("💎 TREASURE FOUND!")
    print("🎉 Mission Successful!")

elif current_state == fire_state:

    print("🔥 FELL INTO FIRE!")
    print("❌ Mission Failed!")

print("\nTotal Steps  :", steps)
print("Total Reward :", total_reward)

print("==========================")