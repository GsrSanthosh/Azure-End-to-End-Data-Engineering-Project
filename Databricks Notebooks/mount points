# Databricks notebook source
dbutils.secrets.list("EV_Scope")

# COMMAND ----------

dbutils.secrets.get(scope="EV_Scope",key="storagekey")

# COMMAND ----------

dbutils.fs.mount(
    source=f"wasbs://bronze@evmanufacturestorage.blob.core.windows.net/",
    mount_point="/mnt/bronze",
    extra_configs={f"fs.azure.account.key.evmanufacturestorage.blob.core.windows.net":dbutils.secrets.get(scope="EV_Scope",key="storagekey") }
)

# COMMAND ----------

dbutils.fs.mount(
    source=f"wasbs://silver@evmanufacturestorage.blob.core.windows.net/",
    mount_point="/mnt/silver",
    extra_configs={f"fs.azure.account.key.evmanufacturestorage.blob.core.windows.net":dbutils.secrets.get(scope="EV_Scope",key="storagekey") }
)

# COMMAND ----------

dbutils.fs.mount(
    source=f"wasbs://gold@evmanufacturestorage.blob.core.windows.net/",
    mount_point="/mnt/gold",
    extra_configs={f"fs.azure.account.key.evmanufacturestorage.blob.core.windows.net":dbutils.secrets.get(scope="EV_Scope",key="storagekey") }
)
