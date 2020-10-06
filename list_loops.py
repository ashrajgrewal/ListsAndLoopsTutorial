#AshrajGrewal Lists and Loops Tutorial
#Q1
songs = ["ROCKSTAR", "Do It", "For The Night"]
#Q2
print(songs[0])
print(songs[2])
print(songs[1:3])
#Q3
songs[2] = "We are Young"
print(songs)
#Q4
songs.append("Headlines")
songs.extend(["Twin Turbo", "ElDorado"])
print(songs)
songs.remove("ElDorado")
#del songs[5]
print(songs)
#Q5
#for song in songs:
#    print(song)
#for i in range(len(songs)):
#    print(songs[i], i)
#The difference between these is that the first one allows us to access the elements in the list by element while the second one does it by index.
#Q6
animals = ["Lion", "Bear", "Whale"]
animals.append("Rhino")
print(animals)
print(animals[2])
del animals[0]
print(animals)
for animal in animals:
    print(animal)