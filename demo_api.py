# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC_uDzY8MwR4lrHI1l6pdVhwYncpT95pj0"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)


#    request = youtube.channels().list(
#        part="contentDetails,statistics",
#        id="UCFsBFxR52KFQIemfaVG5ROg"
#    )

    request = youtube.search().list(
        part="",
        #fields=items(snippet/title),
        maxResults=25,
        q="COVID-19 treatment",
    )

    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
