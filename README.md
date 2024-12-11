# Electronic_vechile_manufacture_analysis(2015-2024)
# Project overview
# Purpose :
The project aims to analyze the growth and trends in the electronic vehicle (EV) manufacturing industry between 2015 and 2024. It provides insights into production volumes, market penetration, and the adoption of EV technology by manufacturers globally.
# Scope :
This analysis focuses on understanding how leading EV manufacturers have evolved over the years, examining factors such as production outputs, sales performance, key markets, and the impact of technological advancements. The project also identifies trends influencing the industry, such as government policies, battery technology innovations, and infrastructure developments.
# Key Objectives
1 Market Trends Analysis : Examine production and sales data to identify growth patterns.

2 Manufacturer Insights : Study the performance of key players like Ola Electric Technologies pvt ltd,Bajaj Auto ltd,Mahindra Last Mile Mobility ltd,TVS Motor Company ltd.

3 Regional Distribution : Explore the geographical spread of EV production and adoption, highlighting emerging markets.

4 Technological Advancements : Assess the influence of battery innovations, charging infrastructure, and software upgrades.

5 Environmental Impact : Understand how the rise in EV production contributes to carbon reduction goals globally.

# Target Audience
* Manufacturers: To benchmark performance and identify areas for improvement.
  
* Policymakers: To support evidence-based policy formulation for sustainable growth.

* Investors: To uncover potential investment opportunities in the EV market.

* Consumers: To gain insights into how the EV industry is shaping their transportation options.

# Expected Outcomes
* Comprehensive dashboards showcasing EV production and sales trends.

* Data-driven insights to predict future industry growth.

* Recommendations for manufacturers to optimize production strategies.
  
* Detailed analysis of how policies and technology have shaped the industry trajectory.

  This project combines historical and modern data, leveraging advanced data engineering tools to process, transform, and visualize meaningful insights for stakeholders.

# Architecture
  Include a diagram and a description of the system's architecture:

* Key Components: Mention the services like Azure Data Factory (ADF), Databricks, Synapse Analytics, ADLS Gen2, Key Vault, etc.

* Data Flow: Explain how data flows from source to destination.
  
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/bd9518530c9181fef3ed8602286e21e1d6944ea5/EV_Project/Screenshot%202024-11-23%20142948.png
)
# implementation
# Data ingestion
1. Matillion Architecture
   
   Designed and built the Bronze, Silver, and Gold layers:
   Bronze: Stores raw data directly from APIs.
   Silver: Contains cleaned and enriched data.
   Gold: Stores analytics-ready data.
2. ETL Pipeline
   
   Designed ETL pipelines to extract data from APIs and load it into ADLS Gen-2 bronze layer for transformation and storage.

![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/187751a9a7b448c22a54061feab81485a144560b/Screenshot%202024-11-23%20191310.png)

# Data transformation
  Data is loading into databricks through a secure connection using Azure key vault and secret scope in databricks.
  Creating of mount point  for getting data from Adls gen-2 to Azure databricks.
  Cluster nodes, and compute automatically managed by the Databricks service.
  The Initial Data is cleaned and processed in two steps. Bronze to Silver and Silver to Gold.
  Bronze to Silver notebook we used to clean data and performing transformations like removing null values and other and getting data for visualization.
  Silver to Gold notebook based upon requirement data required for visualization data is moved to gold container.
  * storing of keys and secrets in key vault for secure connection.
    
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/160e5601d0e378f1ccaa825cbe92e56c5aec1dac/Screenshot%202024-11-25%20193214.png)

  * Creation of mount point  for getting data from Adls gen-2 to Azure databricks.
    
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/160e5601d0e378f1ccaa825cbe92e56c5aec1dac/Screenshot%202024-12-09%20184434.png)

  * Performing transformation in Databricks in bronze to silver notebook.
    
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/160e5601d0e378f1ccaa825cbe92e56c5aec1dac/Screenshot%202024-12-09%20184205.png)

  * Moving of data based on requirement from silver to gold.
    
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/160e5601d0e378f1ccaa825cbe92e56c5aec1dac/Screenshot%202024-12-09%20184510.png)

  * End to End of Extract Transform Load (ETL) Pipeline.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/adb461b83412788d43b9b8a0648ab55528aec1da/EV_Project/Screenshot%202024-11-28%20201530.png)
 # Data Warehouse
 * Azure Synapse Analytics: This was chosen as it integrates data warehousing, big data, and data integration capabilities into a single platform.
   It is built on a massively parallel processing architecture and an extremely robust analytics tool which shares many functionalities with Azure Data factory.
   It makes setting up a database and enables querying it in a very short span of time.
   Costs can be optimized as it supports on-demand provisioning and automatic pause and resume capabilities.
   It can be easily integrated with the Azure data lake and other Azure services.

![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/33e5697610ea66676ec4548f90349174df01969c/Screenshot%202024-12-09%20192157.png)

 # Data Visualization
 * PowerBI : Now that the data can be analyzed using Azure Synapse. We can use that to create dashboards.
   In this project I have used PowerBI to accomplish that. PowerBI needs to be connected to the the synapse database.
   We can connect using the Azure Synapse option under Azure from the Data Source option in PowerBI and then entering the severless endpoint of the Synapse in the source and the database name.
   We can connect using the Sign in option instead of using credentials.
   This requires the same email address be used for the Azure account and PowerBI sign in.
   Else, a guest can be invited using Azure active directory and required permission be added to that user.
   That is the mode that I had to use in this case.
   The data can be loaded directly onto the device or using direct query.
   Once the data is loaded it needs to be modelled using the models tab.
   The relationships generated by PowerBI are usually not correct and it needs to be done manually.
   This can be achieved using the manage relationship option from the visualizations in ribbon.
   Once the relationships are set the cross-filter direction needs to be set to both to allow all the fields to be updated across all visualizations in PowerBI.

  * connecting to azure synapse analytics through Endpoint.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/4f8ffd005d2c047d3ce3e622d51bbc0afeda25a4/Screenshot%202024-12-09%20194447.png)

  * Loading Data to PowerBI.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/ade9f610eb95152570c21d7447171c49669eb968/Screenshot%202024-12-09%20195102.png)

  * Now of Electronic vechile charging stations state wise.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/588a6c444e3e363136e14586d87a900fb2dc67e5/PowerBI/Screenshot%202024-12-09%20132447.png)

  * statewise Electoric vechiles manufacturing Details.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/588a6c444e3e363136e14586d87a900fb2dc67e5/PowerBI/Screenshot%202024-12-09%20165459.png)

 * Ratio of yearwise Electronic vechiles manufacturing Details.
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/c0c64847c1e14f9b9cd9a43e60c2dacf238e7e8b/PowerBI/Screenshot%202024-12-09%20171414.png)

 * Total Electronic vechiles manufactured by makers from (2015-2024).
![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/c0c64847c1e14f9b9cd9a43e60c2dacf238e7e8b/PowerBI/Screenshot%202024-12-09%20172457.png)

![Screenshot (1)](https://github.com/GsrSanthosh/Electronic_vechile_manufacture_analysis-2015-2024-/blob/c0c64847c1e14f9b9cd9a43e60c2dacf238e7e8b/PowerBI/Screenshot%202024-12-09%20174607.png)



