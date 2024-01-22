<h1 align='center'> Fare Play: An Unraveling of the Mystery of Flight Prices</h1>

<h3 align='center'> Group project created by Mark Dunlea Tate, Landry Houston, and Anthony Amadasun for General Assembly DSI-1113</h3>

<div align='center'>

![AltText](https://www.latentview.com/wp-content/uploads/2023/08/ai-and-analytics-in-the-airline-industry-driving-efficiency-and-enhancing-cx-featured.jpg)

</div>

---

<h2 align='center'> Overview </h2>

Welcome to our project repository! In this project, we aim to address the challenges faced by travel agencies in the post-COVID-19 era. Our focus is on developing an advanced predictive model that offers personalized recommendations for cost-effective flight options, ultimately enhancing customer satisfaction and empowering travel agencies with valuable insights.

---

<h2 align='center'>Table of Contents</h2>

1. [Data Cleaning](code/01_data_cleaning.ipynb)

    - 1.1 Introduction
    - 1.2 Data Collection
    - 1.3 Data Cleaning

2. [Data Analysis](code/02_data_analysis.ipynb)

    - 2.1 Introduction
    - 2.2 Data Transformation/Engineering
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

With the resurgence of travel following the COVID-19 pandemic, our objective is to develop an advanced predictive model tailored for travel agencies. The model aims to assist travel agencies in providing their customers with personalized recommendations for securing the most cost-effective flight options from a specific airport. By leveraging historical data, the model will predict optimal timeframes for lower-priced flights, enabling travel agencies to offer strategic advice to their customers. This initiative seeks to enhance customer satisfaction, streamline the booking process, and empower travel agencies with actionable insights to navigate the dynamic landscape of airfare pricing and seasonal trends. The model will attempt to optimize for RMSE to make our performance as accessible as possible.

The goal is to have the Root Mean Squared Error (RMSE) of our flight price and travel assistant model be less than $50 off the actual prices.

---

<h2 align='center'>Questions</h2>

To address our problem statement, we will explore the following questions:

1. How can we preprocess and clean the data to ensure accurate predictions?
2. What features are crucial for predicting optimal timeframes for lower-priced flights?
3. How generalizable are the insights derived from this specific dataset to other airports or travel scenarios

---

<h2 align='center'>Part 1: Data Cleaning</h2>

In this section, we will detail the process of acquiring and preparing the data for our predictive model. This includes data gathering, cleaning, and any necessary transformations. Some of the tasks explored in this section are that we will convert Rupees to USD, duration into minutes, number of stops column changed to numeric, binarize the 'class' column for better modeling, and column labels cleaned up.

---

<h2 align='center'>Part 2: Data Analysis</h2>

This analysis explores various factors influencing airline prices, shedding light on key trends and considerations. Notable findings include the presence of outliers above $1200, emphasizing the need to consider airline pricing tendencies in dynamic markets. Vistara and Air India, with significantly higher averages, stand out as major players, driven by their market control, operational scale, and demand for consistent service. Airport location impacts pricing, with Delhi and Hyderabad offering slightly lower fares, attributed to efficient cost distribution and central positioning, respectively. Mumbai and Delhi emerge as popular destinations, while Hyderabad stands out as a cost-effective departure point due to its central location. Time analysis reveals night and mid-afternoon departures as more affordable, aligning with lower demand during these periods. First-class travel unsurprisingly commands higher prices. Trips with one stop, being the most frequent, correlate with higher costs, indicating high demand for this travel style. Correlation analysis identifies attributes like class, airline choice, and duration as most influential. The Folium Map visually displays the locations of analyzed airports, providing geographical context to the findings. This comprehensive exploration aims to enhance understanding and decision-making in the dynamic realm of airline pricing.

---

<h2 align='center'>Part 3: Data Modeling</h2>

This section will provide an executive summary of our findings, including the evaluation of model performance and key insights derived from the data. Four machine learning models were evaluated for predicting flight prices based on selected features, preprocessing, and cleaning methods. The models include Linear Regression, Random Forest, Decision Tree, and Gradient Boost. The Random Forest model, with its robust performance metrics, is recommended for predicting flight prices based on the provided dataset and features. Further optimization, a larger dataset,  and fine-tuning may enhance the model's predictive capabilities.

<div align='center'>
| Model                | Training Score | Testing Score | RMSE Score |
|----------------------|-----------------|---------------|------------|
| Linear Regression    | 0.9428          | 0.9420        | 65.64      |
| Random Forest        | 0.9793          | 0.9754        | 42.75      |
| Decision Tree        | 0.9291          | 0.9283        | 72.94      |
| Gradient Boost (XGB) | 0.9593          | 0.9586        | 55.81      |
</div>

In this notebook, we also employ a Random Forest Classifier to predict the cardinal direction of flights. The goal is to develop a robust model capable of accurately determining flight directions. Through feature importance analysis, we identify arrival time, departure time, and ticket price as crucial predictors. Fine-tuning the model using Grid Search reveals optimal hyperparameters below. The model's effectiveness is evaluated with an accuracy score, reaching a noteworthy 0.8994 on the test set. This notebook provides a comprehensive exploration of the classification modeling process, emphasizing feature selection, model tuning, and insights into the predictive capabilities of the Random Forest Classifier for flight direction prediction.

<div align='center'>
| Parameter                 | Value |
|---------------------------|-------|
| `rfc__max_depth`          | 30    |
| `rfc__min_samples_leaf`   | 1     |
| `rfc__min_samples_split`  | 2     |
| `rfc__n_estimators`       | 160   |
| accuracy                  |  0.8994 |
</div>

<h2 align='center'> Conclusion </h2>

In summary, our analysis centered on developing an advanced predictive model for travel agencies, addressing the resurgence of flight travel post-COVID-19. The Random Forest model emerged as the most effective, achieving a remarkable RMSE score of 42.75. This outcome provides robust evidence of the model's ability to predict flight prices with high accuracy. Aligned with our problem statement's focus on optimizing for RMSE, the model is poised to deliver personalized recommendations, strategic advice on optimal timeframes, and actionable insights for travel agencies. The exceptional performance not only meets but surpasses our expectations. This initiative is positioned to enhance customer satisfaction, streamline the booking process, and empower travel agencies in navigating the dynamic airfare pricing landscape.


<br>

<div align='center'>

![AltText](https://media.licdn.com/dms/image/D5612AQFwNc05_ndXIQ/article-cover_image-shrink_720_1280/0/1698694514274?e=1710979200&v=beta&t=ibpfjqzM24Lot2cKZ34GcW-3A4rDEQB5G5FKEhNEnhY)

</div>
