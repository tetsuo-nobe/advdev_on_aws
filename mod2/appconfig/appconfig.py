#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import boto3
from boto3.session import Session
import time


# In[5]:


# デモ用のプロファイルを使用
profile = 'advdev'
session = Session(profile_name=profile)

# 現在の設定値を取得・表示
client = session.client('appconfig')
response = client.get_configuration(
            Application="DemoAppConfig",
            Environment="prod",
            Configuration="imageFile",
            ClientId="client-999"
)
config = response["Content"].read().decode('utf-8')
files = json.loads(config)

for imageFile in files["imageFileList"]:
        print(imageFile["name"])


# In[7]:


# 10個のクライアントが繰り返し設定を取得する
for cnt in range(1,21):
    for i in range(0,10):
        clientId = "client-" + str(i)
        response = client.get_configuration(
                    Application="DemoAppConfig",
                    Environment="prod",
                    Configuration="imageFile",
                    ClientId=clientId
        )
        config = response["Content"].read().decode('utf-8')
        files = json.loads(config)
        for imageFile in files["imageFileList"]:
                print(clientId+": "+imageFile["name"])
    time.sleep(3)
    sec = 3 * cnt
    print("--- " + str(sec) + "秒経過 -----------------------------")
