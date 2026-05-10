# 3DGS & 4D生成 デイリーレポート｜2026年5月10日

**新規収集件数: 17件**（論文12件 / 業界ニュース3件 / コミュニティ2件）

---

## 📌 今日の注目トレンド TOP5

1. **4DGS×SLAM統合が加速** — CVPR 2026採択のRU4D-SLAM・Flow4DGS-SLAMなど複数の4D Gaussian SLAM手法が続々登場。動的環境でのリアルタイム3D再構成が現実に近づく
2. **GS応用の新フロンティア：天気予報・電波場・炎合成** — 研究対象が純粋な3D描画を超え、気象予報AI・無線通信・リアルタイム燃焼シミュレーションへ広がる
3. **ビュー一貫性&高速学習の新アプローチ** — Softmax-GS・Structure-Aware Densificationなど根本的な最適化改善が相次ぎ、3DGSの画質・速度の底上げが続く
4. **ゲーム業界への商用GS採用が本格化** — 商用PCゲーム「Snap & Grab」がGSによるフォトリアリスティック環境を実装。AMD GPUでの3DGSサポートも開始
5. **3DGS改ざん検出という新課題** — Fake3DGSが3D操作・ディープフェイク問題を提起。GS技術の社会的影響が拡大中

---

## 📑 注目論文（重要度：高）

### 1. CoherentRaster — ライトフィールドディスプレイ向けリアルタイムGS

- **arXiv:** https://arxiv.org/abs/2605.04509
- **分野:** 3DGS・ライトフィールドディスプレイ
- **何ができるようになったか:**
  - 特殊な立体ディスプレイ（ライトフィールドディスプレイ）でGaussian Splattingをリアルタイム描画可能に
  - 一般向け家庭用GPUで高品質なライトフィールド映像を実現
- **課題と解決:**
  - 立体ディスプレイは多視点画像を同時生成する必要がありGPU負荷が膨大
  - 隣接視点間でGaussian属性を共有再利用（Cross-view Coherent Attribute Reuse）し冗長計算を排除
  - ViewcoherentRemappingでGPUスレッドのメモリ効率を回復

---

### 2. GOR-IS — 3D物体除去（固有空間内処理）⭐ CVPR 2026 Highlight

- **arXiv:** https://arxiv.org/abs/2605.00498
- **分野:** 3DGS・シーン編集
- **何ができるようになったか:**
  - 3DGSシーンから任意の物体をリアルに消去し、背後の空間を自然に補完
  - 映画VFX・不動産撮影・デジタルツインでの不要物体消去が劇的に品質向上
- **課題と解決:**
  - 既存手法は大域照明を無視し不自然な影・反射が残る
  - 固有空間（Intrinsic Space：照明と材質を分離した空間）内で除去処理することで照明も一貫修正

---

### 3. FieryGS — 炎・燃焼の物理統合GS合成 ⭐ ICLR 2026

- **OpenReview:** https://openreview.net/forum?id=ziKFH7whvy
- **ICLR:** https://iclr.cc/virtual/2026/poster/10006432
- **分野:** 3DGS・物理シミュレーション・特殊効果
- **何ができるようになったか:**
  - リアルな炎・煙・表面炭化など燃焼現象を3DGSシーンに物理的に正確合成
  - 炎の強さ・風向・着火点をパラメーター制御可能
- **課題と解決:**
  - CGの炎は物理的整合性が低く、ユーザー制御も困難
  - マルチモーダルLLMで材料特性を自動推論し体積燃焼シミュレーションとGSレンダラーを統合

---

### 4. Structure-Aware Densification — 3DGS学習の高速収束

- **arXiv:** https://arxiv.org/abs/2604.28016
- **分野:** 3DGS最適化・高速化
- **何ができるようになったか:**
  - 同じ画質で3DGSの学習時間を大幅短縮
- **課題と解決:**
  - 3DGSは品質に達するまで多数の反復が必要
  - Densification（ガウシアン点群の増殖）を構造情報に基づき早期実施することで収束を高速化

---

### 5. Softmax-GS — ビュー一貫性と輪郭品質の統一改善

- **arXiv:** https://arxiv.org/abs/2604.27437
- **分野:** 3DGS最適化・描画品質
- **何ができるようになったか:**
  - 視点変化でのちらつきや輪郭ぼけをゼロに近づける統一フレームワーク
  - 再構成品質・パラメーター効率ともにSoTA達成
