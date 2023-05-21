numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(0, len(numbers)+1):
    if numbers[i] > 500:
        break
    if numbers[i] % 5 == 0 and numbers[i] <= 150:
        print(numbers[i])
