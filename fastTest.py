import urllib.request
import gzip
webAddress = "http://andrews.cs.fit.edu/~cse1002-stansifer/projects/flags/corpus2.utf.gz"
file = urllib.request.urlopen(webAddress)
data = file.read()
if file.headers['content-encoding'].lower() == 'gzip':
    data = gzip.decompress(data)
file.close()
dataString = data.decode(encoding='UTF-8')