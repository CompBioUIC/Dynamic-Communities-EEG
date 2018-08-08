import os,sys
folder = '/home/shared_brain/EEG_shared/EEG_dataset-1/pair_files/brain_freq/theta/theta'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.txt', '.pair')
       output = os.rename(infilename, newname)
