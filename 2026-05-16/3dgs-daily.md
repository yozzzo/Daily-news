# 3DGS & 4D生成 デイリーレポート | 2026年5月16日

## サマリー
本日は重複排除後、新規10件（論文2件・ニュース5件・コミュニティ3件）を収集。

## 注目トレンド（本日のハイライト）
1. **3DGSが「物理的に正しい形」へ進化（PG-3DGS）** — 見た目だけでなく物理機能も最適化
2. **拡散モデルで4DGS生成が実用化へ（Splat4D / SIGGRAPH 2026）** — 単眼動画から高品質4DGS
3. **明日 Geo Week 2026 でGSが主役（建設・GIS分野）** — AEC業界での本格採用
4. **SolidWorksにGS統合（製造CADへの浸透）** — Veesus Arena4D経由
5. **GSゲームがブラウザで動作・HackerNews話題** — ゲーム×GSの新たな可能性

---

## 論文

### 1. PG-3DGS: 物理目標を満たす3DGS最適化
- **分野**: 物理シミュレーション × 3DGS
- **重要度**: 🔴 高
- **ソース**: arxiv:2605.11266 (2026年5月11日投稿)
- **URL**: https://arxiv.org/abs/2605.11266
- **著者**: Purdue大学研究チーム

**概要**  
3DGSで生成した形状を、視覚的品質だけでなく物理的機能も満たすよう最適化できるフレームワーク。物理シミュレーター（流体・空力計算）の勾配を3DGSのガウシアンパラメータに直接フィードバックする微分可能結合により、「本当に注げるティーポット」「揚力を生む翼」など現実で機能する形状を生成可能。従来の3DGSは視覚再現に特化しており、物理的な動作を考慮しなかった課題を解決。

---

### 2. Splat4D: 拡散モデルによる時空間一貫4DGS生成
- **分野**: 4DGS生成 · 拡散モデル
- **重要度**: 🔴 高
- **ソース**: arxiv:2508.07557 | SIGGRAPH 2026採択 / ACM TOG掲載
- **URL**: https://arxiv.org/abs/2508.07557
- **プロジェクトページ**: https://visual-ai.github.io/splat4d/

**概要**  
単眼動画から高品質な4DGS（時間変化する3Dシーン）を自動生成するフレームワーク。Video拡散モデルと非対称U-Netによりマルチビュー画像列を生成・精緻化し、時空間の一貫性を保つ。テキスト/画像条件付け・4D人物生成・テキスト誘導編集にも対応。単眼動画1本から動く3Dコンテンツを生成できる実用的な手法として注目。

---

## 業界ニュース

### 3. Geo Week 2026 Gaussian Splatting特集セッション（5/17開催）
- **分野**: AEC・GIS・業界イベント
- **重要度**: 🟡 中
- **URL**: https://radiancefields.com/gaussian-splatting-at-geo-week-2026
- **URL2**: https://www.geo-week.com/session/ai-gaussian-splatting-and-what-comes-next/

**概要**  
建設・測量・GIS分野最大の会議「Geo Week 2026」でGSをテーマとした2セッションが開催。午前セッション (11:00–12:30) ではNVIDIA・XGRIDS・Esri・Cesium・Skenderが登壇し建設・マッピング・シミュレーションでのGS実用事例を発表。午後セッション (16:30–17:30) では「AI・GS・その次は何か」をテーマに空間データ処理の未来を議論。AEC産業でGSが本格採用されていることを示す重要イベント。

---

### 4. Esri Site Scan for ArcGIS May 2026 — クラウドGS生成機能追加
- **分野**: 測量・GIS・ドローン
- **重要度**: 🟡 中
- **URL**: https://radiancefields.com/gaussian-splatting-at-geo-week-2026

**概要**  
GIS最大手EsriのドローンデータAPI「Site Scan for ArcGIS」の2026年5月版でクラウド上でのGS生成が可能に。1ミッションあたり最大1万枚の画像処理に対応するよう上限が引き上げられた。大規模建設・土木・インフラ現場をドローン撮影してクラウドで自動3DGS化できる実用ツールの大幅強化。

---

### 5. Esri ArcGIS Reality for ArcGIS Pro May 2026 — GSフィデリティ向上
- **分野**: 測量・フォトグラメトリ・GIS
- **URL**: https://www.esri.com/arcgis-blog/products/arcgis-pro/3d-gis/how-to-create-the-best-gaussian-splats-in-arcgis-reality

**概要**  
ArcGIS Proのフォトグラメトリ処理モジュール「ArcGIS Reality」の5月アップデートでGS品質（フィデリティ）が向上。測量・都市計画・デジタルツインへのGS統合がさらに高精度になった。EsriがGS機能を継続強化しており、GISプロフェッショナルがGSを実務で活用する基盤が整いつつある。

