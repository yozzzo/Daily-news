# 3DGS & 4D生成 デイリーレポート — 2026-06-14

**収集件数:** 17件（論文9件・ニュース5件・コミュニティ3件）
**過去配信との重複排除:** past_3dgs.json 照合済み（最終更新: 2026-05-30）

---

## 🔥 今日の注目トレンド TOP 5

1. **Apple WWDC 2026でGaussian Splattingがメインストリームへ** — iOS 27・macOS 27・visionOS 27でApple Maps FlyoverがGS技術に移行。Appleが世界規模で採用。
2. **ComfyUI + TripoSplatで誰でも画像→3DGSが可能に** — 1枚の画像から高品質な3D Gaussian Splatsを生成するオープンソースモデルがComfyUI Day 1統合。
3. **Gaussian Point Splatting（SIGGRAPH 2026）** — ソートなし・タイルなしで4.2億個のGaussianをRTX 4070Ti上でリアルタイム表示可能に。
4. **HiGS：元の3DGSより最大15.8倍高速・FastGS：100秒で学習** — レンダリングと学習の両面で大幅な高速化が実現。CVPRコードも公開。
5. **Cesium ion・ArcGIS Enterprise 12.1でGSが企業インフラに普及** — 測量・地図・GISツールへのGS統合が本格化。

---

## 📄 論文（重要度：高）

### 1. Gaussian Point Splatting（SIGGRAPH 2026）
- **リンク:** https://momentsingraphics.de/Siggraph2026.html / https://github.com/JorisAR/gaussian-point-splatting
- **分野:** レンダリング・超大規模シーン
- **概要:** 4億2500万個ものGaussianをNVIDIA RTX 4070Ti 1枚でリアルタイム表示できるようになった。従来のGSはGaussianを全て並べ替え（ソート）してから描画するため、数が増えるほど遅くなった。本手法は「ランダムな点サンプリング」と「確率的透明度」を組み合わせることでソートが不要に。GPU並列処理も均等に分散できるため、超大規模シーンでも安定して高速動作する。
- **発表:** SIGGRAPH 2026（ACM Trans. Graphics 45, 4）/ 2026-07-20発表予定・コード公開済み

### 2. HiGS — 元の3DGSより最大15.8倍高速レンダリング
- **リンク:** https://arxiv.org/abs/2606.00352
- **分野:** リアルタイムレンダリング・高速化
- **概要:** 3DGSをリアルタイムで最大15.8倍高速に描画できるようになった。画質は同等を維持。従来のタイル分割レンダリングでは「大きいタイル→ソート効率よいが描画コスト高」「小さいタイル→描画効率よいがソートコスト高」というジレンマがあった。HiGSは「粗いタイルでソート・細かいタイルで描画」の2段階構造（階層タイル）を採用し、両方の効率を同時に得ることに成功。
- **投稿日:** 2026-05-29（arxiv 2606.00352）

### 3. FastGS: Training 3D Gaussian Splatting in 100 Seconds（CVPR 2026 Highlight・Gold Star賞）コード公開
- **リンク:** https://github.com/fastgs/FastGS / https://openaccess.thecvf.com/content/CVPR2026/html/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.html
- **分野:** 学習高速化
- **概要:** 通常30〜60分かかる3DGSの学習が、最短77秒（平均100秒）で完了するようになった。FastGSは「どのGaussianが複数アングルから一貫して重要か」を判断し、学習リソースを効率よく配分。平均2〜7倍の学習高速化を達成しつつ画質を維持。CVPR 2026でGold Star賞（計算効率分野最優秀）受賞。CVPR 2026（2026年6月・Denver）に合わせてGitHubでコード公開。

### 4. EvoGS — 木構造階層でGaussianを管理してストリーミング効率2.4倍向上
- **リンク:** https://arxiv.org/abs/2606.07179
- **分野:** ストリーミング・大規模シーン
- **概要:** 3DGSシーンのストリーミング配信が高効率になり、通信量を2.4倍削減、GPU VRAMも最大5.5倍削減できるようになった。大規模シーンを配信する際、Gaussianデータの冗長性が高く（65%以上が重複）課題だった。EvoGSはGaussianを「進化の木（Evolution Tree）」として親子関係で階層化し、段階的に詳細を追加するウェーブレット的な仕組みを採用。冗長性を25%以下に削減。
- **投稿日:** 2026-06-05（arxiv 2606.07179）

