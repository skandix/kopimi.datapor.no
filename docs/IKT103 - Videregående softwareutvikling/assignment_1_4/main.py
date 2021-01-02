def letter_count(word):
    count = {}

    for i in word:
        count[i] = word.count(i)
    for j in count:
        print("'" + j + "'" + " : " + str(count[j]))


def main():

    print("Please enter a string: ")
    word = input("")
    print(letter_count(word))


if __name__ == "__main__":
    main()
