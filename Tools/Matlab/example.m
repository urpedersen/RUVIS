%% Example of Matlab script for making a RUVIS trejectory file.

% Make 4 of type 0 and 4 of type 1
traj.N=8;
traj.types=2;

% Set diameter of particle types
traj.diameter=[1.0 0.8];

% Set color of particle types
traj.color=[0.7 0.7 0.9; 0.0 0.0 0.9];

% Set boundaries of cubic box
traj.bbox=[-10 -10 -10 10 10 10];

% Generate a dummy trajectory with 5 frames
frames=5;
traj.xyz = zeros(traj.N*frames,4);
for f=1:frames       % loop frames
    for n=1:traj.N   % loop particles
        type=mod(n,traj.types);
        x=(rand()-0.5)*(traj.bbox(4)-traj.bbox(1));
        y=(rand()-0.5)*(traj.bbox(5)-traj.bbox(2));
        z=(rand()-0.5)*(traj.bbox(6)-traj.bbox(3));
        row=(f-1)*traj.N+n;
        traj.xyz(row,:)=[type x y z];
    end
end

% Write the xyz.js file for RUVIS
ruvis(traj)