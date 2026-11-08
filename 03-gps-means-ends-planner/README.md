# 03 - GPS Means-Ends Planner

A simple General Problem Solver style planner. Each operator has **preconditions**, an **add list**
and a **delete list**, and the planner works backwards from the goal to find a sequence of actions.

Scenarios included in `gps_planner.py`:
- Blocks world (move blocks A, B and C)
- Drive son to school (battery repair, phone call, payment)
- Making a sandwich, preparing coffee, cleaning a room
- Driving to work, building a house
- Grocery shopping and cooking dinner

**Run:** `python gps_planner.py`
**Concepts:** recursion, goal stacks, lists and dictionaries, state-space search
