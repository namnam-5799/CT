import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

for i in range(len(progresses)):
    progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])

answer = []
now = 0

print(progresses)

for i in progresses:

    if i > now:
        answer.append(1)
        now = i

    else:
        answer[-1] += 1

print(answer)