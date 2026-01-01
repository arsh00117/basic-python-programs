import math
print("****Calculating Area of Shapes****")

attempt = 1

print("s for Square, c for circle, cy for clyinder ,co for cone")
shape = input("Enter Desired Shape: ").lower()

def menu(): 
    print("s for Square","c for circle", "cy for clyinder","co for cone")
    shape = input("Enter Desired Shape: ").lower()


def sq_area(s) :
       area = s*s
       return area

def c_area(r) :
       area = (math.pi*r*r)
       return area

def cy_csa(h,r) :
       csa = (2*math.pi*r*h)
       return csa

def cy_tsa(h,r) :
       tsa = ((2*math.pi*r*h)+(2*math.pi*r*r))
       return tsa

def l_slant(h,r):
       l = math.sqrt((h**2)+(r**2))
       return l

def lt_cone(h,r) :
      l = l_slant(h,r)
      csa = (math.pi*r*l)
      return csa

def csa_cone(h,r) :
      l= l_slant(h,r)
      tsa = math.pi*r*(l+r)
      return tsa

def base_acone(r) :
      bcone = math.pi*(r**2)
      return bcone



def cal():
    if(shape == "s") :
        side = float(input("Side of Square: "))
        area = sq_area(side)
        print("Area of Sqaure is: ",round(area,2))
    elif(shape == "c") :
            radii = float(input("Radius of Circle: "))
            area = c_area(radii)
            print("Area of Circle having Radius ",radii," is ",round(area,2))
    elif(shape == "cy") :
            h = int(input("Enter Height of Cylinder: "))
            r = int(input("Enter Radius of Cylinder: "))
            csa = cy_csa(h,r)
            tsa = cy_tsa(h,r)
            print("CSA of cylinder is: ",round(csa,2)," approx")
            print("TSA of cylinder is: ",round(tsa,2)," approx")
    elif(shape == "co") :
          h = float(input("Enter Height of cone: "))
          r = float(input("Enter Radius of cone: "))
          lsacone = lt_cone(h,r)
          csacone = csa_cone(h,r)
          basearea = base_acone(r)
          print("LSA of cone is : ",lsacone)
          print("CSA of cone is : ",csacone)
          print("Base area of cone is : ",basearea)
    else:
            print("Invalid Input")

if attempt == 1 or attempt == 2 or attempt == 3:   
    if len(shape)!=0 :
        cal()
    else: 
            menu()
            attempt= attempt+1

else :
        exit()

