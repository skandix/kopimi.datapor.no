def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

print("Enter numbers. To quit enter 0: ")
average = 0
count = 0
total = 0
user_input = int(input())
thislist = []


while user_input != 0:
    numbers = user_input
    total += numbers
    count += 1
    thislist.append(user_input)
    user_input = int(input())


for x in thislist:
    descending = sorted(thislist, reverse=True)

med = median(thislist)
average = total / count
des = " ".join(repr(x) for x in descending)
print("Average :", int(average))
print("Median :", med)
print("Descending :", des)
