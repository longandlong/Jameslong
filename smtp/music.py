import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://222.204.1.115/20160602225658/40477108c498d0f5a3a875faea345fcf/ymusic/b578/4360/fecf/f71ec9f18617ba142eb7ef8afabbe216.mp3?&ncs_hash_key_one=a9&ncs_hash_key_two=70&ncs_hash_key=a970619a80b1a23c06439e2fb9980902&ncs_dir=0004/163cloudnmusic&')
mu.download()
