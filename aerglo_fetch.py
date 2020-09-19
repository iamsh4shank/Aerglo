import sys
import requests
import json
from skimage import io
import matplotlib.pyplot as plt
from galaxy_classifier import initialize, initial


def apod(date):
    url = "https://api.nasa.gov/planetary/apod?api_key=FyP5abZv4Le0RahAWvkPXySz2LaYJ2Jgtar40V02&date="+date
    response = requests.get(url).json()
    img = response["hdurl"]
    info = response["explanation"]
    a = io.imread(img)
    plt.imshow(a)
    plt.show()
    print ("Date: "+ response["date"]+"\n")
    print("Info about the image: \n"+info+"\n")

def marsRover(id):
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=FyP5abZv4Le0RahAWvkPXySz2LaYJ2Jgtar40V02"
    response = requests.get(url).json()
    for r in response['photos']:
        if (r['id'] == id):
            img = r['img_src']
    a = io.imread(img)
    plt.imshow(a)
    plt.show()
    
def epic(dateUse, imgName):
    imgUrl = 'https://api.nasa.gov/EPIC/archive/natural/'+dateUse+'/png/epic_1b_'+imgName+".png?api_key=FyP5abZv4Le0RahAWvkPXySz2LaYJ2Jgtar40V02"
    a = io.imread(imgUrl)
    plt.imshow(a)
    plt.show()
    
def earth(lat, lon):
    url = "https://api.nasa.gov/planetary/earth/assets?lon=" + lon+"&lat="+lat + "&date=2018-01-01&&dim=0.10&api_key=FyP5abZv4Le0RahAWvkPXySz2LaYJ2Jgtar40V02"
    response = requests.get(url).json()
    img = response['url']
    a = io.imread(img)
    plt.imshow(a)
    plt.show()
    
argList = []
for arg in sys.argv:
    argList.append(arg)
if (len(argList) != 2):
    print("Error: No such command exist, enter 'python3.6 aerglo_fetch.py -help' for help")
if (argList[0]+argList[1] == 'aerglo_fetch-help'):
    print ('Help...\nEnter "./aerglo_fetch <choice>"\nwhere choice can be ->'
                   '\n    -apod    for astronomy picture of the day'
                   '\n    -marsR   for fetching image taken by mars rover'
                   '\n    -epic    for earth polychromatic imaging camera'
                   '\n    -earth   for earth observation data'
                   '\n    -clGal   Classify galaxy')
    
if (argList[1] == '-apod'):
    date = str(input("Enter date(YYYY-MM-DD) to fetch image: "))
    apod(date)
elif (argList[1] == '-marsR'):
    id = int(input("Enter id: "))
    marsRover(id)
elif (argList[1] == '-epic'):
    dateUse = str(input("Enter date(YYYY/MM/DD): "))
    imgName = str(input("Enter image name: "))
    epic(dateUse, imgName)
elif (argList[1] == '-earth'):
    lat = str(input("Enter latitude: "))
    lon = str(input("Enter longitude: "))
    earth(lat, lon)
elif (argList[1] == '-clGal'):
    print ("Do you want to use demo data(Y/N): ")
    ch = str(input())
    if (ch.lower() == 'y'):
        initialize()
    elif (ch.lower() == 'n'):
        fName = str(input("Enter NumPy file name: "))
        initial(fName)
    else:
        print ("Enter correct choice in Y or N")
else:
    print("No such options found, enter 'python3.6 aerglo_fetch -help' for help")