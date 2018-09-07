This folder contains tools for usage with [RUMD](http://rumd.org/) software package for Molecular Dynamics simulations.

## Usage from Linux commandline
``sh
rumd2ruvis
``

## Usage with iPython console
Generate html/js files and launch RUVIS in external browser.
```py
ruvispath="/net/dirac/urp/git/RUVIS/"
sys.path.insert(1,ruvispath + "Tools/RUMD")
import ruvis as rv
rv.browser='chromium'
rv.visualize()
```

## Usage with Jupyter notebook
Write the foloing 
```py
ruvispath="/net/dirac/urp/git/RUVIS/"
sys.path.insert(1,ruvispath + "Tools/RUMD")
import ruvis as rv
rv.update()
from IPython.display import IFrame
IFrame('ruvis.htm',width='100%',height=400)
```
