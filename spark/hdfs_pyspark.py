from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
conf = SparkConf().setAppName("iris")#.setMaster("spark://master:7077")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
iris = sqlContext.read.format("com.databricks.spark.csv")\
            .options(header="true",inferSchema="true")\
            .load("iris.csv").repartition(2).cache()
#print(type(iris))
#print(iris.show())

stridx = StringIndexer(inputCol="Name", outputCol = "label")
inputs = ["SepalLength","SepalWidth","PetalLength","PetalWidth"]
va = VectorAssembler(inputCols=inputs,outputCol="features")
pipeline = Pipeline(stages = [va,stridx])
pipelineModel = pipeline.fit(iris)
dataDF = pipelineModel.transform(iris)\
                .drop("SepalLength","SepalWidth","PetalLength","PetalWidth","Name")
#dataDF.show()

(train,test) = dataDF.randomSplit([0.7,0.3], seed=0)
lr = LogisticRegression( labelCol = "label", featuresCol="features", maxIter=10)
model = lr.fit(train)
predict = model.transform(test)
predict.show()

# 검증
evaluator = MulticlassClassificationEvaluator()
evaluator.setPredictionCol("prediction")
evaluator.setLabelCol("label")
print(evaluator.evaluate(predict, \
                          {evaluator.metricName:"truePositiveRateByLabel", \
                           evaluator.metricLabel : 1.0}))           #0.867

# 최적화
paramGrid = ( ParamGridBuilder().addGrid( lr.regParam, [0.01,0.1] )\
                        .addGrid( lr.elasticNetParam, [0.0, 0.5, 1.0])\
                        .addGrid( lr.maxIter, [5,10,20]).build())
cv = CrossValidator( estimator=lr , estimatorParamMaps=paramGrid, \
                            evaluator=evaluator, numFolds=5)
cvModel = cv.fit(train)
print(cvModel.bestModel.getMaxIter( ))                      #20
print(cvModel.bestModel.getRegParam())                  #0.01    
print(cvModel.bestModel.getElasticNetParam())       # 1.0



