# A Data Analysis Investigating TikTok Content and Spotify Listening Habits
## Project Idea

In this project, I'm using my TikTok liked video data and Spotify listened genre data simultaneously. By extracting the URL of the TikTok videos that I liked, I aim to reach the hashtags of the videos, then classify them under two contrasting categories using the words from the hashtags: negative content and positive content. At the same time, I will get the genre of the music I’ve mostly listened to from Spotify on the specific month that I've liked those TikToks.

The main purpose of this project is to explore the relationship between the content I'm exposed to on TikTok and the music type I choose to listen to on Spotify, and to understand the emotional effect these contents might have on my mood. This data analysis could highlight the huge impact of social media and the content we consume on our daily mood and emotions.

## Data Sources

The datasets used in this project include two main sources:

TikTok Liked Video Data:
The URL of the TikTok videos that I liked.
Each URL is accompanied by specific date and time information.
The hashtags of the liked TikTok videos are extracted and classified into positive or negative content based on the words in the hashtags.

Spotify Listening Data:
The genre of music I listened to most frequently on each specific time.
This dataset includes specific date information associated with the genres.

## Hypothesis

I expect to choose more upbeat and hype genres (e.g., pop, electronic, or hip-hop) when I am exposed to positive TikTok content and more slow and emotional genres (e.g., indie, classical, or lo-fi) when exposed to negative TikTok content.


## Data Extraction
TikTok Data:
Extract the URLs of liked videos from the TikTok API.
Retrieve the associated hashtags of these liked videos.
Classify the hashtags into positive or negative categories based on their sentiment or meaning.

Spotify Data:
Extract the genre of music I listened to the most on each specific month using the Spotify API.

