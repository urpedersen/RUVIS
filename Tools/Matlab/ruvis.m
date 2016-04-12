%%  Convert MD trajectory to RUVIS (http://www.urp.dk/ruvis)
%
% Writes a xys.js trajectory file for visualization of a 
% Molecular Dynamics (MD) trajectory with RUVIS. 
% Please visit www.urp.dk/ruvis for documentation.
%
function ruvis(traj)

    if(nargin~=1)
        error('This function expects one traj struct as input.')
    end
    file = fopen('xyz.js','w');
    
    fprintf(file,'var bbox=[%3.3f,%3.3f,%3.3f,%3.3f,%3.3f,%3.3f];\n',traj.bbox);
    fprintf(file,'var N=%d;\n',traj.N);
    fprintf(file,'var types=%d;\n',traj.types);
    
    for c=1:length(traj.diameter)
        if(c==1)
            fprintf(file,'var diameter=[%3.3f',traj.diameter(1));
        else
            fprintf(file,',%3.3f',traj.diameter(c));
        end
    end
    fprintf(file,'];\n');
    
    for c=1:length(traj.diameter)
        if(c==1)
            fprintf(file,'var color=[new BABYLON.Color3(%3.3f,%3.3f,%3.3f)',traj.color(1,:));
        else
            fprintf(file,',new BABYLON.Color3(%3.3f,%3.3f,%3.3f)',traj.color(c,:));
        end
    end
    fprintf(file,'];\n');
    
    for c=1:length(traj.xyz)
        if(c==1)
            fprintf(file,'var xyz=[%d,%3.3f,%3.3f,%3.3f',traj.xyz(1,:));
        else
            fprintf(file,',%d,%3.3f,%3.3f,%3.3f',traj.xyz(c,:));
        end
    end
    fprintf(file,'];\n\n');
    
    fclose(file);
end