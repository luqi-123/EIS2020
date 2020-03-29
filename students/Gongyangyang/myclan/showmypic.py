import cv2 
import numpy as np 
import mcpi.minecraft as minecraft
import mcpi.block as block
import time



def mcsimg(x0,y0,z0,img,b,a):
    img1 = cv2.imread(img, 0) 
    ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    resized_image = cv2.resize(thresh1,(b,a))
    L = len(resized_image)
    W = len(resized_image[0])
    H = 0
    pat = resized_image          
    for x in range(L):
        for z in range(W):
            time.sleep(0.01)
            if pat[x][z] == 0:
                mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.STONE.id)
            # elif pat[x][z] == 2:
            #     mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.DIAMOND_BLOCK.id)
            # elif pat[x][z] == 3:
            #     mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.REDSTONE_ORE.id)
            else:
                mc.setBlock(x0+L-x-1, y0+H-1, z0+z,block.IRON_BLOCK.id)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


# mcsimg(pos.x,pos.y,pos.z,resized_image)

