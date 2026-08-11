# みんなのPython勉強会 スタッフ作業 手順書

みんなのPython勉強会（stapy）のスタッフ作業を、他のスタッフ・コーディングエージェントに依頼するための手順書です。

## 入力（依頼者が用意するもの）

以下の4点を依頼時に提示してください。

| # | 項目 | 例 |
|---|---|---|
| 1 | connpassイベントURL | `https://startpython.connpass.com/event/374561/` |
| 2 | Zoom URL | `https://us02web.zoom.us/j/...` |
| 3 | Slido URL | `https://app.sli.do/event/...` |
| 4 | Googleフォーム URL（アンケート） | `https://docs.google.com/forms/d/e/.../viewform` |

> イベント回数 **N**（例：121）は、connpassイベントURLをブラウザで開き、イベントタイトル（例：「みんなのPython勉強会#121」）に含まれる `#` の後の数字から確認してください。

> **作業の順序**：作業1（短縮URL準備）が先、作業2（メッセージ送信予約）はその後。作業2のメッセージ本文には作業1で作成する `bit.ly/stapy{N}xxx` 形式のURLが含まれているため、**作業1を完了させずに作業2を実施するとリンク切れになります**。

## 前提

- リポジトリのルート（`meetup-host-ops/`）で作業すること
- Python処理系が利用できること（`bitly.py` は標準ライブラリのみで動作するため、追加のパッケージインストールは不要）
- 1Password CLI（`op` コマンド）が利用できること。bitly APIアクセストークンは 1Password に保管されており、リポジトリルートの `.env`（1Passwordへの参照を記述したファイル）と `op run --env-file .env` で環境変数 `BITLY_ACCESS_TOKEN` を実行時に注入します。`op run` 実行時にデスクトップアプリの生体認証が走るため、事前の `op signin` は不要です

## 作業1. 短縮URLを3つ準備し、connpass掲載を確認する

### 1-1. `bitly.py` で短縮URLを3つ作成する

以下の3つの短縮URLを作成します。

| 短縮URL（カスタムスラッグ） | 元URL |
|---|---|
| `bit.ly/stapy{N}zoom` | Zoom URL |
| `bit.ly/stapy{N}slido` | Slido URL |
| `bit.ly/stapy{N}form` | Googleフォーム URL |

`{N}` はconnpassページで確認したイベント回数（例：121）に置き換えてください。

#### 実行コマンド

リポジトリのルートで、以下を3回実行します（`{N}` は実際の数値に置換）。

```bash
op run --env-file .env -- python3 bitly.py "<Zoom URL>"            "stapy{N}zoom"
op run --env-file .env -- python3 bitly.py "<Slido URL>"           "stapy{N}slido"
op run --env-file .env -- python3 bitly.py "<Googleフォーム URL>"  "stapy{N}form"
```

例（N=121）：

```bash
op run --env-file .env -- python3 bitly.py "https://us02web.zoom.us/j/..."                  "stapy121zoom"
op run --env-file .env -- python3 bitly.py "https://app.sli.do/event/..."                   "stapy121slido"
op run --env-file .env -- python3 bitly.py "https://docs.google.com/forms/d/e/.../viewform" "stapy121form"
```

各コマンドの実行で `Created: http://bit.ly/stapy{N}xxx` が表示されれば成功です（`http` で表示されますが bit.ly 側で `https` にリダイレクトされるため、テンプレートの `https://bit.ly/...` のままで問題ありません）。

#### 確認

3つの短縮URLにアクセスし、それぞれ正しい遷移先（Zoom / Slido / Googleフォーム）に飛ぶことを確認してください。手段は問いません：

- ブラウザで開いて目視確認
- ブラウザMCP（Claude in Chrome 等）で `navigate` し、リダイレクト先ドメインを確認
- `curl -sI <短縮URL>` で `location:` ヘッダの遷移先を確認

### 1-2. connpassイベントの「参加者への情報」欄を確認する

connpassイベントは前回イベントから複製して作成されているため、「参加者への情報」欄には既に `bit.ly/stapy{N}xxx` 形式の短縮URLテンプレートが入っていることが多いです。短縮URLのスラッグは予測可能（作業1-1で作成するURLと一致）なので、**N が今回の回数に置換済みであれば、新たな掲載作業は不要です**。

connpassイベントページの編集画面で、以下を確認してください：

- [ ] 3つの短縮URL（`stapy{N}zoom` / `stapy{N}slido` / `stapy{N}form`）が今回の N に置換済み
- [ ] 順序・フォーマットが下記の標準フォーマットと一致

