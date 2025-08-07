from PIL import Image
import os

filepath = input("Enter file path of function folder in datapacks: ")
ImagesFilepath = input("Enter file path of the folder with Bad Apple frames: ")

x = int(input("The following is the xyz coordinates of the bottom right corner of the screen, facing west.\nx-coordinate: "))
y = int(input("y-coordinate: "))
z = int(input("z-coordinate: "))

def generate(frame):
    f = open(f"{filepath}/signs{frame}.mcfunction", "x")

    im = Image.open(f"{ImagesFilepath}/frame{frame}.jpg")
    pix = im.load()
    size = im.size

    CurrentSign = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(80):
        for j in range(60):
            sign(i, j, pix, CurrentSign, frame)
    
    with open(f"{filepath}/signs{frame}.mcfunction", "a") as f:
        f.write("\n"+f"schedule function uh:signs{frame+1} 4t")
        print(f"signs #{frame} completed")

def sign(Xoffset, Yoffset, pix, CurrentSign, frame):
    for i in range(3, -1, -1):
        for j in range(11): #239
            if pix[j + (Xoffset*22),117 - (i + (Yoffset*8))][1] > 200:
                CurrentSign[-i][j] = 1
            else:
                CurrentSign[-i][j] = 0

    base = f"pale_oak_wall_sign"
    base += "[facing=east]{front_text:{color:\"white\",messages:[{\"text\":\"\",\"extra\":["

    for i in range(len(CurrentSign)):
        for j in range(len(CurrentSign[i])):
            if CurrentSign[i][j] == 1 and j == 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"}]} ,"
            elif CurrentSign[i][j] == 1 and j != 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},"

            
            if CurrentSign[i][j] == 0 and j == 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"}]} ,"
            elif CurrentSign[i][j] == 0 and j != 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},"
            
            if CurrentSign[i][j] == 2 and j == 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/light_gray_concrete_powder\"}]} ,"
            elif CurrentSign[i][j] == 2 and j != 10:
                base += "{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/light_gray_concrete_powder\"},"


        if i != 3:
            base += "{\"text\":\"\",\"extra\":["
    base = base[:-2] + "]}}"
    if base == "pale_oak_wall_sign[facing=east]{front_text:{color:\"white\",messages:[{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/black_concrete\"}]}]}}":
        base = f"function uh:fb {{\"x\":\"{x}\",\"y\":\"{y+Yoffset}\",\"z\":\"{z-Xoffset}\"}}"
    elif base == "pale_oak_wall_sign[facing=east]{front_text:{color:\"white\",messages:[{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"}]} ,{\"text\":\"\",\"extra\":[{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"},{\"type\":\"object\",\"atlas\":\"minecraft:blocks\",\"sprite\":\"block/snow\"}]}]}}":
        base = f"function uh:fw {{\"x\":\"{x}\",\"y\":\"{y+Yoffset}\",\"z\":\"{z-Xoffset}\"}}"
    else:
        base = f"setblock {x} {y+Yoffset} {z-Xoffset} " + base

    with open(f"{filepath}/signs{frame}.mcfunction", "a") as f:
        f.write("\n"+base)

for i in range(int(input("start frame: ")),int(input("stop frame: "))+1):
    generate(i)
