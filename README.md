<h1 align='center'> Fare Play: An Unraveling of the Mystery of Flight Prices</h1>

<h3 align='center'> Group project created by Mark Dunlea Tate, Landry Houston, and Anthony Amadasun for General Assembly DSI-1113</h3>

<div align='center'>

![AltText](https://www.latentview.com/wp-content/uploads/2023/08/ai-and-analytics-in-the-airline-industry-driving-efficiency-and-enhancing-cx-featured.jpg)

</div>

---

<h2 align='center'> Overview </h2>

Welcome to the our project repository! In this project, we aim to address the challenges faced by travel agencies in the post-COVID-19 era. Our focus is on developing an advanced predictive model that offers personalized recommendations for cost-effective flight options, ultimately enhancing customer satisfaction and empowering travel agencies with valuable insights.

---

<h2 align='center'>Table of Content</h2>

1. [Data Cleaning](code/01_data_cleaning.ipynb)

    - 1.1 Introduction
    - 1.2 Data Collection
    - 1.3 Data Cleaning

2. [Data Analysis](code/02_data_analysis.ipynb)

    - 2.1 Introduction
    - 2.2 Data Tranformation/Engineering
    - 2.3 Analysis/Visuals
    - 2.4 Conclusion

3. [Data Modeling](code/03_data_modeling.ipynb)

    - 3.1 Introduction
    - 3.2 Regression Modeling
    - 3.3 Data Visualization
    - 3.4 Conclusion

4. [Data](data/)

    - 4.1 Data Dictionary
    - 4.2 Data Files

5. [Images](images/)

    - 5.1 Visualizations

6. [Presentation](FarePlay.pdf)

    - 6.1 PowerPoint Presentation (PDF)

<br>

---

<h2 align='center'>Data Description</h2>

<div align='center'>

| column         | type   | description                       |
| -------------- | ------ | --------------------------------- |
| airline        | object | airline company                   |
| flight         | object | flight number                     |
| origin         | object | departure city                    |
| departure_time | object | departure time of day             |
| stops          | int    | number of stops                   |
| arrival_time   | object | arrival time of day               |
| destination    | object | arrival city                      |
| class          | int    | economy (0) or business (1) class |
| duration       | float  | flight duration in minutes        |
| price          | int    | ticket price in USD               |

</div>

---

<h2 align='center'>Problem Statement</h2>

With the resurgence of travel following the COVID-19 pandemic, our objective is to develop an advanced predictive model tailored for travel agencies. The model aims to assist travel agencies in providing their customers with personalized recommendations for securing the most cost-effective flight options from a specific airport. By leveraging historical data, the model will predict optimal timeframes for lower-priced flights, enabling travel agencies to offer strategic advice to their customers. This initiative seeks to enhance customer satisfaction, streamline the booking process, and empower travel agencies with actionable insights to navigate the dynamic landscape of airfare pricing and seasonal trends. The model will attempt to optimize for RMSE in order to make our performance as accessible as possible.

The goal is to have the Root Mean Squared Error (RMSE) of our flight price and travel assistant model be less than $50 of the actual prices.

---

<h2 align='center'>Questions</h2>

To address our problem statement, we will explore the following questions:

1. How can we preprocess and clean the data to ensure accurate predictions?
2. What features are crucial for predicting optimal timeframes for lower-priced flights?
3. How generalizable are the insights derived from this specific dataset to other airports or travel scenarios

---

<h2 align='center'>Part 1: Data Cleaning</h2>

In this section, we will detail the process of acquiring and preparing the data for our predictive model. This includes data gathering, cleaning, and any necessary transformations. Some of the task explored in this section is that we will converted Rupees to USD, duration into minutes, number of stops column changed to numeric, binarize the 'class' column for better modeling and column labels cleaned up.

---

<h2 align='center'>Part 2: Data Analysis</h2>

Here, we will delve into the application of the linear regression algorithm to our travel data. This section will provide an executive summary of our findings, including the evaluation of multiple model performance and key insights derived from the data.

---

<h2 align='center'>Part 3: Data Modeling</h2>

This section will provide an executive summary of our findings, including the evaluation of model performance and key insights derived from the data. Additionally, we will make future recommendation where we will discuss the potential use of a time series model like RNN for future enhancements. Expand upon the online form that when you put in your budget and starting location, the model can predict and advise what directions and locations that would fit your desires. And lastly, take into account the change of
flight prices over time in order to give a more robust assistance.

<br>

<div align='center'>

![AltText](https://media.licdn.com/dms/image/D5612AQFwNc05_ndXIQ/article-cover_image-shrink_720_1280/0/1698694514274?e=1710979200&v=beta&t=ibpfjqzM24Lot2cKZ34GcW-3A4rDEQB5G5FKEhNEnhY)

</div>
