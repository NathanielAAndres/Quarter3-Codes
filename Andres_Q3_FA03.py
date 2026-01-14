import numpy as np

names = ["Nate", "Keith", "Andrew"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],   # Nate
    [4000, 4100, 3900, 4200, 4600],   # Keith
    [6000, 5800, 5900, 6100, 6200]    # Andrew
])

for i in range(len(names)):
    total_steps = steps[i].sum()
    avg_steps = steps[i].mean()
    min_steps = steps[i].min()
    max_steps = steps[i].max()

print(names[i], "- Total Steps:", int(total_steps), "/", "Average Steps:", int(avg_steps), "/", "Min Steps:", int(min_steps), "/", "Max Steps:", int(max_steps))