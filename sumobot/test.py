# mock_ev3.py (test on your computer)
import random
import time

class MockColorSensor:
    def color(self):
        return random.choice(["BLACK", "BLACK", "WHITE"])  # sometimes "detects" white

class MockUltrasonicSensor:
    def distance(self):
        return random.randint(100, 400)  # random distance between 10cm–40cm

class MockRobot:
    def drive(self, speed, turn_rate):
        print(f"Driving: speed={speed}, turn={turn_rate}")
    def stop(self):
        print("Robot stopped")
    def turn(self, angle):
        print(f"Turned {angle} degrees")
    def straight(self, dist):
        print(f"Moved straight {dist} mm")

def cycle():
    robot = MockRobot()
    color_sensor = MockColorSensor()
    ultrasonic = MockUltrasonicSensor()

    while True:
        color = color_sensor.color()
        if color == "WHITE":
            robot.stop()
            robot.turn(180)
            robot.straight(200)
            continue

        dist = ultrasonic.distance()
        if dist < 200:
            robot.drive(500, 0)
        else:
            robot.drive(200, 0)
        time.sleep(0.5)

cycle()
