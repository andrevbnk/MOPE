import math
import random

#y = b0 + b1*x1 + b2*x2

def genY(l):
    """Генерує випадкові випадкові списки заданої довжини"""
    y=[]
    for i in range(l):
        y.append(random.randint(-2990,-2890))
    return(y)

def serY(y):
    """Знаходить середнє значення списку"""
    return sum(y)/len(y)

def disper(y, m):
    """Знаходить дисперсію по рядках"""
    s=0
    for i in range(len(y)):
        s=s+math.pow((y[i]-serY(y)),2)
    s=s/m
    return round(s,2)

def miss(m):
    """Повертає основне відхилення"""
    return round(math.sqrt((2*(2*m-2))/(m*(m-4))),2)

def fuv(y1,y2,m):
    """Обчислює Fuv списку"""
    if disper(y1,m)>disper(y2,m):
        return round(disper(y1,m)/disper(y2,m),2)
    else:
        return round(disper(y2,m)/disper(y1,m),2)

def tetta(y1,y2,m):
    """Повертає Тетта списку"""
    return round((m-(2/m))*fuv(y1,y2,m),2)

def ruv(y1,y2,m):
    """Повертає Ruv списку"""
    return round((abs(tetta(y1,y2,m)-1))/miss(m),2)

def testDisOd(y1,y2,y3,m,r):
    """Перевіряє три списки на однорідність дисперсіі
    m-розмір списка, r - R критичне"""
    if ruv(y1,y2,m)<r and ruv(y3,y2,m)<r and ruv(y3,y1,m)<r :
        print("Дисперсія однорідна")
    else:
        print("Дисперсія неоднорідна")

def mxn(x1,x2,x3):
    return (x1+x2+x3)/3

x11,x12,x13=-1,1,-1
x21,x22,x23=-1,-1,1

x1min=-20
x1max=30
x2min=20
x2max=60

y1=genY(5)
y2=genY(5)
y3=genY(5)

#y1=[9,10,11,15,9]
#y2=[15,14,10,12,14]
#y3=[20,18,12,10,16]

print("x1     x2     y1     y2     y3     y4     y5 \n"
      "{0:2}{1:7}{2:7}{3:7}{4:7}{5:7}{6:7}\n".format(x11,x21,y1[0],y1[1],y1[2],y1[3],y1[4]) +
      "{0:2}{1:7}{2:7}{3:7}{4:7}{5:7}{6:7}\n".format(x12,x22,y2[0],y2[1],y2[2],y2[3],y2[4]) +
      "{0:2}{1:7}{2:7}{3:7}{4:7}{5:7}{6:7}".format(x13,x23,y3[0],y3[1],y3[2],y3[3],y3[4]))


testDisOd(y1,y2,y3,5,2)

mx1=mxn(x11,x12,x13)
mx2=mxn(x21,x22,x23)
my=mxn(serY(y1),serY(y2),serY(y3))

a1=mxn(x11*x11,x12*x12,x13*x13)
a2=mxn(x11*x21,x12*x22,x13*x23)
a3=mxn(x21*x21,x22*x22,x23*x23)

a11=mxn(x11*serY(y1),x12*serY(y2),x13*serY(y3))
a22=mxn(x21*serY(y1),x22*serY(y2),x23*serY(y3))

b0 = (my*a1*a3+mx1*a2*a22+a11*a2*mx2 - (mx2*a1*a22+mx1*a11*a3+a2*a2*my))/(1*a1*a3+mx1*a2*mx2+mx1*a2*mx2 - (mx2*a1*mx2+mx1*mx1*a3+a2*a2*1))
b1 = (1*a11*a3+my*a2*mx2+mx1*a22*mx2 - (mx2*a11*mx2+a22*a2*1+my*mx1*a3))/(1*a1*a3+mx1*a2*mx2+mx1*a2*mx2 - (mx2*a1*mx2+a2*a2*1+mx1*mx1*a3))
b2 = (1*a1*a22+mx1*a11*mx2+mx1*a2*my - (my*a1*mx2+mx1*mx1*a22+a2*a11*1))/(1*a1*a3+mx1*a2*mx2+mx1*a2*mx2 - (mx2*a1*mx2+mx1*mx1*a3+a2*a2*1))

print("Нормоване рівняння:")
print("y="+str(round(b0,2))+"+"+str(round(b1,2))+"*x1+"+str(round(b2,2))+"*x2")
print("b0-b1-b2="+str(round(b0-b1-b2,2)))
print("b0+b1-b2="+str(round(b0+b1-b2,2)))
print("b0-b1+b2="+str(round(b0-b1+b2,2)))

delx1=abs(x1max-x1min)/2
delx2=abs(x2max-x2min)/2
x10=(x1max+x1min)/2
x20=(x2max+x2min)/2
a0n=b0-b1*(x10/delx1)-b2*(x20/delx2)
a1n=(b1/delx1)
a2n=(b2/delx2)

print("Натуралізоване рівняння:")
print("y="+str(round(a0n,2))+"+"+str(round(a1n,2))+"*x1+"+str(round(a2n,2))+"*x2")


print("a0+a1*x1min+a2*x2min="+str(round(a0n+a1n*x1min+a2n*x2min,2)))
print("a0+a1*x1max+a2*x2min="+str(round(a0n+a1n*x1max+a2n*x2min,2)))
print("a0+a1*x1min+a2*x2max="+str(round(a0n+a1n*x1min+a2n*x2max,2)))

#print(mxn(serY(y1),serY(y2),serY(y3)))

