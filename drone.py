class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Drone is flying.")

class Drone(Device, Flyer):
    def __init__(self, device_id):
        Device.__init__(self, device_id)

    def capture_image(self):
        print("Image captured.")

# Demonstrate functionality
d1 = Drone("DR-101")
d1.info()
d1.fly()
d1.capture_image()
