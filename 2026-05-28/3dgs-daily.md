# 3DGS/4DGS デイリーレポート — 2026-05-28

**対象期間:** 2026-05-16 〜 2026-05-28（前回レポート: 2026-05-15）
**収集件数:** 20件（論文8件・ニュース6件・ツール3件・コミュニティ3件）

---

## 📌 今日の注目トレンド TOP5

1. 🔬 **TideGS**（ICML 2026 Spotlight）：24GB 単一 GPU で 10 億超のGSプリミティブ学習が初めて可能に。大規模シーン構築のハードルが劇的に低下
2. 🤖 **SpAItial Echo-2**：テキスト 1 行 or 写真 1 枚からブラウザで歩き回れる物理的に整合した 3D 空間を即時生成。専用ハード不要でウェブ完結
3. 🎬 **Netflix × Volinga**：「Berlin and the Lady with an Ermine」の LED ボリューム撮影に GS を本格採用。主流映像制作への定着が加速
4. 🗺️ **Esri ArcGIS May 2026**：GIS 世界最大手がドローン映像からのクラウドGS生成を 1 万枚/ミッション対応に拡大
5. 📡 **RxGS**：「電波」を使って GS 空間を構築する新手法が登場。Wi-Fi・BLE 伝搬シミュレーションに 3DGS を応用

---

## 🔬 注目論文

### 1. TideGS — 10 億超のGSプリミティブを単一GPUで学習可能に ⭐ ICML 2026 Spotlight
- **URL:** https://arxiv.org/abs/2605.20150
- **プロジェクト:** https://sponge-lab.github.io/TideGS/
- **著者:** 香港科技大学・長城汽車・清華大学・北京人工智能研究院
- **概要:**
  通常は数百万個が限界だった GS プリミティブを、たった 24GB の単一 GPU で **10 億個以上** 学習できるようになった。都市規模の超高精細 3D 再構成が 1 台の PC で実現可能に。
- **解決した課題:**
  従来の 3DGS 学習はすべての GS を GPU メモリに乗せる必要があり、大規模シーンでは GPU 容量がすぐ上限（約 1100 万個）に達していた。TideGS はカメラ視点ごとに「今見えている GS だけ」を GPU にキャッシュし、SSD→CPU→GPU の階層型メモリ構造を設計することで問題を解消。品質も従来の単一 GPU 手法を上回った。
- **分野:** 大規模シーン再構成・GS最適化

---

### 2. SCOUP — 3D言語GS学習を400倍高速化・メモリ3倍削減
- **URL:** https://arxiv.org/abs/2605.13600
- **概要:**
  「この机の上のコップだけ移動させて」のような言語指示で 3D シーンを操作できる「言語GS」の学習が **400 倍高速化・メモリ 3 倍削減** された。
- **解決した課題:**
  3D Language GS は言語モデルの埋め込みベクトルを毎フレームの GS 最適化に組み込む必要があり、学習が非常に遅くメモリを大量消費していた。SCOUP は言語理解の学習と 3D Gaussian の最適化を切り離す「疎コードアップリフティング」を提案し、この問題を解消した。
- **分野:** 言語 + 3D / オープンボキャブラリーシーン理解

---

### 3. RxGS — 電波/無線周波数場のGS合成（受信機汎化対応）
- **URL:** https://arxiv.org/abs/2605.24290
- **概要:**
  Wi-Fi・BLE・RFID などの **電波の伝搬を 3D Gaussian Splatting で表現・合成** できるようになった。送受信機の位置を変えても 1 つのモデルで対応可能。
- **解決した課題:**
  従来の RF 伝搬合成は受信機の位置ごとに別モデルが必要だった。RxGS は「部屋のジオメトリは受信機によらず共通」という物理的洞察を活かし、2 段階学習で受信機汎化を実現。BLE RSSI・RFID・Wi-Fi CSI の 3 データセットで検証済み。
- **分野:** 無線通信シミュレーション・RF 場再構成・室内ナビゲーション

---

### 4. GuardMarkGS — 3DGS著作権保護（透かし＋編集妨害の統合フレームワーク）
- **URL:** https://arxiv.org/abs/2605.12919
- **概要:**
  公開した 3DGS アセットに **著作権の透かしを埋め込みながら、不正な編集も同時に防止** できる統合フレームワーク。Mip-NeRF 360 や Instruct-NeRF2NeRF シーンで評価済み。
