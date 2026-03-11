def custom_hash(x):
    return (x * 2654435761) % 65536



with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

hash_values = [custom_hash(num) for num in numbers]

for num, hv in zip(numbers, hash_values):
    print(f"Number: {num} -> Hash: {hv}")

distribution = {}
for hv in hash_values:
    if hv not in distribution:
        distribution[hv] = 0
    distribution[hv] += 1

distribution_sorted = sorted(distribution.items())

for hv, freq in distribution_sorted:
    print(f"Hash: {hv}, Frequency: {freq}")
