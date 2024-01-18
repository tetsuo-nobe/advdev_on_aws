# AWS Lambda レイヤーのサンプル 

### このサンプルの内容
* AWS Lambda レイヤー: my-boto3-layer
    - AWS SDK for Python (boto3) の バージョン 1.26.73 のパッケージを Lambda レイヤー化したもの
    - myLayer/boto3-layer.zip 
* AWS Lambda 関数: WithLayerFunction
    - 上記 Lambda レイヤーを使用する Lambda 関数
    - withLayerFunction/app.py
* AWS Lambda 関数: WithoutLayerFunction
    - Lambda レイヤーを使用しない Lambda 関数
    - **コードは、WithLayerFunctionと同じ**
    - withoutLayerFunction/app.py
* AWS SAM テンプレート
    - 上記の Lambda レイヤーや、Lambda 関数をデプロイするための AWAS SAM テンプレート
    - template.yaml

### このサンプルの使用方法

1. AWS SAM CLI を使用して、上記のリソースをデプロイする
1. AWS マネージメントコンソールで、WithLayerFunctionを開き、テストタブからテスト実行する。
    - ログに下記が表示されれば、Lambda レイヤーの boto3 を使用していることの確認となる
    ````
    boto3 version: 1.26.73
    botocore version: 1.29.73
    ````
1. AWS マネージメントコンソールで、WithoutLayerFunctionを開き、テストタブからテスト実行する。
    - ログに表示される boto3 のバージョンは、Lambda レイヤーではなく Lambda 関数の実行環境に含まれるものを使用するので、上記とは異なるバージョンが表示されることを確認する。（下記は例）
    ````
    boto3 version: 1.26.90
    botocore version: 1.29.90
    ````
   





