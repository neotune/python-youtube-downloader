import os
import youtube_dl


VIDEO_DOWNLOAD_PATH = '../../downlaod'  # 다운로드 경로
VIDEO_DOWNLOAD_URL_TXT_FILE_NAME = 'url.txt'  # 다운로드 대상 url txt 파일 이름
VIDEO_DOWNLOAD_URL_TXT_FILE_PATH = './'  # 다운로드 대상 url txt 파일 위치


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
                ydl.download([video_url])
        except Exception as e:
            print('error', e)


def make_download_url_list(file_path, file_name):
    list_file = [line.rstrip('\n') for line in open(file_path + file_name, 'r')]
    return list_file


if __name__ == '__main__':
    print('Start Youtube Download!')

    download_video_and_subtitle(
        VIDEO_DOWNLOAD_PATH,
        make_download_url_list(VIDEO_DOWNLOAD_URL_TXT_FILE_PATH, VIDEO_DOWNLOAD_URL_TXT_FILE_NAME)
    )

    print('Complete download!')
