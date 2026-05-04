# 3DGS & 4D生成 デイリーレポート — 2026-05-04

## 概要

**収集期間**: 2026年4月中旬〜5月4日  
**新着件数**: 論文8件 / 業界ニュース3件 / コミュニティ3件（合計14件）  
**重複排除**: past_3dgs.json 照合済み

---

## 今日の注目トレンド TOP5

1. 🎥 **Sony XYN Spatial Capture** — 大手ソニーがGaussian Splatting活用のプロ向け空間キャプチャソリューションを正式発売。映像制作・バーチャルプロダクションへの本格展開
2. 🌍 **Cesium 3D GS with LOD** — 都市スケール〜センチメートル精度の大規模GSデータをLODストリーミングで配信可能に。地理空間+3DGSの決定版インフラが整備
3. 🌑 **暗所3DGS 2連発** — ELoG-GS・MERID-GSと低照度環境対応論文が同週に登場。夜間撮影や医療内視鏡への応用が加速
4. 📡 **GS-SCNet** — 3DGSと映像圧縮コーデックを初めて統合したフレームワーク。リアルタイムXR通信の新基盤
5. 🏛️ **3DISE Prague（本日・明日開催）** — GS業界の最前線が集結するカンファレンスがプラハで開幕

---

## 1. 注目論文（重要度：高）

### 1-1. GS-SCNet — リアルタイム没入型ビデオ通信への3DGS統合（初の統一フレームワーク）

