# Databricks notebook source
place_df = spark.read.option("header",True).option("inferschema",True).csv("/mnt/bronze/Evmanufactureplace")
display(place_df)

# COMMAND ----------

place_df.write.mode('append').format('parquet').save("/mnt/silver/Evmanufactureplace")

# COMMAND ----------

manufacture_year_df = spark.read.option("header",True).option("inferschema",True).csv("/mnt/bronze/makersyearswise")
display(manufacture_year_df)

# COMMAND ----------

from pyspark.sql.functions import col
from functools import reduce

manufacture_total_df = manufacture_year_df.withColumn(
    "total_manufactured_vehicles",
    reduce(lambda x, y: x + y, [col(str(year)) for year in range(2015, 2025)])
)
display(manufacture_total_df)


# COMMAND ----------

manufacture_total_filter_df = manufacture_total_df.filter(
    col("total_manufactured_vehicles") > 10000
)
display(manufacture_total_filter_df)

# COMMAND ----------

manufacture_total_filter_df.write.mode('append').format('parquet').save("/mnt/silver/makersyearswise")

# COMMAND ----------

manufacturevechilecategory_df = spark.read.option("header",True).option("inferschema",True).csv("/mnt/bronze/manufacturevechilecategory")
display(manufacturevechilecategory_df)

# COMMAND ----------

from pyspark.sql.functions import col, to_date, lit
from pyspark.sql.functions import expr
df = manufacturevechilecategory_df.withColumn("Date", to_date(col("Date"), "MM/dd/yy"))

melted_df = df.selectExpr(
    "Date",
    "stack(16, " + 
    ", ".join([f"'{col}', `{col}`" for col in df.columns if col != "Date"]) + 
    ") as (Vehicle_Type, Count)"
)
display(melted_df)

# COMMAND ----------

null_df=melted_df.dropna(subset=["Date"])
display(null_df)

# COMMAND ----------

from pyspark.sql.functions import year, col, sum, to_date
df = null_df.withColumn("Date", to_date(col("Date"), "yyyy-dd-MM"))
df = df.withColumn("Year", year(col("Date")))

aggregated_df = df.groupBy("Year", "Vehicle_Type").agg(sum("Count").alias("Total_Count"))
ordered_df = aggregated_df.orderBy(col("Year").asc(), col("Vehicle_Type").asc())

display(ordered_df)


# COMMAND ----------

ordered_df.write.mode('append').format('parquet').save("/mnt/silver/manufacturevechilecategory")

# COMMAND ----------

OperationalPC_df = spark.read.option("header",True).option("inferschema",True).csv("/mnt/bronze/OperationalPC")
display(OperationalPC_df)

# COMMAND ----------

OperationalPC_df.write.mode('append').format('parquet').save("/mnt/silver/chargingstations")

# COMMAND ----------

vechileclass_df = spark.read.option("header",True).option("inferschema",True).csv("/mnt/bronze/vechileclass")
display(vechileclass_df)

# COMMAND ----------

vechileclass_df.write.mode('append').format('parquet').save("/mnt/silver/vechileclassregistrations")
