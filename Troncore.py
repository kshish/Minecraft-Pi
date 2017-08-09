from mcpi.minecraft import Minecraft
import random
from time import sleep

running = True

mc = Minecraft.create()


w, h = 2, 5


team = []

array = [[0 for x in range (w)] for y in range (h)]



entityIds = mc.getPlayerEntityIds()

i = 0


for entityId in entityIds:
    #print(i)
    #r = i % 2

    #if r > 0:
        #team.append("b")
    #elif r == 0:
        #team.append("a")

    #print(team[i])
    i = i + 1
begin = input()

if i/2 == float(i/2)
    redteam = i/2
    blueteam = redteam
else:
    blueteam = i/2 - 1
    redteam = blueteam


if begin == "go"
    mc.setBlock(0, -60, 0, 1)
    mc.setBlock(1, -60, 0, 2)
    mc.setBlock(2, -60, 0, 1)
    mc.setBlock(3, -60, 0, 2)
    mc.setBlock(4, -60, 0, 1)
    mc.setBlock(5, -60, 0, 2)
        
while running:

    iD = mc.getBlock(0,-60,0)
    iD1 = mc.getBlock(1,-60,0)
    iD2 = mc.getBlock(2,-60,0)
    iD3 = mc.getBlock(3,-60,0)
    iD4 = mc.getBlock(4,-60,0)
    iD5 = mc.getBlock(5,-60,0)
    


    if iD == 0 or iD1 == 0 or iD2 == 0:
        redteam = redteam - 1
        mc.setBlock(0, 0, 64, 41)


    elif iD3 == 0 or iD4 == 0 or iD5 == 0:
        blueteam = blueteam - 1

    elif blueteam == 0 or redteam == 0:
        
        mc.setBlock(0, -60, 0, 3)
        mc.setBlock(1, -60, 0, 3)
        mc.setBlock(2, -60, 0, 3)
        mc.setBlock(3, -60, 0, 3)
        mc.setBlock(4, -60, 0, 3)
        mc.setBlock(5, -60, 0, 3)
