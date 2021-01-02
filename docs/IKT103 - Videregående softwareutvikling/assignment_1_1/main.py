for number in range(1, 11):
    print(number, end=" ")

print("")
for number in range(2, 21, 2):
    print(number, end=" ")

print("")
for number in range(1, 21, 2):
    print(number, end=" ")

print("")
for number in range(1, 51, 3):
    print(number, end=" ")

print("")
for number in range(40, 1, -4):
    print(number, end=" ")

print("")
for number in range(1, 100 + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, end=" ")


def main():

    if __name__ == "__main__":
        main()
