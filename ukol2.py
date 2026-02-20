scores = [50, 80, 45, 90, 30, 60]
for i in scores:
    if i < 50:
        scores.remove(i) # pro jednoduchy  seznam funguje, ale pro slozitjsi ne
print(scores)