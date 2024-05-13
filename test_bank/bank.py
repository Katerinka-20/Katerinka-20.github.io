def main():
    greeting = input("Приветствие: ")
    result = value(greeting)
    print(result)

def value(greeting):
    first_word = greeting.split()[0]
    first_letter = first_word[0]
    if first_word == "здравствуйте":
        return 0
    elif first_letter == "з" and first_word != "здравствуйте":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
