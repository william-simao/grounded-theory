import pandas as pd
import nltk.corpus
from nltk.corpus import stopwords


origin = 'Portuguese' #'Portuguese' or 'General'


def start():
    # Starting download corpus
    nltk.download('stopwords')

    df = pd.DataFrame(columns=["id", "source", "token", "counter"])
    df_datastructures = pd.read_csv(f'Output/1-datastructure-{origin}.csv')
    convert_data(df_datastructures, df)


def convert_data(df_datastructures, df):
    for i, row in df_datastructures.iterrows():
        print(i, row['id'], row['source'])
        lst_tokens = clean_text(row['html'])
        update_df(row, df, lst_tokens)
    df.to_csv(f'Output/2-data_cleaned-{origin}.csv')


def update_df(row, df, lst_tokens):
    from collections import Counter
    counter = Counter(lst_tokens)
    for key in counter:
        df.loc[len(df)] = [row['id'], row['source'], key, counter[key]]


def clean_text(text):
    text = str(text).lower()

    #  Removing Unicode Characters and stopwords
    import re
    if origin == 'General':
        stop_english = stopwords.words('english')
        text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
        text = " ".join([word for word in text.split() if word not in (stop_english)])
    else:
        stop_portuguese = stopwords.words('portuguese')
        text = re.sub(r"(@\[A-Za-zà-úÀ-Ú0-9]+)|([^0-9A-Za-zà-úÀ-Ú \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
        text = " ".join([word for word in text.split() if word not in (stop_portuguese)])

    # Tokenization
    tokens = nltk.word_tokenize(text)

    return tokens
