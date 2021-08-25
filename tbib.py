import requests
import time

URL_API = 'https://tbib.org/index.php?page=dapi&s=post&q=index&tags={0}&pid={1}'

try:
    import art
    print(art.text2art('RB downloader'))
    print("                                         by L0k1")
    print("\r\n")

except:
    print("RB downloader\r\nby l0k1")

def getpostscount(tags):
    api = URL_API.format('+'.join(tags.split()), 0)
    data = requests.get(api).text.split('>')[1]. split(" ")[1]. split('"')[1]
    print (data)
    return int(data)

def inttopages(integer):
    pages = int()
    if integer>=101:
        pages = int(integer/100)+1
        return(pages)
    else: return(0)

def getallimages(tags):
    images = list()
    for pid in range(inttopages(getpostscount(tags))):
        api = URL_API.format('+'.join(tags.split()), pid)
        xmldata = requests.get(api).text.split('>')
        for i in range(len(xmldata)-4):
            i = i + 2
            post = str(xmldata[i]).replace('\r', '').replace('\n', '')[1: -1]
            imageurl = post.split(' ')[3].split('"')[1]
            
            nameforfile='+'.join(tags.split())
            try:
            
                img = requests.get(imageurl, timeout=7.5)
                img_file = open('./'+str(nameforfile)+str(imageurl).split("/")[-1], 'wb')
                img_file.write(img.content)
                img_file.close() 
                print(" ✓ | File saved: "+str(nameforfile)+str(imageurl).split("/")[-1])
                
            except:
                print(" X | Loading error: "+imageurl)

        time.sleep(1)
    return images

pornlist = []

print("Enter the tags you need to download\nLeave the field blank to start downloading")
while True:
    inputdata = input("Tags: ")
    if inputdata == "":
        break

    pornlist.append(inputdata)
        

for tags in pornlist:
    getallimages(tags)
        
print()   
print(" ✓ | Loading is complete")

#'https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={0}&pid={1}' 