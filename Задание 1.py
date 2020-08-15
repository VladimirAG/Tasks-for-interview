from string import ascii_uppercase

names_summ = {}
word_summ = 0
main_summ = 0
alphabet = {k: v for v, k in enumerate(ascii_uppercase, start=1)}

with open('names.txt', 'r', encoding='utf8') as file:
    names = file.read().split(',')
    names.sort()
    for name in names:
        for letter in range(1, len(name)-1):
            word_summ += alphabet[name[letter]]
        names_summ[name] = word_summ
        word_summ = 0

for count, num in enumerate(names_summ.values(), start=1):
    main_summ += count * num

print(main_summ)
