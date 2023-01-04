
# このリポジトリについて 
Microsoft Sentinelのリポジトリからルールリストのファイルを生成するツール群です。

# 出力例
ルールリストのファイルはresultsディレクトリの中に生成されます。ファイル名のフォーマットは「yyyy-mm-dd_HHMMSS.log」です。ファイルの中身はセミコロン区切りCSV形式です。

以下が中身のサンプルです。
```
severity;ruleName;kind;version;sigmaFile
Medium;Unusual Anomaly;Scheduled;1.0.1;Azure-Sentinel/Detections/Anomalies/UnusualAnomaly.yaml
Medium;Brute force attack against user credentials (Uses Authentication Normalization);Scheduled;1.2.2;Azure-Sentinel/Detections/ASimAuthentication/imAuthBruteForce.yaml
Medium;Potential Password Spray Attack (Uses Authentication Normalization);Scheduled;1.1.2;Azure-Sentinel/Detections/ASimAuthentication/imAuthPasswordSpray.yaml
High;User login from different countries within 3 hours (Uses Authentication Normalization);Scheduled;1.2.2;Azure-Sentinel/Detections/ASimAuthentication/imAuthSigninsMultipleCountries.yaml
Medium;Sign-ins from IPs that attempt sign-ins to disabled accounts (Uses Authentication Normalization);Scheduled;1.0.2;Azure-Sentinel/Detections/ASimAuthentication/imSigninAttemptsByIPviaDisabledAccounts.yaml
Medium;(Preview) TI map Domain entity to Dns Events (ASIM DNS Schema);Scheduled;1.1.2;Azure-Sentinel/Detections/ASimDNS/imDns_DomainEntity_DnsEvents.yaml
Medium;Excessive NXDOMAIN DNS Queries (ASIM DNS Schema);Scheduled;1.3.3;Azure-Sentinel/Detections/ASimDNS/imDns_ExcessiveNXDOMAINDNSQueries.yaml
Medium;Potential DGA detected (ASIM DNS Schema);Scheduled;1.3.2;Azure-Sentinel/Detections/ASimDNS/imDns_HighNXDomainCount_detection.yaml
Low;DNS events related to mining pools (ASIM DNS Schema);Scheduled;1.3.1;Azure-Sentinel/Detections/ASimDNS/imDNS_Miners.yaml
```

# 使い方
1. このリポジトリのルートディレクトリに[Azure-Sentinelリポジトリ](https://github.com/Azure/Azure-Sentinel)をクローンします。
2. 「makeSigmaFiles.sh」をカスタマイズし、対象にするルールの重大度や種類を指定する（デフォルトはscheduled）。
3. main.pyを実行する。

# ツール群の説明
|ファイル|説明|
|--|--|
|main.py|メインプログラム。shファイルをラッピングしておりルールリストを生成する。|
|makeSigmaFiles.sh|指定された条件に基づきSigmaファイルのリストを生成する。|
|SigmaFiles.txt|Sigmaファイルのリスト。Azure-SentinelリポジトリのSigmaファイルパスが記載される。|
|results/yyyy-mm-dd_HHMMSS.log|生成されたルールリスト。|

# 動作保証環境
Linux上で動作させることを想定しています。基本的にBashおよびPython3がインストールされていれば動作すると思います。

```
[marseille@altair ~]$ uname -a
Linux altair 3.10.0-1127.el7.x86_64 #1 SMP Tue Mar 31 23:36:51 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
[marseille@altair ~]$ cat /etc/redhat-release
CentOS Linux release 7.9.2009 (Core)
[marseille@altair ~]$ python3 -V
Python 3.6.8
```