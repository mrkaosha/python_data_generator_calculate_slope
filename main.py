f = open("data.txt","w")
num = []
den = []
x1 = []
y1 = []

def slopeDenominator(slopeNumerator, y):
  for d in [-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9]:
    for x in [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]:
      if (x + d >= -10 and x + d <= 10):
        num.append(slopeNumerator)
        den.append(d)
        y1.append(y)
        x1.append(x)

for y in [-1,0,1,2,3,4,5,6,7,8,9,10]:
  slopeDenominator(-9,y)
for y in [-2,-1,0,1,2,3,4,5,6,7,8,9,10]:
  slopeDenominator(-8,y)
for y in [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-7,y)
for y in [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-6,y)
for y in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-5,y)
for y in [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-4,y)
for y in [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-3,y)
for y in [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-2,y)
for y in [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  slopeDenominator(-1,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
  slopeDenominator(1,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]:
  slopeDenominator(2,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7	]:
  slopeDenominator(3,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]:
  slopeDenominator(4,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
  slopeDenominator(5,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]:
  slopeDenominator(6,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]:
  slopeDenominator(7,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]:
  slopeDenominator(8,y)
for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]:
  slopeDenominator(9,y)

print("static List<int> num=",file=f,end="")
print(num, file=f,end="")
print(";",file=f)
f.write("")
print("static List<int> den=",file=f,end="")
print(den,file=f,end="")
print(";",file=f)
f.write("")
print("static List<int> x1=",file=f,end="")
print(x1,file=f,end="")
print(";",file=f)
f.write("")
print("static List<int> y1=",file=f,end="")
print(y1,file=f,end="")
print(";",file=f)

