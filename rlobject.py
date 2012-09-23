#-------------------------------------------------------------------------------
# Name:        rlobjects
# Purpose:
#
# Author:      Simon Huynh
#
# Created:     20/09/2012
#
# Base object class for rl
# All drawn characters on screen are objects
#-------------------------------------------------------------------------------

import libtcod

"""--------------------------------------------------------------"""
"""                           CLASS OBJECT                       """
"""--------------------------------------------------------------"""

class Object:
    #Base abstract object class for object
    def __init__(self, x, y, direction='N', char, color, collision, description):
        self.x = x
        self.y = y
        #N, E, S, or W
        self.direction = direction
        self.char = char
        self.color = color
        self.collision = collision
        #The description of the character
        self.description = description
    def move_to(x, y):
        #sets object's coordinate
        self.x = x
        self.y = y
    def move(dx, dy):
        self.x += dx
        self.y += dy
    def draw(self):
        #set color and draw char at x, y
        #libtcod.console_set_foreground(0, self.color)
        #libtcod.console_put_char(0, self.x, self.y, self.char, libtcod.BKGND_NONE)
        pass
    def clear(self):
        #libtcod.console_put_char(0, self.x, self.y, ' ', libtcod.BKGND_NONE)
        pass

"""--------------------------------------------------------------"""
"""                           CLASS  PC                          """
"""--------------------------------------------------------------"""

class Character(Object):
    def __init__(self, maxHP, exp, curHP=maxHP, status, attack, defense):
        #Calls Character's superclass(Object)'s __init__ function
        # with collision true
        super(Object, self).__init__()
        self.maxHP = maxHP
        self.hp = maxHP
        self.exp = exp
        #A list of buffs/debuffs
        self.status = status
        self.attack = attack
        self.defense = defense

    def is_dead(self):
        """Returns death state of character object"""
        return self.hp <= 0


class PC(Character):
    """The class for a player character, the @ the player controls"""
    def __init__(self, level=1, inventory):
        super(Character, self, char='@').__init__()
        self.level = level
        self.inventory = inventory


"""--------------------------------------------------------------"""
"""                           CLASS NPC                          """
"""--------------------------------------------------------------"""
class NPC(Character):
    def __init__(self, dropTable):
        super(Character, self).__init__()
        #A list of tuples, (p, item) where 0 < p <= 1 and item is of class Item
        self.dropTable = dropTable

"""--------------------------------------------------------------"""
"""                           CLASS ITEM                         """
"""--------------------------------------------------------------"""

class Item(Object):
    def __init__(self):
        super(Object, self).__init__()
    def execute(self):
        #Used virtually, to be inherited
        pass

"""--------------------------------------------------------------"""
"""                       CLASS PROJECTILE                       """
"""--------------------------------------------------------------"""

class Projectile(Object):
    def __init__(self, maxDistance, trajectory):
        super(Object,self).__init__()
        self.maxDistance = maxDistance
        #Can figure out later, maybe an enumberation of trajectories?
        self.trajectory = trajectory