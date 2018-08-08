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
# The .pair files will be stored in a directory called .../brain_freq
#
#========================================================================

# Frequency Range Desired (Delta = 1; Theta = 2; Alpha = 3; Beta = 4;):
FREQ=${1:-2}

# Directory (MATLAB):
MATLAB_DIREC='/usr/local/MATLAB/R2017b/bin'

# Directory (Store the created .pair files):
PARENT_DIREC="'/data/yang171/EEG_shared/EEG_dataset-1/pair_files'"

# Directory (Get the .mat files):
DATA_DIREC="'/data/yang171/EEG_shared/EEG_dataset-1/mat_files'"

# Adds the directory of the .mat files to MATLAB's path; calls the MATLAB Script
EXEC_CODE="try addpath(genpath("$DATA_DIREC")); convert_to_pair("$FREQ", "$DATA_DIREC", "$PARENT_DIREC"); catch; end; quit;"


# Executes MATLAB Script
$MATLAB_DIREC/matlab -nodisplay -nodesktop -nojvm -r "$EXEC_CODE"
