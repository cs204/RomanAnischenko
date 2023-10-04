def main():
    sentence = input("Сколько футов:")
    sentence = convert(sentence)
    print(sentence)


def convert(sentence):
    sentence = sentence.replace("180.9ft", "Это будет 55.14 метров.")
    return sentence


main()