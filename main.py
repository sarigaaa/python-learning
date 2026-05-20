import numpy as np
scores = np.array([
    [85, 90, 78],  
    [72, 68, 80],  
    [91, 95, 88],  
    [60, 55, 70], 
    [77, 82, 79], 
])
names=["Ali","Sara","Raj","mia","tom"]

students_average= scores.mean(axis=1)
for name, average in zip(names, students_average):
    print(f"{name}'s average score: {average:.1f}")

print(f" subaject average: {scores.mean(axis=0)}")

print(f" top score is : {scores.max()}")

top = [names[i] for i, avg in enumerate(students_average) if avg > 80]
print(f"Above 80: {top}")