- **解決した課題:**
  これまでの手法は「透かし埋め込み」と「編集妨害」が別々の処理で、両立が困難だった。GuardMarkGS は 1 回の最適化で両方を同時に実現し、重要度の高い Gaussian にのみ強い保護を与えることで視覚品質を維持した。
- **分野:** セキュリティ・知的財産保護

---

### 5. Underwater360 — 水中パノラマ画像からの全方位GS再構成（世界初）
- **URL:** https://arxiv.org/abs/2605.26447
- **概要:**
  パノラマカメラで撮影した水中映像から **360 度の 3D Gaussian シーン** を再構成できるようになった（水中での全方位 GS は世界初）。合成＋実写水中データセットも新規公開。
- **解決した課題:**
  水中は光の屈折・散乱・色ズレが激しく、通常の 3DGS は誤差が大きかった。Underwater360 は球面ラスタライズ方式で水の光学特性を物理的に補正し、パノラマ画像特有の歪みも解消した。
- **分野:** 水中ロボット・海洋探査・VR・文化財調査

---

### 6. Transcoding 3DGS — 元の撮影画像なしでポイントクラウド/メッシュから3DGS変換
- **URL:** https://arxiv.org/abs/2605.21051
- **概要:**
  既存の 3D ポイントクラウドやメッシュデータを、**元の撮影写真なしで** 高品質な 3DGS に変換できるようになった。従来の SfM ベース初期化より大幅に速く収束し、表面が滑らかな GS が生成される。
- **解決した課題:**
  これまで 3DGS への変換には元の多視点画像が必須だったため、既存の膨大な 3D アセット（ゲーム・CAD・文化財）を GS 化するのが困難だった。本手法はポイントクラウドの分布を初期配置として活用する専用アルゴリズムで解決。
- **分野:** 3D アセット変換・コンテンツ制作・デジタルアーカイブ

---

### 7. GScomp-QA — 圧縮GSの主観品質評価データセット（世界初）
- **URL:** https://arxiv.org/abs/2605.26880
- **概要:**
  GS 圧縮の品質を人間の主観評価と照合できる、世界初の大規模データセット。331 本の動画（13 シーン × 9 圧縮手法）を収録。
- **解決した課題:**
  これまで GS 圧縮の評価は PSNR などの数値指標だけで行われており、人間の知覚との乖離が問題だった。今後の圧縮研究の品質基準として活用が期待される。
- **分野:** 品質評価・圧縮研究・標準化

---

### 8. FaceParts — GS アバター内での顔パーツ教師なし分割・スワップ
- **URL:** https://scipapermill.com/2026/05/23/gaussian-splatting-from-billion-scale-worlds-to-intelligent-robot-hands/
- **著者:** Wrocław University of Science and Technology
- **概要:**
  GS アバターの中で「鼻だけ」「目だけ」を **教師なし（ラベル不要）** で自動認識し、他のアバターのパーツと入れ替えができるようになった。
- **解決した課題:**
  GS アバターはピクセル単位の構造ではなく点群なので、顔の「どの部分か」を認識するのが難しかった。FaceParts は空間的クラスタリングで顔の構造意味を自動発見する。
- **分野:** アバター生成・顔編集・デジタルヒューマン

---

## 🏢 業界ニュース

### 1. SpAItial Echo-2 — 1枚の写真/テキストからブラウザで探索可能な3D世界を即時生成
- **URL:** https://radiancefields.com/spaitial-ai-announces-new-model-echo-2
- **公式:** https://spaitial.ai/blog/echo-2-release
- **概要:**
  1 枚の写真かテキストプロンプトを入力するだけで、**ブラウザ内をリアルタイムで歩き回れる** 物理的に整合した 3D Gaussian シーンが即座に生成される。専用ハードウェア不要。GS をレンダリングプリミティブとして採用することでゲーム用 GPU でもブラウザで高速動作。
- **主な機能:** バーチャルステージング（空の部屋に家具を配置）・全体スタイル転送・2D 間取り図からの部屋生成
- **対応分野:** 建築・インテリア・デジタルツイン・XR

