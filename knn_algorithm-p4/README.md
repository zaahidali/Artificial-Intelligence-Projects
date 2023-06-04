# K-Nearest Neighbors (KNN) Algorithm

This repository contains the implementation of the K-Nearest Neighbors (KNN) algorithm for classification. The KNN algorithm is a popular machine learning algorithm used for both regression and classification tasks. It predicts the class of a given data point by finding the majority class among its k nearest neighbors in the training dataset.

## Project Description

The `knn.py` file contains the main code for implementing the KNN algorithm. It includes the following steps:

**1. Loading Data:** The code reads the training and testing data from the **`train.csv`** and **`test.csv`** files, respectively. Make sure to update these files with the appropriate data before running the code.

**2. Euclidean Distance:** The algorithm calculates the Euclidean distance between two data samples to measure their similarity.

**3. Neighbor Selection:** For each data point in the test dataset, the algorithm selects k nearest neighbors from the training dataset based on their Euclidean distances.

**4. Voting for Class:** The algorithm collects the class labels of the k nearest neighbors and determines the majority class as the predicted class for the test data point.

**5. Accuracy Calculation:** The algorithm compares the predicted class labels with the actual class labels in the test dataset and calculates the accuracy of the predictions.

**6. Plotting Accuracy:** The algorithm plots the accuracy of the predictions for different values of k using Matplotlib. The resulting plot is saved as a PDF file named **`plot.pdf`**.

## Requirements

To execute the code, you need to have the following dependencies installed:

- Python 3.x
- Pandas
- NumPy
- Matplotlib

## Installation

1. Clone this repository to your local machine or download the code as a ZIP file.

2. Install the required dependencies by running the following command:

   ```shell
   pip install pandas numpy matplotlib
   ```

   This will install the necessary packages to run the code.

## Usage

1. Update the input files:
   - **`train.csv`** should contain the training data with class labels.
   - **`test.csv`** should contain the testing data for which predictions need to be made.

   Make sure the data in the CSV files is correctly formatted, with the class labels in the last column.

2. Run the **`knn.py`** script using Python:

   ```shell
   python knn.py
   ```

3. The algorithm will calculate the accuracy of the predictions for different values of k and generate a plot named **`plot.pdf`**.

Feel free to customize the input data files and explore the code to further understand the implementation of the K-Nearest Neighbors (KNN) algorithm for classification.

For any questions or issues, please open an issue on this repository.

Happy coding!

---

Please make sure to replace **`train.csv`** and **`test.csv`** with the actual filenames you have for the training and testing data.