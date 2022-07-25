# Classification in Machine Learning using `scikit-learn` in Python

Included here are the Jupyter Notebook markdown, the CSV containing the data, and an image of the Feature Importance as a result of the model.

The models explored in this project are:
* Logistic Regression - `LogisticRegression()`
* K-Nearest Neighbors - `KNeighboursClassifier()`
* RandomForest - `RandomForestClassifier()`

## Data Collection

Data was collected in Microsoft Excel every week via online credit card usage history. Cash spending was recorded as often as possible, but is negligible. 

## Results

Based on the current ML model, the biggest contributing factor to overspending (i.e., exceeding monthly budget) is the frequency of spending. In other words, regardless of the location or amount of the spending, it's most likely that I would go overbudget if I were to have multiple spending days within the month. 
