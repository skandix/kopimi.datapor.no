def countfreq(my_list):

    freq = {}

    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print(key + " :", value)


print("Please enter you word. type stop to exit.")
user_input = input("")
count = 0
thisdict = {}
mydict = []

while user_input != "stop":
    word = user_input
    count += 1
    mydict.append(word)
    thisdict.update({word: count})
    user_input = input("")

print("Unique :", len(thisdict))
print("Total :", count)
countfreq(mydict)
