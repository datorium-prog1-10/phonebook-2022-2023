file = open("data.txt", "a")
for i in range(101, 201):
    file.write(f"Name{i}\n")
file.close()