 = input()

upper_count = 0
lower_count = 0

for muba in x:
    if muba.isupper():
        upper_count += 1
    elif muba.islower():
        lower_count += 1

if upper_count > lower_count:
    print(x.upper())
else:
    print(x.lower())
