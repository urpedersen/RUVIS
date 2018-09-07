This folder contains tools for usage with [RUMD](http://rumd.org/) software package for Molecular Dynamics simulations.

All the below usage examples assume that you are located in folder with a RUMD simulation. The examples will generate a webpage in the folder that can be viewed with any browser. The examples assume you have firefox installed, however, pick your favorite.

## Usage from Linux commandline
```sh
path=/net/dirac/urp/git/RUVIS/
cp $path/Platforms/WebGL/* .
$path/Tools/RUMD/rumd2js
firefox ruvis.htm
```

## Usage with iPython console
Generate html/js files and launch RUVIS in external browser.
```py
path="/net/dirac/urp/git/RUVIS/"
sys.path.insert(1,path + "Tools/RUMD")
import ruvis as rv
rv.browser='firefox'
rv.visualize()
```

## Usage with Jupyter notebook
```py
path="/net/dirac/urp/git/RUVIS/"
sys.path.insert(1,path + "Tools/RUMD")
import ruvis as rv
rv.update()
from IPython.display import IFrame
IFrame('ruvis.htm',width='100%',height=400)
```