- **課題と解決:**
  - Gaussianが重なる領域でアーティファクト発生
  - softmaxで競合学習させ「なめらかなブレンド↔くっきりな境界」を連続パラメーター制御

---

### 6. Flow4DGS-SLAM — 光学フロー誘導の4D GS SLAM

- **arXiv:** https://arxiv.org/abs/2604.22339
- **分野:** 4DGS・SLAM・ロボット
- **何ができるようになったか:**
  - 動く人・車がいる動的シーンでもリアルタイムに3Dマップを構築
  - 追跡・動的再構成・学習効率の全項目でSoTA
- **課題と解決:**
  - 動的物体があると静的・動的領域の区別が困難でSLAM精度が劣化
  - 光学フロー + エゴモーション分解で領域を自動特定し、GMM（ガウス混合モデル）で動的Gaussianの時間変化を学習

---

### 7. RU4D-SLAM — 不確実性再重み付けによる4D GS SLAM ⭐ CVPR 2026 Findings

- **arXiv:** https://arxiv.org/abs/2602.20807
- **Project:** https://ru4d-slam.github.io/
- **分野:** 4DGS・SLAM・ロボット
- **何ができるようになったか:**
  - 動的環境でカメラが動きながら4Dシーン（動く物体含む）を同時再構成
  - TUMデータで平均軌跡誤差1.69cmを達成（ベンチマーク最小）
- **課題と解決:**
  - 動く物体でカメラ追跡が乱れる
  - Reweighted Uncertainty Mask（RUM）で各ピクセルの信頼性を動的に推定し、不安定部分の影響を重み調整

---

### 8. PAGaS — 1自由度ピクセル整合GS深度推定

- **arXiv:** https://arxiv.org/abs/2604.22129
- **分野:** 3DGS・深度推定
- **何ができるようになったか:**
  - 従来より高速・省メモリで高精細な深度マップを生成
- **課題と解決:**
  - 通常の3DGSは1Gaussianに59パラメーター → 各ピクセルに1Gaussianを配置し深度のみ（1DoF）を最適化するラジカルな簡略化

---

### 9. BiSplat-WRF — 電波場再構成への3DGS応用

- **arXiv:** https://arxiv.org/abs/2604.25945
- **分野:** 3DGS・無線通信・電波工学
- **何ができるようになったか:**
  - 部屋や屋外空間の電波強度・伝搬特性を3Dで連続的に予測・可視化
  - 基地局配置・Wi-Fi設計・自動運転の無線マップに応用可能
- **課題と解決:**
  - 従来の電波場推定は空間解像度・精度に限界
  - 平面型Gaussian + 双線形空間変換器（BST）で電磁散乱や遠距離依存性を考慮

---

### 10. Generative 3DGS for Atmospheric Forecasting — GS×天気予報AI

- **arXiv:** https://arxiv.org/abs/2604.07928
- **分野:** 3DGS・気象科学・AI
- **何ができるようになったか:**
  - 3DGSの技術で任意解像度の天気予報を世界初実現
  - ERA5データで87種気象変数を任意解像度で中期予報
- **課題と解決:**
  - 気象モデルは固定解像度に縛られる
  - 緯度経度の各格子点をGaussianの中心として扱い、気象変数をGSSA-ViTで生成的に予測

---

### 11. Fake3DGS — 3D改ざん検出ベンチマーク（セキュリティ）

- **arXiv:** https://arxiv.org/abs/2604.27590
- **分野:** 3DGS・セキュリティ・フォレンジック
- **何ができるようになったか:**
  - GS改ざん3Dシーンから作られた偽画像を検出する技術の基盤整備
  - 多視点整合性+GS表現を使った3D対応検出器を提案
- **課題と解決:**
  - 3DGSで3Dシーンを操作→リレンダリングで極めてリアルな偽画像が生成可能
  - 既存の2D偽造検出器が無力と判明 → 3D対応ベンチマークデータセットを構築し研究基盤を整備

---

### 12. In Depth We Trust — 単眼深度プライアの信頼性改善

- **arXiv:** https://arxiv.org/abs/2604.05715
- **分野:** 3DGS・深度推定・モバイル3D再構成
- **何ができるようになったか:**
  - スマホ1台で撮影した動画から、アーティファクトのない高品質な3DGSを生成
