import base64
url = 'https://raw.githubusercontent.com/Tempest0580/xml/master/testing.txt'
url = base64.b64encode(url)
print url