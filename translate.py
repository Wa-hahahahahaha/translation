import requests 
url = 'https://fanyi.baidu.com/sug'
class translate:
    def __init__(self,url=url):
        self.url = url
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0}"}
    def tran(self,word):
        data = {'kw':word}
        try:
            raw = requests.post(url=self.url,headers=self.header,data = data)
            text_list = raw.json()['data']
            contents = ''
            for text in text_list:
                content = text['k'] +':'+ text['v']+'\n'
                contents += content
            return contents
        except:
            return 'Error'
