# Task 1: Class for Pieces of Music
class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer: {self.artist}\n"
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")

# Object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# Object usage
print(song1)
print()
print(song2)

# Task 2: TV Class
# tv.py file
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            channel_name = f" ({self.channels[self.channel_no - 1]})" if 0 < self.channel_no <= len(self.channels) else ""
            print(f"TV is on, channel {self.channel_no}{channel_name}, volume {self.volume}")
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        if self.is_on:
            self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, start=1):
                print(f"{idx}. {channel}")
        else:
            print("No channels available")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

# tv_show.py file
import tv

def main():
    my_tv = tv.TV()

    # TV usage
    print("Create TV set")
    my_tv.show_status()

    print("\nTurn TV on")
    my_tv.turn_on()
    my_tv.show_status()

    print("\nSet TV channels")
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    my_tv.show_channels()

    print("\nChange TV channel to 4")
    my_tv.set_channel(4)
    my_tv.show_status()

    print("\nIncrease volume")
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.show_status()

    print("\nDecrease volume")
    my_tv.decrease_volume()
    my_tv.show_status()

    print("\nTurn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
