import matplotlib.pyplot as plt
import numpy as np
x = ["python", "java", "C++", "PHP"]
y = [34, 56, 30, 36]
z =  [15,14,20,24]
p=np.arange(len(x))
width=.3
p1=[j+width for j in p]

plt.xlabel("Language",fontsize="15")
plt.ylabel("User number",fontsize="15")
c=["g","r","b","black"]
plt.title("programming Language User",fontsize="10")
plt.bar(x,y,width=0.4,color=c,align="edge")
plt.show()




plt.xlabel("Language", fontsize=15)
plt.ylabel("User number", fontsize=15)
c = ["g", "r", "b", "black"]

plt.title("Programming Language User", fontsize=20)
plt.bar(p, y, width=0.4, color="g", align="center",  linewidth=3, label="popularity")
plt.bar(p1, z, width=0.4, color="black", align="center", linewidth=3, label="popularity2")

plt.legend()
plt.show()




#*888888888888888888888888888888888888888888
x = ["python", "java", "C++", "PHP"]
y = [34, 56, 30, 36]
z =  [15,14,20,24]
p=np.arange(len(x))
width=.4

p1=[j+width for j in p]
plt.xlabel("Language", fontsize=15)
plt.ylabel("User number", fontsize=15)
c = ["g", "r", "b", "black"]
plt.title("Programming Language User", fontsize=20)
plt.bar(x, y, width=0.4, color="g", align="center",  linewidth=3, label="popularity")
plt.bar(p1, z, width=0.4, color="black", align="center", linewidth=3, label="popularity2")
plt.xticks(p+width/2,x,rotation=5)
plt.legend()
plt.show()


