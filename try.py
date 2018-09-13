from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import AbstractGroup
import pygame
import sys
# ship_image = pygame.image.load('images/ship.bmp')
# rect = ship_image.get_rect()
# print(rect)
# print(rect.centerx)
# print(rect.bottom)
# print(rect.midleft)


class AbstractPrint(Sprite):
    def __init__(self):
        super().__init__()
        self.lines = 'abstract'

    def update(self):
        print(self.lines + " * ")


abstract_prints = AbstractGroup()
for numb in range(4):
    abstract_print = AbstractPrint()
    abstract_prints.add(abstract_print)
    print(abstract_print.lines + " " + str(numb) + " *")
print(abstract_prints.update())
print(abstract_prints.spritedict)


# def shot_bullet():

#     pygame.init()
#     pygame.display.set_mode((100, 100))
#     # abstract_bullets = AbstractGroup()
#     bullets = Group()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                 new_bullet = Bullet()
#                 bullets.add(new_bullet)
#                 print(bullets.sprites())
#             elif event.type == pygame.QUIT:
#                 sys.exit()


# class Bullet(Sprite):
#     def __init__(self):
#         super().__init__()

#         self.name = 'bullet.py'

# shot_bullet()


# class A(object):
#     def __init__(self):
#         self.__s = '6'

#     def __method(self):
#         print("I'm a method in class A")

#     def method_x(self):
#         print("I'm another method in class A\n")

#     def method(self):
#         print(self.__s)
#         self.__method()
#         self.method_x()


# class B(A):
#     def __method(self):
#         print("I'm a method in class B")

#     def method_x(self):
#         print("I'm another method in class B\n")


# print("situation 1:")
# a = A()
# a.method()
# b = B()
# b.method()
# print("situation 2:")
# # a.__method()
# a._A__method()
# print(a._A__s)
