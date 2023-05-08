numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # створюємо масив

for i in range(len(numbers)): # робимо крок з довжиною в numbers, тобто 10
    for j in range(i+1, len(numbers)): # додаємо +1 допоки довжина numbers не закінчиться
        if numbers[i] + numbers[j] == 10: # умова, що змінні i і j дорівнює 10, то виконуються наступні дії >
            print(numbers[i], "+", numbers[j]) # виводимо змінні i і j з знаком "+" між ними