- **課題と解決:**
  - 単眼深度推定モデルはスケール曖昧性・多視点不整合があり、そのまま使うと3DGSが歪む
  - 不確実な幾何領域のみを特定して選択的に深度正則化を適用

---

## 📰 業界ニュース

### 13. Snap & Grab — 商用PCゲームが3DGSを正式採用

- **記事:** https://www.ingamenews.com/2026/05/gaussian-splatting-in-snap-grab-2026.html
- **分野:** ゲーム開発・商用採用
- **概要:** Snap Inc.エンジニアが開発した泥棒シム「Snap & Grab」がGS描画を商用ゲームで本格採用。廃墟スキャンデータをGSに変換し、自作ツールでコリジョンメッシュを自動生成。大型AAAスタジオ頼みだったフォトリアル背景が少人数チームでも実現可能に

---

### 14. Emergent Vision Technologies — 36カメラ4DGSアレイをNAB 2026で披露

- **記事:** https://www.tvtechnology.com/production/emergent-vision-unveils-4d-gaussian-splatting-and-high-speed-cameras
- **分野:** 4DGS・ボリュームキャプチャ・放送
- **概要:** 36台の高解像度/高速カメラアレイ + 複数サーバーGPUDirect処理 + NVIDIA DGX Spark統合でリアルタイム4DGSキャプチャシステムを展示。スポーツ・コンサート・XRイベントへの商用展開に向けた動き

---

### 15. AMD ROCm + Street Gaussians — 3DGSがAMD GPUで動作可能に

- **記事:** https://rocm.blogs.amd.com/artificial-intelligence/street-gaussians/README.html
- **分野:** 3DGS・GPU対応拡張・自動運転
- **概要:** 自動運転シミュレーション用Street GaussiansがgsplatのAMD ROCmサポートにより対応。これまでNVIDIA GPU前提だった3DGS開発環境がAMD環境へ拡張され、研究機関・スタートアップのGPU選択肢が広がる

---

## 🌐 コミュニティ・SNS話題

### 16. SOG (Spatially Ordered Gaussians) — PlayCanvas製超圧縮GSフォーマット

- **Blog:** https://blog.playcanvas.com/playcanvas-open-sources-sog-format-for-gaussian-splatting/
- **仕様:** https://developer.playcanvas.com/user-manual/gaussian-splatting/formats/sog/
- **分野:** 3DGS圧縮・Webフォーマット
- **概要:** PlayCanvasがSOGフォーマットをオープンソース公開。PLYより15〜20倍小さい圧縮率（WebP形式エンコード＋Mortonオーダー）を実現。SplatTransform CLIでPLY→SOG変換可能。Webモバイル向けGS配信の新標準候補として開発者間で注目

---

### 17. GSAC — スマホ動画1本でUnity統合フォトリアルアバターを40分で生成（IEEE 2026公式出版）

- **arXiv:** https://arxiv.org/abs/2504.12999
- **GitHub:** https://github.com/VU-RASL/GSAC
- **IEEE:** https://ieeexplore.ieee.org/document/11172560/
- **分野:** GS・アバター生成・Unity統合
- **概要:** スマートフォンで撮影した普通の動画のみから表情付きGSアバターを40分で自動生成するオープンソースパイプライン。Unityネイティブ統合済みでVR/ARアプリにそのまま組み込める。IEEE 2026で正式出版

---

## 🛠️ 開発者向けインサイト（今すぐ対応すべき動向）

| 優先度 | アクション | 参照 |
|--------|-----------|------|
| ⭐⭐⭐ | AMDユーザーはgsplat最新版でStreet Gaussiansを試す | ROCm Blog |
| ⭐⭐⭐ | WebアプリはSOGフォーマットへの移行を検討（15-20x圧縮） | PlayCanvas Dev Docs |
| ⭐⭐ | GSACパイプラインでUnity向けアバター開発を高速化 | GitHub: VU-RASL/GSAC |
| ⭐⭐ | 4DGS SLAM（RU4D-SLAM/Flow4DGS-SLAM）の動向を継続ウォッチ | CVPR 2026 |
| ⭐ | Fake3DGSの示すセキュリティリスクを把握し対策を検討 | arXiv:2604.27590 |

---

*生成日時: 2026-05-10 / 情報収集ソース: arXiv, ICLR 2026, CVPR 2026, CG Channel, TV Tech, AMD ROCm Blog, PlayCanvas Blog*
