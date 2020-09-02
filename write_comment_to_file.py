import json
from os import listdir
from os.path import isfile, join, dirname

com_path = '/home/is/vipul-mi/data_collection/crawl_data/tries/try1/comments'

def get_all_comments(all):
    dir_content = listdir(com_path)
    files = [join(com_path, f) for f in dir_content if isfile(join(com_path, f)) and 'comments_for_' in f]
    print(len(files))
    for f_path in files:
        with open(f_path, 'r') as com_file:
            data = json.load(com_file)
            video_id = f_path[-11:]
            comment_num = len(data['items'])
            comments=[]
            for item in data['items']:
                comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
            all.append([video_id, comment_num, comments])


def main():
    all_comments=[]
    get_all_comments(all_comments)
    with open(join(com_path, 'all_comments.txt'), 'w') as all_com_file:
        for i,j,k in all_comments:
            for com in k:
                all_com_file.write('{0}\n'.format(com))
    print(all_comments[-4])
    print(len(all_comments))
    


if __name__=='__main__':
    main()

