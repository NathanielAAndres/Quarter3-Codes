import numpy as np

names = ["Nate", "Keith", "Andrew"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],   # Nate
    [4000, 4100, 3900, 4200, 4600],   # Keith
    [6000, 5800, 5900, 6100, 6200]    # Andrew
])

total_daily_steps = []

for day_index in range(len(days)):
    total = 0
    for person_index in range(len(names)):
        total += steps[person_index][day_index]
    total_daily_steps.append(total)

print("Total steps per day:")
for i in range(len(days)):
    print(days[i], ":", total_daily_steps[i])

max_day_index = total_daily_steps.index(max(total_daily_steps))
print("Most active day:")
print(days[max_day_index], ":", total_daily_steps[max_day_index], "steps")