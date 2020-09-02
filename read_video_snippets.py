import json
import pandas as pd

def main():
    all_files = range(1,13)
    vid_infos = [] 
    for i in all_files:
        read_api_resps(i, vid_infos)
    
    search_df = pd.DataFrame(vid_infos)
    search_df.to_csv('/home/is/vipul-mi/data_collection/crawl_data/tries/try1/search_result.csv', index=False, header=False)    

    for i in vid_infos:
        print(i)


def read_api_resps(i, vid_infos):
    with open('/home/is/vipul-mi/data_collection/crawl_data/tries/try1/result' + str(i) + '.json', 'r') as cur_file:
        data = json.load(cur_file)
        snippets = data['items']
        for j in range(len(snippets)):
            #print(type(snippets[j]))
            try:
                vid_id = snippets[j]['id']['videoId']
                ch_id = snippets[j]['snippet']['channelId']
                vid_title = snippets[j]['snippet']['title']
                ch_title = snippets[j]['snippet']['channelTitle']
                published_at = snippets[j]['snippet']['publishedAt']
                vid_infos.append([vid_id, ch_id, vid_title, ch_title, published_at])
            except:
                print(snippets[j])



if __name__=='__main__':
    main()


