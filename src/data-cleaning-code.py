# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Data Cleaning Service
# MAGIC This Service lets you integrate datasets, select and clean columns and save resultant dataset as csv or parquet
# MAGIC 
# MAGIC ## Parameters 
# MAGIC 
# MAGIC  - ###  job_id
# MAGIC 	 - Description:
# MAGIC 	 - Type:
# MAGIC 	 - Example
# MAGIC  - ### notebook_params
# MAGIC 	 - #### resource_type
# MAGIC        - Description:
# MAGIC        - Type:
# MAGIC        - Example:
# MAGIC 	 - 
# MAGIC  - 

# COMMAND ----------

'''
    Import dependencies
'''
from pyspark.sql.functions import col
from pyspark.sql.utils import AnalysisException
from src.utils.utils import Utils
string_to_list = Utils.string_to_list

# COMMAND ----------

'''
    This code finds one or more datasets with the route, integrate them and selects a list of columns to keep
'''
print(Utils.string_to_list("hola.nomvre,   perros"))

## List of columns to keep
select_columns = string_to_list(dbutils.widgets.get("selectColumns"))

## Resource Info
resource_type = dbutils.widgets.get("resourceType")
resource_id = dbutils.widgets.get("resourceId")

if resource_type == "json" or resource_type == "parquet" :
    try:
        df3 = spark.read.format(resource_type).load(resource_id)
        
    except AnalysisException as e:
        print(e)
else:
    raise (Exception("Invalid resourceType"))

try:
    df3 = df3.select([col(col_name).alias(col_name) for col_name in select_columns])
    df3.show()
    df3.printSchema()
except Exception as e:
    pass  # buscar las excepciones posibles



# COMMAND ----------

## List of columns which you want to apply dropDuplicated
dupl_cols = string_to_list(dbutils.widgets.get("clearDuplicated"))
nan_cols = string_to_list(dbutils.widgets.get("clearNaN"))








