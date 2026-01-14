import numpy as np

names = ["Nate", "Keith", "Andrew"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Nate
    [4000, 4100, 3900, 4200, 4600],  # Keith
    [6000, 5800, 5900, 6100, 6200]   # Andrew
])

steps_total = steps.sum(axis=1)

print("Total steps per person:")
for i in range(len(names)):
    print(names[i], ":", steps_total[i])
max_index = np.argmax(steps_total)
print("Person with highest total steps:")
print(names[max_index], ": ", steps_total[max_index], "steps")

difference = steps_total.max() - steps_total.min()
print("Difference between highest and lowest total steps:", difference)