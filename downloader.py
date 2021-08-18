import os
import youtube_dl


VIDEO_DOWNLOAD_PATH = '../../download'                        # 다운로드 경로
VIDEO_DOWNLOAD_URL_TXT_FILE = './url.txt'                     # 다운로드 대상 url txt 파일 이름
VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE = './complete_url.txt'  # 다운로드 완료 URL txt 파일
DOWNLOAD_COMPLETE_LIST = []


def download_video_and_subtitle(youtube_video_list):
    download_path = os.path.join(VIDEO_DOWNLOAD_PATH, '%(title)s.%(ext)s')
    youtube_dl.utils.std_headers['Referer'] = "https://www.google.com/"

    for video_url in youtube_video_list:
        # youtube_dl options
        ydl_opts = {
            'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
            'outtmpl': download_path,  # 다운로드 경로 설정
            # 'writesubtitles': 'best', # 자막 다운로드(자막이 없는 경우 다운로드 X)
            # 'writethumbnail': 'best',  # 영상 thumbnail 다운로드
            'writeautomaticsub': False,  # 자동 생성된 자막 다운로드
            # 'subtitleslangs': 'en'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
            'http_chunk_size': 2097152,
            'retries': 3,
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                status = ydl.download([video_url])
                if status == 0:
                    if video_url not in DOWNLOAD_COMPLETE_LIST:
                        with open(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE, "a") as file:
                            file.write("%s\n" % video_url)
                        print("complete download : " + video_url)
                    #     new_download_complete_list.append(video_url)

        except Exception as e:
            print('error', e)


def make_download_url_list():
    url_list = [line.rstrip('\n') for line in open(VIDEO_DOWNLOAD_URL_TXT_FILE, 'r')]
    print("download url list count : ", len(url_list))

    complete_url_list = []
    if os.path.isfile(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE):
        complete_url_list = [line.rstrip('\n') for line in open(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE, 'r')]
        print("download complete url list count : ", len(complete_url_list))

    new_url_list = []
    for url in url_list:
        if url not in complete_url_list:
            new_url_list.append(url)

    print("download complete url delete new url list count : ", len(new_url_list))

    return new_url_list, complete_url_list


if __name__ == '__main__':
    print('Start Youtube Download!')
    download_url_list, DOWNLOAD_COMPLETE_LIST = make_download_url_list()

    new_download_complete_list = download_video_and_subtitle(download_url_list)

    print('Complete download!')
