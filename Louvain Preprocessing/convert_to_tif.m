%{
    Desired Frequency Ranges:
        Delta -> 1
        Theta -> 2
        Alpha -> 3
        Beta  -> 4
%}

function convert_to_tif(desiredFreq, dataDirec, parentDirec)

    mkdir(parentDirec, 'brain_freq');
    dest = [parentDirec, '/brain_freq'];

    delta = [1:3];      mkdir(dest, 'delta');
    theta = [4:8];      mkdir(dest, 'theta');
    alpha = [8:14];     mkdir(dest, 'alpha');
    beta = [13:30];     mkdir(dest, 'beta');

    freqs = {delta, theta, alpha, beta};
    freq_Folder = {'delta', 'theta', 'alpha', 'beta'};

    files = dir(dataDirec);
    fileCount = countFiles(files);
    counter = 0;
    for i = [1:length(files)]
        [~, file, extension] = fileparts(files(i).name);
        if extension == ".mat"
            load(files(i).name);

            file = ZeroPad(file);

            x = cell2mat(freqs(desiredFreq));
            for y = x
               freqBand = ZeroPad(int2str(y));
               for z = [1:130]
                   image = Connect(:,:,y,z);
                   z = ZeroPad(int2str(z));
                   filename = ['freq_', z,'.tif'];
                   imwrite(image, [dest, '/', cell2mat(freq_Folder(desiredFreq)), '/',filename]);
               end
            end

            counter = counter + 1;
            fprintf('%d of %d completed\n', counter, fileCount);
        end
    end
end

function result = countFiles(files)

    result = 0;
    for i = [1:length(files)]
        [~, ~, extension] = fileparts(files(i).name);
        if extension == ".mat"
            result = result + 1;
        end
    end
end

function result = ZeroPad(s)

    if (length(s) < 3)
       for i = [1:3-length(s)]
           s = ['0', s];
       end
    end
    
    result = s;
end

