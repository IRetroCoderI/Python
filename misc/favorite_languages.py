

fav_languages = {
    'jen': ['python', 'ruby'],
    'jesus': ['java', 'c', 'c++'],
    'sarah': ['c', 'go'],
    'edward': ['ruby', 'javascript', 'sql', 'html'],
    'phil': ['python', 'css', 'cobalt', 'flask']
}



for person, languages in fav_languages.items():
    print(f"\n{person.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")


for name in fav_languages.keys():
    print(name.title())
print("\n")

for langs in fav_languages.values():
    print(langs.title())
print("\n")

for langs in set(fav_languages.values()): #set() ignores repeats
    print(langs.title())

