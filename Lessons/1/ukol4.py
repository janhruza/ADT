temperatures = [20.5, 21.0, 22.5, 20.0, 19.5, 23.0, 24.0]
window_size = 3
moving_averages = []

for i in range(len(temperatures)):
    window = temperatures[i:i+window_size]
    if len(window) == window_size:
        average = sum(window) / window_size
        moving_averages.append(average)

print(moving_averages)