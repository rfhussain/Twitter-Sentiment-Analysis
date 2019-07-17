# TwitterSentimentAnalysis
Analysis of Twitter Sentiments for Random 3 minutes Tweets


The twitter sentiments analysis was part of an assignment given to be solved during a course. 
The task was to download the tweets for 3 minutes only , using the twitter stream API, and and save all the tweets to an output file. 


#### Output.text

The output.txt file is the output of twitterstream.py which is in JSON format. where the output from the three minutes stream was saved through the python pipe code.
The file is roughly around 50 megabytes.


#### happiest_state.py

The file calculates upon the happiest state of US using the tweet sentiments only from the US states. States/Cities & countries other than the US are ignored. 
there are two arguments which must be given while running the file as follows:
```
python happiest_state.py AFINN-111.txt output.txt 
```
and the result should be calculated as :

```
TX 12 (where TX is the state code while the 12 is the score calculated through the twitter sentiment analysis)
```

#### AFINN-111.txt

This is a file which lists combinations of possible words and their score. 
So once the JSON file is read for tweets, each word in the tweet will be calculated against this file and the corresponding result will be communicated back.