### 5. BEAST3D — 動物の3D行動を自動解析・脳活動とのマッピングを実現
- **リンク:** https://arxiv.org/abs/2606.02937
- **分野:** 科学応用・動物行動解析
- **概要:** 実験室で複数カメラで撮影した動物映像から、3D姿勢・行動を自動で解析し、脳の神経活動データと対応付けることができるようになった。わずか4台のカメラで動作。アノテーション不要の自己教師あり学習で、動物と背景を自動分離しながら3D Gaussianを生成する。
- **投稿日:** 2026-06-01（arxiv 2606.02937）

### 6. Unpaired RGB-Thermal Gaussian Splatting — キャリブレーションなしで可視光+熱画像を3D化
- **リンク:** https://arxiv.org/abs/2606.05491
- **分野:** マルチモーダル・センサー融合
- **概要:** 対応関係のない可視光カメラと熱センサーカメラの画像を組み合わせて3DGSを生成できるようになった。従来は精密なキャリブレーションが必須だった。新手法はVGGT（3Dフィードフォワードトランスフォーマー）で各カメラ姿勢を独立に推定し、Procrustes法で位置合わせ。工業検査・セキュリティ・夜間監視などに応用可能。
- **投稿日:** 2026-06-03（arxiv 2606.05491）

### 7. Multi-Spectral Gaussian Splatting with Neural Color Representation
- **リンク:** https://arxiv.org/abs/2506.03407 / https://meyerls.github.io/ms_splatting/
- **分野:** マルチスペクトル・センサー融合
- **概要:** 1つの3DGSモデルで可視光・熱・近赤外線など複数の波長帯を同時に再現できるようになった。Gaussianごとにニューラルネットワークで多スペクトル情報をエンコードし、浅いMLPでデコード。クロスモーダルなキャリブレーション不要。
- **投稿日:** 2026-06-03（arxiv 2506.03407）

### 8. Optimizing 3D GS via Point Cloud Upsampling — 深度ガイド点群補間で初期化を改善
- **リンク:** https://arxiv.org/abs/2606.00450
- **分野:** 点群最適化・初期化改善
- **概要:** 深度マップを活用して点群を幾何学的に一貫した形で補間する手法を提案。線形補間・スプライン・MLS・ボロノイなど複数のアップサンプリング手法を評価し、深度ガイド点持ち上げが最も優れることを確認。点群の密度が低い場所でも3DGSの品質を維持。
- **投稿日:** 2026-05-30（arxiv 2606.00450）

### 9. TripoSplat（VAST AI）— 画像1枚から最大26万個の3D Gaussiansを生成
- **リンク:** https://github.com/VAST-AI-Research/TripoSplat
- **分野:** 生成AI・フィードフォワード3DGS
- **概要:** 1枚の写真から、任意の個数（最大262,144個）の3D Gaussian Splatsを秒単位で生成できるモデルがオープンソース（MITライセンス）で公開。「Density-Sampled Gaussians（DeG）」技術により必要な場所に必要なだけGaussianを配置する適応的手法を実現。SIGGRAPH 2026採択。

---

## 📰 業界ニュース

### 1. Apple WWDC 2026 — iOS 27・visionOS 27でGaussian Splattingが公式採用【最重要】
- **リンク:** https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade / https://developer.apple.com/documentation/visionos/gaussian-splats-on-visionos
- **概要:** 2026年6月8日のWWDCキーノートで、AppleがApple Maps FlyoverにGaussian Splatting技術を採用すると発表。iOS 27 / macOS 27 / visionOS 27（2026年秋リリース予定）から世界中の都市の3D表示がフォトグラメトリからGSに移行。visionOS 27のRealityKitでは開発者向けにGaussian Splat APIも提供開始。

### 2. ComfyUI v0.23.0 + TripoSplat統合 — ノーコードで画像→3DGS生成が可能に
- **リンク:** https://radiancefields.com/comfyui-adds-native-3d-gaussian-splat-generation-with-triposplat / https://blog.comfy.org/p/bringing-native-support-for-3d-gaussian
- **概要:** ComfyUI v0.23.0でGAUSSIAN型を標準サポート。TripoSplatモデルとの統合により、画像ノードをつなぐだけで3D GaussianSplatsを生成できるように。ゲーム開発・AR/VR・Eコマース向けアセット量産パイプラインに直結。

