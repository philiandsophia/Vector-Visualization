# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:42:17 2017

@author: user
"""

#https://stackoverflow.com/questions/3461869/plot-a-plane-based-on-a-normal-vector-and-a-point-in-matlab-or-matplotlib

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import *
x = symbols('x')
init_printing(use_unicode=True)








def plot_cross_products(a,b):
    "a and b are two vectors being crossed, this function returns a cross b. a and b needs to be a list"
    #green vector is the result of cross product
    #cross_product = [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    #didn't know there was np.cross
#    soa = np.array([a,b,np.cross(a,b)])
#    print(soa)
#other person's codes went something like 
##soa = np.array([[0, 0, 1, 1, -2, 0], [0, 0, 2, 1, 1, 0],
#                [0, 0, 3, 2, 1, 0], [0, 0, 4, 0.5, 0.7, 0]])
#
#X, Y, Z, U, V, W = zip(*soa)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.quiver(X, Y, Z, U, V, W)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    U,V,W = zip(a,b,np.cross(a,b))
    print (np.cross(a,b))
    ax.quiver(0,0,0,U,V,W, color = ('b','b','r'))
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.show()

def plot_a_line_in_3d(position,direction):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(-10,10)
    x = position[0] + t*direction[0]
    y = position[1] + t*direction[1]
    z = position[2] + t*direction[2]
    ax.plot(x,y,z, label = '{}+t{}'.format(position,direction))
    ax.legend()
    plt.show()

def poi_in_3d_lines(position1,direction1,position2,direction2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(-100,100)
    x = position1[0] + t*direction1[0]
    y = position1[1] + t*direction1[1]
    z = position1[2] + t*direction1[2]
    u = position2[0] + t*direction2[0]
    v = position2[1] + t*direction2[1]
    w = position2[2] + t*direction2[2]
    ax.plot(x,y,z)
    ax.plot(u,v,w)
    plt.show()

def lines_as_vectors(position,direction):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    t = np.linspace(-5,5)
    x = position[0] + t*direction[0]
    y = position[1] + t*direction[1]
    z = position[2] + t*direction[2]
    ax.plot(x,y,z)
    u,v,w = zip(position,direction)
    ax.quiver(0,0,0,u,v,w, color = ('r', 'b'))
    print (u,v,w)
    plt.show()



def plot_planes(normal, apoint):
    
    #point or normal can't be zero vector     
    apoint = np.array(apoint)
    normal = np.array(normal)
    
    # a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
    d = -apoint.dot(normal)
    # create x,y

    xx, yy = np.meshgrid(range(25),range(25))
    
 # calculate corresponding z
    z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
    
    # plot the surface
    plt3d = plt.figure().gca(projection='3d')
    plt3d.plot_surface(xx, yy, z)
    plt.show()

def find_intersection_between_plane_and_line(position,direction,plane):
    scalar = solveset(plane[0]*(position[0]+direction[0]*x)+plane[1]*(position[1]+direction[1]*x)+plane[2]*(position[2]+direction[2]*x)+plane[3],x)
    scalar = list(scalar)
    if not scalar:
        return 'paraelle'
    u = position[0] + direction[0]*scalar[0]
    v = position[1] + direction[1]*scalar[0]
    w = position[2] + direction[2]*scalar[0]
    return [u,v,w]

def plot_plane_and_line(position,direction,plane):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    t = np.linspace(-200,200)
    x = position[0] + t*direction[0]
    y = position[1] + t*direction[1]
    z = position[2] + t*direction[2]
    normal = np.array([plane[0],plane[1],plane[2]])
    xx, yy = np.meshgrid(range(500),range(500))
    z1 = (-normal[0] * xx - normal[1] * yy - plane[3]) * 1. /normal[2]
    ax.plot_surface(xx, yy, z1, alpha = 0.2)
    ax.plot(x,y,z)
    point = find_intersection_between_plane_and_line(position,direction,plane)
    print (point)
    ax.scatter(point[0],point[1],point[2], color = 'green')
    plt.show()
 
    
#def intersection_of_two_planes(plane1,plane2):
#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection = '3d')
#    normal1 = np.array([plane1[0],plane1[1],plane1[2]])
#    xx1, yy1 = np.meshgrid(range(1000),range(1000))
#    z1 = (-normal1[0] * xx1 - normal1[1] * yy1 - plane1[3]) * 1. /normal1[2]
#    normal2 = np.array([plane2[0],plane2[1],plane2[2]])
#    xx2, yy2 = np.meshgrid(range(1000),range(1000))
#    z2 = (-normal2[0] * xx2 - normal2[1] * yy2 - plane2[3]) * 1. /normal2[2]
#    direction = np.cross([plane1[0],plane1[1],plane1[2]],[plane2[0],plane2[1],plane2[2]])
#    y1 = 0
#    z1 = 0 
#    x1 = -1*plane1[3]
#    x2 = 0
#    z2 = 0
#    y2 = -1*plane1[3]
#    #aline = t * [x2-x1,y2-y1,z2-z1] + [x1,y1,z1]
#    intersection_point = find_intersection_between_plane_and_line([x1,y1,z1],[x2-x1,y2-y1,z2-z1],plane2)
#    s = np.linspace(-10,10)
#    x = s*direction[0] + intersection_point[0]
#    y = s*direction[1] + intersection_point[1]
#    z = s*direction[2] + intersection_point[2]
#    ax.plot_surface(xx1, yy1, z1, alpha = 0.7)
#    ax.plot(x,y,z)
#    ax.plot_surface(xx2, yy2, z2, color = 'red' )
#    plt.show()
#doesn't work 
