import pandas as pd


origin = 'Portuguese' # 'Portuguese' or 'General'


def start():
    df = pd.read_csv(f'Output/1-datastructure-{origin}.csv')
    LDA(df)


def LDA(df):
    from gensim import corpora, models
    import gensim

    texts = transform_text(df)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=20)

    # writing topics
    writing_topics(ldamodel)

    # saving each OER according to topics
    save(df, dictionary, ldamodel)


def transform_text(df):
    from nltk.stem.porter import PorterStemmer
    p_stemmer = PorterStemmer()

    texts = []
    for i, row in df.iterrows():
        try:
            raw = row['html'].lower()
            raw = ''.join((x for x in raw if not x.isdigit()))
            tokens = tokenize_and_clean(raw)
            stopped_tokens = [i for i in tokens if not i in get_stop_words()]
            stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
            texts.append(stemmed_tokens)
        except:
            print('Error: ', i)
    return texts


def get_stop_words():
    from nltk.corpus import stopwords

    if origin == 'Portuguese':
        stop_portuguese = stopwords.words('portuguese')
        return stop_portuguese

    stop_english = stopwords.words('english')
    stop_english.extend(['de', 'richard', 'baldwin', 'kenneth', 'leroy', 'mordechai', 'moti', 'jan', 'fev', 'dez',
                         '2016', '2014', '4', 'abr', '2022', '2015', '13h', '2013', '2012'])
    return stop_english


def writing_topics(ldamodel):
    df_topics = pd.DataFrame(columns=['Topic'])
    for topic in ldamodel.print_topics():
        df_topics.loc[len(df_topics)] = [topic]
    df_topics.to_csv(f'Output/Axial Coding/topics-{origin}.csv')


def save(df, dictionary, ldamodel):
    df_axial_coding = pd.DataFrame(columns=['id', 'source', 'Topic'])
    for i, row in df.iterrows():
        try:
            new_doc_bow = dictionary.doc2bow(row['html'].split(' '))
            result = ldamodel.get_document_topics(new_doc_bow)
            df_axial_coding.loc[len(df_axial_coding)] = [row['id'], row['source'], result]
        except:
            print('Error: ', i)
    df_axial_coding.to_csv(f'Output/Axial Coding/OER_topics-{origin}.csv')


def tokenize_and_clean(text):
    import cleaner as cleaner
    return cleaner.clean_text(text) # ver se a classe está com a variável 'origin' correta
