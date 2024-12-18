animals = ['monkey', 'elephant', 'rabbit']
fruits = ['apple', 'mango', 'banana', 'cherry', 'pear']

for a in animals:
    print(a)

for f in fruits:
    print(f)

# O (len(animals) + len(fruits))

for a in animals:
    for f in fruits:
        print(f'{a} loves {f}')

# O (len(animals) * len(fruits))

a = len(fruits)
while a > 0:
    print(a)
    a = a - 1
    for f in fruits:
        print(f)


# O(F*F) => O(F**2)

def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)

counter(3)