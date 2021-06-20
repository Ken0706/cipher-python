def bruteforceCaesar():
    mess = input("Enter text : ").upper()
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key, value in enumerate(LETTERS):
        translated = ""
        for character in mess:
            if character in LETTERS:
                # get index of character
                index = LETTERS.find(character)
                index -= key
                if index < 0:
                    index += len(LETTERS)
                translated += LETTERS[index]
            else:
                translated += character
        print(f"Key #{key}: {translated}")


def main():
    bruteforceCaesar()


if __name__ == "__main__":
    main()
