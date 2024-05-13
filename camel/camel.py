def camelcase_to_snake_case(s):

    def substitute_character(index_character):
        (index, c) = index_character

        if c.isupper() and index != 0:
            return '_' + c.lower()
        elif c.isupper():
            return c.lower()
        else:
            return c

    return (
        ''.join(
            map(
                substitute_character,
                enumerate(s),
            )
        )
    )

def main():
    temp = (input("Р’РµСЂР±Р»СЋР¶РёР№ СЃС‚РёР»СЊ: "))
    result = camelcase_to_snake_case(temp)
    print(result)

if __name__ == "__main__":
    main()


