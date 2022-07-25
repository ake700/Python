# Predictive machine learning based on several students' 16S rRNA gene sequencing datasets.

Included are a copy of 16S rRNA CSV for the phyla in addition to the Jupyter Notebook associated with the model.

The model explored in this project is the Random Forest Regressor, but future work will explore other time-series models based on the [scikit-learn page](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) and others. 

## Data Collection

16S rRNA data were compiled from the same gut model from different students. Therefore, timepoints, composition, and internal conditions of the machine vary and impact the raw data used for the ML model. Data (e.g., timepoints) were normalized prior to the model, but will still have an impact on the accuracy. 

## Results

Due to the variability in experiments, it's difficult to accurately conclude whether certain taxa are more likely to drive changes in the gut microbiota within the machine. Based on the current model, time is the biggest factor in driving the change in microbiota despite differences in experimental design and sequencing. Whether any taxa can indeed drive changes to the gut microbiota will need to be assessed for each separate dataset. 

A future iteration will be to create the same ML model for each dataset to identify any similarities and differences in contributing factors to microbial change. 
