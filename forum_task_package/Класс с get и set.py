# -*- coding: utf-8 -*-

class Rectangle:

    def __init__(self, x: int, y: int, width: int, height: int):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getX(self) -> int:
        self.__printlog("Запрошено свойство 'x'")
        return self.__x

    def setX(self, x: int):
        self.__printlog("Изменено свойство 'x'")
        self.__x = x

    def getY(self) -> int:
        self.__printlog("Запрошено свойство 'y'")
        return self.__y

    def setY(self, y: int):
        self.__printlog("Изменено свойство 'y'")
        self.__y = y

    def getWidth(self) -> int:
        self.__printlog("Запрошено свойство 'width'")
        return self.__width

    def setWidth(self, width: int):
        self.__printlog("Изменено свойство 'width'")
        self.__width = width

    def getHeight(self) -> int:
        self.__printlog("Запрошено свойство 'height'")
        return self.__height

    def setHeight(self, height: int):
        self.__printlog("Изменено свойство 'height'")
        self.__height = height

    def __printlog(self, message: str): print(message)


r = Rectangle(0, 0, 200, 100)

r.setX(1)
r.setY(10)
r.setWidth(300)
r.setHeight(250)

print(r.getX())
print(r.getY())
print(r.getWidth())
print(r.getHeight())