- **ソース**: [arXiv 2604.25330](https://arxiv.org/abs/2604.25330)
- **投稿日**: 2026年4月28日
- **フィールド**: 没入型ビデオ通信・圧縮

**何ができるようになったか**  
XR/テレプレゼンスの映像配信で、「映像の圧縮（コーデック）」と「3D再構成（レンダリング）」を完全に一体化した世界初のフレームワーク。3DGSによる3D再構成と意味コーディング（深い理解を使った圧縮）を同時に最適化することで、従来の「圧縮→ノイズ乗り→3D再構成で品質劣化」という悪循環を断ち切る。

**これまでの課題と解決策**  
従来の分離型アプローチでは圧縮ノイズが3D再構成の品質を大きく低下させていた。GS-SCNetは「レート-レンダリング歪み（RRD）」という新しい最適化パラダイムを採用し、並列ステレオエンコーディングで遅延なしのリアルタイム処理を実現。実験では従来の映像コーデックおよび学習型コーデック双方を圧縮効率・レンダリング品質・知覚品質で上回る。

---

### 1-2. ELoG-GS — 極暗所・夜間環境での高品質3D再構成

- **ソース**: [arXiv 2604.12592](https://arxiv.org/abs/2604.12592)
- **投稿日**: 2026年4月14日
- **フィールド**: 低照度3DGS・ロバスト再構成

**何ができるようになったか**  
夜間や暗い室内など「極低照度」環境での写真・映像から、フォトリアリスティックな3DGSを安定して生成できるようになった。防犯カメラ映像や医療内視鏡画像からの3D再構成が現実的に。

**これまでの課題と解決策**  
従来の3DGSは「輝度一定（輝度は常に安定している）」を前提とするため、暗所では大きく精度が落ちていた。ELoG-GSは「デュアルブランチ（2系統）構造」で輝度ガイド付き色補正を組み込み、学習ベースの点群初期化と組み合わせることで安定した再構成を実現。

---

### 1-3. MERID-GS「Light 'em Up」— 数枚の暗所写真から360° 3DGS生成

- **ソース**: [arXiv 2604.24053](https://arxiv.org/abs/2604.24053)
- **投稿日**: 2026年4月27日
- **フィールド**: 低照度3DGS・フューショット対応

**何ができるようになったか**  
少ない枚数（数枚〜）の暗所写真だけで、360°全方位の3DGSを生成できるフューショット（few-shot）手法。明るいシーンで学習したモデルを、少量のデータで暗所シーンに素早く適応させられる。低照度マルチビュー360°データセットも新規構築・公開。

**これまでの課題と解決策**  
Retinex理論（照明成分と反射成分を分離するアルゴリズム）を3DGSに組み込み、照明状態に応じた周波数ゲーティング（Illumination-State-Guided Frequency Gating）でノイズ伝播を抑制。複数データセットで最高水準の性能を達成。

---

### 1-4. Instant Colorization of Gaussian Splats — 3DGSへの高速カラー付け（最大10倍高速）

- **ソース**: [arXiv 2604.17155](https://arxiv.org/abs/2604.17155)
- **投稿日**: 2026年4月18日
- **フィールド**: 3DGS編集・セグメンテーション

**何ができるようになったか**  
2D画像の色情報・ニューラル特徴量・セグメンテーションマスクを既存の3DGSシーンに「瞬時に」反映させる手法。3Dシーンの再照明、スタイル転写、3Dセマンティックセグメンテーションが従来の最大10倍の速度で実行可能に。

**これまでの課題と解決策**  
従来の勾配降下法では各Gaussian点への情報反映に時間がかかっていた。「法線方程式を使った可視性重み付き最小二乗問題」として定式化し、既存の微分可能ラスタライザで効率的に実装。再照明・特徴付与・3Dセグメンテーションの3タスクで有効性を実証。

---

### 1-5. GS-2M — 反射素材でも高精度にメッシュ化（Eurographics 2026採択）

- **ソース**: [arXiv 2509.22276](https://arxiv.org/abs/2509.22276) | [GitHub](https://github.com/ndming/GS-2M)
- **採択**: Eurographics 2026（Computer Graphics Forum）
- **フィールド**: メッシュ再構成・マテリアル分解

**何ができるようになったか**  
ガラスや金属など反射素材のある物体を、外部AIモデルに頼らず高精度な3Dメッシュ（ポリゴンモデル）として再構成できるようになった。3DGSの最適化プロセスにマテリアル情報（粗さ・光沢）を直接組み込んだシンプルかつ効果的な手法。

**これまでの課題と解決策**  
従来手法は高反射面の再構成に失敗しやすく、高精度化のために大型事前学習モデルへの依存が課題だった。GS-2Mは多視点測光変動をベースにした新しい粗さ監督戦略を導入し、外部依存なしで解決。コードはGitHubで公開。

---

### 1-6. Lumina-4DGS — 自動運転向け、照明変化に強い4DGS（Sensors 2026掲載）

- **ソース**: [MDPI Sensors 2026](https://www.mdpi.com/1424-8220/26/5/1650)
- **掲載**: 2026年3月（MDPI Sensors誌）
- **フィールド**: 4DGS・自動運転・照明補正

**何ができるようになったか**  
自動運転車の複数台カメラが撮影した映像から、カメラ間の照明差（自動露出・ホワイトバランスのズレ）を自動補正しながら高品質な4DGSを生成。Waymo Open Datasetで最高精度PSNR 31.12 dBを記録、深度推定誤差（Depth RMSE）1.89 mも達成。

**これまでの課題と解決策**  
標準的な3DGSは輝度一定を前提とするため、複数カメラ間の露出差・ホワイトバランス差に脆弱だった。「階層的露出補正パイプライン」と「物体認識SSIM最適化」を統合することで解決。

---

### 1-7. VolSplat — ボクセル型フィードフォワード3DGS（視点依存性を根本解決）

- **ソース**: [arXiv 2509.19297](https://arxiv.org/abs/2509.19297) | [GitHub](https://github.com/ziplab/VolSplat)
- **更新**: 2026年3月
- **フィールド**: フィードフォワード3DGS・新視点合成

**何ができるようになったか**  
カメラ入力から即座に3DGSを生成する「フィードフォワード」方式で、シーンごとの個別学習（最適化）なしでも高品質な新視点合成が可能に。RealEstate10K・ScanNetベンチマークで最高水準を記録。

**これまでの課題と解決策**  
従来の方式は「各ピクセル→1 Gaussian」という対応付けのため入力カメラ数依存・オクルージョン（物体が重なる箇所）に弱かった。VolSplatは「深度推定→3Dボクセルグリッド→スパース3Dデコーダー」という新パイプラインでこれを解決し、視点一貫性を大幅改善。

---

### 1-8. BiSplat-WRF — 電波（RF信号）の3D空間分布をGaussian Splattingで再構成

- **ソース**: [arXiv 2604.25945](https://arxiv.org/abs/2604.25945)
- **投稿日**: 2026年4月17日
- **フィールド**: 無線通信・RF場再構成（ニッチだが驚き）

**何ができるようになったか**  
光の3DGSと同じ発想で、電波（RF信号）の3D空間分布（Wireless Radiance Field）を再構成。送信機の位置を指定すると、受信機位置での電波特性を予測できる。5Gや次世代無線ネットワークの精密シミュレーションへの応用が期待される。

**これまでの課題と解決策**  
3D空間のRF信号は電磁波の相互干渉・散乱が複雑で既存手法では不十分だった。平面状のGaussian Primitive（2D平面GS）と双線形空間変換器（BST）を組み合わせ、電磁波の長距離依存性をグローバルにモデリング。「光以外の波動現象」へのGS拡張という意味で先駆的。

---

## 2. 業界ニュース

### 2-1. Sony XYN Spatial Capture Solution — ソニーがGS活用プロ向けソリューションを正式発売

- **ソース**: [Sony プレスリリース](https://sony.mediaroom.com/2026-04-15-Sony-Electronics-Announces-the-Launch-of-XYNs-Spatial-Capture-Solution-for-Professionals-Generating-High-Quality-3DCG-Assets-from-Real-World-Spaces) | [Radiance Fields](https://radiancefields.com/sony-xyn-launches-spatial-capture-solution-with-gaussian-splatting)
- **発表日**: 2026年4月15日

**概要**  
ソニーのXYNブランドが「Spatial Capture Solution」を正式発表。3つのソフトウェアで構成される：
- **XYN Spatial Scan Navi**（スマホアプリ）：撮影アシスタント
- **XYN Spatial Scan**（クラウドアプリ）：3DGSアセット自動生成
- **XYN Spatial Renderer Plugin**（レンダリングプラグイン）：LEDウォールへの高品質・安定投影

NAB Show 2026（ラスベガス）で展示済み。米国での一般提供は2026年夏の予定。映画・ドラマ・CMの映像制作現場での採用を主軸に、将来はゲーム・建築・文化財保存への展開も計画中。

---

### 2-2. Cesium 3D Gaussian Splats with Hierarchical LOD — 都市スケールGSストリーミングが実現

- **ソース**: [Cesium Blog](https://cesium.com/blog/2026/04/27/3d-gaussian-splats-lod/)
- **発表日**: 2026年4月27日

**概要**  
Cesiumが3D Tiles + glTFの業界標準を活用して、大規模GSデータセットを「近いところは高精細・遠いところは低精細」でストリーミングできるLOD（Level of Detail）システムを実装。

主なポイント：
- Cesium ion / CesiumJS / Cesium for Unrealに対応
- glTF拡張「KHR_gaussian_splatting + KHR_gaussian_splatting_compression_spz」で最大90%圧縮
- 写真アップロード→3D Tileset自動生成のエンドツーエンドパイプライン
- Khronos / OGC / Esri / Niantic Spatialとの業界協力体制

---

### 2-3. Preferred Networks 3DGS UE5 Plugin 正式発表

- **ソース**: [Radiance Fields](https://radiancefields.com/preferred-networks-inc-announces-3dgs-unreal-engine-5-plugin) | [VP-land](https://www.vp-land.com/p/preferred-networks-brings-photorealistic-3d-environments-to-unreal-engine-5-with-new-gaussian-splatt)
- **発表日**: 2026年4月

**概要**  
Preferred Networks（PFN）がUnreal Engine 5向けの独自3DGSプラグインを正式発表。バーチャルプロダクション向けに特化した機能を搭載。

主な特徴：
- **指向性・点光源リライティング**：3DGSシーン内で動的な照明変更が可能
- **被写界深度（DoF）制御**：映画的なフォーカスコントロール
- **シャドウキャスト・シャドウレシーブ**：より自然な影表現

TBS日曜劇場「GIFT」での実績をベースに、Unity対応も検討中。価格は未公開。

---

## 3. コミュニティ・SNS話題

### 3-1. 3DISE Conference Prague 2026 — 本日・明日開催、GS業界最前線

- **ソース**: [3DISE公式サイト](https://3dise.com/)
- **開催日**: 2026年5月5〜6日（プラハ）

**概要**  
「3D Immersive & Spatial Experience（3DISE）」カンファレンス第2回がプラハで開幕。フォトグラメトリ・レーザースキャン・GS・没入型テクノロジーの業界リーダーが集結。GS専門パネル「Gaussian Splatting in tech and creative industry」ではRadiance Fields創設者Michael Rubloff、他業界著名人が登壇。

---

### 3-2. Cesium May 2026 リリース — GS関連クラッシュバグ修正

- **ソース**: [Cesium May 2026 Releases](https://cesium.com/blog/2026/05/01/cesium-releases-in-may-2026/)
- **公開日**: 2026年5月1日

**概要**  
Cesiumの5月定期リリース。Cesium for UnrealでGS点が際限なく蓄積してクラッシュするバグを修正（v2.26.0対応）。大規模GSシーンを使っている開発者は即時アップデート推奨。

---

### 3-3. PC Gamer「これが私の新お気に入り」— フォトリアルFPSブラウザゲームにGSが活用

- **ソース**: [PC Gamer](https://www.pcgamer.com/hardware/this-photorealistic-fps-runs-in-browser-thanks-to-gaussian-splatting-which-is-now-my-new-favorite-thing/)

**概要**  
PC Gamer誌がGaussian Splattingを使ったフォトリアルなブラウザFPSゲームを大きく特集。「これが私の新しいお気に入り」と大々的に紹介し、一般ゲーマー層へのGS認知が拡大中。「CGI以来最大の革命」という業界内の評価が、一般メディアへと浸透しつつある重要な兆候。

---

## 4. 開発者向けインサイト — 今すぐ対応すべき動向

### ✅ 今すぐ使えるもの

| 項目 | 内容 | 優先度 |
|------|------|--------|
| Cesium for Unreal v2.26.0 更新 | GS点蓄積クラッシュバグ修正済み | 🔴 即時対応 |
| Cesium ion LOD付きGSデプロイ | 写真→自動3D Tileset生成パイプラインが整備 | 🟡 高 |
| VolSplat コード確認 | シーンごと学習不要のフィードフォワードGS | 🟡 高 |
| GS-2M（GitHub公開） | Eurographics 2026採択、メッシュ再構成向け | 🟢 中 |

### 📊 注視すべきトレンド

1. **暗所3DGS の実用化加速**  
   ELoG-GS・MERID-GSと低照度対応論文が同週2本登場。防犯・医療・夜間ドローン応用案件がある場合は、両コードのリリースを注視。

2. **Sony XYN の業界標準化リスク**  
   ソニーがLEDウォールパイプライン向けGSエコシステムを形成しつつある。映像制作・広告制作案件での採用評価を今から開始すべき時期。

3. **Cesium + glTF KHR標準の収束**  
   Cesium / Khronos / OGC / Esri / Niantic Spatialが連携しGS業界標準化が急速に進行中。地理空間・インフラ可視化案件はCesiumエコシステムへの移行を強く推奨。

4. **RF（電波）へのGS拡張**  
   BiSplat-WRFは「光以外の波動現象」へのGS応用の先駆け。テレコム・IoT・自動運転用センサーフュージョン分野での応用研究が今後増加する見通し。

---

*レポート生成日: 2026-05-04 | 収集ソース: arXiv, MDPI, GitHub, radiancefields.com, CGChannel, Sony公式, Cesium公式, PC Gamer*
