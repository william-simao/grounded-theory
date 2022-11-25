normalizer_data = False
reader_data = True
cleaner_data = False

start_lexical_selection = False
start_unsupervised = False

start_lda = False

if normalizer_data:
    import normalizer as normalizer
    normalizer.start()

if reader_data:
    import reader as reader
    reader.start()

if cleaner_data:
    import cleaner as cleaner
    cleaner.start()

if start_lexical_selection:
    import lexical_selection as lexical_selection
    lexical_selection.start()

if start_unsupervised:
    import unsupervised as unsupervised
    unsupervised.start()

if start_lda:
    import lda as lda
    lda.start()