import os
            
def get_articles(words):
    files = os.listdir('./data')
    for word in words:
        max_frep_article_name = ''
        max_freq = 0
        for i in files:
            freq = 0
            with open ('./data/' + i, 'r') as f:
                article = f.read().split()
                for j in article:
                    if j.lower().find(word[0]) >= 0:
                        freq += 1
            if max_freq <= freq:
                max_freq = freq
                max_frep_article_name = i
        words[words.index(word)]+=(max_freq, max_frep_article_name)
    return words
