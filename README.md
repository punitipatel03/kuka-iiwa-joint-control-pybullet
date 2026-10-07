# KUKA iiwa Joint Control Simulation (PyBullet)

Interactive keyboard teleoperation of a **KUKA LBR iiwa** industrial robot arm in the **PyBullet** physics simulator. Each of six joints is driven with position control, and the current joint angles (J1–J6) are shown live in the 3D view.

## Features

- Loads the KUKA iiwa URDF model on a ground plane with real gravity (-9.81 m/s²)
- Controls 6 joints in real time from the keyboard
- Uses PyBullet `POSITION_CONTROL` motors with a 500 N·m force limit
- Limits joint angles to ±180° in software
- Shows J1–J6 angles live as overlay text in the simulation
- Runs the simulation at 240 Hz

## Requirements

- Python 3.8+
- PyBullet

```bash
pip install -r requirements.txt
```

## Run

```bash
python joint_control.py
```

Click the PyBullet window so it receives keyboard input, then use the controls below.

## Keyboard Controls

| Joint | Increase (+2°) | Decrease (−2°) |
|-------|:--------------:|:--------------:|
| J1    | `Q` | `A` |
| J2    | `W` | `S` |
| J3    | `E` | `D` |
| J4    | `R` | `F` |
| J5    | `T` | `G` |
| J6    | `Y` | `H` |

## How It Works

1. Connects to PyBullet in GUI mode and loads `plane.urdf` and `kuka_iiwa/model.urdf` from `pybullet_data`.
2. Each frame, reads keyboard events and updates the target angle of the matching joint.
3. Sends each target angle (converted to radians) to the joint motor using `setJointMotorControl2`.
4. Updates the angle text and steps the simulation.

## Author

**Puniti Patel** — [GitHub](https://github.com/punitipatel03)
