#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" RUVIS: visualization of MD simulations (http://urp.dk/ruvis/)

Animates RUMD trajectory in browser using the babylonJS API (babylonjs.com)

Usage example:
    import ruvis
    ruvis.view()
    
    This will open up an external browser (if you are in a folder
    containing a RUMD simulation). 
    Hit 'i' for information screen with help.
    
    The modules has some string with setting:
        path: location of RUVIS (download at http://urp.dk/ruvis/)
        browser: external browser
        diameterStr: Set particle diameters
        colorStr: Set particle colorts
     
"""

path = '/net/dirac/urp/git/RUVIS/'
html = 'Platforms/WebGL/ruvis.htm'
babylon = 'Platforms/WebGL/babylon.2.3.js'

browser = 'chromium'
diameterStr='var diameter=[1.0,0.8,1.0,1.0];\n'
colorStr='var color=[new BABYLON.Color3(0.7, 0.7, 0.9), \
new BABYLON.Color3(0.0, 0.0, 0.9), \
new BABYLON.Color3(0.9, 0.0, 0.0), \
new BABYLON.Color3(0.0, 0.9, 0.0)];\n'

def view():
    """ View RUMD simulation """
    write_xyz_js()
    view_in_webbrowser()

def view_in_webbrowser():
    """ Open external webbrowser to view simulation. 
    The default browser is chromium. Change to other browser like this
       ruvis.browser='firefox'
    """
    import shutil
    shutil.copy(path+html,'.')
    shutil.copy(path+babylon,'.')
    import subprocess
    subprocess.run([browser,'ruvis.htm'])
    
def write_xyz_js():
    """ Write xyz.js file with trejectory data """
    import gzip
    trjdir='./TrajectoryFiles/'
        
    fo = open('xyz.js','wt') # Output file
    fo.write('// Trajactory file for RUVIS\n')
    
    fname=trjdir+"/restart0000.xyz.gz"
    f = gzip.open(fname, "r")
    natoms = int(f.readline())
    fo.write('var N=%d\n' % natoms)
    
    commentline = f.readline()
    sections = commentline.decode().split(' ')
    for section in sections:
        chunk=section.split('=')
        if(chunk[0]=='sim_box'):
            value=chunk[1].split(',')
            X=float(value[1])
            Y=float(value[2])
            Z=float(value[3])
            fo.write('var bbox=[%f,%f,%f,%f,%f,%f];\n' % (-X/2,-Y/2,-Z/2,X/2,Y/2,Z/2))
        if(chunk[0]=='numTypes'):
            fo.write('var types=%d;\n' % int(chunk[1])) 
            
    
    fo.write(diameterStr)
    fo.write(colorStr)
    fo.flush()
    
    f = open(trjdir + 'LastComplete_restart.txt', 'rt')
    last_block = int(f.readline().split(' ')[0])
    f.close()
    
    fo.write('var xyz=[\n')
    isFirst = True
    for block in range(last_block + 1):
        fname=trjdir+"/restart%0.4d.xyz.gz"%block
        f = gzip.open(fname, "r")
         # Number of atoms
        natoms = int(f.readline())
        commentline = f.readline()
        for line in f:
            column = line.decode().split(' ')
            i=int(column[0])
            x=float(column[1])
            y=float(column[2])
            z=float(column[3]) # FIXME
            if(isFirst):
                fo.write('%d,%3.3f,%3.3f,%3.3f\n' % (i,x,y,z))
                isFirst=False
            else:
                fo.write(',%d,%3.3f,%3.3f,%3.3f\n' % (i,x,y,z))

            
        f.close()

    fo.write(']\n')
    fo.close()
    print('Wrote xyz.js with trajectory RUVIS.')
