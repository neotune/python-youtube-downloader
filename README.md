# python-youtube-downloader

> ###python version : 3.9.1
> #### module
> - youtube_dl 2021.1.8 (pip install youtube_dl)
> - beautifulsoup4 (pip install beautifulsoup4)
> - Selenium (pip install selenium)
> - lxml (pip install lxml)

-------------

### 실행 방법
> 해당 실행 환경은 윈도우10에서 실행 하도록 되어 있음
> 2번의 파일의 실행을 통해 동영상이 저장됨
 
1. 수집하고자 하는 채널의 동영상 리스트 주소 복사 (ex: https://www.youtube.com/c/pororo/videos)
2. ```url_crawler.py``` 파일의 YOUTUBE_URL 변수에 해당 주소로 수정
3. 전체 수집이 아닌 특정 동영상만 수집 하고 싶을 경우 정규식 수정
4. 크롬 버젼에 따라서 ```https://chromedriver.chromium.org/downloads``` 에서 ```chromedriver.exe```
를 최신화 해야함
5. 원하는 내용 수정 후 ```pyhton url_crawler.py``` 실행
6. ```url_crawler.py``` 위치에 url.txt 파일 생성됨
7. ```downloader.py``` 에 원하는 저장 경로 수정
8. ```python downloader.py``` 실행
9. 모정의 이유로 다운로드가 중단 될 경우 ```complete_url.txt``` 파일에 다운로드 완료된 url 경로가 저장 되므로 중단되었더라도 ```python downloader.py``` 를 재실행 하면 됨

