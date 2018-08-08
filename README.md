# Dynamic-Communities-EEG
Classifying generalized social anxiety disorder using dynamic community analysis of EEG signals.

Background
Electroencephalography (EEG) connectivity from patients diagnosed with generalized social anxiety (gSAD) have shown an overall increase in clustering coefficient and decrease in path length compared to those without gSAD. Our experiment aims to study EEG graph-based dynamics for the purpose of classifying gSAD.

EEG graphs created with weighted-phase lag index (WPLI) connectivity from 64 patients were analyzed by community identification algorithms to understand the behavior of EEG sensor nodes over time. Classification of the gSAD state was performed on the outputs of these dynamic communities using support vector machines (SVM), random forest, and decision trees.

Accuracy of the classification methods reached approximately 0.60 in this binary class problem. Dynamic community analysis reveals that the average community size was smaller and the maximum stay was longer in gSAD samples. 

Conclusions
Community dynamics in gSAD and healthy patients may not have the variance required for high-accuracy classification. Future studies could focus more on clustering coefficient and path length.

