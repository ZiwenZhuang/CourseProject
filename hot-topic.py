import os
from Spiders import *
from Prasers import MainRanker
from getarticles import get_articles

def saveresult(result):
    with open('result.txt', 'w') as f:
        for i in result:
            f.write(str(i)+'\n')

if __name__ == '__main__':
    area_specifics_words = ['student', 'children', 'school', 'safe', 'educ', 'teacher', 'learn', ]


    # crawl pages from data.gov
    #spider = DataGovSpider()
    #spider.start('./data/DataGov')

    # crawl pages from USnews
    #spider = USnewsSpider()
    #spider.start('./data/USnews')

    # crawl pages from TheGuardian
    #spider = TheGuardianSpider()
    #spider.start('./data/TheGuardian')

    ranker = MainRanker('all', 748, True)
    #word_freq = ranker.simple_BOW_rank()
    #word_freq = ranker.BOW_stem_stop_rank()
    #word_freq = ranker.POS_rank('NNP')
    #word_freq = ranker.ngrams_rank()
    #word_freq = ranker.tfidf_rank(myhottest=30, stemmer_name='Snowball', para='"english"', to_remove=area_specifics_words)
    word_freq = ranker.tfidf_POS_rank(['NN', 'NP', 'NNS'],  myhottest=50, stemmer_name='Snowball', para='"english"', to_remove=area_specifics_words)
    result = get_articles(word_freq)
    
    saveresult(result)
    print('Program ' + os.path.basename(__file__) + ' ends sucessfully')
    
