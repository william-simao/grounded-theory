def start():
    import os
    lst_entries = os.listdir("OER/General") # Mudar p/ General ou Portuguese
    get_pdf(lst_entries)


def get_pdf(lst_entries):
    for entry in lst_entries:
        if entry.endswith('pdf'):
            print(entry)