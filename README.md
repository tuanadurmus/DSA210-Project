# A Data Analysis Investigating TikTok Content and Spotify Listening Habits

## Contents

-[Project Idea](## Project Idea)

## Project Idea

In this project, I'm using my TikTok liked video data and Spotify listened genre data simultaneously. By extracting the URL of the TikTok videos that I liked, I aim to reach the hashtags of the videos, then classify them under two contrasting categories using the words from the hashtags: negative content and positive content. At the same time, I will get the genre of the music I’ve mostly listened to from Spotify on the specific month that I've liked those TikToks.

## Motivation

The main purpose of this project is to explore the relationship between the content I'm exposed to on TikTok and the music type I choose to listen to on Spotify, and to understand the emotional effect these contents might have on my mood. This data analysis could highlight the huge impact of social media and the content we consume on our daily mood and emotions.

## Tools

**pandas** – Used for data manipulation and analysis, enabling efficient handling of structured datasets such as CSV files.

**selenium** – A web automation tool used to scrape TikTok hashtags by interacting with web elements programmatically.

**chromedriver** – A driver required by Selenium to automate Google Chrome for web scraping and data extraction.

**Spotify Web API** – An API service used to fetch music-related metadata, including song genres and artist information.

**numpy** – A numerical computing library used for handling arrays, performing mathematical operations, and optimizing computations.

**sklearn (scikit-learn)** – A machine learning library providing tools for classification, clustering, and feature extraction, essential for sentiment analysis.

**scipy.stats** – A module from SciPy used for performing statistical tests, including hypothesis testing and correlation analysis.

**matplotlib** – A data visualization library used to generate graphs, plots, and charts to analyze trends in TikTok and Spotify content consumption.



## Hypothesis

I expect to choose more upbeat and hype genres (e.g., pop, electronic, or hip-hop) when I am exposed to positive TikTok content and more slow and emotional genres (e.g., indie, classical, or lo-fi) when exposed to negative TikTok content.

## Tools

## Data Sources

The datasets used in this project include two main sources:

### TikTok Liked Video Data:
This data is directly exported from TikTok's personal data request. The data file contains the URL's of the TikTok videos that I liked, accompanied by the information of the date and exact time that I liked the video. 


### Spotify Listening Data:
This data is also extracted from the Spotify's personal data request. The dataset holds the information of the track name that I listened to at a specific date and time accompanied by artist name and album name. 


## Data Extraction
### TikTok Data:

The data which Tiktok provides do not contain the hashtag information of the videos. To reach each liked video's hashtag, I made use of a powerful web scraping tool dealing with dynamic TikTok content which is **Selenium** (which also makes use of ChromeDriver to dynamically extract the hashtags). [The codes](Tiktok_Hashtag_Extract.py) to extract the hashtags from the URLs are provided as a file above.


### Spotify Data:

With the help of **Spotify Web API**, I was able to reach the genre of the music I've listened to. The first step was to create a Spotify Developer Account and get a Client ID. Next step was to run the [following codes](Spotify_genre_extract.py) to reach the genre of the artists to categorize the songs.

## Data Processing

### TikTok Data Processing:

The TikTok hashtag csv file includes some lines with no hashtags and also a column with the URLs. For a clean dataset, I should get rid of them with [data processing methods](Tiktok_data_process.ipynb).

### Spotify Data Processing:

The Spotify csv file has so many additional information that we are not going to use throughout our project. That's why we choose the way to [process the data](Spotify_data_process.ipynb) before doing analysis.

## Machine Learning Approaches for Data Classification

Machine learning approaches were used to classify TikTok hashtags and Spotify music genres into two opposing categories (e.g., positive and negative). This classification was achieved using supervised learning techniques to uncover patterns in textual data and automate the sentiment categorization process.

### TikTok Data Classification

While classification of the hashtag content, supervised machine learning algorithm Support Vector Machines are used. The reason to choose that approach is because it is widely used for text classification, it makes use of decision boundary concepts. This method firstly converts input data (hashtag content in our case) into numerical form, chooses a kernel based on the distribution of the data, does the training to optimize the boundary and uses it to classify the new data. Code implementation is shown [here.](tiktok_data_classification.ipynb)

### Spotify Data Classification

After the data processing step we have the table of timestamps and music genres listened. Just like we did when we classified TikTok data we use supervised machine learning approaches here either. But here, we use random forest approaches different than the TikTok data because Spotfiy data is more high dimensional than TikTok liked video data. Random forest approach creates multiple decision trees and for each output of a decision tree, the model takes the majority vote for predictions. Code implementation on the spotify data csv file is shown [here.](spotify_data_classification.ipynb)

## Data Visualization

### TikTok Hashtag Data Visualization

To reach a better understanding of the data, it is useful to visualize them using matplotlib. [Here](tiktok_visualization.ipynb)'s the several graphs of our extracted, processed and classified data's representing the distribution of the percentage of the negative and positive content I was exposed to in each month in 2024.

### Spotify Music Genre Distribution Visualization

We go through each step as we did for TikTok data, [Here's](spotify_data_visualization.ipynb) the plotted graphs to gain a more precise insight about the distribution of the data. 

## Data Analysis and Findings

At the beginning of the project, "The content I'm exposed to on TikTok has a relation with the music I listen to on Spotify" was my first hypothesis. We now, either reject or fail to reject the null hypothesis of "There are no such relation between the TikTok content and Spotify listening habits". Let's first look at [some graphs](sentiment_comparison.ipynb) in which we compare the findings from both datasets. 

At first glance, we can deduce some interpretations from the graphs such as:
#### TikTok and Spotify Have Different Sentiment Trends

TikTok's positive content percentage fluctuates significantly over the months, reaching a peak around mid-year before dropping again.
Spotify’s positive content is relatively stable compared to TikTok, with a higher baseline percentage of positive content overall.
#### Negative Content on TikTok is Lower Than Spotify's Negative Content

The orange dashed line (TikTok Negative) remains low throughout the year, indicating that TikTok content tends to be more positive.
The red dashed line (Spotify Negative) shows fluctuations, peaking in some months and declining in others.
#### There is a Clear Opposite Trend Between TikTok & Spotify

When TikTok positive content increases, Spotify’s positive content tends to decrease (e.g., around June-July).
When TikTok’s negative content rises (October), Spotify’s negative content remains relatively stable.
#### Possible Explanations for This Trend

TikTok is a social media platform where viral trends and algorithmic changes may cause fluctuations in sentiment consumption.
Spotify users may have more stable preferences in music, making sentiment changes more gradual and predictable.
Exam periods, seasonal effects, or global events could be influencing the type of content people consume.

### Hypothesis Testing 

#### State the Null Hypothesis (H₀):
→ There is no significant relationship between TikTok and Spotify sentiment distributions.
#### State the Alternative Hypothesis (H₁):
→ There is a significant relationship between TikTok and Spotify sentiment distributions.
#### Perform Pearson Correlation Test:
This test measures the linear correlation between two datasets.
It outputs a correlation coefficient (r) and a p-value.
If the p-value is less than 0.05, we reject the null hypothesis (H₀), meaning there's a significant correlation.

[Here's](hypothesis_testing.ipynb) the code of the hypothesis testing done on the datasets and if we set the significance level to 0.05, it is clear to see that we fail to reject the null hypothesis of the project.


## Limitations and Future Work

The major difficulty I encountered in this project was to extract data from TikTok, it took a very long time to dynamically extract hashtag contents. Also, not being able to classify the hashtags and genres perfectly was such a limitation of the precision of this type of projects. Also platform differences between TikTok and Spotify created a problem and influence from external factors such as the trends and the viral videos from Tiktok may have affected my liked video dataset (it is not an unbiased dataset).

With expanding the datasets and enhancing the sentiment classification analysis, this project can show the way for more compact social media consumption analysis. It is possible to gain more deeper insights into how digital platforms shape our emotional engagement with content.

