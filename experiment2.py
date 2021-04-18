import os
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.oggvorbis import OggVorbis
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3

# apply metadata to FLAC audio files based on specific filename structure
# example filename: 07. M-Project - Pure Powerstomper (feat. Jonjo) [(Refix)].flac

# load folder
basefolder = 'D:\\mega\\z_hold\\test'

with os.scandir(basefolder) as folder:

    # specify track being worked on
    for track in folder:
        if track.is_file():

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
            print("#:", trnumber, "artist:", trartist, "title:", trtitle, "filetype:", trtype)

            # mutagen me captain
            trpath = basefolder + "\\" + track.name

            # understand filetype
            skipvar = False
            if trtype == "flac":
                trfile = FLAC(trpath)
            if trtype == "ogg":
                trfile = OggVorbis(trpath)
            if trtype == "mp3":
                trfile = MP3(trpath)
                # skipvar = True
            if trtype == "m4a":
                trfile = MP4(trpath)
                # skipvar = True

            # apply mutagen to the problem
            if not skipvar:
                trfile["tracknumber"] = trnumber
                trfile["title"] = trtitle
                trfile["artist"] = trartist
                trfile.save()
                print("Track data saved")
            else:
                print("Track skipped")