---

### 2. Esri ArcGIS May 2026 大型アップデート — ドローン×GS が測量インフラへ
- **URL:** https://www.esri.com/arcgis-blog/products/site-scan/imagery/whats-new-in-site-scan-for-arcgis-q2-2026
- **概要:**
  GIS 世界最大手 Esri の「Site Scan for ArcGIS（ドローン管理）」と「ArcGIS Reality for ArcGIS Pro（3D 再構成）」の両製品が 5 月に同時 GS 強化。ドローン映像から **クラウドで 1 万枚/ミッション** まで GS を生成できるようになった。
- **重要性:** 世界の政府・建設・インフラ管理機関が使う GIS の事実上の標準プラットフォームが GS 生成を標準ワークフローに組み込んだことで、測量・都市計画・インフラ点検での大規模導入が現実化。
- **注記:** EU ホスティングを要求する欧州顧客は GS 生成機能が利用不可（AWS インフラ制約）

---

### 3. Netflix「Berlin and the Lady with an Ermine」× Volinga — GS がメインストリーム映像制作に
- **URL:** https://web.volinga.ai/
- **概要:**
  Netflix スペイン語シリーズ（全 8 話、2026 年 5 月配信）の LED ボリュームバーチャルプロダクションに Volinga の GS ワークフローを採用。マドリードのカジェ・アルカラをリアルタイム GS で LED ウォールに映し出した。
- **重要性:** 主流の Netflix オリジナルシリーズへの本番採用事例が登場。GS 採用が「将来の話」から「現在進行形」になったことを示す象徴的な出来事。

---

### 4. XGRIDS LCC Cloud 商用化 — SLAM+3DGS クラウドが $800/年で正式提供開始
- **URL:** https://lcc-cloud.xgrids.com/
- **概要:**
  これまでフリーベータだった XGRIDS の「LCC Cloud」が正式商用化。SLAM（自己位置推定）と 3DGS 再構成をすべてクラウドで処理するサービスが、**月 250 分の処理枠で年間 $800** で利用可能に。
- **重要性:** 専用ハードを持たない中小の建設・不動産・製造業者でも撮影するだけで高精度 3D 空間を得られるサービスが本格始動。GS の「インフラ化」が進む。

---

### 5. Veesus × SolidWorks — CADソフトの中でGSを直接操作・可視化
- **URL:** https://novedge.com/blogs/design-news/veesus-may-2026-updates
- **概要:**
  製造業向け CAD ソフトの代名詞 SolidWorks に Veesus の GS ビューアーが統合。現実の工場や部品のスキャンデータ（GS）を **CAD モデルと並べて同時表示・操作** できるようになった。
- **重要性:** 「設計 CAD データ」と「現実の 3D キャプチャ」をシームレスに比較する需要が急増している製造業に直接刺さるアップデート。設計ズレの検出やライン確認が効率化される。

---

### 6. geofront × NHM Vienna — 70万スプラットでマリア・テレジアの宝石ブーケを3D復元
- **URL:** https://www.geofront.eu/
- **概要:**
  ウィーン自然史博物館が所蔵するマリア・テレジアの **宝石ブーケ（18 世紀の希少工芸品）** を、geofront が 70 万スプラットで高精細 3D 化。劣化で色あせた葉の部分をキュレーターがデジタル上で復元・修復できるようになった。
- **重要性:** 物理的に触れられない・分解できない文化財の修復研究に GS が直接活用された具体的な事例。博物館・文化財保存での GS 応用が国際的に広がっていることを示す。

---

## ⚙️ 開発者向けツール・インサイト

### 1. PlayCanvas Engine 2.13 — WebGSレンダリング大幅強化
- **URL:** https://radiancefields.com/playcanvas-engine-2-13-expands-unified-gsplat-performance-and-customization
- **概要:**
  - **ColorRamp モード追加:** 深度・密度をグラデーション色で可視化。デバッグや品質確認が格段に楽に
  - **SH 動的再評価:** カメラ移動時に球面調和関数をリアルタイム再計算し照明の見た目がより正確に
  - **ストリーミング改善:** 大規模シーンの配信がよりスムーズに
  - **シェーダーカスタマイズ強化:** vertex shader を直接上書きできる新 API
