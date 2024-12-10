# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channels = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
      
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")

    def set_channels(self, channels_list):
        for channel in channels_list:
            self.channels.append(channel)
    



