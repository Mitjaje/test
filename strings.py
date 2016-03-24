some_word = "ninja"
print len(some_word)


some_word = "ninja"
print some_word.upper()

big_word = "BIG NINJA"
print big_word.lower()

print big_word.capitalize()

song = "Somewhere over the rainbow"
print song.find("rainbow")

print song.find("ninja")
print song.find("e")

needle = "o"

pos =song.find(needle)

print pos

pos = song.find(needle, pos + 1)
print pos
pos = song.find(needle, pos + 2)
print pos
some_text = open("besedilo.txt", "r").read()
print some_text