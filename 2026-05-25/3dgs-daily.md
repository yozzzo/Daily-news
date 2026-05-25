# 3DGS & 4D生成 デイリーレポート — 2026-05-25

> **新着12件** | 論文3件 / ニュース5件 / コミュニティ4件

---

## 今日の注目トレンド

1. **スケーリングの壁を突破** — TideGSが単一GPU（24GB VRAM）で10億以上のGaussianを学習可能に。従来の約1,100万限界を100倍突破。
2. **製造業・GISへの本格参入** — Esri（ArcGIS）がクラウドGS生成を提供開始、VeesusがSolidWorks内でGS可視化に対応。
3. **プロ向け新ハードウェア** — XGRIDS Lixel K2がRTK内蔵・3cm精度で6月発売。点群・メッシュ・3DGSを同時出力。
4. **Netflixドラマで3DGS活用** — 世界視聴率1位「ベルリンとエルミタージュの女性」がVolinga GS技術でバーチャルプロダクション採用。
5. **CVPR 2026 Denver直前** — 6/3〜7の開幕に向けてGS論文50件以上のコード公開ラッシュが続く。

---

## 🔬 注目論文（重要度：高）

### 1. TideGS：10億個のGaussianを1台のGPUで学習

- **arXiv**: https://arxiv.org/abs/2605.20150
- **プロジェクト**: https://sponge-lab.github.io/TideGS/
- **投稿日**: 2026-05-19
- **著者**: Chonghao Zhong, Linfeng Shi et al.

**何ができるようになったか：**  
これまで3DGSは「Gaussianの数が増えるほどGPUメモリが足りなくなる」という根本的な問題を抱えていました。標準的な手法では1台のGPUで約1,100万個（11M）が上限でしたが、TideGSはSSD・CPUメモリ・GPUメモリを賢く使い分ける「アウトオブコア最適化」によって、**10億個（1B）以上のGaussianを24GB VRAM 1台のGPUで学習可能**にしました。都市規模の超高精細なシーン再構成が、低コストなシングルGPU環境で実現できます。

**解決された課題：**  
従来のアウトオブコア手法（約1億個が限界）の10倍以上のスケールを達成。大規模シーン評価でも既存シングルGPUベースラインで最高の再構成品質を記録。

---

### 2. GS Transcoding：元の写真なしで既存3DモデルをGSに変換

- **arXiv**: https://arxiv.org/abs/2605.21051
- **投稿日**: 2026-05-20

**何ができるようになったか：**  
3DGSを作るには通常、何十枚もの写真から始める必要があります。この手法では**既存の3D点群やメッシュモデルがあれば、元の写真なしでGSモデルに変換**できるエンドツーエンドパイプラインを提案。「過去に作った3Dスキャンデータを最新のGS形式でリアルタイムレンダリングしたい」というニーズに直接応えます。

**解決された課題：**  
元撮影データが失われた・撮影条件の異なる既存アセットをGS化できなかった問題を解消。既存3Dアセットの活用範囲が大幅に拡大。

---

### 3. AIR：2D Gaussian Splattingの自己教師あり学習フレームワーク

- **arXiv**: https://arxiv.org/abs/2605.20820
- **投稿日**: 2026-05-20

**何ができるようになったか：**  
通常の3DGSは1シーンに対して何分もかけて最適化（fine-tuning）する必要があります。AIR（Amortized Image Reconstruction）は、この反復最適化をニューラルネットワーク1回のフォワードパスに「圧縮」し、**画像を見た瞬間にGaussianパラメータを推定**できるフレームワークです。

**解決された課題：**  
自己教師あり学習（ラベルなし大量データで学習）を2D GS分野に導入。ポーズ情報（カメラ位置データ）が不要で、初見シーンでも高速に処理できます。

---

## 📰 業界ニュース

### 4. Esri ArcGIS Reality Studio / Site Scan — 2026年5月アップデート

- **URL**: https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026

世界最大のGIS企業Esriが、ArcGIS Reality Studioの5月アップデートで3DGSを大幅強化。

- 薄い構造物・植生・高周波テクスチャの**GS再現精度を向上**
- クラウドで処理するGS生成ワークフローに対応（大型データセンター不要）
- Site Scan（ドローン測量向け）で**1ミッションあたり最大10,000枚の画像処理**が可能に

GIS・測量・建設業界での本格採用が加速します。

---

### 5. Veesus × SolidWorks — 製造業CADにGS視覚化が統合

- **URL**: https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update

点群・GS可視化プラットフォームVeesusが、5月アップデートでSolidWorksプラグインへのGS対応を追加。**エンジニアがCADソフト上でリアルな現場スキャンデータとGSを重ね合わせて確認**できるようになりました。同時にXGRIDS LCC2フォーマットのサポートも追加。レンズフレアと動的シャドウのGS対応も近日公開予定。

---

### 6. XGRIDS Lixel K2 + LixelStudio 4.0 — RTK内蔵の新型スキャナー発売（6月）

- **URL**: https://radiancefields.com/xgrids-announces-k2-camera
- **製品ページ**: https://www.xgrids.com/intl/lixelk2

