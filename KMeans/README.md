# Spark K Means

This folder contains the source code/ Jupyter notebook for the K Means clustering program using Spark ML Lib. The `sample` folder contains a sample spark K Means clustering code with a small dataset of 5 datapoints from the link : https://stackoverflow.com/questions/47585723/kmeans-clustering-in-pyspark

### Inputs

The input to the program is the Iris Dataset. https://archive.ics.uci.edu/ml/datasets/iris 

Excerpts from the dataset description: 
   --- The data set contains 3 classes of 50 instances each,
       where each class refers to a type of iris plant.  One class is
       linearly separable from the other 2.
   --- Predicted attribute: class of iris plant.

### Outputs

We have performed the Clustering of the classes in the dataset by using the elbow method and also visually representing the different clusters using seaborn library. 

The notebook has all the details and outputs from the code run.

### Steps to run

1. Install Apache Hadoop, HDFS, Spark and Yarn.
2. Start the dfs nodes (Namenode, Datanode etc) using `sbin/start-dfs.sh` from inside the hadoop installation folder. 
3. Start YARN (Nodemanager and Resourcemanager) using `sbin/start-yarn.sh` from inside the hadoop installation folder.
4. Install the dependencies required such as pyspark, seaboarn, scikit-learn etc.
5. Make sure spark cluster is up and running.
5. Execute the cells in the jupyter notebook. Spark context will communicate for resources from the notebook.

### Reference

https://www.data4v.com/tutorial-k-means-clustering-on-spark/ \
https://stackoverflow.com/questions/47585723/kmeans-clustering-in-pyspark