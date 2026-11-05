read = 0

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
        read += 1

print("Total lines in file: ", read)