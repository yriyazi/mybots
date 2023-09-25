
import pybullet as p
import time 

physicsClient = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.loadSDF("box.sdf")
for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()