---

### 6. Veesus Arena4D × SolidWorks — 製造CADにGS統合
- **分野**: 製造業・CAD・デジタルツイン
- **重要度**: 🟡 中
- **URL**: https://www.veesus.com/

**概要**  
製造業向けCADの最大手SolidWorksでGaussian Splatsの表示・活用が可能に（Veesus Arena4D経由）。現実の工場・設備を3DGSでスキャンしCAD設計データと同環境で確認・比較できる。製造業・建設業での「デジタルツイン × GS」活用が一般設計ツールに降りてきた重要なマイルストーン。

---

### 7. SuperSplat 新機能: ダウンロード可能Splats・ライセンス・ソーシャルリンク
- **分野**: GS編集ツール・プラットフォーム
- **URL**: https://blog.playcanvas.com/new-in-supersplat-downloadable-splats-licenses-and-social-links/

**概要**  
PlayCanvasのGS編集ツールSuperSplatに新機能追加。公開したSplatsのダウンロード許可、Creative Commons 4.0の6種からライセンス設定、プロフィールへのX・LinkedIn・YouTubeなどソーシャルリンク追加に対応。GSコンテンツの共有・流通エコシステムが整備されてきている。

---

## コミュニティ・SNS話題

### 8. Plattipus houdini-gsplat — Houdini 21 SolarisでGS USDスキーマOSS公開
- **分野**: VFXツール・Houdini・USD
- **重要度**: 🟡 中
- **URL**: https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921
- **URL2**: https://www.sidefx.com/forum/topic/103786/

**概要**  
OpenUSD v26.03で正式化された`ParticleField3DGaussianSplat`スキーマをHoudini 21 SolarisでサポートするOSSプラグイン。カスタムHydraデリゲート・UsdImaging Adapter・3つのLOPノード（PLY Import / Gsplat Instancer / Uruk）を提供。VFXスタジオのGSパイプライン統合を大幅に簡素化する。

---

### 9. GSブラウザFPSゲームがHackerNews・Tom's Hardwareで話題
- **分野**: ゲーム開発・コミュニティ
- **重要度**: 🟡 中
- **URL1**: https://www.tomshardware.com/software/programming/developer-creates-a-basic-first-person-shooter-game-using-gaussian-splats-and-you-can-play-it-for-free-in-your-browser
- **URL2**: https://tech.yahoo.com/gaming/articles/gaussian-splatting-could-bring-future-150000571.html
- **URL3**: https://news.ycombinator.com/item?id=47876071

**概要**  
Snap社エンジニアによるGSを使ったFPSゲームがブラウザで動作し、Tom's Hardware・Yahoo Tech・HackerNewsなど多数のメディアで注目を集めている。現実の場所をGSでスキャンしてゲームステージとして使用、ダウンロード不要でブラウザから体験可能。GS×ゲーム開発の可能性を示す注目事例。

---

### 10. Geo Week 2026 Reality Capture Network レポート公開
- **分野**: 業界レポート・AEC
- **URL**: https://www.geoweeknews.com/news/reality-capture-network-at-geo-week-2026-a-focus-on-integration-precision-and-enduring-data-value

**概要**  
Geo Week 2026に向けてReality Capture Networkが産業界でのGS活用状況をまとめたレポートを公開。「統合・精度・データの長期的価値」の3テーマでGSの現状と展望が整理されている。

---

## 開発者向けインサイト

### 今すぐ試せるもの
| ツール | 用途 | URL |
|--------|------|-----|
| Plattipus houdini-gsplat | HoudiniパイプラインへのGS統合 (OSS) | https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921 |
| Esri Site Scan for ArcGIS | ドローンデータからのクラウドGS生成 | https://radiancefields.com/gaussian-splatting-at-geo-week-2026 |
| Splat4D | 単眼動画からの4DGS生成 (SIGGRAPH 2026) | https://visual-ai.github.io/splat4d/ |

### 対応すべきトレンド
- **産業用ソフトへのGS統合加速**: SolidWorks (Veesus)、ArcGIS (Esri)、Houdini (houdini-gsplat) と専門ソフトへの統合が相次ぐ
- **GS × 物理シミュレーション**: 「見た目再現」から「物理機能最適化」へGSの用途が拡大
- **Geo Week 2026 (5/17)**: AEC・GIS業界での本格採用状況をリアルタイムウォッチ推奨
- **GSゲームのブラウザ普及**: ゲーム×GSの新たな入口としてブラウザゲームが有効

---
*このレポートはyozzzo/Daily-newsプロジェクトの一部として自動生成されました。*
