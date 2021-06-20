from math import ceil


def transDecrypt(text, key) -> str:
    n = len(text)
    numCols = ceil(n / key)
    numRows = key
    boxsNotUse = (numCols * numRows) - len(text)
    translated = [''] * numCols
    col = 0
    row = 0
    for character in text:
        translated[col] += character
        # pointer move next col of translated
        col += 1
        # pointer move next row after add character at end col of translated
        if (col == numCols) or (col == (numCols - 1) and row >= numRows - boxsNotUse):
            col = 0
            row += 1
    return ''.join(translated)


def main():
    print("Text after decrypt: " + transDecrypt('MIloa puyh ? ey', 4))


if __name__ == '__main__':
    main()
