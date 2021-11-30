from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.ml.feature import  StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
# 하둡에서 돌리기 위한 환경설정 
conf = SparkConf().setAppName("bank")#.setMaster("spark://master:7077")    # 리눅스에서 주석 풀기
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
bank = sqlContext.read.format("com.databricks.spark.csv")\
            .options(header="true",inferSchema="true")\
            .load("bank.csv").repartition(2).cache()
# print(bank.printSchema)
# print(bank.show())

df = bank.select("age","job", "marital","education","balance"\
                            ,"housing","loan","duration","campaign","pdays"\
                            ,"previous","poutcome","y")
cols = df.columns
categories = ["job","marital","education","housing","loan","poutcome"]
stages = []
for category in categories: 
    stringIndexer = StringIndexer(inputCol=category, outputCol=category+"_index")
    encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], \
                            outputCols=[category+"_vec"])
    stages += [stringIndexer, encoder]
label = StringIndexer(inputCol="y",outputCol="label")
stages += [label]
    
numerics = ["age","balance","duration","pdays","previous"]
inputs = [ category+"_vec" for category in categories] + numerics
va = VectorAssembler(inputCols = inputs, outputCol="features")
stages += [va]
pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(df)
pipelineModel.transform(df)
bankDF = pipelineModel.transform(df)
selectedCols = ["label","features"] + cols
bankDF = bankDF.select(selectedCols)
# print(bankDF.printSchema())
# print(bankDF.show())

train, test = bankDF.randomSplit([0.7, 0.3], seed=1)
forest = RandomForestClassifier( featuresCol="features",labelCol="label")
model = forest.fit(train)
predicts = model.transform(test)
print( predicts.select("age","job","label","prediction").show() )

evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate(predicts, {evaluator.metricName : "areaUnderROC"})
print("Area under ROC: "+ str(score))

from pyspark.ml.classification import GBTClassifier
gbt = GBTClassifier(maxIter=10)
model = gbt.fit(train)
model.transform(test)
predicts = model.transform(test)
evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate(predicts, {evaluator.metricName : "areaUnderROC"})
print("Area under ROC: "+ str(score))
#print(gbt.explainParams() )

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
paramGrid = (ParamGridBuilder().addGrid(gbt.maxDepth,[2,4,6] ) \
                        .addGrid(gbt.maxBins,[20,60])\
                        .addGrid(gbt.maxIter, [10,20]).build() )
cv  = CrossValidator(estimator = gbt, estimatorParamMaps=paramGrid, \
                            evaluator=evaluator, numFolds=5 )
cvModel = cv.fit(train)
predicts = cvModel.transform(test)
evaluator.evaluate(predicts)
score = evaluator.evaluate(predicts)
print(score)

