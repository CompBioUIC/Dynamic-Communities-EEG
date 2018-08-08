#!/bin/bash
  
#========================================================================
# In order to run the script, please verify that the following variables
# are specified correctly:
#
#   MATLAB_DIREC
#   PARENT_DIREC
#   DATA_DIREC
#   FREQ
#
# The .tif files will be stored in a directory called .../brain_freq
#
#========================================================================

# Frequency Range Desired (Delta = 1; Theta = 2; Alpha = 3; Beta = 4;):
FREQ=${1:-2}

# Directory (MATLAB):
#MATLAB_DIREC='/Applications/MATLAB_R2017b.app/bin'

# Directory (Store the created .tiff files):
PARENT_DIREC="'/Users/luis/Documents/Brain Project/brain-project-master/Data'"

# Directory (Get the .mat files):
DATA_DIREC="'/Users/luis/Documents/Brain Project/brain-project-master/Data/EEG data'"

# Adds the directory of the .mat files to MATLAB's path; calls the MATLAB Script
EXEC_CODE="try addpath(genpath("$DATA_DIREC")); convert_to_tif("$FREQ", "$DATA_DIREC", "$PARENT_DIREC"); catch; end; quit;"


# Executes MATLAB Script
$MATLAB_DIREC/matlab -nodisplay -nodesktop -nojvm -r "$EXEC_CODE"
