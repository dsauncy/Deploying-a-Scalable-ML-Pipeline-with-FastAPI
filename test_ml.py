import pytest
import pandas as pd
from sklearn.linear_model import LogisticRegression
from ml.data import process_data
from ml.model import train_model
import numpy as np



# set up some data

# Creating a dataframe using pandas that will be run through training
# imagine this is a table representing a bunch of houses that have various
# features.  So like, a den, a kitchen, a yard.  And we want to see
# what features contribute to selling a house

# (this is made up data)

data = pd.DataFrame(
    {
        'den': [0, 0, 0, 0, 0, 1],
        'kitchen': [0, 1, 1, 1, 1, 1],
        'garage': [1, 0, 1, 1, 0, 1, ],
        'yard': [0, 0, 0, 0, 0, 1],
        'sold': [0, 0, 0, 1, 1, 1]
    }
)

# Process data
X_train, y_train, _, _ = process_data(
    data,
    categorical_features=['den', 'kitchen', 'garage', 'yard'],
    label='sold',
    training=True,
)

# Train model
model = train_model(X_train, y_train)

def test_one():
    """
    Testing to determine if any ML functions return the expected type of result.
    """

    # Check if model returned by train_model is of the expected type
    # (looking for LogicalRegression)
    expected_model = LogisticRegression
    assert isinstance(model, expected_model)


def test_two():
    """
    Test to determine if the ML model uses the expected algorithm.
    """
    # Check if the model uses the expected algorithm
    assert isinstance(model, LogisticRegression)


def test_three():
    """
    Test to determine if  the training and test datasets have the expected size or data type.
    """
    # Check to see if X_train is a Pandas DataFrame or NumPy array
    assert isinstance(X_train, (pd.DataFrame, np.ndarray))

    # Check if y_train is a Pandas Series or Numpy Array
    assert isinstance(y_train, (pd.Series, np.ndarray))