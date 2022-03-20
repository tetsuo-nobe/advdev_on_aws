#!/usr/bin/env python
# coding: utf-8

# In[7]:


import boto3
from boto3.session import Session
import time

# デモ用のプロファイルを使用
profile = 'advdev'
session = Session(profile_name=profile)


# In[8]:


# 現在の値を取得・表示
client = session.client('evidently')

# 値の取得
response = client.evaluate_feature(
  entityId='myId',
  # Name of your feature
  feature='test-function1',
  # Name of your project
  project='test-project-1'
)
# 値の表示
val = response['value']['stringValue']
print(val)


# In[9]:


# 10個のクライアントが繰り返し設定を取得する
for cnt in range(1,21):
    for i in range(0,10):
        clientId = "client-" + str(i)
        response = client.evaluate_feature(
                    entityId=clientId,
                    feature='test-function1',
                    project='test-project-1'
        )
        val = response['value']['stringValue']
        print(clientId+": " + val)
    time.sleep(3)
    sec = 3 * cnt
    print("--- " + str(sec) + "秒経過 -----------------------------")


# In[ ]:
