# Reference : https://stackoverflow.com/questions/47585723/kmeans-clustering-in-pyspark


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="KMeansExample")
sqlContext = SQLContext(sc)

df = sqlContext.createDataFrame([[0, 33.3, -17.5],
                              [1, 40.4, -20.5],
                              [2, 28., -23.9],
                              [3, 29.5, -19.0],
                              [4, 32.8, -18.84]
                             ],
                              ["other","lat", "long"])

df.show()

vecAssembler = VectorAssembler(inputCols=["lat", "long"], outputCol="features")
new_df = vecAssembler.transform(df)
new_df.show()

kmeans = KMeans(k=2, seed=1)  # 2 clusters here
model = kmeans.fit(new_df.select('features'))

transformed = model.transform(new_df)
transformed.show()  