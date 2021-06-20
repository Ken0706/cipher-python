def caesarCipher() -> str:
    mess = input("Enter text: ")
    lst = []
    # get index of lower characters
    for i, v in enumerate(mess):
        if v.islower():
            lst.append(int(i))
    mess = mess.upper()
    while True:
        mode = input("Enter mode ('encrypt' or 'decrypt'): ")
        if mode == 'encrypt' or mode == 'decrypt':
            break
    tranlasted = ""
    tmp = ""
    key = int(input("Enter number key: "))
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for character in mess:
        if character.upper() in LETTERS:
            # get index of character in letters
            index = LETTERS.find(character)
            if mode == 'encrypt':
                index += key
            else:
                index -= key
            # check if index >= 26 or index < 0
            if index >= len(LETTERS):
                index -= len(LETTERS)
            elif index < 0:
                index += len(LETTERS)
            tmp += LETTERS[index]
        else:
            tmp += character
    for i, v in enumerate(tmp):
        if i in lst:
            tranlasted += v.lower()
        else:
            tranlasted += v
    return tranlasted


def main():
    print("Text after use Caesar cipher: " + caesarCipher())


if __name__ == '__main__':
    main()