XGRIDSが新型ハンドヘルド3Dスキャナー「Lixel K2」と処理ソフト「LixelStudio 4.0」を発表。

- **RTK（リアルタイムキネマティクス）を本体に内蔵**：水平・垂直3cm RMSE（リアルタイム）、ポスト処理後は1cm RMSE
- LiDAR＋カメラで**点群・メッシュ・3DGSを同時出力**
- 本体重量約1,200g
- 6月発売予定

建設・測量・文化財保存分野向けの測量精度GSキャプチャが現実的になります。

---

### 7. XGRIDS LCC Cloud — SLAM+3DGSクラウド処理が商用化

- **URL**: https://lcc-cloud.xgrids.com/

無料ベータだったXGRIDSのクラウドGS生成サービス「LCC Cloud」が正式商用化。

- **$800 USD / 年（月250分の処理時間付き）**
- 現場データをアップロードするだけでSLAM（3D地図生成）+ 3DGSモデルを自動生成
- オンプレミス環境不要

GSパイプラインをクラウドで持てる選択肢が増え、スモールチームでの導入障壁が下がりました。

---

### 8. Netflix「ベルリンとエルミタージュの女性」× Volinga — 世界1位ドラマで3DGS採用

- **Netflix**: https://www.netflix.com/title/82152349

Netflixドラマ「ベルリンとエルミタージュの女性（Berlin and the Lady with an Ermine）」のバーチャルプロダクション（スタジオLED背景撮影）に、**Volinga（GS専門スタジオ）のGaussian Splattingワークフローが採用**。マドリードの路地「カジェ・アルカラ」をGSで撮影し、スタジオのLEDウォールに投影する形で映像制作が行われました。本作は公開3日で世界視聴率1位を獲得。GS技術が商業映像制作の現場に本格浸透した象徴的な事例です。

---

## 💬 コミュニティ・SNS話題

### 9. 360 Splat Pro v1.2.5 — Insta360 Raw静止画（.insp）に対応

- **URL**: https://radiancefields.com/360-splat-pro-v1.2.5-gpu-friendly-alignment-and-insta360-raw-photo-support

360度カメラ専用GS処理ツール「360 Splat Pro」がv1.2.5をリリース。

- **Insta360のRAW静止画形式（.insp）に対応**：動画だけでなくスチル撮影でも同一パイプラインを利用可能に
- GPUフレンドリーなアライメント処理で高速・安定化
- QoocamデュアルフィッシュアイRAWのエッジケース処理を強化

---

### 10. Arrival Space 2026.2「Vibes」機能 — テキストプロンプトでシーンが動く

- **URL**: https://radiancefields.com/arrival-space-release-2026.2

GSプラットフォーム「Arrival Space」が2026.2をリリース。目玉機能「Vibes」はテキストプロンプトでシーン内の挙動（ライティング変化・オブジェクト動作など）をプログラムできるシステム。**「夕方の光に変えて」「このオブジェクトを揺らして」のような指示でシーンが変化する**仕組みです。GSスプラットが静的な記録物から「動くキャンバス」へと進化しつつあります。

---

### 11. Geofront × NHM Vienna — 70万スプラットでマリア・テレジアの宝石を修復

- **URL**: https://www.geofront.eu/

オーストリアのgeofront社がウィーン自然史博物館（NHM）の依頼で、18世紀の宝石工芸品「マリア・テレジアの宝石ブーケ」を**約70万個のGaussian Splatsで3D復元**。経年劣化で色が失われた葉の部分を、学芸員がデジタル空間上で修復・補完できるようになりました。文化財保存・博物館展示での3DGS活用が実務レベルで進んでいます。

---

### 12. CVPR 2026 Denver 直前 — GS論文50件超のコード公開ラッシュ

- **URL**: https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

世界最大のコンピュータビジョン学会**CVPR 2026が6月3日〜7日**（米コロラド州デンバー）で開幕直前。GS関連採択論文は50件以上。FastGS（100秒で学習）・EDGS（高速化）・Mobile-GS（モバイルGS、ICLR 2026採択）などのコードが続々GitHubに公開中。開幕前後の2週間が最もコードが集中する時期です。

---

## 🛠 開発者向けインサイト

| 項目 | 優先度 | アクション |
|------|--------|------------|
| TideGS（arXiv:2605.20150） | ★★★ | 24GB GPU 1台で10億Gaussian学習。コード公開後すぐに確認 |
| GS Transcoding（arXiv:2605.21051） | ★★★ | 既存3DアセットのGS化に。EA Mesh2Splatと組み合わせると強力 |
| CVPR 2026コード公開（6/3〜） | ★★★ | Awesome3DGS GitHubをWatchして論文コードを追跡 |
| Esri ArcGIS Reality + Site Scan | ★★☆ | GIS業界向けのフルクラウドGSパイプラインの商業実装として参考に |
| XGRIDS LCC Cloud（$800/年） | ★★☆ | SLAM+3DGSクラウド処理の価格ベースラインとして参考 |

---

*レポート作成日: 2026-05-25 | 対象期間: 2026-05-16〜25 | 新着件数: 12件*
