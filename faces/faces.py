def convert(text):
    # Замена :) на 🙂
    text = text.replace(":)", "🙂")
    # Замена :( на 🙁
    text = text.replace(":(", "🙁")
    return text

def main():
    # Ввод текста от пользователя
    input_text = input("Введите текст: ")
    # Преобразование текста с помощью функции convert
    result = convert(input_text)
    # Вывод результата
    print("Результат:", result)

# Вызов функции main для запуска программы
if __name__ == "__main__":
    main()
