def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    input_text = input("Введите текст: ", )
    result = convert(input_text)
    print(result)

if __name__ == "__main__":
    main()
