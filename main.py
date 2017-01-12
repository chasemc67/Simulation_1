import os
import sys
import time

# object oriented. make a class for each node.
# Each node needs it's location, and a move function

# Keep a priority queue sorted by next event. 
# Each event should be a class, 
# Holds time until event, and reference objects in event
# After event, invalidate all events relating to the two objects
# Find all new events for 2 objects, and add to queue

# Make a statistics object (or just keep as counters in environment)
# Keep track of average "talking" time. 



class Drawer():
	# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
	# redOnWhite = '\x1b[1;31;47m' 
	# blueOnWhite = '\x1b[1;34;47m' 
	def __init__(self, x, y):
		self.width = x
		self.height = y


	def clear(self):
		print("Clearing")
		os.system('cls' if os.name == 'nt' else 'clear')

	def nodeAtPosition(self, nodeList, posX, posY):
		for node in nodeList:
			if node.x == posX and node.y == posY:
				return True
		return False

	#def draw(self, nodeList):
	def draw(self, nodeList):
		self.clear()
		for y in range(self.height):			
			#sys.stdout.write('\x1b[6;30;42m %s \x1b[0m' % y)
			sys.stdout.write('\x1b[1;31;47m %s \x1b[0m' % y)
			sys.stdout.flush()
			for x in range(self.width):
				if (self.nodeAtPosition(nodeList, x, y)):
					sys.stdout.write('\x1b[1;34;47mo ')	
				else:
					sys.stdout.write('\x1b[1;34;47m  ')
				sys.stdout.flush()
			sys.stdout.write('%s\n' % y)
			sys.stdout.flush()



class Node():
	def __init__(self):
		self.x = 4
		self.y = 5
		self.dx = 1
		self.dy = 1
		#self.x = rand()
		#self.y = rand()
		#self.dx = rand()  # X movement speed
		#self.dy = rand()  # Y movement speed
		#self.commDistance = communicationDistance # r

	def move(self, timeSteps):
		self.x = self.x + (timeSteps * self.dx)
		self.y = self.y + (timeSteps * self.dy)


class Environment():
	def __init__(self):
		#self.eventList = priorityQueue()
		self.nodeList = list() # list of nodes in environment

	def moveNodes(self):
		for node in self.nodeList:
			node.move(1)


class Event():
	def __init__(node1, node2):
		self.valid = True
		self.left = node1
		self.right = node2


env = Environment()
output = Drawer(10, 10)

env.nodeList = list();
env.nodeList.append(Node())
env.nodeList.append(Node())

env.nodeList[1].x = 7
env.nodeList[1].y = 7
env.nodeList[1].dx = -1
env.nodeList[1].dy = -1

for i in range(10):
	output.draw(env.nodeList)
	env.moveNodes()
	time.sleep(1)
