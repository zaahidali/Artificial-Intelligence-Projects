**K-Means Algorithm**

This repository contains an implementation of the K-Means algorithm in Python. The K-Means algorithm is a popular unsupervised machine learning algorithm used for clustering data points into distinct groups based on their similarities.

## Files

- `kmeans.py`: The main Python code file containing the implementation of the K-Means algorithm.
- `test.csv`: Input file containing the test dataset.
- `train.csv`: Input file containing the training dataset.
- `README.md`: This readme file providing an overview of the project.

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required dependencies by running the following command:

   ```
   pip install matplotlib
   pip install pandas
   ```

3. Place your training data in the `train.csv` file and your test data in the `test.csv` file. The data should be in CSV format.
4. Run the `kmeans.py` script using the following command:

   ```
   python kmeans.py
   ```

5. The algorithm will cluster the data points and generate a plot showing the clusters.
6. The resulting plot will be saved as `plot.pdf` in the current directory.

## Customization

- You can adjust the number of clusters (`k`) in the `kmeans.py` file by modifying the `clusters` variable.
- The colors used for the clusters can be customized by modifying the `colors` list in the `kmeans.py` file.
- If you want to use different input file names or file paths, make sure to update the `test.csv` and `train.csv` file paths in the `kmeans.py` file.

## Example Output

The resulting plot will show the clusters formed by the K-Means algorithm based on the provided data points. Each cluster will be represented by a different color.

## References

- [K-Means Clustering](https://en.wikipedia.org/wiki/K-means_clustering)

Please note that this implementation assumes that the input data is suitable for the K-Means algorithm. Ensure that your data is properly preprocessed and formatted before running the algorithm.

For any further information or inquiries, please contact [author's name] at [author's email].

Enjoy clustering with K-Means!