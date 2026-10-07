import pybullet as p
import pybullet_data
import time
import math


# ============================================================
# START PYBULLET
# ============================================================

p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.81)


# ============================================================
# GROUND
# ============================================================

p.loadURDF("plane.urdf")


# ============================================================
# ROBOT
# ============================================================

robot = p.loadURDF(
    "kuka_iiwa/model.urdf",
    [0, 0, 0]
)
print("Robot loaded!")

# ============================================================
# SIX JOINTS
# ============================================================

joints = [0, 1, 2, 3, 4, 5]

joint_angles = [
    0,
    0,
    0,
    0,
    0,
    0
]


# ============================================================
# KEYBOARD
# ============================================================

controls = {

    ord('q'): (0, +2),
    ord('a'): (0, -2),

    ord('w'): (1, +2),
    ord('s'): (1, -2),

    ord('e'): (2, +2),
    ord('d'): (2, -2),

    ord('r'): (3, +2),
    ord('f'): (3, -2),

    ord('t'): (4, +2),
    ord('g'): (4, -2),

    ord('y'): (5, +2),
    ord('h'): (5, -2)
}


# ============================================================
# DISPLAY J1-J6 ANGLES IN PYBULLET
# ============================================================

angle_text = p.addUserDebugText(
    "",
    [0, 0, 2.5],
    textSize=1.5
)


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    # --------------------------------------------------------
    # READ KEYBOARD
    # --------------------------------------------------------

    keys = p.getKeyboardEvents()

    for key, action in controls.items():

        if key in keys:

            joint_number = action[0]
            change = action[1]

            joint_angles[joint_number] += change

            # Limit angle
            joint_angles[joint_number] = max(
                -180,
                min(180, joint_angles[joint_number])
            )


    # --------------------------------------------------------
    # MOVE ROBOT
    # --------------------------------------------------------

    for i in range(6):

        p.setJointMotorControl2(
            bodyIndex=robot,
            jointIndex=joints[i],
            controlMode=p.POSITION_CONTROL,
            targetPosition=math.radians(
                joint_angles[i]
            ),
            force=500
        )


    # --------------------------------------------------------
    # UPDATE ANGLE DISPLAY
    # --------------------------------------------------------

    text = (
        f"J1 = {joint_angles[0]:6.1f} deg\n"
        f"J2 = {joint_angles[1]:6.1f} deg\n"
        f"J3 = {joint_angles[2]:6.1f} deg\n"
        f"J4 = {joint_angles[3]:6.1f} deg\n"
        f"J5 = {joint_angles[4]:6.1f} deg\n"
        f"J6 = {joint_angles[5]:6.1f} deg"
    )

    p.addUserDebugText(
        text,
        [0, 0, 2.5],
        textSize=1.2,
        replaceItemUniqueId=angle_text
    )


    # --------------------------------------------------------
    # STEP SIMULATION
    # --------------------------------------------------------

    p.stepSimulation()

    time.sleep(1 / 240)