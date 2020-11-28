# フラグ、メッセージ管理ツール

このツールは所属するIT×謎解きプロジェクトで使用するためのツールです。<br>
当プロジェクトと関係のない方には需要のないツールであることご容赦ください。<br>
<br>
当プロジェクトにおけるFirebase Realtime Databaseのフラグ、メッセージの管理を簡単にするためのツールです。

## 利用方法

### 前提ツール

このツールは同プロジェクト所属のBroccolingual様の<br>
”Firebase Realtime Databaseをより簡単に利用するためのツール”<br>
を使用して作成されています。<br>
このツールの使用にあたり、下記URLよりこの前提ツールのダウンロードも行ってください。<br>
https://github.com/broccolingual/firebase

### 使用時のディレクトリ配置
```python
├main.py #メインの実行ファイル
├firebase.py # Broccolingual様の前提ツールの本体
├config.ini # Broccolingual様の前提ツールより引用(詳細は下記)
└hoge.json # Firebaseの認証用jsonファイル(詳細はBroccolingual様のページを参照してください)
```
#### config.iniの内容
```python
[firebase]
url = <your url>
```
＜your url＞には、使用するFirebase Realtime DatabaseのURLを入力して下さい。

### 実際の利用方法

ご使用のOSのCUIにて、main.pyを配置したディレクトリに移動し、
```python
python main.py
```
と、入力して下さい。<br>
以降、表示される指示に従って入力して下さい。

## 環境及び使用ライブラリ
python 3.8.5
<br>firebase-admin 4.4.0

## 前提ツール製作者
Broccolingual 様

## 製作者
syuumy5050
<br>Gmail: osamigaki3856@gmail.com