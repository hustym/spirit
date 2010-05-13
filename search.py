#-*- coding:utf-8 -*-

class Node:
	def __init__(self, text, end):
		self.text = text
		self.left, self.center, self.right = None, None, None
		self.end = end

class TernaryTree:
	def __init__(self):
		self.root = None
	
	def add_node(self, string, pos, node):
		print "add_node ",string[pos] 
		if string[pos] < node.text:
			print "add node to left"
			if node.left is None:
				node.left = Node(string[pos], False)
			self.add_node(string, pos, node.left)
		elif string[pos] > node.text:
			print "add node to right"
			if node.right is None:
				node.right = Node(string[pos], False)
			self.add_node(string, pos, node.right)
		else:
			if pos + 1 == len(string):
				print "set node end"
				node.end = True
			else:
				print "add node to center"
				if node.center is None:
					node.center = Node(string[pos], False)
				self.add_node(string, pos + 1, node.center)
				
	def add(self, string):
		if string is None or string == "":
			return
		if self.root is None:
			self.root = Node(string[0], False)
		self.add_node(string, 0, self.root)
		
	def search(self, string):
		if string is None or string == "":
			return False
		
		pos = 0
		node = self.root
		while node != None:
			if string[pos] < node.text:
				node = node.left
			elif string[pos] > node.text:
				node = node.right
			else:
				pos += 1
				if pos == len(string):
					return node.end
				node = node.center

		return False
	
t = None	

def main():
	global t
	t = TernaryTree()
	h = file("d:/python25/a.txt", "r")
	lines = h.read().split("\n")
	h.close()
	for line in lines:
		if len(line) > 0:
			t.add(line)
	
		
if __name__ == "__main__":
	main()
	