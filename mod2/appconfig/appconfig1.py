import json
import boto3
from boto3.session import Session
import time

# デモ用のプロファイルを使用
profile = 'default'
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




