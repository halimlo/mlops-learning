# Day 03 - Python Basics with Road Layers

# Variables
project_name = "RoadTopo QC"
daily_hours = 4
days_per_week = 6
weekly_hours = daily_hours * days_per_week

print("Project:", project_name)
print("Weekly study hours:", weekly_hours)

# List
layers = ["TUF", "GNT", "Tricouche"]

print("\nRoad layers:")
for layer in layers:
    print("-", layer)

# Dictionary
tuf_layer = {
    "name": "TUF",
    "level": -0.23,
    "type": "foundation"
}

print("\nLayer information:")
print("Name:", tuf_layer["name"])
print("Level:", tuf_layer["level"])
print("Type:", tuf_layer["type"])