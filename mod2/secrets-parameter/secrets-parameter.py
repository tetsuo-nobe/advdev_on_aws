import boto3
import json
import os
from boto3.session import Session
from botocore.exceptions import ClientError

# デモ用のプロファイルを使用
profile = 'default'
session = Session(profile_name=profile)

# 初期設定
ssm = session.client('ssm')
ssm_param_name = 'DemoParameter'
sm_secret_name = 'DemoSecrets'
region_name = 'ap-northeast-1'
prefix = "/aws/reference/secretsmanager" 


#　SSM Parameter Storeの内容の表示
def printSSMParameter():
  # パラメータ名から復号したパラメータ値を取得
  ssm_response = ssm.get_parameters(
    Names = [
      ssm_param_name
    ],
    WithDecryption = True
  )
  # パラメータ値を格納する配列を準備
  params = {}
  # 復号化したパラメータ値を配列に格納
  for param in ssm_response[ 'Parameters' ]:
     print("-- SSM Parameter -- :"+param['Name'] + ":" + param['Value'])


#　SecretsS Managerのシークレットの内容の表示
def printSMSecret():

    #  Secrets Manager clientの作成
    session = boto3.session.Session(profile_name=profile)
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=sm_secret_name
        )
    except ClientError as e:
        raise e
    else:
        secret = get_secret_value_response['SecretString']
        secret_dict = json.loads(secret)
        for key in secret_dict.keys():
            print("-- Secret Manager Secret -- :"+ key + ":" + secret_dict[key])

#　SSM Parameter StoreのAPIでSecrets Managerのシークレットの取得と表示
def printSMSecretFromSSM():
  # パラメータ名から復号したパラメータ値を取得
  param_name = prefix + "/" + sm_secret_name
  ssm_response = ssm.get_parameters(
    Names = [
      param_name,
    ],
    WithDecryption = True
  )
  secrets = ssm_response[ 'Parameters' ][0]['Value']
  secret_dict = json.loads(secrets)
  for key in secret_dict.keys():
      print("-- Secret Manager Secret from SSM -- :"+ key + ":" + secret_dict[key])


printSSMParameter()
printSMSecret()
printSMSecretFromSSM()






