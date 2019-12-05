class Node:

	def __init__(self,dictionary):
		self.parent = None
		
		self.left = None
		self.right = None

		self.age = dictionary["age"]
		self.sex = dictionary["sex"]
		self.name = dictionary["name"]


	def returnAge(self):
		return self.age

	def returnName(self):
		return self.name

	def returnSex(self):
		return self.sex

	def changeAge(self, new):
		self.age = new

	def setParent(self, parent):
		self.parent = parent

	def returnParent(self):
		return self.parent

	def returnAncestors(self, output):

		if self.returnParent() == None:
			output = output[:-1]
			return output
		else:
			parent = self.returnParent().returnName()
			output = output + parent + "\n"
			return self.returnParent().returnAncestors(output) #why does this work ver 1 [[TRACE THIS LATER]]



	def addLeft(self, child): #patricks child is alex

		child.setParent(self) # alexs parent is patrick
		self.left = child

	def addRight(self, child): #patricks child is alex

		child.setParent(self) # alexs parent is patrick
		self.right = child


def getNode(name):
	return 




def LCA(p1,p2):
	print("end LCA")

def d(p1,p2): #distance of child to parent

	print("end d")


def relationship(p1,p2):
	l = LCA(p1,p2)	

def makeDict():
	return {}




def load(filename):
	f = open(str(filename) + ".ft","r")

	lines = f.readlines()
	print(lines)

	lines[0]





	print("end load")

def reset():
	print("end reset")





print("start")



	
# -------------------------------------

master = {
}


	
# ------------------------------------- (load)

dictPatrick = {
	"name": "Patrick",
	"age": "20",
	"sex": True
}




nodePatrick = Node(dictPatrick)

master["Patrick"] = nodePatrick

# -------------------------------------

dictAlex = {
	"name": "Alex",
	"age": "7",
	"sex": True
}

nodeAlex = Node(dictAlex)

master["Alex"] = nodeAlex


# -------------------------------------

dictKirby = {
	"name": "Kirby",
	"age": "100",
	"sex": True
}

nodeKirby = Node(dictKirby)

master["Kirby"] = nodeKirby

# ------------------------------------- 

dictChristian = {
	"name": "Christian",
	"age": "18",
	"sex": True
}

nodeChristian = Node(dictChristian)

master["Christian"] = nodeChristian

# ------------------------------------- 

dictKaloy = {
	"name": "Kaloy",
	"age": "12",
	"sex": True
}

nodeKaloy = Node(dictKaloy)

master["Kaloy"] = nodeKaloy


# ------------------------------------- 

dictAbby = {
	"name": "Abby",
	"age": "9",
	"sex": False
}

nodeAbby = Node(dictAbby)

master["Abby"] = nodeAbby



# ------------------------------------- 

dictBen = {
	"name": "Ben",
	"age": "81",
	"sex": True
}

nodeBen = Node(dictBen)

master["Ben"] = nodeBen


# ------------------------------------- 

dictCidney = {
	"name": "Cidney",
	"age": "69",
	"sex": True
}

nodeCidney = Node(dictCidney)

master["Cidney"] = nodeCidney


# ------------------------------------- 


# ------------------------------------- 



# ------------------------------------- relationships 

nodePatrick.addLeft(nodeAlex)
nodePatrick.addRight(nodeBen)
nodeAlex.addLeft(nodeKirby)
nodeAlex.addRight(nodeChristian)
nodeKirby.addLeft(nodeKaloy)
nodeKirby.addRight(nodeAbby)
nodeBen.addRight(nodeCidney)


# -------------------------------------


while True:
	command = input()

	if command == "get age":
		print(nodePatrick.returnAge())
	elif command == "get sex":
		if nodePatrick.returnSex() == True:
			print("Male")
		elif nodePatrick.returnSex() == False:
			print("Female")
	elif command[0] == "c":
		nodePatrick.changeAge(command[7:])
	elif command[0] == "a":

		name = str(command[10:])

		print(master[name].returnAncestors(""))

# load("TheFamilyName")

#parent
#change


print('end')
