
# このリポジトリについて 
Microsoft Sentinelのリポジトリからルールリストのファイルを生成するツール群です。
ツール名はsrl(Sentinel rule lister))です。

# 出力例
ルールリストのファイルはresultsディレクトリの中に生成されます。ファイル名のフォーマットは「yyyy-mm-dd_HHMMSS.log」です。ファイルの中身はカンマ区切りCSV形式です。

以下が中身のサンプルです。
```
"ruleName","severity","version","kind","filePath"
"Lookout - New Threat events found.","High","1.0.0","Scheduled","Azure-Sentinel/Solutions/Lookout/Analytic Rules/LookoutThreatEvent.yaml"
"User Sign in from different countries","Medium","1.0.1","Scheduled","Azure-Sentinel/Solutions/Salesforce Service Cloud/Analytic Rules/Salesforce-SigninsMultipleCountries.yaml"
"Brute force attack against user credentials","Medium","1.0.1","Scheduled","Azure-Sentinel/Solutions/Salesforce Service Cloud/Analytic Rules/Salesforce-BruteForce.yaml"
"Potential Password Spray Attack","Medium","1.0.1","Scheduled","Azure-Sentinel/Solutions/Salesforce Service Cloud/Analytic Rules/Salesforce-PasswordSpray.yaml"
"Failed Logins from Unknown or Invalid User","Medium","1.0.1","Scheduled","Azure-Sentinel/Solutions/Okta Single Sign-On/Analytic Rules/FailedLoginsFromUnknownOrInvalidUser.yaml"
"User Login from Different Countries within 3 hours","High","1.0.1","Scheduled","Azure-Sentinel/Solutions/Okta Single Sign-On/Analytic Rules/LoginfromUsersfromDifferentCountrieswithin3hours.yaml"
"Potential Password Spray Attack","Medium","1.0.1","Scheduled","Azure-Sentinel/Solutions/Okta Single Sign-On/Analytic Rules/PasswordSpray.yaml"
"AIShield - Image classification model theft vulnerability detection","High","1.0.1","SingleAlert","Azure-Sentinel/Solutions/AIShield AI Security Monitoring/Analytic Rules/ImageClassficationModelTheftVulnDetection.yaml"

```

# 使い方
1. このリポジトリのルートディレクトリに[Azure-Sentinelリポジトリ](https://github.com/Azure/Azure-Sentinel)をクローンします。
2. slr.pyを実行する。

# オプション
```
usage: srl.py [-h] [-s SEVERITY] [-k KIND] [-v]

Generate sigma file path for Azure Sentinel Repository. Build by Python 3.10.9.

optional arguments:
  -h, --help            show this help message and exit
  -s SEVERITY, --severity SEVERITY
                        Specify for rule severity. default is All, severity of High, Medium, Low, Informational
  -k KIND, --kind KIND  Specify for rule kind. default is Scheduled, kind of Scheduled, ...
  -v, --verbose         Output debug level messages.
```

# ツール群の説明
|ファイル|説明|
|--|--|
|srl.py|メインプログラム|
|modules/sigmafiles.py|Sentinelのリポジトリデータからリストデータを生成する|
|results/yyyy-mm-dd_HHMMSS.log|生成されたルールリスト|
