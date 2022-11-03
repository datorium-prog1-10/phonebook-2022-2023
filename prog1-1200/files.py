file = open("data.txt", "w")
for i in range(1, 101):
    file.write(f"Name{i}\n")

file.close()

#UZDEVUMS
#Izveido failu ar nosaukumu data.txt
#Name1
#Name2
#Name3
#...
#Name100