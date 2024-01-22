# group-1-project | Fare Play: An Unraveling of the Mystery of Flight Prices



![AltText](https://www.latentview.com/wp-content/uploads/2023/08/ai-and-analytics-in-the-airline-industry-driving-efficiency-and-enhancing-cx-featured.jpg)

---

## Overview

Welcome to the our project repository! In this project, we aim to address the challenges faced by travel agencies in the post-COVID-19 era. Our focus is on developing an advanced predictive model that offers personalized recommendations for cost-effective flight options, ultimately enhancing customer satisfaction and empowering travel agencies with valuable insights.

---

## Table of Content

1. [Data Wrangling/Gathering/Acquisition](01_Data_Wrangling_Gathering_Acquisition.ipynb)
   - 1.1 Introduction
   - 1.2 Data Collection
   - 1.3 Data Cleaning
   - 1.4 Data Transformation

2. [Data Modeling](02_Data_Modeling.ipynb)
   - 2.1 Feature Engineering
   - 2.2 Linear Regression Algorithm
   - 2.3 Model Training
   - 2.4 Model Evaluation
   - 2.5 Summary and Future Enhancements

3. [Data](data/)
   - 3.1 Dataset Dictionary
   - 3.2 Data Files

4. [Images](images/)
   - 4.1 Visualizations
   - 4.2 Charts

5. [Presentation](presentation/)
   - 5.1 PowerPoint Presentation (PDF)

6. [Model](model/)
   - 6.1 Trained Model (.pkl)
   


---

## Data Description

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

## Problem Statement

With the resurgence of travel following the COVID-19 pandemic, our objective is to develop an advanced predictive model tailored for travel agencies. The model aims to assist travel agencies in providing their customers with personalized recommendations for securing the most cost-effective flight options from a specific airport. By leveraging historical data, the model will predict optimal timeframes for lower-priced flights, enabling travel agencies to offer strategic advice to their customers. This initiative seeks to enhance customer satisfaction, streamline the booking process, and empower travel agencies with actionable insights to navigate the dynamic landscape of airfare pricing and seasonal trends. The model will attempt to optimize for RMSE in order to make our performance as accessible as possible.

---

## Hypothesis

Null Hypothesis:
The mean Root Mean Squared Error (RMSE) of our flight price and travel assistant model is greater than or equal to $50 ofthe actual prices, indicating that our model does not effectively predict prices within the acceptable range.

Alternative Hypothesis:
The mean RMSE of our flight price and travel assistant model is less than 50$ of the actual prices,suggesting that our model successfully predicts prices within the acceptable range.

--- 

## Questions

To address our problem statement, we will explore the following questions:

1. How can we preprocess and clean the data to ensure accurate predictions?
2. What features are crucial for predicting optimal timeframes for lower-priced flights?
3. How generalizable are the insights derived from this specific dataset to other airports or travel scenarios

---

## Part 1: Data Wrangling/Gathering/Acquisition

In this section, we will detail the process of acquiring and preparing the data for our predictive model. This includes data gathering, cleaning, and any necessary transformations. Some of the task explored in this section is that we will converted Rupees to USD, duration into minutes, number of stops column changed to numeric, binarize the 'class' column for better modeling and column labels cleaned up.

---

## Part 2: Data Modeling and Executive Summary

Here, we will delve into the application of the linear regression algorithm to our travel data. This section will provide an executive summary of our findings, including the evaluation of model performance and key insights derived from the data. Additionally, we will make future recommendation where we will discuss the potential use of a time series model like RNN for future enhancements. Expand upon the online form that when you put in your budget and starting location, the model can predict and advise what directions and locations that would fit your desires. And lastly, take into account the change of
flight prices over time in order to give a more robust assistance.

---


![AltText](https://media.licdn.com/dms/image/D5612AQFwNc05_ndXIQ/article-cover_image-shrink_720_1280/0/1698694514274?e=1710979200&v=beta&t=ibpfjqzM24Lot2cKZ34GcW-3A4rDEQB5G5FKEhNEnhY)
