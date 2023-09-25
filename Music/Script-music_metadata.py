# native libraries
import os

# third party libraries
from mutagen import File, mp3, id3, mp4, asf, aac, oggopus
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

        fileFormat = fileName[-4:]
        fileArtist = fileSplitter[0]
        fileTitle = fileSplitter[1]
        fileFormat = fileName[-4:]
        fileAlbum = filePath.split("/")[-2]

        df.loc[len(df)] = [fileName, fileArtist, fileTitle, fileFormat, fileAlbum, "OK", "NO", "NO"]

        fileToModify = File(filePath,easy=True)

        fileToModify.delete() # to delete all metatags
        fileToModify.save()

        fileToModify.tags["artist"] = fileArtist
        fileToModify.tags["title"] = fileTitle
        fileToModify.tags["album"] = fileAlbum
        fileToModify.save()

    except IndexError as error:
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat,"NO", "NOOK", "IndexError", str(error)]

    except mp3.HeaderNotFoundError as error: # mutagen.mp3.HeaderNotFoundError: can't sync to MPEG
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "HeaderNotFoundError", str(error)]
    
    except TypeError as error: # TypeError: 'titlename' not a Frame instance
        try:
            fileToModify.add_tags()
            fileToModify.tags["artist"] = fileArtist
            fileToModify.tags["title"] = fileTitle
            fileToModify.tags["album"] = fileAlbum
            fileToModify.save()
            df.loc[len(df)] = [fileName, fileArtist, fileTitle, fileFormat, fileAlbum, "CORRECTED", "TypeError", str(error)]
        except:
            df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "TypeError", str(error)]

    except id3._util.error as error: # mutagen.id3._util.error: an ID3 tag already exists
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat,"NO", "NOOK", "UtilError", str(error)]

    except mp4.MP4StreamInfoError as error:
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "MP4StreamInfoError", str(error)]

    except asf._util.ASFError as error: # mutagen.asf._util.ASFError
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "ASFError", str(error)]

    except mp4.error as error: # mutagen.mp4.error: an MP4 tag already exists
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "MP4error", str(error)]

    except aac.error as error: # mutagen.aac.AACError: doesn't support tags
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "AACerror", str(error)]

    except oggopus.OggOpusHeaderError as error: # mutagen.oggopus.OggOpusHeaderError
        df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO", "NOOK", "OGGerror", str(error)]

    # except Exception as error:
    #     df.loc[len(df)] = [fileName, "NO", "NO", fileFormat, "NO",  "NOOK", "Exception", str(error)]

# execution
df = pd.DataFrame(columns=["FileName", "Artist", "Title", "Format", "Album", "Result", "Error", "ErrorMessage"])


fileTotal = 0
for currentDir, subFolders, files in os.walk(musicPath):
    fileTotal += len(files)
print(f"Total files to process: {fileTotal}")

fileNumber = 0
for currentDir, subFolders, files in os.walk(musicPath):
    for file in files:
        filePath = os.path.join(currentDir, file)
        fileNumber +=1
        fileModifier(filePath)

        if fileNumber == round(fileTotal * 0.25):
            print(f"Processed 25% of the files: {fileNumber}")
        elif fileNumber == round(fileTotal * 0.50):
            print(f"Processed 50% of the files: {fileNumber}")
        elif fileNumber == round(fileTotal * 0.75):
            print(f"Processed 75% of the files: {fileNumber}")



df.to_csv("Music/Scriptcraft-music_logs.csv", index=False)

print(f"Finished, proccessed {fileTotal} music files\nErrors found: {df[df['Result'] == 'NOOK'].shape[0]}\nErrors corrected: {df[df['Result'] == 'CORRECTED'].shape[0]}")