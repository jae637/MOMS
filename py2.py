from flask import Flask
app = Flask(__name__)

# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request
import datetime

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
from py3 import load,recommend

app = Flask(__name__)

slack_token = 'xoxb-506274278966-508887136742-2iRUA91ZyCZXFvLB8AoyOiC1'
slack_client_id = '506274278966.506747096752'
slack_client_secret = '8e4975288d9fc328c9dc6b60177b4503'
slack_verification = 'PRfEmQNri2IGZRvPOZWJaFzJ'
sc = SlackClient(slack_token)

'''elice_sample=[]
elice_sample['pretext'] = "attachments 블록 전에 나타나는 text"
elice_sample['title'] = "다른 텍스트 보다 크고 굵은 title"
elice_sample['title_link'] = "https://sample.github.io"
elice_sample['fallback'] = "클라이언트 알림에서 보이는 텍스트."
elice_sample['text'] = "본문 텍스트가 5줄이 넘어가면 show more로 보이게 됩니다."
'''
# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
    
    #여기에 함수를 구현해봅시다    
    keywords =[]

    text = text.upper()
    
    if "오늘" in text :
        text = text+ str(datetime.datetime.now().day)
    elif "내일" in text :
        if "모레" in text :
            text = text+ str((datetime.datetime.now()+datetime.timedelta(days=2)).day)
        else:
            text = text+ str((datetime.datetime.now()+datetime.timedelta(days=1)).day)
    elif "어제" in text :
        text = text+ str((datetime.datetime.now()-datetime.timedelta(days=1)).day)
    elif "그제" in text :
        text = text+ str((datetime.datetime.now()-datetime.timedelta(days=2)).day)
    
    if '밥줘' in text:
        keywords.append('싫어 ㅡㅡ :angry:')
    elif "식단" or '밥' in text :
        if "17" in text :
            keywords.append(':rice: 17일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1203',1,5)                
            elif "B" in text :
                keywords+=load('1203',1,13)        
            elif "먹을까요" in text :
                keywords+=recommend('1203',1)
            else: 
                keywords+=load('1203',1,5)
                keywords+='\n'
                keywords+=load('1203',1,13)      

        elif "18" in text :
            keywords.append(':rice: 18일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1203',2,5)                
            elif "B" in text :
                keywords+=load('1203',2,13)
            elif "먹을까요" in text :
                keywords+=recommend('1203',2)
            else: 
                keywords+=load('1203',2,5)
                keywords+='\n'
                keywords+=load('1203',2,13)      
        elif "19" in text :
            keywords.append(':rice: 19일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1203',3,5)                
            elif "B" in text :
                keywords+=load('1203',3,13)      
            elif "먹을까요" in text :
                keywords+=recommend('1203',3)   
            else: 
                keywords+=load('1203',3,5)
                keywords+='\n'
                keywords+=load('1203',3,13)      
        elif "20" in text :
            keywords.append(':rice: 20일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1203',4,5)                
            elif "B" in text :
                keywords+=load('1203',4,13)  
            elif "먹을까요" in text :
                keywords+=recommend('1203',4)  
            else: 
                keywords+=load('1203',4,5)
                keywords+='\n'
                keywords+=load('1203',4,13)           
        elif "21" in text :
            keywords.append(':rice: 21일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1203',5,5)                
            elif "B" in text :
                keywords+=load('1203',5,13)  
            elif "먹을까요" in text :
                keywords+=recommend('1203',5)
            else: 
                keywords+=load('1203',5,5)
                keywords+='\n'
                keywords+=load('1203',5,13)
        elif "24" in text :
            keywords.append(':rice: 24일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1204',1,5)                
            elif "B" in text :
                keywords+=load('1204',1,13)  
            elif "먹을까요" in text :
                keywords+=recommend('1204',1)
            else: 
                keywords+=load('1204',1,5)
                keywords+='\n'
                keywords+=load('1204',1,13)
        elif "26" in text :
            keywords.append(':rice: 26일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1204',3,5)                
            elif "B" in text :
                keywords+=load('1204',3,13)  
            elif "먹을까요" in text :
                keywords+=recommend('1204',3)
            else: 
                keywords+=load('1204',3,5)
                keywords+='\n'
                keywords+=load('1204',3,13)
        elif "27" in text :
            keywords.append(':rice: 27일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1204',4,5)                
            elif "B" in text :
                keywords+=load('1204',4,13)  
            elif "먹을까요" in text :
                keywords+=recommend('1204',4)
            else: 
                keywords+=load('1204',4,5)
                keywords+='\n'
                keywords+=load('1204',4,13)
        elif "28" in text :
            keywords.append(':rice: 28일 식단 :rice:\n')
            if "A" in text :
                keywords+=load('1204',5,5)                
            elif "B" in text :
                keywords+=load('1204',5,13) 
            elif "먹을까요" in text :
                keywords+=recommend('1204',5) 
            else: 
                keywords+=load('1204',5,5)
                keywords+='\n'
                keywords+=load('1204',5,13)
        else :
            keywords.append('식당 쉬신대요... 저도 좀 쉴래요ㅠㅠ')
    


        
    
    # 한글 지원을 위해 앞에 unicode u를 붙혀준다.
    return u'\n'.join(keywords)
'''
elice_sample = {}

elice_sample['pretext'] = "attachments 블록 전에 나타나는 text"
elice_sample['title'] = "다른 텍스트 보다 크고 굵은 title"
elice_sample['fallback'] = "클라이언트 알림에서 보이는 텍스트."

elice_sample['text'] = "본문 텍스트가 5줄이 넘어가면 show more로 보이게 됩니다."
'''
# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = _crawl_naver_keywords(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords,
        )

        return make_response("App mention message has been sent", 200,)

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                             "application/json"
                                                            })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})
    
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})

@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"

if __name__ == '__main__':
    app.run(debug=True)