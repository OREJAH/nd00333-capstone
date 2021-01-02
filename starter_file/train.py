import argparse
import os
import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error, auc
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from azureml.core.workspace import Workspace
from azureml.core import Run, Dataset

import joblib

run = Run.get_context()

    workspace = run.experiment.workspace
    dataset_name = 'heart-failure'
    dataset = Dataset.get_by_name(workspace=workspace, name=dataset_name)

    df = dataset.to_pandas_dataframe()

    y = df.pop("DEATH_EVENT")

         # Clean data
                
def clean_data(data):

    x_df = data.to_pandas_dataframe().dropna()
    y_df = x_df.pop("DEATH_EVENT")
    return x_df, y_df

X, y = clean_data(dataset)
        
# TODO: Split data into train and test sets.

x_train, x_test, y_train, y_test=train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=42)


def main():
    # Add arguments to script
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")
    
    args = parser.parse_args()

    run.log("Regularization Strength: ", np.float(args.C))
    run.log("Max iterations: ", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    
    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model,"outputs/hyperdrive_model.joblib")
    
if __name__ == '__main__':
    main()
