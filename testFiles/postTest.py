import urllib.parse
import urllib.request
url=""
try:
	province=urllib.parse.quote("广东")
	city=urllib.parse.quote("深圳")
	data="province="+province+"&city="+city
	data=data.encode()
	
