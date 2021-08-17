import os
import youtube_dl


VIDEO_DOWNLOAD_PATH = '../../download'                        # 다운로드 경로
VIDEO_DOWNLOAD_URL_TXT_FILE = './url.txt'                     # 다운로드 대상 url txt 파일 이름
VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE = './complete_url.txt'  # 다운로드 완료 URL txt 파일


def download_video_and_subtitle(output_dir, youtube_video_list):
    download_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    for video_url in youtube_video_list:

        # youtube_dl options
        ydl_opts = {
            'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
            'outtmpl': download_path,  # 다운로드 경로 설정
            # 'writesubtitles': 'best', # 자막 다운로드(자막이 없는 경우 다운로드 X)
            # 'writethumbnail': 'best',  # 영상 thumbnail 다운로드
            'writeautomaticsub': False,  # 자동 생성된 자막 다운로드
            # 'subtitleslangs': 'en'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                status = ydl.download([video_url])
                if status == 0:
                    with open(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE, "w") as file:
                        file.write(video_url)
                        print("complete download : " + video_url)

        except Exception as e:
            print('error', e)


def make_download_url_list():
    download_list = [line.rstrip('\n') for line in open(VIDEO_DOWNLOAD_URL_TXT_FILE, 'r')]
    print("download url list count : ", len(download_list))

    download_complete_list = []
    if os.path.isfile(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE):
        download_complete_list = [line.rstrip('\n') for line in open(VIDEO_DOWNLOAD_COMPLETE_URL_TEXT_FILE, 'r')]
        print("download complete url list count : ", len(download_complete_list))

    new_donwload_list = []
    for url in download_list:
        if url not in download_complete_list:
            new_donwload_list.append(url)

    print("download complete url delete new url list count : ", len(new_donwload_list))

    return download_list


if __name__ == '__main__':
    print('Start Youtube Download!')

    download_video_and_subtitle(
        VIDEO_DOWNLOAD_PATH,
        make_download_url_list()
    )

    print('Complete download!')
