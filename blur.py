from PIL import Image
print("Enter image: ")
imgStr = input()
print("Enter blur amount")
BLUR_RAD = int(input())

img = Image.open(imgStr)
imgX,  imgY = img.size[0],  img.size[1]
im = img.load()

for y in  range(0, imgY):
    for x in range(0, imgX-BLUR_RAD):
        avgR,  avgG,  avgB = 0,  0,  0
        for i in range(x-BLUR_RAD,  x+BLUR_RAD+1):
            avgR += im[i, y][0]**2
            avgG += im[i, y][1]**2
            avgB += im[i, y][2]**2
        avgR = int((avgR/(BLUR_RAD*2+1))**0.5)
        avgG = int((avgG/(BLUR_RAD*2+1))**0.5)
        avgB = int((avgB/(BLUR_RAD*2+1))**0.5)
        im[x, y] = (avgR, avgG,  avgB,  255)

for y in  range(0, imgY-BLUR_RAD):
    for x in range(0, imgX):
        avgR,  avgG,  avgB = 0,  0,  0
        for i in range(y-BLUR_RAD,  y+BLUR_RAD+1):
            avgR += im[x, i][0]**2
            avgG += im[x, i][1]**2
            avgB += im[x, i][2]**2
        avgR = int((avgR/(BLUR_RAD*2+1))**0.5)
        avgG = int((avgG/(BLUR_RAD*2+1))**0.5)
        avgB = int((avgB/(BLUR_RAD*2+1))**0.5)
        im[x, y] = (avgR, avgG,  avgB,  255)
        
img.save("image2.png")
