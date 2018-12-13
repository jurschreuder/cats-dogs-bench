from PIL import Image
import os


inFolder = "raw"
size = 128
outFolder = str(size)+"x"+str(size)
border = 0

os.makedirs(outFolder+"/pre-train")
os.makedirs(outFolder+"/100")
os.makedirs(outFolder+"/250")
os.makedirs(outFolder+"/500")
os.makedirs(outFolder+"/1000")
os.makedirs(outFolder+"/test")

def cutScale(im, border, size):
    # get smallest side 
    w, h = im.size
    s = w
    if h < s:
        s = h

    # crop picture
    im = im.crop((s*border, s*border, s-s*border, s-s*border))

    # scale picture
    im = im.resize((size, size), Image.ANTIALIAS)
    
    return im

# crawl input folder
i = 0
catsN = 0
dogsN = 0
for path, subdirs, files in os.walk(inFolder):
    for name in files:
        if name.endswith(".jpg"):
            im = Image.open(os.path.join(path, name))
            im = cutScale(im, border, size)
            if name.startswith("cat"):
                if catsN < 50:
                    im.save(outFolder+"/100/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if catsN < 125:
                    im.save(outFolder+"/250/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if catsN < 250:
                    im.save(outFolder+"/500/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if catsN < 500:
                    im.save(outFolder+"/1000/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                elif catsN < 1000:
                    im.save(outFolder+"/test/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                else:
                    im.save(outFolder+"/pre-train/"+name.replace(".jpg", "")+str(i)+".jpg")
                    im = im.transpose(Image.FLIP_LEFT_RIGHT)
                    im.save(outFolder+"/pre-train/"+name.replace(".jpg", "")+str(i)+"-flip.jpg")
                    i += 1

                catsN += 1
                
            if name.startswith("dog"):
                if dogsN < 50:
                    im.save(outFolder+"/100/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if dogsN < 125:
                    im.save(outFolder+"/250/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if dogsN < 250:
                    im.save(outFolder+"/500/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                if dogsN < 500:
                    im.save(outFolder+"/1000/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                elif dogsN < 1000:
                    im.save(outFolder+"/test/"+name.replace(".jpg", "")+str(i)+".jpg")
                    i += 1
                else:
                    im.save(outFolder+"/pre-train/"+name.replace(".jpg", "")+str(i)+".jpg")
                    im = im.transpose(Image.FLIP_LEFT_RIGHT)
                    im.save(outFolder+"/pre-train/"+name.replace(".jpg", "")+str(i)+"-flip.jpg")
                    i += 1

                dogsN += 1

            
