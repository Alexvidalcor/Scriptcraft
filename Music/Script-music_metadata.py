# native libraries
import os

# third party libraries
import mutagen
import pandas as pd


# main vars
musicPath = "test"

# functions
def fileModifier(filePath):
    '''
    Modify metadata
    return music file with metadata modified
    '''
    try:
        fileName = filePath.split("/")[-1]
        fileSplitter = fileName[:-4].split(" - ")

        fileArtist = fileSplitter[0]
        fileTitle = fileSplitter[1]
        fileFormat = fileName[-4:]

        df.loc[len(df)] = [fileArtist, fileTitle, fileFormat, "OK"]

    except IndexError:
        df.loc[len(df)] = ["NO", "NO", "NO", fileSplitter]

# execution
df = pd.DataFrame(columns=["Artist","Title","Format","Result"])

for currentDir, subFolders, files in os.walk(musicPath):
    for file in files:
        filePath = os.path.join(currentDir, file)
        fileModifier(filePath)

df.to_csv("test.csv", index=False)
    




# a = mutagen.File("",easy=True)

# fileMusic = ""
# fileSplitter = ""[:-4].split(" - ")
# formatDetector = fileMusic[-4:]


# a.delete()
# a.saver()

# a.add_tags()
# a.tags["artist"]=""
# a.tags["title"]=""

# print(a.tags)




# # a.delete()
# # a.saver()