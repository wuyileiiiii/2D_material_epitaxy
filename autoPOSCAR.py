#!/usr/bin/python
#本程序用来生成MOS2在衬底不同位置的POSCAR
#需要文件：POSCAR
#Author: Yilei Wu
#Date: 2022/10/27

import re
import numpy as np
from ase import io
from ase.geometry.analysis import Analysis

#读取POSCAR
atoms = io.read('POSCAR.vasp', format='vasp')
c = atoms.get_cell()
x = c[0][0]
y = c[1][1]
x_step = x/20
y_step = y/20

#读取POSCAR内容并记录
POSCAR_file = open("POSCAR.vasp", 'r')
POSCAR_line = POSCAR_file.readlines()


#分开不同原子，并记录其位置
Au = []
#O = []
Mo = []
S = []
symbols = atoms.get_chemical_symbols()
atomnumber = len(symbols)
for i in range(atomnumber):
    ss = symbols[i]
    if ss == "Au":
        Au.append(i)
    #elif ss == "O":
        #O.append(i)
    elif ss =="Mo":
        Mo.append(i)
    elif ss =="S":
        S.append(i)
    else:
        print("error")

#x方向平移
position = atoms.get_positions()
MoS2 = S
MoS2.extend(Mo)

for m in range(20):
    for n in range(20):
        name = "POSCAR_" + str(m) + "_" + str(n)
        file_out = open(name, 'w')
        for k in range(204):
            file_out.write(POSCAR_line[k])
        for i in range(196, 246):
            print(position[i])
            atom_x_change = float(position[i][0]) + m * x_step
            atom_y_change = float(position[i][1]) + n * y_step
            atom_D_x = atom_x_change
            atom_D_y = atom_y_change
            atom_D_z = float(position[i][2])
            print("    ", atom_D_x, "    ", atom_D_y, "    ", atom_D_z, file=file_out)


file_out.close()

print(MoS2)



