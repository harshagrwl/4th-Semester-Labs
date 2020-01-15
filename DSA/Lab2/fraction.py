class Fraction:

	def __init__(self,num,den):
		self.nume = num
		self.dene = den
		self.simplify()

	def __str__(self):
		
		return str(self.nume)+"/"+str(self.dene)

	def __add__(self,other):
		nnum = self.nume*other.dene + self.dene*other.nume
		nden = self.dene*other.dene
		return Fraction(nnum,nden).simplify()

	def inverse(self):
		nnum = self.dene
		nden = self.nume
		return Fraction(nnum,nden).simplify()

	def __mul__(self,other):
		nnum = self.nume*other.nume
		nden = self.dene*other.dene
		return Fraction(nnum,nden).simplify()

	def __eq__(self,other):
		
		if(self.nume == other.nume and self.dene == other.dene):
			return True
		else:
			return False

	def simplify(self):
		for i in range(min(self.nume,self.dene),1,-1):
			if(self.nume%i == 0 and self.dene%i == 0):
				self.nume //= i
				self.dene //= i
				break
		return self

print(Fraction(3,5)+Fraction(4,5))
print(Fraction(3,5)*Fraction(4,5))
print(Fraction(3,5)==Fraction(4,5))