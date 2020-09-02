from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd

valid_pos={'noun':['NN' ,'NNS']}
stop_list = stopwords.words('english')

def tokenize_comments(comments):
    nouns = []
    proper = []
    for comm in comments:
        toks = pos_tag(word_tokenize(comm.lower()))
        for tok in toks:
            if tok[1] in valid_pos['noun'] and tok[0] not in stop_list:
                nouns.append(tok[0])
                if tok[1] in ['NNP', 'NNPS'] and tok[0] not in stop_list:
                    proper.append(tok[0])    
    nouns = Counter(nouns)
    tags=[]
    counts=[]
    for tag, count in nouns.items():
        tags.append(tag)
        counts.append(count)
    sorted_tags = [t for _,t in sorted(zip(counts,tags), reverse=True)]
    sorted_counts = sorted(counts, reverse=True)
    noun_count = pd.DataFrame(data={'tags': sorted_tags, 'counts': sorted_counts})
    noun_count.to_csv('/home/is/vipul-mi/data_collection/scripts/counts.csv', index=False)

    
    #print(list(Counter(nouns).items())[:10])
    #print(list(Counter(proper).items())[:10]) 

def main(): 
    lines=[]
    with open('/home/is/vipul-mi/data_collection/crawl_data/tries/try1/comments/all_comments.txt', 'r') as lines:
        comments = lines.readlines()
    tokenize_comments(comments)
    nouns=[]
    verbs=[]
    adj=[]
    adv=[]


if __name__=='__main__':
    main()
