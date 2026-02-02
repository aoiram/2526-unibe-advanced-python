import numpy as np
import pandas as pd


def test_numpy_and_pandas_work_together():
    """
    Tests basic interaction between NumPy and pandas.

    - Creates a NumPy array
    - Performs a simple numeric operation
    - Converts the array into a pandas DataFrame
    - Verifies that the DataFrame contains the expected data
    """

    arr = np.array([1, 2, 3])

    # Check a simple NumPy operation
    assert arr.mean() == 2

    # Convert to a pandas DataFrame
    df = pd.DataFrame({"numbers": arr})

    # Verify DataFrame content
    assert df["numbers"].sum() == 6
    assert len(df) == 3
    assert list(df.columns) == ["numbers"]


def test_numpy_statistics():
    """
    Tests simple statistical operations in NumPy.

    - Creates a NumPy array
    - Computes mean, minimum, and maximum
    - Verifies the results
    """

    data = np.array([10, 20, 30, 40])

    assert data.mean() == 25
    assert data.min() == 10
    assert data.max() == 40


def test_pandas_groupby():
    """
    Tests a basic pandas groupby operation.

    - Creates a DataFrame
    - Groups values by a column
    - Checks the aggregated results
    """

    df = pd.DataFrame({
        "city": ["Bern", "Bern", "Zürich"],
        "value": [10, 20, 5]
    })

    grouped = df.groupby("city")["value"].sum()

    assert grouped["Bern"] == 30
    assert grouped["Zürich"] == 5
    assert len(grouped) == 2


import matplotlib.pyplot as plt


def test_matplotlib_creates_figure():
    """
    Tests basic figure creation in matplotlib.

    - Creates a figure and axis
    - Verifies that the figure exists
    - Verifies that exactly one axis is present
    """

    fig, ax = plt.subplots()

    # Check that a figure object exists
    assert fig is not None

    # Check that one Axes object exists
    assert len(fig.axes) == 1
    assert ax in fig.axes
