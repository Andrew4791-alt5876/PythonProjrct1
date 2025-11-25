import string

"""Программа, которая считает и выводит каких букв в тексте максимальное количество"""

text = """My name is Bob. Each day I drive my kids to school.
My daughter goes to a school that’s far from our house. It takes 30 minutes to get there.
Then I drive my son to his school. It’s close to my job.
I say good morning to all my workmates then I get a big cup of hot coffee.
I turn on my computer and read my email. Some days I have a lot to read.
# Soon I need another cup of coffee."""

resalt = dict.fromkeys(string.ascii_lowercase, 0)
for char in text:
    if char not in resalt:
        continue
    resalt[char] += 1

new_resalt = {}

for letter, cnt in resalt.items():
    new_resalt[cnt] = letter
new_resalt_sort = sorted(new_resalt, reverse=True)
new_resalt_a = new_resalt_sort[:3]
print(new_resalt_a)

new_resalt_b: dict = {}

for i in new_resalt_a:
    new_dict = {key: value for key, value in resalt.items() if i == value}
    for k, v in new_dict.items():
        print(f"{k} - {v}")
