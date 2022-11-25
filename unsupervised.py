import pandas as pd


origin = 'Portuguese' # 'Portuguese' or 'General'


def start():
    df = pd.read_csv(f'Output/1-datastructure-{origin}.csv')
    clusterize(df)


def clusterize(df):
    from sklearn.cluster import KMeans

    vectorizer = get_vectorizer()
    X = vectorizer.fit_transform(df["html"].values.astype('U'))

    n_clusters = 4 # Update to generate new .csvs
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    print("Prediction")
    df_result = pd.DataFrame(columns=['id', 'cluster'])
    for i, row in df.iterrows():
        try:
            X = vectorizer.transform([row["html"]])
            predicted = model.predict(X)
            df_result.loc[len(df_result)] = [row['id'], predicted]
        except:
            print('Error: ', i)
        print(i)
    df_result.to_csv(f'Output/Open Coding/cluster-{origin}.csv')


def get_vectorizer():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from nltk.corpus import stopwords
    stop_portuguese = stopwords.words('portuguese')
    stop_english = stopwords.words('english')
    if origin == 'Portuguese':
        return TfidfVectorizer(stop_words=stop_portuguese)
    return TfidfVectorizer(stop_words=stop_english)