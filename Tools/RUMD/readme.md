This folder contains tools for usage with [RUMD](http://rumd.org/)

## Usage with Jupyter
Write the foloing 
```py
ruvispath="/net/dirac/urp/git/RUVIS/"
sys.path.insert(1,ruvispath + "Tools/RUMD")
import ruvis as rv
rv.update()
from IPython.display import IFrame
IFrame('ruvis.htm',width='100%',height=400)
```
