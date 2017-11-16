from mcpi.minecraft import Minecraft
import random
from time import sleep

WOOL=35

running = True
finding = False

mc = Minecraft.create()
#specify ip address and port
#mc = minecraft.Minecraft.create("192.168.1.28", 4711)

def start_tnt_find(
    finding=True
    tnt_x=x
    tnt_y=y
    tnt_z=z
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        print(i)
    #r = i % 2

    #if r > 0:
        #team.append("b")
    #elif r == 0:
        #team.append("a")

    #print(team[i])
    i = i + 1


while running:
    x, y, z = mc.player.getPos()
    blockObj = mc.getBlockWithData(0,0,0)
    if blockObj.id==WOOL:
        if block.data==WHITE and finding==False:

        

