# 3DGS & 4D生成 デイリーレポート｜2026年5月15日（木）

## サマリー

- **新規論文:** 7件
- **業界ニュース:** 4件
- **コミュニティ:** 2件
- **合計:** 13件

---

## 🔥 今日の注目トレンド TOP5

1. 🌐 **World Labs Spark 2.0（見逃し注意！）** — オープンソース(MIT)Webレンダラーが1億Splatsをスマホでもリアルタイム表示。ブラウザ時代の3DGSが本格始動
2. 🤖 **MAGS-SLAM** — カラーカメラのみで複数ロボットが協調3Dマッピング。深度センサー不要の時代へ
3. 🏭 **製造業・測量業界への本格普及** — Autodesk VRED 2027×BSH家電、PIX4Dmatic ProがGS統合を発表
4. 📰 **The New Yorker** — 一流報道メディアがGSを使ったアートポートレートを初掲載。メディア文化への浸透が加速
5. 📅 **CVPR 2026（6/3〜7 デンバー）目前** — 3DGS論文50件以上が一斉公開直前。コードラッシュ到来中

---

## 📚 注目論文

### 1. MAGS-SLAM：カラーカメラだけで複数ロボットが協調3Dマッピング

- **arXiv:** [2605.10760](https://arxiv.org/abs/2605.10760)
- **投稿日:** 2026年5月11日
- **分野:** SLAM・マルチエージェント・ロボット

**概要（わかりやすく）:**

これまでの3DGS SLAMは「深度カメラ（RGBDセンサー）」が必須でした。本研究は安価なカラーカメラのみで複数のロボットが協調しながらリアルタイムに高精度な3Dマップを生成できる、世界初のシステムです。各ロボットがローカルで小さな「サブマップ」を作り、コンパクトな情報だけをやり取りしながら最終的に一つの高品質マップに統合します。

**課題と解決:**
- 従来: 深度センサー（高価）必須 → 現在: 安価なカラーカメラのみで実現
- 複数ロボットの協調 → 農業ロボット群、ドローン群への直接応用が射程内
- 品質: RGB-Dベースラインを超えるPSNR 43.24dBを達成

---

### 2. AnySplat：カメラ位置の事前記録ゼロで写真から即3D化

- **arXiv:** [2505.23716](https://arxiv.org/abs/2505.23716)
- **出版:** SIGGRAPH Asia 2025 (ACM TOG)
- **GitHub:** [InternRobotics/AnySplat](https://github.com/InternRobotics/AnySplat)
- **分野:** フィードフォワード3DGS・ポーズフリー

**概要（わかりやすく）:**

写真を撮る際に「カメラの位置・角度を記録する前処理（SfM）」が一切不要になりました。どんな角度・どんな枚数の写真でも1回の計算で3Dシーンに変換できます。重複するGaussianを30〜70%削減しながら従来手法と同等の品質を実現。

**課題と解決:**
- SfM前処理の廃止 → スマートフォンで気軽に撮った写真群でも即座に高品質3D化
- ゼロショット評価でポーズあり手法と同等の品質を達成

---

### 3. PanoPlane：たった3枚の室内写真から3D空間を完全復元

- **arXiv:** [2605.14135](https://arxiv.org/abs/2605.14135)
- **投稿日:** 2026年5月13日
- **分野:** スパースビュー3DGS・パノラマ補完・室内シーン

**概要（わかりやすく）:**

室内をわずか3枚の写真から高精度な3Dシーンへ変換できる手法です。全周パノラマ（360°）の拡散モデルを使い、「撮影されていない方向」を壁・床・天井の幾何構造から推測・補完します。カメラが向いていなかった角や未撮影エリアも正確に復元。

**課題と解決:**
- 従来: 少枚数入力では未撮影エリアで精度が激しく落ちる
- 解決: 全周パノラマ補完で360°を推測、幾何構造を錨として不自然な補完を防止
- 不動産・インテリアデザインのバーチャルツアー革命へ直結

---

### 4. SparseOIT：ガラスや水など透明素材が苦手だった問題を解決

- **arXiv:** [2605.13855](https://arxiv.org/abs/2605.13855)
- **投稿日:** 2026年5月13日
- **分野:** 透明・半透明材質・3DGS品質改善

**概要（わかりやすく）:**

3DGSの長年の弱点「ガラス・水・半透明な物体が正確に表現できない」を解決します。Order-Independent Transparency（OIT：描画順序に依存しない透明処理）を3DGSに最適な形で統合。既存のOIT手法を大幅に上回る品質を達成しながら、通常の3DGS品質も維持します。

**課題と解決:**
- 従来: 透明物体は深度ソートの問題で大きなアーティファクトが発生
- 解決: 変数間の依存スパース性を活用した効率的なOIT最適化
- 製品デザインレビュー・建築CGで透明素材がリアルに表現可能に

---

### 5. AV1動画コーデックで3DGS訓練を63%高速化

- **arXiv:** [2605.14629](https://arxiv.org/abs/2605.14629)
- **投稿日:** 2026年5月14日
- **分野:** 3DGS高速化・SfM効率化

**概要（わかりやすく）:**

動画を3DGSに変換する前段階「SfM処理（3D点群生成）」は計算時間の大半を占めていました。最新動画コーデックAV1の「動きベクトル」情報を再利用することで、従来のSfM処理を劇的に短縮。訓練時間63%削減・画質（VMAF）9ポイント向上を同時達成。

**課題と解決:**
- SfMがGSパイプラインのボトルネックを解消
- スマホ動画→3DGSサービスのリアルタイム化が射程内
- 長尺映像の3D化ワークフローを抜本的に短縮

---

### 6. Faster-GS（CVPR 2026）：既存比2〜5倍速、コード公開

- **arXiv:** [2602.09999](https://arxiv.org/abs/2602.09999)
- **GitHub:** [nerficg-project/faster-gaussian-splatting](https://github.com/nerficg-project/faster-gaussian-splatting)
- **採択:** CVPR 2026
- **分野:** 3DGS高速化・最適化・コード公開

**概要（わかりやすく）:**

3DGS訓練の既存実装より2〜5倍速く、VRAM使用量も削減。既存の最善研究手法を集約・再実装し、新たな最適化（数値安定性・Gaussian打ち切り・勾配近似改善）を追加した研究ベースラインです。CVPR 2026採択論文のコードが公開されました。

**課題と解決:**
- 研究・開発コードの断片化を解消 → 統合されたファストベースライン
- 4DGSの非剛体シーン最適化にも適用可能
- 3DGS研究・開発の新標準ライブラリ候補

---

### 7. XFreq-GS：複数周波数帯の電波場を3DGSで同時モデリング

- **arXiv:** [2605.11432](https://arxiv.org/abs/2605.11432)
- **分野:** 電波場・無線通信応用・クロス周波数GS

**概要（わかりやすく）:**

3DGSの「任意視点から空間を再現する」技術を電波に応用。従来は1つの周波数帯しか扱えなかったところ、1つのモデルで複数帯域（4G/5G/6G等）の電波伝搬パターンを同時推定・可視化できます。

**課題と解決:**
- 従来: 単一周波数のみ対応 → 解決: 周波数駆動型Gaussian表現で複数帯域を統一モデル化
- 基地局配置・通信インフラ設計の効率化に直結
- ニッチだが驚きの応用：3DGSが電波インフラ設計へ

---

## 🏭 業界ニュース

### 8. World Labs Spark 2.0 — ブラウザで1億Splatsをストリーミング（オープンソース）⭐重要

- **公開日:** 2026年4月14〜15日
- **URL:** [worldlabs.ai/blog/spark-2.0](https://www.worldlabs.ai/blog/spark-2.0)
- **GitHub:** [sparkjsdev/spark](https://github.com/sparkjsdev/spark)（MIT License）
- **分野:** WebGSストリーミング・オープンソース・3D普及

**概要（わかりやすく）:**

Fei-Fei Li氏率いるWorld Labsが、**1億以上のGaussian SplatsをスマホでもVRでもWebブラウザからリアルタイム表示できる**レンダラー「Spark 2.0」をMITライセンスでオープンソース公開しました。

**技術ポイント:**
- THREE.js + WebGL2で動作 → 追加インストール不要、既存Webプロジェクトに即統合可能
- 独自の`.RAD`ファイル形式でLoD付きプログレッシブストリーミング（64,000 Splatsの概要がロード直後に表示、詳細は順次追加）
- バーチャルGPUメモリ管理でメモリ上限を克服

**何が変わったか:** 超高スペックPCが必要だった大規模3DGSシーンが、スマートフォン・VRヘッドセットを含むあらゆるデバイスのWebブラウザで閲覧可能になりました。映画・ゲーム・不動産・教育分野でのGS体験共有が一気に大衆化する可能性があります。

---

### 9. Autodesk VRED 2027 × BSH家電 — 製造業設計レビューにGSが本格採用

- **公開日:** 2026年5月8日
- **URL:** [blogs.autodesk.com](https://blogs.autodesk.com/design-studio/2026/05/08/bsh-adopts-gaussian-splats-in-vred-2027-for-high-fidelity-visualization/)
- **分野:** 製造業・設計レビュー・Autodesk

**概要（わかりやすく）:**

ヨーロッパ最大の家電メーカーBSH（BoschとSiemensの合弁ブランド、食洗器・洗濯機・冷蔵庫等を製造）が、Autodesk VRED 2027のGaussian Splatting機能を採用。製品デザインの評価・意思決定レビューに3DGSスキャン環境を本格活用。

**業界インパクト:**
- 3DモデルがGSシーン内に影を落とす等、CGと現実スキャンの高度な統合が実現
- XGRIDS PortalCamでのスキャン → VRED 2027で即時設計レビューのパイプライン確立
- 自動車・家電・建築業界のデザインレビューにGSが「標準ツール」として組み込まれる動きが本格化

---

### 10. PIX4Dmatic Pro にGS統合 — 測量パイプラインの「ループを完結」

- **公開日:** 2026年5月12日
- **URL:** [geoweeknews.com](https://www.geoweeknews.com/sponsored/pix4d-closes-the-loop-with-gaussian-splatting-in-pix4dmatic)
- **分野:** 測量・GIS・ドローン・地理空間情報

**概要（わかりやすく）:**

世界的な測量・ドローン処理ソフト大手PIX4Dが、プロ向けデスクトップ「PIX4Dmatic Pro」にGaussian Splatting機能を追加。これにより**現場キャプチャ → デスクトップ処理 → クラウド共有** のパイプラインが地理座標付きで完全に一貫（「ループを閉じる」）。

**技術的特徴:**
- 従来フォトグラメトリーの点群と比べてノイズが少なく均一な点群を生成
- 既存PIX4Dワークフローにシームレスに統合
- Esri ArcGIS Pro、DJI Terra等も同様にGS対応済み（業界標準化が進行中）

---

### 11. The New Yorker がGaussian Splatting初採用 — 報道ビジュアルの新地平

- **URL:** [radiancefields.com/gaussian-splatting-at-the-new-yorker](https://radiancefields.com/gaussian-splatting-at-the-new-yorker)
- **分野:** 報道・メディア・文化・ジャーナリズム

**概要（わかりやすく）:**

米国の代表的な高級文芸誌「The New Yorker」が、Gaussian Splattingを使った初のポートレート記事を掲載しました。著名アーティスト・Lorna Simpsonをテーマにした作品で、同誌のニューヨーク周年特集の一部として掲載。

**注目ポイント:**
- 「AI生成画像ではなく、現実の空間からキャプチャしたデータのみ使用」と明記
- GS特性「撮影後から新しい視点を作れる」を「新しいビジュアル文法」と評価
- ドキュメンタリー・報道写真の次世代表現として業界が注目

---

## 🌐 コミュニティ・SNS話題

### 12. Postshot V1.1 リリース — VRプレビュー＆測光補正が追加

- **公開日:** 2026年5月13日
- **URL:** [jawset.com](https://www.jawset.com)
- **分野:** 3DGS処理ツール・VR対応

主な新機能：
- VRヘッドセットでのリアルタイムプレビュー
- 測光補正（Photometric Compensation）の正式対応
- ラッソ＆矩形選択ツール
- Pix4D OPF・SPZシーケンス形式のサポート拡大

---

### 13. CVPR 2026 デンバー開催まであと3週間 — 3DGS論文コードラッシュ到来

- **開催日:** 2026年6月3〜7日（コロラド州デンバー）
- **URL:** [cvpr.thecvf.com/Conferences/2026](https://cvpr.thecvf.com/Conferences/2026)
- **分野:** カンファレンス・論文コード公開

CVPR 2026では3DGS関連論文が50件以上採択。主要採択論文：
- **FastGS（Highlight）** — 100秒で3DGSトレーニング
- **EDGS** — 密度化なしで効率的なGS収束
- **Faster-GS** — 2〜5倍高速な研究ベースライン（コード公開済み）

追跡リポジトリ: [Awesome3DGS CVPR.md](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md)

---

## 🛠️ 開発者向けインサイト（今すぐ対応すべき動向）

### 🔴 今週イチオシのアクション（優先度：高）

1. **World Labs Spark 2.0 を試す（MIT License）**
   - Webアプリ・サービスに100M+ Splatsのブラウザ表示を組み込める
   - THREE.js統合なので既存WebGLプロジェクトにすぐ追加可能
   - 🔗 https://github.com/sparkjsdev/spark

2. **Faster-GS コードを導入（CVPR 2026）**
   - 研究・開発コードベースで今すぐ使える最速のGS実装
   - 既存コードの2〜5倍速、VRAM削減、4DGSにも適用可
   - 🔗 https://github.com/nerficg-project/faster-gaussian-splatting

3. **AnySplat モデルを検証（Hugging Face）**
   - カメラポーズ不要・SfM不要でリアルタイム3D化が可能
   - スマホ写真→3DGSサービス開発のゲームチェンジャー候補
   - 🔗 https://huggingface.co/papers/2505.23716

### 🟡 今週注目しておくべき動向（中期対応）

4. **AV1 Motion Vectors アプローチ（2605.14629）を研究パイプラインへ**
   - 動画→GS変換のSfMボトルネックを63%削減するアイデア
   - 長尺映像のリアルタイム3D化サービスへの応用余地大

5. **PIX4Dmatic / 測量業界クライアント向けGSワークフローを整備**
   - 建設・土木・インフラ管理分野でGSが「標準成果物」になりつつある

6. **CVPR 2026（6/3〜7）の採択論文コードに注目**
   - 今後2週間でコードラッシュが起きる
   - 追跡: github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

---

## 📋 新規項目一覧

| # | 名前 | 種別 | 分野 | URL |
|---|------|------|------|-----|
| 1 | MAGS-SLAM | 論文 | SLAM・マルチエージェント | https://arxiv.org/abs/2605.10760 |
| 2 | AnySplat | 論文 | フィードフォワードGS・ポーズフリー | https://arxiv.org/abs/2505.23716 |
| 3 | PanoPlane | 論文 | スパースビュー・パノラマ補完 | https://arxiv.org/abs/2605.14135 |
| 4 | SparseOIT | 論文 | 透明材質3DGS | https://arxiv.org/abs/2605.13855 |
| 5 | AV1 Motion Vectors for GS | 論文 | 高速化・SfM効率化 | https://arxiv.org/abs/2605.14629 |
| 6 | Faster-GS (CVPR 2026) | 論文 | 高速化・最適化 | https://arxiv.org/abs/2602.09999 |
| 7 | XFreq-GS | 論文 | 電波場・通信応用 | https://arxiv.org/abs/2605.11432 |
| 8 | World Labs Spark 2.0 | ニュース | WebGSストリーミング | https://www.worldlabs.ai/blog/spark-2.0 |
| 9 | Autodesk VRED 2027 × BSH | ニュース | 製造業・設計レビュー | https://blogs.autodesk.com/design-studio/2026/05/08/bsh-adopts-gaussian-splats-in-vred-2027-for-high-fidelity-visualization/ |
| 10 | PIX4Dmatic Pro GS統合 | ニュース | 測量・GIS・ドローン | https://www.geoweeknews.com/sponsored/pix4d-closes-the-loop-with-gaussian-splatting-in-pix4dmatic |
| 11 | The New Yorker × GS Portrait | ニュース | 報道・メディア・文化 | https://radiancefields.com/gaussian-splatting-at-the-new-yorker |
| 12 | Postshot V1.1 | コミュニティ | 3DGS処理ツール | https://www.jawset.com |
| 13 | CVPR 2026 Denver | コミュニティ | カンファレンス・コード公開 | https://cvpr.thecvf.com/Conferences/2026 |

---

*レポート生成日時: 2026-05-15*
