# 大会動画サムネイル作成ツール

## 注意
このツールは容量のほとんどがファイター画像に割かれているので，容量を減らしたい場合は`setting/fighter_image`のうち必要なキャラクターの画像のみダウンロードしてください．

おかしなところがあったら[製作者のTwitter](https://twitter.com/Sycama_ssb)までどんどん指摘してください！

# 必要なもの
- Pythonの環境
- Pythonライブラリの”pillow”, ”matplotlib”
- 使用したい背景画像
- 使用したい大会アイコン

# 使い方
`make_thumbnail.py`に色々と書いて実行するだけ．


# 各フォルダ・ファイルの説明

- `fixing`

基本的にいじらない場所.  
全ファイター画像とマスク画像が入っています．  
詳しくは後述しますが，ファイター名の略称をいじりたい場合は`fixing/fighter_image`フォルダのフォルダ名をいじってください．

- `make_thumbnail.py`

使用するPythonコード．

# `make_thmbnail.py`の設定項目

## プレイヤー・ラウンド・その他情報

表示させる文字が長すぎると，改行ができない関係上物凄く小さくなってしまうので注意．

- `P1_name`  

プレイヤー1の名前を記入（サムネイル左上に書きたい内容を記入）．

- `P1_fighter`  

表示させたいファイターの英語名を入力（例外あり，後述します）．  
最大で3ファイターまで入力可能.  
使用しない欄は空欄にしてください．  

>例: マリオのみ表示する場合  
>`P1_fighter = ['mario', ,]`

- `P1_color`

表示させるファイターのカラーを1-8の数字で指定．  
`P1_fighter`に書いたファイターの位置と対応させてください．こちらも`P1_fighter`同様使用しない欄は空欄にしてください．

P2についてはP1と同様なので省略

- `Round`

大会のラウンド（GRAND FINALSとか）など，サムネイル左下に表示させたい項目を書く場所．  

- `Rules`

ルール（スマブラSP シングルスとか）や大会名（とんスマ！ #2とか）など，サムネイル右下に表示させたい項目を書く場所．  
>YouTubeはサムネイル右下に再生時間が表示されるため，ここに書かれた項目は基本的には読まれにくい．大会名は`Round`に書いても良いかも．

## 変更が必要な項目

- `opt_img_path`

背景画像のパスを入力．  
>例：`./background.png`

- `icon_path`

大会アイコンのパスを入力．  
>例：`./icon.png`

- `opt_img_name`

生成された画像の保存場所パスと保存名を入力．  
`.png`などは入力しないでください．  
空のフォルダを作成して，その場所を指定するといいです．
>例：フォルダ"save_image"に"image"という名前で保存する場合
`./save_image/image`

- `opt_font_path`
- `vs_font_path`

使用する文字のフォントのパスを入力．Macユーザーは多分変更しなくても大丈夫です.  
下は中央に表示される「VS」の文字のフォントです．他の文字より太めにした方が良さげだから分けてあるだけなので同じでも大丈夫です．

- `bg_color`

上下の文字が書かれる欄の背景色．  
RGBA（赤，緑，青，透明度）で指定してください．

- `fg_color`

上下の文字色  
カラーコードやRGBなどで指定してください．

- `vs_c`

「VS」の文字色
カラーコードやRGBなどで指定してください．

以下は「VS」の縁取り設定です．  
それほどうまく縁取りできないので基本的には使用をおすすめしません．

- `border `

縁取りを利用したいときは，`False`を`True`に変更してください

- `vs_b`

縁取りの色  
カラーコードやRGBなどで指定してください．

- `bw`

縁取り幅．

# 基本的に変更しなくて良い項目

- `rate`

大会アイコンの高さを変更（縦横比は保持されます）．  
アイコンが縦長であったり，キャラに被りすぎててウザいと感じたときは変更するといいです（0以上1以下の値にしてください）．

- `vs`

中央の「VS」と表示される場所に書きたい文字を入力．

- `opt_max_font_size`

フォントサイズの最大値．

- `opt_img_name_num`

同名の画像を生成したときに，上書きされないように後ろに付けるインデックスの最初の値．

この項目より下の部分は変更しないでください．

# ファイター名の例外

`P1_fighter`の欄に書くファイター名は，基本的にはファイターの英語名を記入しますが，都合により一部ファイターは書き方が変わっています．  
基本的には2単語以上の名前のファイターが対象です．

書き方を変更したい場合は`fixing/fighter_image`から変更したいファイターのフォルダ名を変更することにより変更できます．

以下，例外のファイターのみ書き方を表示します．

>ドンキーコング - dk  
ダークサムス - damus  
ピカチュウ - pika  
キャプテン・ファルコン - cf  
プリン - puff  
アイスクライマー - ic  
ドクターマリオ - doc  
こどもリンク - yl  
ガノンドロフ - ganon  
ミュウツー - m2  
Mr. ゲーム&ウォッチ - gw  
メタナイト - mk  
ブラックピット - dp  
ゼロスーツサムス - zss  
ポケモントレーナー - pt  
ディディーコング - ddk  
デデデ - d3  
ピクミン&オリマー - oli  
ロボット - rob  
トゥーンリンク - tl  
むらびと - villy  
ロックマン - mm  
Wii Fit トレーナー - wft  
ロゼッタ&チコ - rosa  
リトル・マック - mac  
パルテナ - palu  
パックマン - pac  
クッパ Jr. - bj  
ダックハント - dh  
ベヨネッタ - bayo  
キングクルール - kkr  
パックンフラワー - pp  
バンジョー&カズーイ - bk  
Mii ファイター - mii  

Miiは`P1_color`により格闘/剣術/射撃を変更できます  
1：格闘顔あり，2：格闘顔なし，3：剣術顔あり，4：剣術顔なし，5：射撃顔あり，6：射撃顔なし

# Licence

Copyright (c) 2020 Sycama  
Released under the [MIT](https://opensource.org/licenses/mit-license.php) license


# Author

Sycama  
Twitter: [@Sycama_ssb](https://twitter.com/Sycama_ssb)