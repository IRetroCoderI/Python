filename = 'alice.txt'

with open(filename, 'r') as file_object:
    words = file_object.read()
    words = words.split()

    count = 0
    for word in words:
        if "Alice" in word:
            count = count + 1

def countWords(filename):
    try:
        with open(filename, encoding = 'utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} does not exist, try again or choose new file")
    else:
        words = contents.split()
        wordCount = len(words)
        return wordCount
    
print(f"There are {countWords(filename)} words in the file, \"Alice\" shows up {count} times")

countWords('secretmessage.txt')
countWords('mobydick.txt')
