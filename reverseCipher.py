def reverseCipher() -> str:
    mess = input("Enter text: ")
    translated = ''
    i = len(mess) - 1
    while i >= 0:
        translated += mess[i]
        i -= 1
    return translated


def main():
    print("Text after use reverse cipher: " + reverseCipher())


if __name__ == '__main__':
    main()
