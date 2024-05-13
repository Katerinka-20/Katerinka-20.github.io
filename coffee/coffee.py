
def main():
    value = 50
    while value>0:
        print(f'Нужная сумма: {value}')
        coin = (input("Вставьте монету: "))
        if coin in ['50','20','10','5']:
            value = value - int(coin)

    if value<0:
        value = value*(-1)
        print(f"Ваша сдача: {value}")
    if value==0:
        print(f"Ваша сдача: {value}")

if __name__ == "__main__":
    main()
