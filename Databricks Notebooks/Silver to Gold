# Databricks notebook source
Evchargingstation_df = spark.read.option("header",True).option("inferschema",True).parquet("/mnt/silver/chargingstations")
display(Evchargingstation_df)

# COMMAND ----------

Evchargingstation_df.write.mode('append').format('parquet').save("/mnt/gold/Evchargingstations")

# COMMAND ----------

Evmanufactureplace_df = spark.read.option("header",True).option("inferschema",True).parquet("/mnt/silver/Evmanufactureplace")
display(Evmanufactureplace_df)

# COMMAND ----------

Evmanufactureplace_df.write.mode('append').format('parquet').save("/mnt/gold/Evmanufactureplace")

# COMMAND ----------

makersyearswise_df = spark.read.option("header",True).option("inferschema",True).parquet("/mnt/silver/makersyearswise")
display(makersyearswise_df)

# COMMAND ----------

makersyearswise_df.write.mode('append').format('parquet').save("/mnt/gold/yearwisemanufacture_ev")

# COMMAND ----------

Ev_vechilecategory_df = spark.read.option("header",True).option("inferschema",True).parquet("/mnt/silver/manufacturevechilecategory")
display(Ev_vechilecategory_df)

# COMMAND ----------

Ev_vechilecategory_df.write.mode('append').format('parquet').save("/mnt/gold/manufacturevechilecategory")

# COMMAND ----------

registrations_df = spark.read.option("header",True).option("inferschema",True).parquet("/mnt/silver/vechileclassregistrations")
display(registrations_df)

# COMMAND ----------

registrations_df.write.mode('append').format('parquet').save("/mnt/gold/vechileclassregistrations")