### 3. Cesium ion June 2026リリース — メッシュ不要のGS/点群パイプラインが実現
- **リンク:** https://cesium.com/blog/2026/06/01/cesium-releases-in-june-2026/
- **概要:** Cesium ionの2026年6月リリースで、再構成ジョブにメッシュ生成が不要になった。点群のみ・GS専用パイプラインが独立実行可能。glTF拡張「KHR_gaussian_splatting」最新仕様に対応した3D Tilesタイルセット出力も実装。

### 4. ArcGIS Enterprise 12.1 — 企業内GISでGaussian Splatが本格対応
- **リンク:** https://www.esri.com/arcgis-blog/products/arcgis-enterprise/announcements/whats-new-in-arcgis-enterprise-12-1
- **概要:** ESRIのエンタープライズ版12.1で、Gaussian Splat LayerがScene Viewerで正式サポート。オンプレミス環境でもGS共有・表示が可能になり、セキュリティ要件の厳しい組織でも導入しやすくなった。

### 5. Irrealix After Effects & Nuke プラグイン更新 — Apple Sharp-ML出力に対応
- **リンク:** https://radiancefields.com/irrealix-updates-after-effects-and-nuke-plugin-for-gaussian-splatting / https://irrealix.com/plugin/gaussian-splatting
- **概要:** VFXコンポジットソフト向けGSプラグインが更新。AppleのSharp-ML（高速単眼GS生成パイプライン）が出力する.plyファイルを直接インポート可能に。iPhone/iPadで撮影・生成したGSをそのままプロVFXワークフローに使えるようになった。

---

## 💬 コミュニティ・SNS話題

### 1. FastGS 公式コード公開 — CVPR 2026 Gold Star受賞作がGitHubで誰でも使えるに
- **リンク:** https://github.com/fastgs/FastGS
- **概要:** CVPR 2026 Highlight選定＆Compute Gold Star受賞のFastGSがGitHubでオープンソース公開。シンプルで読みやすいコード設計で既存パイプラインへの組み込みが容易。Reddit r/GaussianSplattingでも大きく話題に。

### 2. Triangle Splatting が勢いを増す — Babylon.js v9でブラウザ対応が拡大
- **リンク:** https://radiancefields.substack.com/p/triangle-splatting-gaining-steam / https://trianglesplatting.github.io/
- **概要:** 「三角形メッシュ」でGaussian Splat的な表現を実現する「Triangle Splatting」がBabylon.js v9でサポート予定。GPUが最も得意とする三角形形状のため、既存ゲームエンジン・WebGLとの相性抜群。standard PLYファイルで出力されるため既存ツールチェーンがそのまま使える。コードはまだ未公開だが注目度急上昇中。

### 3. Gaussian Point Splatting コード公開（SIGGRAPH 2026）
- **リンク:** https://github.com/JorisAR/gaussian-point-splatting
- **概要:** 4.2億個のGaussianをリアルタイム表示可能にした手法のコードがSIGGRAPH 2026に合わせてGitHubに公開。ソート処理が不要な全く新しいアーキテクチャで、CGコミュニティでは「屋外大規模シーンの次世代標準になりえる」との声。

---

## 🛠️ 開発者向けインサイト

1. **【最優先】Apple visionOS 27 RealityKit GS API** — visionOS 27 Betaでの開発を今から検討。地図・観光・不動産アプリ開発者はiOS 27 GS移行に早めに対応。
2. **【すぐ使える】TripoSplat + ComfyUI** — MITライセンス・GPU不要（fal.ai経由）で商用利用可能な画像→3DGSパイプラインを即構築可能。
3. **【学習高速化】FastGS/HiGS/EvoGSの3段構成** — 学習→レンダリング→ストリーミングの全ボトルネックを解消できる組み合わせ。
4. **【企業向け】Cesium ion + ArcGIS Enterprise 12.1** — 建設・インフラ・GIS部門での3DGS本格導入のタイミングが到来。オンプレミス運用も可能に。
5. **【研究者向け】Gaussian Point Splatting** — ソートフリーアーキテクチャによる4.2億Gaussian対応のGitHubコードを今すぐ検証。

---

*Generated by 3DGS Daily Report Automation — 2026-06-14*
