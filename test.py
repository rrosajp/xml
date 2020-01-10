import requests
url = 'http://hls.123tv.live/ch/StcjxaIJIRZxHcmO1Ivpeg/1578677692/abc.m3u8'
url = requests.get(url).content
print url