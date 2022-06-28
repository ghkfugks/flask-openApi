class Config :
    JWT_SECRET_KEY = 'yhacademy1029##hello'
    JWT_ACCESS_TOKEN_EXPIRES = False # 로그아웃 시간
    PROPAGATE_EXCEPTIONS = True

    # AWS PK
    ACCESS_KEY = 'AKIAZPUXAZQKKMXICDCL'
    SECRET_ACCESS = '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'


    # S3 버킷이름과 기본 url 주소 셋팅
    S3_BUCKET = 'pk-image-test'
    S3_LOCATION = 'https://pk-image-test.s3.amazonaws.com/'

    NAVER_PAPAGO_URL = 'https://openapi.naver.com/v1/papago/n2mt'
    NAVER_MOVIE_SEARCH_URL = 'https://openapi.naver.com/v1/search/movie.json'
    NAVER_NEWS_SEARCH_URL = 'https://openapi.naver.com/v1/search/news.json'



    NAVER_CLIENT_ID = 'Djidio5sW87iKVCzshZE'
    NAVER_CLIENT_SECRET = 'qYBBvvXBZO'

