def main():

    print("Please enter 2 strings: ")
    word1 = input(" ")
    word2 = input(" ")

    if word1 == word2:
        print("are equal")
    else:
        print("are not equal")

    if word2 in word1:
        print("is a substring")
    elif word1 in word2:
        print("is a substring")
    else:
        print("is not a substring")


if __name__ == "__main__":
    main()
