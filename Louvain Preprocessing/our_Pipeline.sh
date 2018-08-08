#!/bin/bash
  
#####DEFAULT PARAMETERS####
defaultCorrelation=0.70
defaultWindow=50
defaultCommdyCost=111
##########################


######UNPACK ARGUMENTS
startPoint="$1"
dataPath="/home/luislove/EEG_data/2_stuff"
imagePath="/home/luislove/EEG_data/output"
correlation=${2:-$defaultCorrelation}
window=${3:-$defaultWindow}
commdyCost=${4:-$defaultCommdyCost}
#######################

MY_PATH="/home/shared_brain/BrainCode/helpers/pachyPipelineAutomation/"

source $MY_PATH'correlationScript.sh' $dataPath $imagePath $correlation $window
   echo 'Starting the split file with corr '$correlation
   /home/shared_brain/BrainCode/Louvain/split_files.py cor_weights_cor70.pair
   echo '>> Pipeline: Finished (NOT FULLY COMPLETED) <<<'
