import os
#import bpy,bmesh
import numpy as np
#from mathutils import Euler, Matrix, Quaternion, Vector
os.chdir('/home/gips/Documents/PreDoc/coding/BLENDPY')
def createBranch(_diam,_P1,_P2,index):
#    bpy.ops.curve.primitive_nurbs_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
#    Bc=bpy.data.objects['NurbsCurve']
    BC=bpy.data.objects['BezierCurve']
    BC.name='B'+str(index)
    BC.data.bevel_depth=_diam
    BC.data.use_fill_caps = True
    BC.data.splines[0].bezier_points[0].co=_P1
    BC.data.splines[0].bezier_points[0].handle_left_type='AUTO'#-(-_P1+_P2)/2
    BC.data.splines[0].bezier_points[0].handle_right_type='AUTO'
    BC.data.splines[0].bezier_points[1].co=_P2
    BC.data.splines[0].bezier_points[1].handle_left_type='AUTO'#-(-_P1+_P2)/2
    BC.data.splines[0].bezier_points[1].handle_right_type='AUTO'
    
#    Bc.data.splines[0].points[2].co=_P2
#    Bc.data.splines[0].points[3].co=_P2+(-_P1+_P2)/2
class NODE:
    def __init__(self,_index,_x,_y,_z):
        self.index=int(_index)
        self.x=float(_x)
        self.y=float(_y)
        self.z=float(_z)
class ELEMENT:
        def __init__(self,_index,_n1,_n2,_width):
            self.index=int(_index)
            self.n1=int(_n1)
            self.n2=int(_n2)
            self.width=float(_width)
list_nodes = [] 
list_elements = [] 
file1=open("Points.txt","r")
myline = file1.readline()
while myline:
    if myline[0]!= "#":
        if myline.count("*NODE") == 1:
            myline = file1.readline()
            while myline != "*END":
                index=myline[1:12]
                x=myline[13:24]
                y=myline[25:36]
                z=myline[37:48]
                list_nodes.append(NODE(index,x,y,z))
                myline = file1.readline()
    myline = file1.readline()
#print(list_nodes[1].index)
file1.close()
file2=open("Streams.txt","r")
myline = file2.readline()
while myline:
    if myline[0]!= "#":
        if myline.count("*ELEMENT_BEAM") == 1:
            myline = file2.readline()
            while myline.count("*END") ==0 :
                index=myline[1:12]
                n1=myline[13:24]
                n2=myline[25:36]
                width=myline[37:48]
                list_elements.append(ELEMENT(index,n1,n2,width))
                myline = file2.readline()
    myline = file2.readline()
for i in list_nodes:
    print(i.index)
for i in list_elements:
    V1=Vector((list_nodes[i.n1-1].x, list_nodes[i.n1-1].y, list_nodes[i.n1-1].z))
    V2=Vector((list_nodes[i.n2-1].x, list_nodes[i.n2-1].y, list_nodes[i.n2-1].z))
    createBranch(i.width,V1,V2,i.index)
    #print(list_nodes[i.n1].index)
#for i in list_elements:
#    print(i)
#    print(list_nodes[i.n1])
#    nP2=list_nodes[i.n2]
#    width=i.width
#    index=i.index