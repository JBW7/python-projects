# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Robot:
	def __init__(self, name, color, weight):	
		self.name = name
		self.color = color
		self.weight = weight 

	
	def introduce_self(self):
		print ("my name is " + self.name )

'''
#objects  without __init__
# __init__ means in it 
robot1 = Robot( )
robot1.name = "Tom"
robot1.color = "Red"
robot1.weight = 30
robot1.introduce_self()
# self refers to robot 1 and robot 2
robot2 = Robot()
robot2.name = "Bob"
robot2.color = "white"
robot2.wight = 10
robot2.introduce_self()
'''

# objct with __init__
robot1 = Robot("Tom", "Red", 30)
robot2 = Robot("Bob", "White", 10)

robot1.introduce_self()
robot2.introduce_self()

class Person:
	def __init__(self, name, personality, is_sitting):
		self.name = name
		self.personality = personality
		self.is_sitting = is_sitting

	def sit_down(self):
		self.is_sitting = True

	def stand_up(self):
		self.is_sitting = False 

person1 = Person("john", "high temper", True)
person2 = Person("bobby", "funny", False)

# robot owned
person1.robot_owned = robot2
person2.robot_owned = robot1

person1.robot_owned.introduce_self()
person2.robot_owned.introduce_self()

























