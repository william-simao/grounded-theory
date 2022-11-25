import pandas as pd


origin = 'General' #'Portuguese' or 'General'


def start():
    lst_entries = get_entries()
    df = pd.DataFrame(columns=["id", "source", "html"])
    read_html_files(lst_entries, df)
    df.to_csv(f'Output/1-datastructure-{origin}.csv')


def get_entries():
    import os
    return os.listdir(f'OER/{origin}')


def read_html_files(lst_entries, df):
    for entry in lst_entries:
        if entry.endswith('.html') or entry.endswith('.htm'):
            html_file = open(f'OER/{origin}/{entry}', "r", encoding="utf-8", errors='ignore')
            print(entry)
            add_entry(df, entry, html_file.read())


def add_entry(df, entry, html_result):
    html = remove_tags(html_result)
    df.loc[len(df)] = [len(df) + 1, entry, html]


def remove_tags(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
    return ' '.join(soup.stripped_strings)
