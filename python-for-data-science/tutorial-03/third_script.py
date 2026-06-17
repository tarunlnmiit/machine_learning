

import numpy as np


# 3 students, 4 tests
grades = np.array([
    [85, 92, 78, 90],   # student 0
    [79, 88, 95, 82],   # student 1
    [91, 76, 84, 88],   # student 2
])

# print(grades.shape)      # (3, 4)
# print(grades[1, 2])      # 95  — student 1, test 2
# print(grades[:, 2])      # [78 95 84]  — all rows, column 2
# print(grades[2, :])      # all columns, row 2

# axis=0 → collapse rows → one value per column (avg score per test)
avg_per_test = grades.mean(axis=0)   # [85.  85.33 85.67 86.67]

# axis=1 → collapse columns → one value per row (avg score per student)
avg_per_student = grades.mean(axis=1)   # [86.25 86.   84.75]

print(avg_per_test)
scores[scores > 90]

print(avg_per_student)