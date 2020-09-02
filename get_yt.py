from googleapiclient.discovery import build
import json

def main():
    api_key = "AIzaSyC_uDzY8MwR4lrHI1l6pdVhwYncpT95pj0"
    
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.search().list(
            part='snippet',
            #forUsername = 'pewdiepie',
            q = 'COVID-19',
            maxResults=50,
            #order='viewCount',
            type='video'
            #relevanceLanguage='en'
            )

    #num of pages in the sarch result to write the data for
    num_pages = 50


    response = request.execute()
    print(response['pageInfo']['totalResults'])
    print(response['items'][0]['snippet']['title'])
    
    n=1

    json_object = json.dumps(response, indent = 4)
    with open("/home/is/vipul-mi/data_collection/crawl_data/result"+str(n)+".json", 'w') as dum_file:
        dum_file.write(json_object)
    
    nextPage = response['nextPageToken']

    
    print('next page token: {0} '.format(nextPage))
    print()
    while(nextPage):
        n+=1
        request = youtube.search().list(
            part='snippet',
            #forUsername = 'pewdiepie',
            q = 'COVID-19',
            maxResults=50,
            #order='viewCount',
            pageToken=nextPage
            #relevanceLanguage='en'
            )

        response = request.execute()
        json_object = json.dumps(response, indent = 4) 
        nextPage = response['nextPageToken']
        #if n==13:
        #    print(response)
        if len(response['items']) > 0: 
            print(response['items'][0]['snippet']['title'])
        print('next page token: {0} '.format(nextPage))
        print() 

        with open("/home/is/vipul-mi/data_collection/crawl_data/result"+str(n)+".json", 'w') as dum_file:
            dum_file.write(json_object)
        if n>=num_pages:
            nextPage = 0



if __name__=='__main__':
    main()
