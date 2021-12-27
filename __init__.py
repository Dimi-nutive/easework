def add(num1 , num2):
	return num1 + num2

def substract(num1 , num2):
	return num1 - num2

def multiply(num1 , num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def sq(num):
	return num * num 

def cb(num):
	return num * num * num 

def sqrt(num):
	return num ** 0.5 

def cbrt(num):
	return num ** 1/3

def area_sq(side):
	return side * side

def area_rect(length, width):
	return length * width 

def area_triangle(base, height):
	return 1/2 * base * height

def area_pgram(base, height):
	return base * height 

def area_kite(diag1, diag2):
	return 1/2 * diag1 * diag2

def area_quad(diag, h1, h2):
	return 1/2 * diag * h1 + h2

def area_trapzium(a, b, h):
	return 1/2 * a + b * h

def area_rhombus(diag1, diag2):
	return 1/2 * diag1 * diag2

def peri_sq(side):
	return 4 * side

def peri_rect(length, width):
	return 2 * length + width

def peri_pgram(b, h):
	return 2 * b * h

def peri_triangle(a, b, c):
	return a + b + c

def peri_kite(a, b): 
	return 2 * a + 2 * b
			
def peri_rhombus(side):
	return 4 * side

def peri_hexa(side):
	return 6 * side

def peri_trapzium(a, b, c, d):
	return a + b + c + d 

def peri_quad(a, b, c, d):
	return a + b + c + d 

def sa_cuboid(l, w, h):
	return 2 * (l * w + l * h + w * h)

def sa_cube(a):
	return 6 * a * a

def sa_cylinder(r, h):
	return 2* 22/7 * r * (r + h)

def sa_cone(r, l):
	return 22/7 * r * (l + r)

def sa_sphere(r):
	return 4 * 22/7 * r * r

def sa_hemisphere(r):
	return 3 * 22/7 * r * r

def lsa_cuboid(l, w, h):
	return 2 * h * (l + w)

def lsa_cube(a):
	return 4 * a * a 

def lsa_cylinder(r, h):
	return 2 * 22/7 * r * h

def lsa_cone(r, l):
	return 22/7 * r * l

def lsa_hemisphere(r):
	return 2 * 22/7 * r * r

def vol_cuboid(l, w, h):
	return l * w * h 

def vol_cube(a):
	return a * a * a

def vol_cylinder(r, h):
	return 22/7 * r * r * h

def vol_prism(b, l):
	return b * l

def vol_sphere(r):
	return 4/3 * 22/7 * r * r * r 

def vol_pyramid(b , h):
	return 1/3 * b * h

def vol_cone(r, h):
	return 1/3 * 22/7 * r * r *h

def simple_interst(p, t, r):
	return(p * t * r)/100

def compound_interest(p, t, r):
	return p * ( (1+r/100)**t - 1)

def mon_emi(p, r, n):
	return p * r * ((1+r)**n)/((1+r)**n - 1)


