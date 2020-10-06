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

#Q6
animals = ["Lion", "Bear", "Whale"]
animals.append("Rhino")
print(animals)
print(animals[2])
del animals[0]
print(animals)
