import flask
from flask import Flask, jsonify, render_template, request

import json
#import fetcher

# open stream for confirmation
import urllib

# boto SQS 
import boto.sqs
from boto.sqs.message import Message


application = Flask(__name__)

# global list 
finalList = []

# / is the home page of PieTwitt
@application.route('/')
def index():
	print "Home sweet home."
	return flask.render_template('index.html')


# /map displays heatmap of all tweets
@application.route('/map/<keywords>')
def displayMap(keywords):
	# allTweets = []
	print "finalList = ", finalList

	return flask.render_template('map.html', keywords=keywords, allTweets = finalList)


# SNS HTTP request endpoint: subscribe, unsubscribe, notification
@application.route('/kitkat', methods = ['POST', 'GET'])
def sns():
	headers = request.headers
	# print "headers", headers
	print "request", request
	obj = json.loads(request.data)
	print "!!!!!!!!!!!!!!!!!!!!!POST SUCCESS!!!!!!!!!!!!!!!!!!!!! = ", obj

	global  finalList
	finalList.append(obj[u'data1'])
	finalList.append(obj[u'data2'])
	finalList.append(obj[u'data3'])

	print finalList

	return '', 200



if __name__ == '__main__':
	try: 
		application.config["DEBUG"] = True
		application.run(host='0.0.0.0', port=9090)
		#application.run(host='199.58.86.213', port=5000)


	except:
		print "application.run failed"

