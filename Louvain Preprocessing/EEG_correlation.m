EEG_fileDirec = input('Directory containing EEG files (.edf): \n', 's');
files = dir(EEG_fileDirec);

for i = [1:length(files)]
    [~, ~, extension] = fileparts(files(i).name);
    if extension == ".edf"
        WPLI_mod(files(i).name(1:end-4));
    end 
end

