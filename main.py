import os
from mutagen.flac import FLAC

# apply metadata to FLAC audio files based on specific filename structure
# example filename: 07. M-Project - Pure Powerstomper (feat. Jonjo) [(Refix)].flac

# load folder to apologize to later
basefolder = 'D:\\mega\\'

with os.scandir(basefolder) as folder:

    # specify track being worked on
    for track in folder:
        if track.is_file():

            # debug print me the track filename
            print(track.name)

            # make filename into nice string
            filename = track.name

            # give me track number
            trdata = filename.split(". ", 1)
            trnumber = trdata[0]

            # give me track artist
            trdata = trdata[1].split(" - ", 1)
            trartist = trdata[0]

            # give me track title
            trdata = trdata[1].rsplit(".", 1)
            trtitle = trdata[0]
            trtype = trdata[1]

            # debug print me the strings
            print("#:", trnumber, "artist:", trartist, "title:", trtitle)

            # mutagen me captain
            trpath = basefolder + "\\" + track.name

            trfile = FLAC(trpath)

            # apply mutagen to the problem
            trfile["tracknumber"] = trnumber
            trfile["title"] = trtitle
            trfile["artist"] = trartist
            trfile.save()
