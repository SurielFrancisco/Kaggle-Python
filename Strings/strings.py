def multi_word_search(doc_list, keywords):
    """Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword.
    """
    return {keyword: word_search(doc_list, keyword) for keyword in keywords}