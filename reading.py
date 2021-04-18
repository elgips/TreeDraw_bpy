#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 00:08:13 2021

@author: gips
"""
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
file1=open("node_list_test.txt","r")
myline = file1.readline()
while myline:
    if myline[0]!= "#":
        if myline.count("*NODE") == 1:
            myline = file1.readline()
            while myline != "*END":
                index=myline[1:10]
                x=myline[11:20]
                y=myline[21:30]
                z=myline[31:40]
                list_nodes.append(NODE(index,x,y,z))
                myline = file1.readline()
    myline = file1.readline()
print(list_nodes[1].index)
file1.close()
file2=open("element_list_test.txt","r")
myline = file2.readline()
while myline:
    if myline[0]!= "#":
        if myline.count("*ELEMENT_BEAM") == 1:
            myline = file2.readline()
            while myline.count("*END") ==0 :
                index=myline[1:10]
                n1=myline[11:20]
                n2=myline[21:30]
                width=myline[31:40]
                list_elements.append(ELEMENT(index,n1,n2,width))
                myline = file2.readline()
    myline = file2.readline()
print(list_elements[1].n1)