# Sentiment Analysis of COVID-19 Tweets: When did the Public Panic Set In?

The purpose of this project is to source historical Tweets from the days before and after the WHO's pandemic declaration, process the tweets with Natural Language Processing, and conduct a sentiment analysis in order to understand public perception of COVID-19 before and after it was declared a pandemic.

#### -- Project Status: Active

<b> -- Contact Info:</b><br>
Allison Kelly<br>
Data Scientist & Digital Marketing Consultant<br>
203.848.0545 | <a href="mailto: allisonkelly42@gmail.com">allisonkelly42@gmail.com<a> | <a href="www.github.com/akelly66">Github Profile</a> | <a href="www.linkedin.com/in/akelly66">Linkedin</a><br> 
  
## Mission

Love it or hate it, social media has gone from angsty teenagers posting poetry on LiVEJOURNAL to the leader of the free world <a href="https://twitter.com/realDonaldTrump/status/1213919480574812160?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1213919480574812160&ref_url=https%3A%2F%2Fmashable.com%2Farticle%2Ftrump-tweets-congress-war-powers-act%2F">waging war on Iran</a> in 265 words (or less) in a matter of years. Social media provides analysts with <i><a href="https://seedscientific.com/how-much-data-is-created-every-day/">zettabytes</a></i> of data every day. That's 1,000 bytes to the seventh power. Specifically, Twitter users generate 500 million tweets per day, of which the content of those Tweets contains invaluable public opinion data. 

As the world has been turned on its head during the COVID-19 global pandemic, an interesting question arises. How seriously is the public taking the pandemic? Millions have lost their jobs, deaths from the disease are in the hundreds each day, and the US meat supply chain is on the brink of failure, but life-saving shelter-in-place orders are being defied as protesters rally all over the country in favor of opening the ecomony. 

The question I seek to answer in this project is whether the public opinion of how serious the pandemic was changed in the United States once the World Health Organization declared a global pandemic. This is not meant to be academically rigorous. As I only have access to a Premium API Sandbox dev environment with  a limit of 5,000 tweets scraped per month, getting the full dataset will take me quite a while, but the framework will hopefully be built beforehand in order to streamline the final process. I chose to look at the two-three days before and after the declaration on January 31, 2020, though this will give a limited scope as stay-at-home orders did not begin until mid-March. 

The following notebooks will demonstrate how I scraped tweets from the Twitter API, processes them with Natural Language Processing methods, and categorized them using sentiment analysis.

### Method
* Data Mining
* Natural Language Processing
* Sentiment Analysis

### Technologies
* Python
* Twitter API
* Requests

## Data & Notebook
* <a href="https://github.com/akelly66/COVID-Tweet-Sentiment/tree/master/tweet-scraping">Sourcing Tweets</a>
* <a href="https://github.com/akelly66/COVID-Tweet-Sentiment/tree/master/text-processing">Processing Tweets</a>
