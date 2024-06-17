

def url_loader(filename):
    video_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            url = line.strip()
            video_list.append(url)
    print(video_list)

if __name__ == '__main__':
    url_loader('video_urls.txt')