class Termometer:
    def __init__(self, degree):
        self.degree = degree
        self.is_on = False
    
    def display_temp(self):
        if self.is_on:
            if self.degree <= 37:
                print(f"Temperature: {self.degree}")
            else:
                print(f"Temperature: {self.degree} (fever)")
                if self.degree >= 41:
                    print("CRITICAL TEMPERATURE!!")
        else:
            print("The thermometer is off.")
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False