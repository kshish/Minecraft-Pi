from mcpi.minecraft import Minecraft
import random
from time import sleep
running = True
mc = Minecraft.create()
hc = Minecraft.create("10.45.101.11")
time = 1
while running:
    x, y, z = mc.player.getPos()
    
    iD = mc.getBlock(0,-60,0)

    block = mc.getBlockWithData(x,y-1,z)

    if y > 12:
        mc.setBlock(0,-60,0,0)
        
    if iD == 1 and block.id == 35 and block.data == 14:
        mc.setBlock(0, -60, 0, 0)
    
    

    elif iD ==  0:
        mc.player.setPos(0, -10000, 0)
        mc = Minecraft.create("10.45.101.11")
        mc.setBlock(0, -60, 0, 3)
        mc = Minecraft.create()

    elif iD ==  1:
        hc.setBlock(x, y-1, z, 35, 11)

    elif iD ==  2:
        hc.setBlock(x, y-1, z, 35, 14)

    elif iD == 3:
        time = time-1
        time = time + 1
    


