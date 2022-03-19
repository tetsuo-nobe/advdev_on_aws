#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import boto3
from boto3.session import Session
import time


# In[2]:


# デモ用のプロファイルを使用
profile = 'advdev'
session = Session(profile_name=profile)

# 現在の設定値を取得・表示
client = session.client('appconfigdata')

config_session= client.start_configuration_session(
    ApplicationIdentifier='DemoAppConfig',
    ConfigurationProfileIdentifier='imageFile',
    EnvironmentIdentifier='prod',
    RequiredMinimumPollIntervalInSeconds=15
)

response = client.get_latest_configuration(
    ConfigurationToken=config_session['InitialConfigurationToken']
)

config = response["Configuration"].read().decode('utf-8')
files = json.loads(config)

for imageFile in files["imageFileList"]:
        print(imageFile["name"])


# In[3]:


# 10個のクライアントセッションを作成
config_sessions = []
for i in range(0,10):
        config_session= client.start_configuration_session(
            ApplicationIdentifier='DemoAppConfig',
            ConfigurationProfileIdentifier='imageFile',
            EnvironmentIdentifier='prod',
            RequiredMinimumPollIntervalInSeconds=15
        )
        config_sessions.append(config_session)
# 10個のクライアントセッションが繰り返し設定を取得する
for cnt in range(1,13):
    no = 0
    for sess in config_sessions:
        no += 1
        clientId = "client-" + str(no)
        response = client.get_latest_configuration(
             ConfigurationToken=sess['InitialConfigurationToken']
        )
        config = response["Configuration"].read().decode('utf-8')
        files = json.loads(config)
        for imageFile in files["imageFileList"]:
                print(clientId+": "+imageFile["name"])
    time.sleep(5)
    sec = 5 * cnt
    print("--- " + str(sec) + "秒経過 -----------------------------")