- **推奨アクション:** Web 上で GS を表示・配信しているプロジェクトは早めのバージョンアップを推奨

---

### 2. Houdini-gsplat (Plattipus, MIT) — HoudiniにUSDネイティブGS統合
- **GitHub:** https://github.com/plattipus/houdini-gsplat
- **URL:** https://radiancefields.com/houdini-gsplat-brings-usd-native-gaussian-splats-to-houdini-solaris
- **概要:**
  Houdini 21 の Solaris（USD 環境）上で .ply ファイルを直接 GS として読み込み、レンダリング・コンポジットできる MIT ライセンスのオープンソースプラグイン。
  - `PLY Import`・`Gsplat Instancer`・`Uruk` の 3 つの LOP ノードを提供
  - ディスク書き出し・Python グルーコード一切不要
  - OpenUSD v26.03 の `UsdVolParticleField3DGaussianSplat` スキーマに準拠
- **推奨アクション:** Houdini を使った VFX・映像制作パイプラインで GS を扱いたい開発者に必須のリリース

---

### 3. GS公式コードベース新機能追加（graphdeco-inria/gaussian-splatting）
- **GitHub:** https://github.com/graphdeco-inria/gaussian-splatting
- **URL:** https://radiancefields.com/gaussian-splatting-codebase-adds-new-features
- **概要:**
  3DGS のオリジナル実装リポジトリに複数の実用的な機能が正式マージ:
  - **高速化:** sparse_adam 使用時に **学習速度 2.7 倍**（Taming-3DGS の高速ラスタライザを統合）
  - **アンチエイリアシング:** `--antialiasing` フラグで EWA フィルタが有効化
  - **Top View 可視化:** SfM 点群とカメラ配置を俯瞰ビューで確認できる新ツール
- **推奨アクション:** `git pull` して `sparse_adam` を有効化するだけで即座に学習が 2.7 倍高速化

---

## 💬 コミュニティ・SNS 話題

### 1. 「Gaussian Splatting: From Billion-Scale Worlds to Intelligent Robot Hands」まとめ記事
- **URL:** https://scipapermill.com/2026/05/23/gaussian-splatting-from-billion-scale-worlds-to-intelligent-robot-hands/
- TideGS（10 億 GS）からロボットハンドの操作への GS 応用まで、最新研究をキュレーション。英語圏の AI・XR コミュニティで Twitter/X や Hacker News で拡散中。

### 2. XGRIDS LCC ファイルフォーマット オープンソース化
- **URL:** https://radiancefields.com/xgrids-open-sources-its-lcc-file-format-aims-to-standardize-3dgs-pipelines
- XGRIDS が独自の LCC フォーマット仕様を OSS 公開。Reddit r/GaussianSplatting で「COLMAP に続く業界標準になるか」と議論が活発化。

### 3. Houdini-gsplat に対する VFX コミュニティの反応
- **URL:** https://radiancefields.com/houdini-gsplat-brings-usd-native-gaussian-splats-to-houdini-solaris
- SideFX フォーラムや LinkedIn で「ついに来た」と反響が大きい。Nuke・USD・Houdini を使うプロダクションパイプラインへの統合検討者は即チェックを推奨。

---

## 📋 開発者向け ToDo リスト

```
□ graphdeco-inria/gaussian-splatting を git pull → sparse_adam 有効化で学習を 2.7 倍高速化
□ Houdini ユーザー：houdini-gsplat (MIT) を試す → USD ステージで GS を直接操作
□ Web 配信系：PlayCanvas Engine 2.13 へのアップグレードを検討
□ 言語 × GS 開発者：SCOUP の実装を確認（400 倍高速化の手法）
□ 著作権・知財リスクが気になる人：GuardMarkGS 論文を読む
□ 測量・GIS 系：Esri Site Scan May 2026 の GS クラウド生成を検証
□ VFX・映像制作：Houdini-gsplat と Volinga の Netflix 事例をウォッチ
□ CAD・製造系：Veesus × SolidWorks GS 統合を検討
```

---

*レポート生成: 2026-05-28 | 情報源: arXiv, Radiance Fields, Esri Blog, Auganix, Eyerys, Novedge, DroneDJ, SciPaperMill*
