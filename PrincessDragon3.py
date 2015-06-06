﻿from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        pause = raw_input("Press enter to continue")
        exit(1)


# Diana’s

class Door(Scene):
    def enter(self):
        print "This is a love story..."
        print " A lovely young princess named Leila fell in love with a dashing young dumbass named Valium."
        print " They met one balmy night in a magical land aptly named The Good Night,"
        print " They moved in together six months later and adopted a baby dragon Pyro."
        print " The good knight Valium has, as of last night, gotten himself in a bit of a jam,"
        print " getting kidnapped by a bunch of bandits, and now Leila has to rescue him one and only true love."
        print " Leila has to go open the door and start her quest. She walks to the door."
        print " Leila (you) stands in front of the door"
        print " Leila can:"
        print " a)push"
        print " b)pull"

        action = raw_input("> ")

        if action == "a":
            print "Great! You did it! Go on and get to rescue that lovely idiot."
            return 'forest'

        elif action == "b":
            print "The door handle broken because you pull it too hard."
            print "You fall and break your head. You are dead!"
            return 'death'
        else:
            print "DOES NOT COMPUTE!"
            return 'door'


#Nicoles

class Forest(Scene):
 
    def enter(self):

        print "You are in the forest"
        print "Leila needs to find the bandits tower."
        print "Leila can get directions if she..."
        print "(a) asks a swallow, (b) asks a deer, (c) asks a rabbit"
        guess = raw_input("> ")
        
        if guess == "a":
            print "Wrong choice! The swallow dies."
            return 'death'
        elif guess == "b":
            print "Wrong answer! The deer runs off."
            return 'death'
        elif guess == "c":
            print "Great job! That rabbits dynamite...You really should get yourself a bunny."
            print "The rabbit takes Leila and Pyro down a rabbit hole to the bandits tower."
            return 'banditstower'
        else:
            print "Not a valid option. Choose a, b or c"
            return 'forest'
     

class BanditsTower(Scene):
    def enter(self):
            print "Leila, Valium. and Pyro need to escape the bandits by pulling up the drawbridge behind them."
            print "Leila can:"
            print "1 get Pyro to throw fireballs at them"
            print "2 push them one by one into the moat"
            print "3 surrender"
             
            action = raw_input("> ")
             
            if action == "1":
                print "Pyro sets Valium on fire by sneezing."
                pause = raw_input(" read")
                return 'death'
                        
             
            elif action == "2":
                print "They all fall into the moat around bandit's tower while fighting"
                return 'moat'
                        

            elif action == "3":
                print "They all die since he forgot his Allegra"
                return 'death'
                        
            else:
                print "DOES NOT COMPUTE!"
                return 'banditstower'


class Moat(Scene):

    def enter(self):
        print "Leila, Valium, and Pyro need to escape the narwhals in the moat."
        print "Options \nLeila can: \n(a) get Pyro to throw fireballs at them \n(b) swim faster than the narwals \n(c) play dead"
        guess = raw_input()
        if guess in ['a','A']:
            print "Pyro's fire is doused under water"
            return 'castle'
        elif guess in ['b','B']:
            print "The narwhals catch them"
            return 'death'
        elif guess in ['c', 'C']:
            print "The narwhals swim past them and the 3 escape."
            return 'castle'
        else:
            print "Oops! Something bad happened!"
            return 'moat'


#Nicoles

class Castle(Scene):
 
    def enter(self):

        print "Leila, Valium and Pyro are back in the castle."
        print "They need to get ready for their /'Heroes Welcome' but Valium is asleep. Leila can: "
        print "(a) kiss him, (b) asks her matron to wake him up, (c) get Pyro to wake him up"
        print "Don't you just hate it when you are in bed with three different women" 
        print "and the least attractive one of them says: /'Save it for me.'Jim Carrey"
        guess = raw_input("> ")
        
        if guess == "a":
            print "She has to do over her lipstick and is late to the party."
            return 'death'
        elif guess == "b":
            print "Valium wakes up."
            return 'finished'
        elif guess == "c":
            print "Pyro sets Valium on fire."
            return 'death'
        else:
            print "Not a valid option. Choose a, b or c"
            return 'castle'

class Finished(Scene):
    def enter(self):
        print "You won! Good job."
        return 'finished'


class Map(object):
    scenes = {
        'door': Door(),
        'forest': Forest(),
        'banditstower': BanditsTower(),
        'moat': Moat(),
        'castle': Castle(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('door')
a_game = Engine(a_map)
a_game.play()
_ = raw_input("Press enter to continue")
