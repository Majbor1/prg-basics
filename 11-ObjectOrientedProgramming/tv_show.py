# tv_show.py file
# main program
from tv import TV

def main():
    my_channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]

    # object creation
    my_tv = TV()
    
    # object usage
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.show_channels()
    my_tv.set_channels(my_channels)
    my_tv.show_channels()
    my_tv.volume_up()
    my_tv.volume_up()
    my_tv.volume_up()
    my_tv.volume_up()
    my_tv.show_status()
    my_tv.volume_down()
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main() 