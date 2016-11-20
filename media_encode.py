import re, os
import subprocess
from collections import Counter

# -------------------------------------------------------------------------------
# CONFIGURABLE SETTINGS
# -------------------------------------------------------------------------------

DEINTERLACE = ''
CODEC = 'libx264'
PRESET = 'superfast'
TUNE = 'film'
PROFILE = 'high'
LEVEL = '4.2'
CRF_VALUE = '20'
FORMAT = 'mkv'

allowedRatios = [ "1,33", "1,55", "1,78", "1,85", "2,35", "2,39", "2,40"]
TMP = r'H:\Temp\test.mkv'

# -------------------------------------------------------------------------------
# Script
# -------------------------------------------------------------------------------

def getFiles():
    cwd = os.getcwd()
    # get a list of files that have the extension txt
    filelist = filter(lambda f: f.split('.')[-1] == 'mkv', os.listdir(cwd))
    filelist = sorted(filelist)

#    print( filelist)
    if os.path.exists( 'converted') == False:
        os.mkdir( 'converted')

    if filelist is not "":
        for file in filelist:
            print( file)
            encode(file, r"converted/" + file)


def encode(INPUT, OUTPUT):
#    try:
        command = [ 'ffmpeg', '-i', INPUT,
            '-map', '0:m:language:eng?', '-map', '0:m:language:deu?',
            '-c:v', CODEC, '-tune', TUNE, '-preset', PRESET, '-profile:v', PROFILE, '-level', LEVEL, '-crf', CRF_VALUE,
            '-vf', cropDetect( INPUT),
            '-c:a', 'copy', '-c:s', 'copy', OUTPUT
            ]

        pipe = subprocess.Popen(command, stdout = subprocess.PIPE, bufsize=10**8)
        print ( pipe)
#    except:
#        pass

def cropDetect( file):
    print("File to detect crop: %s " % file)
    p = subprocess.Popen( ["ffmpeg", "-i", file, "-an", "-vf", "cropdetect=24:16:0", "-vframes", "500", "-y", TMP ],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10 ** 8)
    infos = p.stderr.read()
    print (infos)
    allCrops = re.findall("crop=\S+", str(infos))
    mostCommonCrop = Counter(allCrops).most_common(1)
    if mostCommonCrop == []:
        crop = ""
    else:
        mostCommonCropSolo = str(mostCommonCrop[0][0])
        mostCommonCropStr = mostCommonCropSolo.split(r"\r\n")
        crop = mostCommonCropStr[0]

    #os.remove( 'autocrop.mkv')
    return crop

def correctAR( crop, orgDimentions):
    allowedRatios.sort()
    orgRatio = 1.78
    # crop=1920:1072:0:4
    croplst = crop.split("=", 1)
    w, h, x, y = croplst[1].split(":")
    ratio = float(w)/float(h)

    i = 0
    while allowedRatios[i] <= ratio and i < len(allowedRatios)-1:
        i+=1

    if allowedRatios[i] == ratio:
        print ( "Nothing to do!")
        return crop
    else:
        middle = allowedRatios[i-1] + (allowedRatios[i]-allowedRatios[i-1])/2
        if ratio < middle:
            newRatio = allowedRatios[i-1]
        else:
            newRatio = allowedRatios[i]

        if newRatio > orgRatio:
            pass
    print( round(ratio, 2), "-->", newRatio)


def checkcrop( INPUT, crop="1920:800:0:140", color="red"):
    w, h, x, y =  crop.split(":")
    box = x + ":" + y + ":" + w + ":" + h + ":" + color +"@0.1:t=max"

    #ffplay -i <input> -vf drawbox=0:140:1920:800:red
    command = [ 'ffplay', '-i', INPUT, "-an", "-sn",
        '-vf', "drawbox="+ box +',scale=w=iw/2:h=ih/2',
        "-loglevel", "quiet",
        ]

    pipe = subprocess.Popen(command, stdout = subprocess.PIPE, bufsize=10**8)



# ffmpeg -i The_Hobbit_An_Unexpected_Journey_t05.mkv -ss 120 -t 120 -map 0:m:language:eng? -map 0:m:language:deu? -c:v "libx264" -preset fast -profile:v high -level 4.2 -crf 20 -tune film -c:a copy -c:s copy -threads 12 preview.mkv

if __name__ == "__main__":
    getFiles()
