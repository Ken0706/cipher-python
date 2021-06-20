def transposEncrypt(text, key) -> str:
    # make column of grid
    translated = [''] * key
    # loop each column
    for column in range(key):
        pointer = column
        while pointer < len(text):
            translated[column] += text[pointer]
            # go pointer to character on next row but same col
            pointer += key
    return f"Text after use transpostition cipher: "+ ''.join(translated)


def main():
    print(transposEncrypt("May I help you?", 4))


if __name__ == '__main__':
    main()
