import os

from Spiders import *
from Prasers import MainRanker

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

    ranker = MainRanker('./data/crawled', 748, True)
    #print(ranker.simple_BOW_rank())
    #print(ranker.BOW_stem_stop_rank())
    #print(ranker.POS_rank('NP'))
    #print(ranker.ngrams_rank())
    print(ranker.tfidf_POS_rank(['NN', 'NP', 'NNS'],  myhottest=50, stemmer_name='Snowball', para='"english"', to_remove=area_specifics_words))
    #print(ranker.tfidf_rank(myhottest=30, stemmer_name='Snowball', para='"english"', to_remove=area_specifics_words))

    
    print('Program ' + os.path.basename(__file__) + ' ends sucessfully')
