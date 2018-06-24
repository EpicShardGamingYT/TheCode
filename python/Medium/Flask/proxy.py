#Made using Flask

#Will just be a proxy for the google homepage
import requests
from flask import *
app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET'])
def main():
	#UA is so google dont treat us as a bot
	ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}	
	r = requests.get("https://google.com",headers=ua)
	return r.text
app.run(host='0.0.0.0') #starts the app at localhost, and can be reached out from internet if you portforward