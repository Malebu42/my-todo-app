contents = ["content of first file",
            "content of second file",
            "content of third file"]

filenames = ["first.txt", "second.txt", "third.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w') #creates a file in files
    # for higher directories (f"../files/{filename}", 'w')
    file.write(content)


a = "i am a" \
    " string"

file = open('files/essay.txt', 'r')
content = file.read() #read for all, readlines for lists
print(content.title())
print(len(content))
file.close()