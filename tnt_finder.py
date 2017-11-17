from mcpi.minecraft import Minecraft
import random
from time import sleep

running = True
finding = False

mc = Minecraft.create()
#specify ip address and port
#mc = minecraft.Minecraft.create("192.168.1.28", 4711)
from mcpi.minecraft import Minecraft
import random
from time import sleep

WOOL=35

running = True
finding = False
leap = 2

global x
global y
global z
global tnt_x
global tnt_y
global tnt_z
global pl_x
global pl_y
global pl_z

mc = Minecraft.create()
#specify ip address and port
#mc = minecraft.Minecraft.create("192.168.1.28", 4711)

def start_tnt_find():


    tnt_x=x
    tnt_y=y
    tnt_z=z
    
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        pl_x, pl_y, pl_z=mc.entity.getPos(entityId)

    #r = i % 2

    #if r > 0:
        #team.append("b")
    #elif r == 0:
        #team.append("a")

    #print(team[i])
    

def tnt_find():
    if tnt_x > pl_x:
        tnt_x=tnt_x-leap
    if tnt_x > pl_x:
        tnt_x=tnt_x+leap
    if tnt_y > pl_y:
        tnt_y=tnt_y-leap
    if tnt_y > pl_y:
        tnt_y=tnt_y+leap
    if tnt_z > pl_z:
        tnt_z=tnt_z-leap
    if tnt_z > pl_z:
        tnt_z=tnt_z+leap
    mc.setBlock(tnt_x, tnt_y, tnt_z, 46,1)
        

while running:
    x, y, z = mc.player.getPos()
    blockObj = mc.getBlockWithData(x,y,z-1)
    if blockObj.id==WOOL and finding==False:
        start_tnt_find()
        finding=True
        
    if finding==True:
        tnt_find()
    print (finding)
    print(blockObj)
