songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0:2])

songs[2] = "Yamborghini High"
print(songs)

songs.extend(["HOUSTONFORNICATION", "WINGS", "Praise The Lord"])
print(songs)

del songs [1]
print(songs)

animals = ["Tiger", "Panda", "Polar Bear"]
animals.append("Black Panther")
print(animals)

print(animals[3])
del animals[0]

for animal in animals:
    print(animal)
