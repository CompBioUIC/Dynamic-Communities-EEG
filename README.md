# Dynamic-Communities-EEG

Classifying generalized social anxiety disorder (gSAD) using dynamic community analysis of EEG signals.

This repo contains the scripts needed to process raw EEG files (.edf) into a format that be used by static community (Louvain) and dynamic community (CommDy) algorithms. Scikit-learn machine learning algorithms are the final step used for classification of gSAD.

## Getting Started

Prerequisites
1) Raw EEG data (.edf files)
2) A copy of the CommDy and Louvain codebase
3) MATLAB
4) Python 2.7 (for running CommDy) AND Python 3 (for running sci-kit learn)

## Pipeline Steps


	1. Received .EDF files from experiment
	2. On the brain server, do the following steps.
	3. Run 'WPLI_mod.m' to convert .edf files into .mat files.
	4. Use the 'mat2pair.sh' shell script to automatically run the 'convert_to_pair.m' script. This converts .mat files into .txt files		
	5. Use python script 'convert_to_pair.py' to convert the saved .txt matrices into a .pair format
	6. Separated the patient data into their own folders (needs automation)
	7. Switch to Pachy server, transfer all data. Run the following steps.
	8. Organize and put all data into labeled folders
	9. Run the below steps by running bash Auto.sh
	10. Run Louvain algorithm on each folder.
	11. Run CommDy on each folder.*
	12. Analyze with Rstats script.
	13. Classify the files titled "*_ind_stat_c***.txt' using your preferred method (machine learning, etc.)

*See umbertoDifa's brain-project repository for instructions on how to run the CommDy algorithm.
https://github.com/umbertoDifa/brain-project/blob/master/pipeline-manual.txt 



## Contributing

See also the list of contributors who participated in this project.
Mathew Yang (python, shell, and machine learning scripts) contact for questions: mathew.d.yang@gmail.com
Luis Love (python and shell scripts)
Chayant (CommDy author)
Mengqi Xing (WLPI.m writer, provided EEG data for me)
Tanya Berger-Wolf (servers and guidance)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
Acknowledgments
