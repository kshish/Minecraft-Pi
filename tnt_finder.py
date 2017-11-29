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
leap = 1

x=0
y=0
z=0
tnt_x=0
tnt_y=0
tnt_z=0
pl_x=0
pl_y=0
pl_z=0
enemyId=0

mc = Minecraft.create()
#specify ip address and port
#mc = minecraft.Minecraft.create("192.168.1.28", 4711)

def start_tnt_find():


    global tnt_x
    global tnt_y
    global tnt_z
    tnt_x=x
    tnt_y=y
    tnt_z=z
    global enemyId
    
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        pl_x, pl_y, pl_z=mc.entity.getPos(entityId)
        enemyId=entityId

    #r = i % 2

    #if r > 0:
        #team.append("b")
    #elif r == 0:
        #team.append("a")

    #print(team[i])
    

def tnt_find():
    global pl_x
    global pl_y
    global pl_z
    global tnt_x
    global tnt_y
    global tnt_z
    
    pl_x, pl_y, pl_z=mc.entity.getPos(enemyId)
    if tnt_x > pl_x:
        tnt_x=tnt_x-leap
    if tnt_x < pl_x:
        tnt_x=tnt_x+leap
    if tnt_y > pl_y:
        tnt_y=tnt_y-leap
    if tnt_y < pl_y:
        tnt_y=tnt_y+leap
    if tnt_z > pl_z:
        tnt_z=tnt_z-leap
    if tnt_z < pl_z:
        tnt_z=tnt_z+leap
    mc.setBlock(tnt_x, tnt_y, tnt_z, 46,1)
        

while running:
    global x
    global y
    global z
    global finding
    standingOnWool=False
    x, y, z = mc.player.getPos()
    blockObj = mc.getBlockWithData(x,y-1,z)
    if blockObj.id==WOOL:
        standingOnWool=True
        if finding==False:
            start_tnt_find()
            finding=True
            

    
    if standingOnWool==False:
        finding=False
        
    if finding==True:
        tnt_find()
    print (finding)
    print(blockObj)

