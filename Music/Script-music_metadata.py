import mutagen
import sqlite3

a = mutagen.File("",easy=True)

fileMusic = ""
fileSplitter = ""[:-4].split(" - ")
formatDetector = fileMusic[-4:]


a.delete()
a.saver()

a.add_tags()
a.tags["artist"]=""
a.tags["title"]=""

print(a.tags)