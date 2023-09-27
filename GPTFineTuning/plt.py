import matplotlib.pyplot as plt
import json

# Open the file for reading
with open('graphData.json', 'r') as file:
    data = json.load(file)

# Extract the necessary data
timestamps = []
train_loss = []
valid_loss = []

for entry in data:
    if entry['type'] == 'metrics':
        timestamps.append(entry['created_at'])
        train_loss.append(entry['data']['train_loss'])

# Plotting
plt.figure(figsize=(10,6))
plt.plot(timestamps, train_loss, '-o', label='Training Loss', color='blue')
plt.xlabel('Time')
plt.ylabel('Loss')
plt.legend()
plt.title('Train and Validation Loss over Time')
plt.grid(True)
plt.savefig("out.png")
