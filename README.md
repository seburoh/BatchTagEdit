# BatchTagEdit
Personal project that uses the additional mutagen method to create metadata for audio files based on their filenames. Currently only works for FLAC/OGGvorbis fileypes, with some code to autoskip mp3/m4a/wav files on purpose.

No apologies that the code is choppy, was created for a hopefully one-off personal need which has been completed. Suggestions to make it less choppy welcome though, always down to learn.

test

# Files
main.py - Handles files with the following naming convention:
* [track #]. [track artist] - [track title].[file type]
* To use: input folder path on line 11.

sansartist.py - Handles files with the following naming convention:
* [track #] [track title].[file type]
* To use: input folder path on line 11.

# Resources
* [Mutagen](https://mutagen.readthedocs.io/en/latest/index.html) is required to run these scripts.