from sympy import *
import xlsxwriter
import sympy as sym
from sympy import symbols
from xlrd import open_workbook
from sympy.plotting import plot
from sympy.plotting import plot3d
# Exercise 1 ___________________________________________________


x = sym.symbols('x')
y, i ,n, a, b, z = sym.symbols('y i n a b z')

# a)
expr = x**2 + x**3 +21*x**4 + 10*x +1
print(expr.subs(x,7))



# b)
print(sym.expand((x + y) ** 2 ))


#c)
simp =  4*x**3+21*x**2+10*x+12
print(sym.simplify( simp ))

#d

#e)
print(sym.summation(2*i+i-1,(i,5,n)))


#f
print(sym.integrate( sin(x) + exp(x)*cos(x)+tan(x),x))



#g
print( sym.factor(x**3+12*x*y*z+3*y**2*z))


#h
print( sym.solveset(x -4, x))


#i
m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2, 1, 0])
print(m1*m2)


#j
plot(x**3+3, (x, -10, 10))


#k
x, y = symbols('x y')
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

# Exercise 2 ___________________________________________________

workbook=xlsxwriter.Workbook("excel.xlsx")
worksheet=workbook.add_worksheet()
worksheet.autofilter('A1:A4')

data=['This is Example','My first export example',1,2,3]

format=workbook.add_format()
format.set_font_color('red')


worksheet.write_column('A1',data)
#worksheet.write|('A1:1',format)
worksheet.set_row(0,'A',format)
worksheet.set_row(4,'A',format)

workbook.close()



# Exercise 3 ___________________________________________________
workbook=xlsxwriter.Workbook('Excel.xlsx')
worksheet1=workbook.add_worksheet('sheet1')
worksheet1.autofilter('A1:C2')

worksheet2=workbook.add_worksheet('sheet2')
worksheet2.autofilter('A1:C2')

col1=['Mohammad','Ahlam','Noor']
col2=[1,2,3]
col3=[500,200,400]

worksheet1.write_column('A1',col1)
worksheet1.write_column('B1',col2)
worksheet1.write_column('C1',col3)

coll1=['Shaker','Yasmeen','Haya']
coll2=[1,2,3]
coll3=[600,500,123]

worksheet2.write_column('A1',coll1)
worksheet2.write_column('B1',coll2)
worksheet2.write_column('C1',coll3)

workbook.close()


wb = open_workbook('Excel.xlsx')
for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (values,"'")




