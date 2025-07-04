# Squid_Game_Glass_Bridge
📋 Features

Simulates Squid Game's Glass Bridge challenge

Models learning from earlier players' failures

Runs thousands of simulations

Plots survival rates by player position using matplotlib

🧠 How It Works

Each step has two panels: Left (L) and Right (R); one is randomly safe.

Players go in order (1 to 16), choosing a panel at each step.

If a player picks wrong, they fall, but later players benefit from knowing where others fell.

You simulate this process many times for each position to find which spots are most likely to survive.

▶️ Usage

1. Requirements

Python 3.x

Install matplotlib:

pip install matplotlib

2. Run the simulation

python main.py

Then enter the number of simulations to run (e.g., 1000).

You’ll get a bar graph showing how likely each position (1–16) is to survive.
