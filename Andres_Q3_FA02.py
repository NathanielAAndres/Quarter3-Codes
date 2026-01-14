import numpy as np

names = ["Nate", "Keith", "Andrew"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],   # Nate
    [4000, 4100, 3900, 4200, 4600],   # Keith
    [6000, 5800, 5900, 6100, 6200]    # Andrew
])

print("Step Counts (Monday to Friday):")

for i in range(len(names)):
    print(names[i], ":", steps[i])