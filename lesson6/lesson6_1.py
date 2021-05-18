from time import sleep
import os
from sty import bg, rs


class TrafficLight:
    __color = [bg.red + '   ' + bg.rs, bg.yellow + '   ' + bg.rs, bg.green + '   ' + bg.rs]

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(2)
            print("\n")


a = TrafficLight()
a.running()
