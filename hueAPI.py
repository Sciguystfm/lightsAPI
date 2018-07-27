from phue import Bridge

class HueController:
    def __init__(self, ip):
        self.b = Bridge(ip)

    def turnRoomsOff(self, rooms):
        for room in rooms:
            self.b.set_group(room, 'on', False)

    def normalizeRooms(self, rooms):
        lightIds = []
        for room in rooms:
            lightIds = lightIds + self.b.get_group(room,'lights')
            print (lightIds)
            lights= self.b.get_light_objects('id')
            print (lights)
            for id in lightIds:
                id=int(id)
                lights[id].on = True
                lights[id].brightness = 254
                lights[id].hue = 8597
                lights[id].saturation = 121
        pass

    def nightlight(self, rooms):
        lightIds = []
        for room in rooms:
            lightIds = lightIds + self.b.get_group(room,'lights')
            lights= self.b.get_light_objects('id')
            for id in lightIds:
                id=int(id)
                lights[id].on = True
                lights[id].brightness = 40
                lights[id].hue = 6291
                lights[id].saturation = 251
        pass
