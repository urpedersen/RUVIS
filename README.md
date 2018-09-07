# RUVIS
RUVIS animates a Molecular Dynamics (MD) trajectory in a web-page using the babylonJS API. Trajectories can be viewed a cross platforms, since it only requires a WebGL compatible browser (including Windows PC's, Mac OS, Linux, tablets and phones). Tools are provided for RUMD and Matlab simulations.

Please note that RUVIS is in an early development stage. Feel free to contact me ([Ulf R. Pedersen](http://urp.dk)) for questions or suggestions. The project is currently hosted at GitHub Inc., however, the permanet location of the project is http://urp.dk/ruvis/.

## Download code
Click the download button on GitHub, or get the source code from commandline with

`git clone https://github.com/urpedersen/RUVIS`

Use `git pull` in the RUVIS folder to update files to the lates versions.

## Usage
The folder Platforms/WebGL/ contains html and javascript files for a webpage.
An trajectory is assumed to be avalible in a file named `xyz.js`.
This file can be generated with the tools avaible in the folder Tools/

The tools will generate files for a webpage. You can view them with your favorite browser, or put them on your webserver.

Press `i` in the browser see information screen with keyboard shortcuts.

## Showcase
[Click here to try an interactive example](http://urp.dk/ruvis/ruvis.htm)


![RUVIS in Jupyter](http://urp.dk/ruvis/ruvisJupyter.png)
