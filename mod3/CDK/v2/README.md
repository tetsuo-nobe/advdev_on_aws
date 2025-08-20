# AWS CDK v2のワーク
## CDK v2 を使用し、Lamnada関数と統合した API Gateway の REST API を作成する

### このワークの環境はワーク実施時のみご利用可能です。
---
* インストラクターの案内に基づき環境にマネジメントコンソールにサインインしてください。
* 東京リージョンを使用します。
* Cloud9 のページを開いて下さい。

---

## 手順

1. Cloud9のターミナルを開きます。

2. デモ用のフォルダを作成して異動します。

```
mkdir aws-cdkv2-demo
cd  aws-cdkv2-demo
```

3. CDKのバージョンを確認します。

```
cdk --version
```

4. CDKのリソースを作成します。デモではTypeScriptを使用します。

```
cdk init app --language typescript
```

5. デプロイするPythonのLambda関数を作成します。このデモでは、srcディレクトリにindex.pyとして作成します。

```
(このフォルダのindex.pyの内容を参照してください。)
```

6. bin/aws-cdkv2-demo.ts を開いて、6行目の `AwsCdkv2DemoStack` を `AwsCdkv2DemoStack99` のように末尾に自分の2桁の番号を追記して保存します。


7. lib/aws-cdkv2-demo-stack.ts を開いて、Lambda関数とAPI GatewayのAPIをデプロイするコードを追記します。

```
(このフォルダのaws-cdkv2-demo-stack.tsの内容に置き換え、13行目の functionName の末尾に自分の2桁の番号を追記して保存します。)
```


8. CloudFormation テンプレートに変換した場合のコードを確認します。

```
cdk synth
```

9. CDKを使ってスタックを作成します。確認の応答を求められた場合、`y` を入力します。
(初回の場合は、先にcdk bootstrap を実行して CDKが使用するS3バケットを作成しますが今回は不要です。)

```
cdk deploy
```

10. マネジメントコンソールで CloudFormation のページを表示し、スタックのステータスが CREATE_COMPLETE になっていることを確認します。
    - 出力タブを選択して、**apiEndpointXXX** の値の最後に `/hello` をつけた URL をブラウザアクセスし、Hello World！ と表示されることを確認します。


11. 作成したスタックを削除する場合は下記を実行します。確認の応答を求められた場合、`y` を入力します。

```
cdk destroy
```
---

## お疲れ様でした！
### このワークの環境はワーク実施時のみご利用可能です。




