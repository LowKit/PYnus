from interpreter import mapdata
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
#settings
aproachtime=1 #time for notes to reach grid
aproachdistance=35 #distance that notes spawn
cameramode=1 #1-spin,2-full lock


if cameramode==1:
    player = FirstPersonController()
    player.speed = 0
    player.jump_height = 0
    player.position = (0, 0, 7)
    print("settings = [camera]=spin,[aproachtime]=",aproachtime,",[aproachdistance]=",aproachdistance)
else:
    print("settings = [camera]=Full Lock,[aproachtime]=",aproachtime,",[aproachdistance]=",aproachdistance)
Sky()
a = Audio('tasrppp', pitch=1, loop=True, autoplay=False)
#Scene
ground=Entity(model="plane",
              visible=True,
              texture="grass",
              collider="mesh",
              position=(0,-2,7),
              scale=(2,0,2))
invisiblegrid = Entity(model="cube",
               visible=False,
               collider="mesh",
               position=(0,0,0.05),
               scale=(100,100,1))
grid1 = Entity(model="cube",
               collider="mesh",
               position=(2,0,0),
               scale=(0.05,3,0.05))

grid2 = Entity(model="cube",
               collider="mesh",
               position=(-2,0,0),
               scale=(0.05,3,0.05))

grid3 = Entity(model="cube",
               collider="mesh",
               position=(0,2,0),
               scale=(3,0.05,0.05))

grid4 = Entity(model="cube",
               collider="mesh",
               position=(0,-2,0),
               scale=(3,0.05,0.05))
cursorgame = Entity(model="cube",
                    texture="customcursor6",
                    collider="mesh",
                    position=(0,0,0.05),
                    scale=(0.525, 0.525, 0))
#-------------------------------------
note = Entity(model="Squircle",
               collider="mesh",
               position=(1,1,0),
               scale=(0.5,0.5,0.5))
a.play()
def update():
    cursorgame.position=(mouse.world_point)
    data = {"_time": 0.671, "_x": 1, "_y": -1}, {"_time": 0.696, "_x": 0, "_y": -1}
    print("songtime",a.time)
    noteamount = len(data)
    for i in range(noteamount):
        songtime =a.time
        time = data[i]["_time"]
        x = data[i]["_x"]
        y = data[i]["_y"]
        speed = (time - songtime) * aproachdistance
        if data[i] == time - aproachtime:
            note = Entity(model="Squircle",
                          collider="mesh",
                          position=(x, y, -speed),
                          scale=(0.5, 0.5, 0.5))
















app.run()