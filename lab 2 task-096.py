def custom_fizzbuzz(number, word_for_3, word_for_5):
    result = []
    for num in range(1, number + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append(word_for_3 + word_for_5)
        elif num % 3 == 0:
            result.append(word_for_3)
        elif num % 5 == 0:
            result.append(word_for_5)
        else:
            result.append(str(num))
    return result


try:
    number = int(input("Enter the upper limit for the custom FizzBuzz game: "))
    
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        word_for_3 = input("Enter a custom word for multiples of 3: ")
        word_for_5 = input("Enter a custom word for multiples of 5: ")
        
        custom_fizzbuzz_result = custom_fizzbuzz(number, word_for_3, word_for_5)
        
        print("\n".join(custom_fizzbuzz_result))

except ValueError:
    print("Invalid input. Please enter a positive integer.")
