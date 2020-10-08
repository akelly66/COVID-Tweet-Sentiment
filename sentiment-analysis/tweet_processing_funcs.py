def remove_url_and_RT(row):
    '''
    This function takes each tweet
    and removes the urls and retweet
    indicator from them.
    '''

    row = re.sub('https://[A-Za-z0-9./]+',"",row)
    row = re.sub('http://[A-Za-z0-9./]+',"",row)
    row = re.sub('^RT',"", row)
    return row

def clean_tweet(tweet):

    '''
    This function takes a tweet variable,
    removes punctuation and linebreaks,
    sets all words to lowercase, and
    returns the cleaned tweet as a single
    variable list.
    '''

    # Grabbing most common punctuation symbols and ellipsis symbol
    punctuation_list = list(string.punctuation)+ ["…"] + ['’']
    punctuation_list.remove('#')


    cleaned_tweet = []

    for symbol in punctuation_list:

        tweet = tweet.replace(symbol, "").lower()

        # Removing trailing characters
        tweet = tweet.rstrip()

        # Cleaning non-ASCII characters
        tweet = re.sub("([^\x00-\x7F])+","",tweet)

    cleaned_tweet.append(tweet)

    return cleaned_tweet

def tokenize(clean_tweet):

    '''
    This function takes a cleaned tweet,
    joins into one string (if not already),
    runs the tweet through NLTK work tokenizer,
    removes English stopwords, replaces "us"
    with "usa," removes numbers and returns
    the tokenized tweet in list format.
    '''

    joined_tweet = ' '.join(clean_tweet)
    stopwords_list = stopwords.words('english')

    tokenizer = TweetTokenizer()
    tokenized_tweet = tokenizer.tokenize(joined_tweet)
    # Removing stopwords
    tokenized_tweet = [word for word in tokenized_tweet if word not in stopwords_list]

    # Subbing 'usa' for 'us'
    tokenized_tweet = ['usa' if word == 'us' else word for word in tokenized_tweet]

    # Removing numbers
    tokenized_tweet = [word for word in tokenized_tweet if not word.isnumeric()]

    return tokenized_tweet

def lem_tweet(tweet):
    '''
    This function takes a tweet in
    the form of a tokenized
    word list and lemmatizes it.
    '''
    lemmatizer = WordNetLemmatizer()

    lemmed_tweet = [lemmatizer.lemmatize(word) for word in tweet]

    return lemmed_tweet

def stem_tweet(tweet):

    stemmer = SnowballStemmer('english')
    stemmed_tweet = [stemmer.stem(word) for word in tweet]

    return stemmed_tweet

def process_tweet(tweet):
    '''
    This function takes an original
    tweet, cleans, tokenizes,
    and lemmatizes the tweet.
    '''
    sans_url_tweet = remove_url_and_RT(tweet)
    cleaned = clean_tweet(sans_url_tweet)
    tokenized = tokenize(cleaned)
#     stemmed_tweet = stem_tweet(tokenized)
    lemmed_tweet = lem_tweet(tokenized)

    return lemmed_tweet
