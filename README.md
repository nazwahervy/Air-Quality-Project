# Air Quality Analysis and Visualization Dashboard

## Project Overview
This project involves analyzing air quality data from 12 different stations to understand trends and patterns. The analysis includes data wrangling, exploratory data analysis, and visualizations, all conducted using Python in Jupyter Notebook. A Streamlit dashboard was built to display key insights.

## Dataset
The dataset used in this project consists of air quality measurements from multiple locations. Key columns include:
- **PM2.5**: Concentration of particulate matter smaller than 2.5 micrometers.
- **PM10**: Concentration of particulate matter smaller than 10 micrometers.
- **TEMP**: Temperature in degrees Celsius.
- **WSPM**: Wind speed in meters per second.
- **PRES**: Atmospheric pressure.
- **NO2, SO2, CO, O3**: Various gas concentrations.

## Analysis Steps
1. **Data Wrangling**: Gathering, Assessing, Cleaning and preprocessing of the datasets, including handling missing values, merging datasets, and creating a `datetime` index.
2. **Exploratory Data Analysis**: Summary statistics, trend analysis, and visualizations to uncover insights about the air quality levels over time.
3. **Data Visualization**: 
   - **Daily Wind Speed Trends**: Visualization of wind speed variations across different stations.
   - **Correlation between Wind Speed and Temperature**: Scatterplot to show the relationship between wind speed and temperature.
   - **Seasonal Analysis of Air Quality**: Understanding how air quality varies seasonally.

## Dashboard
The dashboard, built using Streamlit, displays interactive visualizations of the air quality data, including:
- **Line plots**: Show daily wind speed variations across monitoring stations.
- **Scatter plots**: Correlate wind speed with temperature and other weather variables.
- **Interactive Widgets**: Filter data by date, location, and variable of interest.

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/nazwahervy/Air-Quality-Project.git
    ```
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run dashboard.py
    ```

## Technologies Used
- **Python**: Data analysis and manipulation.
- **Pandas**: For data wrangling and cleaning.
- **Matplotlib & Seaborn**: For data visualization.
- **Streamlit**: For building the interactive dashboard.

## Results
The analysis revealed significant variation in air quality across stations and seasons, as well as a correlation between wind speed and temperature. The dashboard allows users to explore these trends interactively.
