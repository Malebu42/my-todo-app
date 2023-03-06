filenames = ["1.2","2.3", "3.4"]

for filename in filenames:
    filenames = filename.replace('.', '-', 1)
    print(filenames)