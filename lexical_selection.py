import pandas as pd

origin = 'Portuguese' #'Portuguese' or 'General'


def start():
    df_data_cleaned = pd.read_csv(f'Output/2-data_cleaned-{origin}.csv')
    count_occurrences(df_data_cleaned)
    df_idf()


def count_occurrences(df_data_cleaned):
    df = pd.DataFrame(columns=["token", "terms occurrences", "occurrences in OER"])

    lst_tokens = df_data_cleaned.token.unique()
    for token in lst_tokens:
        df_aux = df_data_cleaned.query(f"token == '{token}'")
        df.loc[len(df)] = [token, df_aux['counter'].sum(), int(len(df_aux))]
    df.to_csv(f'Output/Open Coding/count_occurrences-{origin}.csv')


# https://www.learndatasci.com/glossary/tf-idf-term-frequency-inverse-document-frequency/
def df_idf():
    from sklearn.feature_extraction.text import TfidfVectorizer
    df = pd.read_csv(f'Output/1-datastructure-{origin}.csv')

    # check language
    tr_idf_model = TfidfVectorizer(stop_words='english', tokenizer=tokenize_and_clean)
    tf_idf_vector = tr_idf_model.fit_transform(df['html'].values.astype('U'))

    tf_idf_array = tf_idf_vector.toarray()
    words_set = tr_idf_model.get_feature_names()
    df_tf_idf = pd.DataFrame(tf_idf_array, columns=words_set)

    df_t = df_tf_idf.T # Transpose dataframe

    df_t.to_csv(f'Output/Open Coding/TF_IDF-{origin}.csv')


def tokenize_and_clean(text):
    import cleaner as cleaner
    return cleaner.clean_text(text)
