import bpy,bmesh
import numpy as np
from mathutils import Euler, Matrix, Quaternion, Vector
def createBranch(_diam,_P1,_P2,index):
    bpy.ops.curve.primitive_nurbs_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    Bc=bpy.data.objects['NurbsCurve']
    Bc.name='NC'+str(index)
    Bc.data.bevel_depth=_diam
    bpy.context.object.data.use_fill_caps = True
    Bc.data.splines[0].points[0].co=_P1
    Bc.data.splines[0].points[1].co=(2*_P1+_P2)/3
    Bc.data.splines[0].points[2].co=(_P1+2*_P2)/3
    Bc.data.splines[0].points[3].co=_P2
P1=Vector((0.0, 0.0, 0.0, 1.0));
P2=Vector((1.0, 1.0, 1.0, 1.0));
Diam=0.1
createBranch(Diam,P1,P2);