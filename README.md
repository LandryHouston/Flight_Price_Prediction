# group-1-project "SkyInsight: Predictive Analytics for Cost-Effective Air Travel"


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
   - 1.5 Summary

2. [Data Modeling](02_Data_Modeling.ipynb)
   - 2.1 Linear Regression Algorithm
   - 2.2 Time Series Modeling (RNN)
   - 2.3 Model Training
   - 2.4 Model Evaluation
   - 2.5 Summary

3. [Data Evaluation/Executive Summary/Recommendation](03_Data_Evaluation_Executive_Summary.ipynb)
   - 3.1 Model Performance Metrics
   - 3.2 Key Findings
   - 3.3 Recommendations, Insights and Conclusions
   - 3.4 Summary and Future Enhancements

4. [Data](data/)
   - 4.1 Dataset Dictionary
   - 4.2 Data Files

5. [Images](images/)
   - 5.1 Visualizations
   - 5.2 Charts

6. [Presentation](presentation/)
   - 6.1 PowerPoint Presentation (PDF)

7. [Model](model/)
   - 7.1 .gitignore
   - 7.2 Trained Model (.pkl)
   


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

## Questions

To address our problem statement, we will explore the following questions:

1. How can we preprocess and clean the data to ensure accurate predictions?
2. What features are crucial for predicting optimal timeframes for lower-priced flights?
3. How generalizable are the insights derived from this specific dataset to other airports or travel scenarios
4. Are there specific seasons or timeframes where the model's predictions excel or struggle?
5. What is the impact of external factors (e.g., holidays, events) on the accuracy of the model predictions?

---

## Part 1: Data Wrangling/Gathering/Acquisition

In this section, we will detail the process of acquiring and preparing the data for our predictive model. This includes data gathering, cleaning, and any necessary transformations.

---

## Part 2: Data Modeling

Here, we will delve into the application of the linear regression algorithm to our travel data. Additionally, we will discuss the potential use of a time series model like RNN for future enhancements.

---

## Part 3: Data Evaluation/Executive Summary

This section will provide an executive summary of our findings, including the evaluation of model performance and key insights derived from the data.

---

## Part 4: Recommendation/Further Research

We'll conclude by offering recommendations based on our analysis and suggest avenues for further research to continually improve the predictive model.

![AltText](https://media.licdn.com/dms/image/D5612AQFwNc05_ndXIQ/article-cover_image-shrink_720_1280/0/1698694514274?e=1710979200&v=beta&t=ibpfjqzM24Lot2cKZ34GcW-3A4rDEQB5G5FKEhNEnhY)
