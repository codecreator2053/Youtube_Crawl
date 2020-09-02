import json
import pandas as pd
from googleapiclient.discovery import build
import time

def get_vids():
    df = pd.read_csv('/home/is/vipul-mi/data_collection/crawl_data/tries/try1/search_result.csv')
    videoIds=[]
    for i in df.iterrows():
        videoIds.append(i[1][0])
    return videoIds


def main():
    videoIds = get_vids()

    #vip_api_key = "AIzaSyC_uDzY8MwR4lrHI1l6pdVhwYncpT95pj0"

    #ujiie
    api_key= "AIzaSyBti9ZLXch4QP3zWfY9eG6a_bqHkBcqgkU"

    youtube = build('youtube', 'v3', developerKey=api_key)

    n=1
    for curId in videoIds[264:]:
        print('vid:', n, 'Id', curId)
        request = youtube.commentThreads().list(
                part='id, replies, snippet',
                videoId=curId,
                maxResults=100,
                order='relevance',
                textFormat='plainText'
                )
        try:
            response = request.execute()
            if len(response['items'])>0:
                print(response['items'][0]['snippet']['topLevelComment']['snippet']['textDisplay'])
            print()
        
            #so that the queries don't get shut down
            time.sleep(10)

            json_object = json.dumps(response, indent=4) 
            with open('/home/is/vipul-mi/data_collection/crawl_data/tries/try1/comments/comments_for_'+curId, 'w') as save_file:
                save_file.write(json_object)
        except:
            print(curId)
            print()
        n+=1


if __name__=='__main__':
    main()
