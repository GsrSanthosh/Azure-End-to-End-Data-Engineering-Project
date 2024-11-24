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





