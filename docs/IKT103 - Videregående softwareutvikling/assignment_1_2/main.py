def reverse(word):
    return word[::-1]


def isPalindrom(word):
    rev = reverse(word)

    if word == rev:
        return True
    return False


def reverseword(word):
    inputWord = input.split(" ")
    inputWord = inputWord[-1::-1]
    output = " ".join(inputWord)
    return output


def main():
    word = input("Please write a word: \n")
    print(len(word))

    ans = isPalindrom(word)
    if ans == 1:
        print("is a palindrome", end=" ")
    else:
        print("is not a palindrome", end=" ")

    print("")
    print(reverse(word))


if __name__ == "__main__":
    main()
