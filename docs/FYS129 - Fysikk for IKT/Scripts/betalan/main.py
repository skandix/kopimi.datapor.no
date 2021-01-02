enc = []
test = [
    20,
    8,
    0,
    2,
    19,
    5,
    58,
    7,
    48,
    54,
    30,
    56,
    46,
    52,
    30,
    43,
    40,
    42,
    36,
    30,
    51,
    39,
    51,
    44,
    30,
    44,
    46,
    35,
    52,
    43,
    52,
    50,
    51,
    50,
    60,
]

test1 = [
    116,
    40,
    93,
    95,
    86,
    99,
    100,
    106,
    95,
    40,
    86,
    91,
    95,
    107,
    43,
    114,
    75,
    56,
    76,
    42,
    40,
    108,
    106,
    42,
    103,
    40,
    86,
    107,
    110,
    92,
    40,
    86,
    101,
    90,
    61,
    58,
    64,
]
enc1 = []

for i in test:
    enc.append(i)
cne = test1[::-1]

cne2 = []
for i in range(00, len(cne), 2):
    cne2.append(cne[i])
for i in range(1, len(cne), 2):
    cne2.append(cne[i])

cne2.reverse()
print(cne)
for i in cne2:
    enc1.append(i)

order = []
order1 = []

for e in enc1:
    order1.append(chr(e))
for e in enc:
    order.append(chr(e))
new1 = ""
new = ""
for x in order:
    new += x
for x in order1:
    new1 += x
print(new1)
