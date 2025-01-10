# A Data Analysis Investigating TikTok Content and Spotify Listening Habits
## Project Idea

In this project, I'm using my TikTok liked video data and Spotify listened genre data simultaneously. By extracting the URL of the TikTok videos that I liked, I aim to reach the hashtags of the videos, then classify them under two contrasting categories using the words from the hashtags: negative content and positive content. At the same time, I will get the genre of the music I’ve mostly listened to from Spotify on the specific month that I've liked those TikToks.



## Motivation

The main purpose of this project is to explore the relationship between the content I'm exposed to on TikTok and the music type I choose to listen to on Spotify, and to understand the emotional effect these contents might have on my mood. This data analysis could highlight the huge impact of social media and the content we consume on our daily mood and emotions.

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


