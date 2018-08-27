# /bin/python
import os
from pymongo import MongoClient
import ConfigParser

def drop_collection(mongodb_url):
	print ("drop ycsb.usertable")
	client = MongoClient(mongodb_url)
	db = client.ycsb
	collection = db.usertable
	result = collection.drop()
	print (result)
	
def run(mongodb_url, recordcount, threads)
	result = os.popen('sh ycsb.sh %s %s' %(mongodb_url, recordcount, threads))
	print (result)

if __name__=="__main__":
	conf = ConfigParser.ConfigParser() 
	conf.read("config.ini")
	mongodb_url = conf.get("mongodb","mongodb_url")
	recordcount_list = conf.get("ycsb","recordcount_list")
	threads_list = conf.get("ycsb","threads_list")
	for recordcount in recordcount_list:
		for threads in threads_list:
			drop_collection(mongodb_url)
			run(mongodb_url, recordcount, threads)
	print (os.popen('cat lujin.txt'))