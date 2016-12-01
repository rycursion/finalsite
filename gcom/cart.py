class Cart:
	def __init__(self):
		self.lst=[]
	def add(self, p_id):
		self.lst.append(int(p_id))
	def remove(self, p_id):
		self.lst.remove(int(p_id))
	def if_empty(self):
		if len(self.lst)==0:
			return True
		else:
			return False
	def empty_cart(self):
		self.lst=[]

c=""

def create():
	c1=Cart()
	global c
	c=c1

def remove():
	global c
	del c
