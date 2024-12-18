# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
      
    def show_status(self):
        if self.is_on:
            print(f"TV is on, volume: {self.volume}")
        else:
            print("TV is off")

    def set_channels(self, channels_list):
        for channel in channels_list:
            self.channels.append(channel)

    def show_channels(self):
        print(f"Available channels: {self.channels}")

    def volume_up(self):
        if self.volume < 10:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1