未掲載・誤りがあった場合のみ、以下の標準フォーマットで掲載/修正してください（参加者と発表者にのみ公開されます）。

```
【イベント配信URL】

[Zoom]
https://bit.ly/stapy{N}zoom

【発表者への質問】

https://bit.ly/stapy{N}slido
(Slido.com #stapy{N})

【勉強会感想のアンケート】

https://bit.ly/stapy{N}form
```

> 参考イメージ（N=121）：
> ```
> 【イベント配信URL】
> [Zoom]
> https://bit.ly/stapy121zoom
>
> 【発表者への質問】
> https://bit.ly/stapy121slido
> (Slido.com #stapy121)
>
> 【勉強会感想のアンケート】
> https://bit.ly/stapy121form
> ```

確認/修正後、connpassのイベントページ（参加者として閲覧する画面）で「参加者への情報」が正しく表示されることを確認してください。

## 作業2. connpassのメッセージを送信予約する

> **前提**：作業1（短縮URLの作成 + connpass掲載の確認）が完了していること。作業2のメッセージ本文には `https://bit.ly/stapy{N}zoom` などの短縮URLが含まれているため、作業1未完了だとリンク切れになります。

作業1で作成した短縮URLを使って、connpassからメッセージを4通送信予約します。

### 手順

1. connpassイベントURLをブラウザで開く
2. リポジトリの [`connpass/message-reservation.md`](./connpass/message-reservation.md) に従って4通分の予約を行う

### `connpass/message-reservation.md` で必要となるテンプレート変数

すべてconnpassイベントページから確認できます。

| 変数 | 値の決め方 |
|---|---|
| `{{回数}}` | connpassのイベントタイトルに含まれる数字（例：121） |
| `{{connpassイベントID}}` | connpass URL の `event/<ID>/` 部分（例：`374561`） |
| `{{開催日}}` | connpassイベントページの開催日（例：2024/12/12） |
| `{{アンケート回答期限}}` | 開催日の **次の月曜日**（例：開催日が12/12（木）なら `12/16（月）`） |

### 送信予約する4通

`connpass/message-reservation.md` 記載のとおり：

| # | メッセージ | 送信予約日時 |
|---|---|---|
| 1 | 配信URLの案内 | 前日 18:00 |
| 2 | 配信URLの案内 | 当日 17:30 |
| 3 | アンケート依頼 | 当日 21:00 |
| 4 | アンケート依頼（リマインダー） | 翌日 11:30 |

### 注意事項

- 宛先は「補欠者」のチェックを外す（「共同管理者」「発表者」「参加者」はチェックしたまま）
- 各メッセージの本文・件名は `connpass/message-reservation.md` のテンプレートをそのままコピーして変数を置換する

### 「即時送信/予約」ボタンを押す判断について

ボタン名に「即時送信」と入っていますが、**connpassの仕様上、送信予約日時が入力されていれば予約として登録され、その場では送信されません**（画面上の注記：「※送信予約日時が設定されていない場合、即時送信されます」）。即時送信されるのは**送信予約日時が空欄のときだけ**です。

また、**予約は後から取り消せます**。予約タブから該当メッセージを開くと「下書きに戻す」ボタンがあり、「※メッセージを編集したい場合は、下書きに戻してから編集してください。」と案内されています。つまり予約は不可逆な操作ではなく、間違えても送信予定時刻より前なら下書きに戻して修正できます。

したがって、依頼を受けた作業者（コーディングエージェントを含む）は、**送信予約日時が未来の日時で入力されていることを確認できたら、依頼者に都度確認を取らずにボタンを押して構いません**。この手順書に沿った作業依頼をもって、4通分の送信予約は承認済みとして扱ってください。

押す前に満たすべき条件は次の3点だけです。すべて画面上で確認できます。

- [ ] 送信予約日時の**日付と時間の両方**が入力されている（どちらか片方でも空欄なら即時送信になるため押さない）
- [ ] その日時が**未来**である
- [ ] 宛先の「補欠者」のチェックが外れている

いずれかを満たせない場合は、ボタンを押さずに依頼者に確認してください。

## 完了報告

依頼者に以下を報告してください：

- [ ] 作業1-1：3つの短縮URL（`bit.ly/stapy{N}zoom`, `bit.ly/stapy{N}slido`, `bit.ly/stapy{N}form`）を作成し、遷移先を確認した
- [ ] 作業1-2：connpassイベントの「参加者への情報」欄に3つの短縮URLが掲載されていることを確認した（未掲載・誤りがあれば修正済み）
- [ ] 作業2：connpassで4通のメッセージを送信予約した（前日18:00 / 当日17:30 / 当日21:00 / 翌日11:30）
