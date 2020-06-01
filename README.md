# Visual Studio Codespaces / TypeScript 開発ハンズオン :computer:
ハンズオンに最後まで参加していただいた方に、プレゼント:green_book:があります！

みんなで楽しく助け合いながらゴールをめざしましょう！

## 本日のゴール

- Type Script の役割を理解し、Visual Studio Codespaces で開発ができるようになること
- Visual Studio Codespaces で Type Script でサーバアプリケーションをコンパイル、デバッグができること
- Visual Studio Codespaces で Type Script で Web フロントエンドのアプリケーションをコンパイルできること

![vscodespaces](https://visualstudio.microsoft.com/wp-content/uploads/2020/05/create-cs.png)

## 解説すること

- Type Script とは何をするコンパイラであるか
- Visual Studio Codespaces で Node.js 上で動作する Type Script の開発環境の構築方法、開発方法、デバッグ方法
- Visual Studio Codespacesで Chrome 上で動作する Type Script の開発環境の構築方法、開発方法方法

## 解説しないこと

- Node.js 、 npm のインストール方法、及び使い方（コマンドで紹介します）
- Vue.js の使い方（完成品ソースコードを提供します）
- Visual Studio Codespaces の利用開始方法（[公式ドキュメント](https://docs.microsoft.com/ja-jp/visualstudio/online/quickstarts/browser)を参照下さい）


## 準備が必要なもの

- Windows、もしくは MacOS の開発用 PC（Linux は Zoom が正常に動作しないため不可、クライアントは Windows/MacOS でリモート開発機能で Linxu の SSH 接続先環境を用意している、リモートコンテナ機能の使用は可）
- Windows の場合、[Git のインストール](https://gitforwindows.org/)
- [VS Code Meetup Slack への参加(こちらのページに案内リンクがあります)](https://vscode.connpass.com/)
- [Zoom クライアントのインストール](https://zoom.us/download)、及び音声、画面共有のテスト
- [Visual Studio Code のインストール](https://code.visualstudio.com/download)
- [Node.js のインストール](https://nodejs.org/ja/)


### ※ VSCode で準備が必要なもの

以下の拡張機能を、事前にインストールして下さい

- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)
  - 事前に、"Start collaboration session..." をクリックし、Microsoft アカウント、Github アカウントとリンクさせておいて下さい


## みなさまにご協力いただきたいこと :pray:

- このハンズオンは有志の実験的取り組みです。至らない点など多数あるかと思いますが、参加者同士でコミュニケーションをとっていただき、一緒に解決できればと思います。
- Live Share を使ってのハンズオンなど、主催者としても初めての取り組みを行っています。ご不便をおかけする点も多いと思いますが、ご協力いただければと思います。
- Live Share は、Share の仕方を誤ると、ターミナルを横取りできたり、ターミナルやプログラムを介して、個人の機密情報にアクセスすることができうるプロダクトです。自己責任の上、注意して使用して下さい。また、もしアクセス可能だとしても他人の情報にはアクセスしないようにして下さい。
- このハンズオンの内容には、書籍[Visual Studio Code 実践ガイド](https://gihyo.jp/book/2020/978-4-297-11201-1)の内容が含まれます。資料は用意するため、購入は必須はありませんが、購入を検討いただければ幸いです。


## アジェンダ:musical_keyboard:

### STEP0. [Codespacesを使ってみよう](docs/0.codespaces.md)
### STEP1. [Live Share 機能を使って、環境を公開してみよう](docs/1.liveshare.md)
### STEP2. [Type Script のプロジェクトをセットアップしよう](docs/2.unittest.md)
### STEP3. [Type Script の Node.js アプリケーションをデバッグしよう](docs/3.server.md)
### STEP4. [Type Script の Vue.js アプリケーションをセットアップしよう](docs/4.frontend.md)


## コミュニケーションのとり方:iphone:

- ハンズオン中は Zoom を繋ぎっぱなしにしてください。不明なところがあれば、サポートします！
- Live Share を活用しましょう！ Live Share で "Start collaboration session..." をクリックすると、クリップボードに Live Share のリンクが作成されます。これを Slack に共有して下さい。Live Share で実際のコードを見ながら聞きに行きます
