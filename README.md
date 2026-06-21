# Daily News

日付ごとの最新のニュースを自動で収集・保存するリポジトリです。

## 概要

GitHub Actions が毎日 UTC 06:00 に実行され、主要な RSS フィードから最新ニュースを取得して `news/YYYY-MM-DD.json` として保存します。

## ディレクトリ構造

```
Daily-news/
├── news/               # 日付ごとの JSON ニュースファイル
│   └── YYYY-MM-DD.json
├── scripts/
│   └── fetch_news.py   # ニュース取得スクリプト
└── .github/
    └── workflows/
        └── daily_news.yml  # 自動実行ワークフロー
```

## ニュースソース

| ソース | URL |
|--------|-----|
| Reuters Top News | https://feeds.reuters.com/reuters/topNews |
| BBC News | https://feeds.bbci.co.uk/news/rss.xml |
| NHK World (English) | https://www3.nhk.or.jp/rss/news/cat0.xml |

## JSON フォーマット

```json
{
  "date": "2026-03-23",
  "fetched_at": "2026-03-23T06:00:00Z",
  "total": 42,
  "articles": [
    {
      "title": "Article title",
      "url": "https://example.com/article",
      "description": "Article description",
      "published_at": "Mon, 23 Mar 2026 05:30:00 +0000",
      "source": "Reuters Top News"
    }
  ]
}
```

## 手動実行

GitHub Actions の **workflow_dispatch** を使って任意の日付で実行できます。

1. [Actions タブ](../../actions/workflows/daily_news.yml) を開く
2. **Run workflow** をクリック
3. 任意で `date` に `YYYY-MM-DD` 形式の日付を入力して実行

## ローカル実行

```bash
# 今日のニュースを取得
python scripts/fetch_news.py

# 特定の日付を指定して取得
python scripts/fetch_news.py --date 2026-03-23
```

Python 3.12+ が必要です。外部ライブラリは不要です（標準ライブラリのみ使用）。