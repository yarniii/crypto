# Сдвиг на 13 символов

rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')



def rot13(text):
    return text.translate(rot13trans)


def main():
    txt=input()

    print (rot13(txt))


if __name__ == "__main__":
    main()