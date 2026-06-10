# 3DGS & 4D生成 デイリーレポート｜2026-06-10

> **配信数：** 論文 8件 ／ 業界ニュース 6件 ／ コミュニティ 2件  
> **総計：16件**（過去掲載済み重複を除外済み）

---

## 🔥 今日の注目トレンド TOP 5

1. **Apple Maps が Gaussian Splatting を正式採用（WWDC 2026）** — 数億人のスマホで3DGSが日常に
2. **Houdini 22 が GS 生成・リギング・アニメーション対応予告** — 主流DCCツールへの本格統合
3. **ComfyUI v0.23.0 TripoSplat** — 写真1枚から3DGSをノーコードで即生成
4. **FastGS（CVPR 2026 Highlight）コード公開** — 3DGS学習が100秒に、しかも無料OSS
5. **EvoGS** — ストリーミング向けGSでVRAMを5.5倍削減、転送量2.4倍削減

---

## 📄 注目論文

### ★★★ 1. FastGS — 3DGS学習を「100秒」で完了 [CVPR 2026 Highlight / Compute Gold Star]
- **概要：** これまで数十分〜数時間かかっていた3DGS（3D空間の学習）を、**わずか100秒**で完了させる汎用フレームワーク。複数の視点画像でGaussianの重要度を測り、無駄なGaussianを積極的に削除することで学習を大幅高速化。バニラ3DGSの**15.45倍速**、既存最速手法の3.29倍速を達成。動的シーン・SLAM・スパースビューなど幅広い設定に適用可能。
- **何が変わる：** 研究者だけでなく現場のエンジニアも「3DGSを試してみる」コストが激減。CVPR最優秀賞候補（Compute Gold Star）受賞。コードはMITライセンスでGitHubに公開済み。
- **リンク：** [論文 arXiv:2511.04283](https://arxiv.org/abs/2511.04283) ／ [GitHub](https://github.com/fastgs/FastGS) ／ [CVPR 2026 Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.html)

---

### ★★★ 2. EvoGS — ストリーミング最適化の「進化の木」型GS表現 [June 5, 2026]
- **概要：** Gaussian Splattingの最大の弱点「重複するGaussianが多すぎる（冗長率65%超）」を、木構造（Evolution Tree）で解決。親Gaussianが子Gaussianを生成するウェーブレット風の階層構造で、細部を段階的に補完。ストリーミング送信時の転送量を最大**2.4倍削減**、GPU VRAM消費を**5.5倍削減**しつつ品質を維持。
- **何が変わる：** モバイルや低スペックPCへのGSストリーミングが現実的に。VR・WebGS・リアルタイムメタバースへの道が開ける。
- **リンク：** [arXiv:2606.07179](https://arxiv.org/abs/2606.07179)

---

### ★★★ 3. HiGS — リアルタイムGSを「2段階タイリング」で高速化 [arXiv:2606.00352]
- **概要：** 3DGSのリアルタイムレンダリングの瓶首「Gaussianの密度に応じた処理割り当て」を、粗いマクロタイル（区画分け）と細かいレンダリングタイル（描画）の2段階に分離するHiGS（Hierarchically Tiled GS）を提案。GPU並列処理を密度に比例して最適化。
- **何が変わる：** スマホ・VRデバイスでのリアルタイムGS表示の実現可能性が大幅向上。
- **リンク：** [arXiv:2606.00352](https://arxiv.org/abs/2606.00352)

---

### ★★ 4. LEGS — ラプラシアンで画質を底上げ [June 6, 2026]
- **概要：** 既存の3DGSは「1次勾配（輝度変化の方向）」で学習を誘導するが、本論文はより構造を捉えやすい「2次ラプラシアン（輝度変化のカーブ）」を使うことで、最大**+1.68 dB PSNR**の画質改善を実現。損失関数の非線形重み付けも併用。
- **何が変わる：** 既存の3DGSパイプラインへの差し込みで即適用できる汎用改善手法。
- **リンク：** [arXiv:2606.07932](https://arxiv.org/abs/2606.07932)

---

### ★★ 5. SparseStreet — 自動運転向けスパースGSストリーミング [arXiv:2606.03909]
- **概要：** 自動運転シミュレーション用に街路シーンを3DGS化する際、冗長なGaussianをノード認識プルーニングと背景圧縮の2段階で削減。International Conference on Multimedia Retrieval 2026 採択。リアルタイム動的シーンシミュレーションに対応。
- **何が変わる：** 自動運転AIの訓練・テスト用3Dシミュレーター生成コストを大幅削減。
- **リンク：** [arXiv:2606.03909](https://arxiv.org/html/2606.03909v1)

---

### ★★ 6. AtlasGS — GS技術で脳MRIの「解像度不揃い問題」を解決 [arXiv:2606.02961]
- **概要：** MRI（磁気共鳴画像）は撮影方向によって解像度が大きく異なる（例：スライス方向が粗い）という医療上の課題をGSで解決。特定被験者の解剖学的構造をGaussianで学習し、T2強調・FLAIR・DWI・ASLなど複数モダリティへ再適用。超解像品質で最先端を達成。
- **何が変わる：** 医療画像診断の精度向上・低被曝での3D再構成が可能に。GS技術の医療応用が加速。
- **リンク：** [arXiv:2606.02961](https://arxiv.org/abs/2606.02961)

---

### ★★ 7. PolarGuide-GSDR — 偏光カメラで鏡面反射シーンを高精度3D化 [CVPR 2026]
- **概要：** ガラスや金属など光が反射する素材（鏡面反射）は3DGSの苦手分野だったが、偏光カメラ（光の振動方向で情報を取得）とGSの相互補完を実現。偏光情報でGSの法線・球面調和関数表現を強化し、環境マップや材質の事前仮定なしに反射を忠実再現。
- **何が変わる：** 工場設備・宝飾品・自動車など光沢素材の3D化がより正確に。
- **リンク：** [arXiv:2512.02664](https://arxiv.org/abs/2512.02664) ／ [CVPR 2026 Poster](https://cvpr.thecvf.com/virtual/2026/poster/36441)

---

### ★ 8. Chorus — 複数の2D基盤モデルを教師にしたフィードフォワード3DGS [CVPR 2026]
- **概要：** 単一の2D基盤モデルの弱点を補うため、複数の2D大規模モデルから「蒸留」して統合的なシーンエンコーダーを学習するMulti-teacher Pretraining Framework。推論時に新たな学習不要でGSシーンを即生成（フィードフォワード）。
- **何が変わる：** 写真数枚から「最初から学習なし」で高品質3DGSシーンを一発生成できる可能性。
- **リンク：** [CVPR 2026 Highlights](https://cvpr.thecvf.com/virtual/2026/events/Highlights2026)

---

## 📰 業界ニュース

### ★★★ 9. Apple、WWDC 2026でApple MapsへのGS統合を発表 [June 8, 2026]
- **概要：** WWDC 2026基調講演でAppleが「Apple Maps Flyover」のGaussian Splatting対応を正式発表。従来のフォトグラメトリー（写真測量）で起きていた「ブロッコリー状の木」「溶けた電線」などのアーティファクトを一掃。新たな航空写真とApple Visual Intelligenceモデルで300都市以上を再処理予定。iOS 27 / macOS 27 / visionOS 27で秋提供開始。
- **なぜ重要：** Appleのマップは数億人が使用する世界最大規模のサービス。GS技術が「研究者の技術」から「スマホで誰でも日常的に使う技術」へ転換する歴史的な瞬間。GoogleはすでにNeRFベースのImmersive Viewを展開済みだが、GSはNeRFより軽量でモバイル向き。
- **リンク：** [Radiance Fields](https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade) ／ [TechRadar](https://www.techradar.com/computing/software/apple-maps-has-a-huge-ios-27-upgrade-on-the-way-for-flyover-that-will-help-you-see-cities-around-the-world-like-never-before-and-users-think-its-down-to-gaussian-splatting-the-next-big-3d-photography-craze) ／ [9to5Mac](https://pasqualepillitteri.it/en/news/4534/apple-maps-3d-gaussian-splatting-wwdc-2026)

---

### ★★★ 10. Houdini 22 — GS生成・再照明・リギング・アニメーション対応のスニークピーク [June 2026]
- **概要：** 映像・VFX業界の標準ツール「Houdini」の次期バージョン（Houdini 22）で、GS生成・再照明・リギング・アニメーション機能が追加予定とスニークピーク映像で判明。TOPs（Task Operators）でGSトレーニングを自動化し、KarmaレンダラーでGSをレンダリング可能に。さらにリグ付き3DキャラクターをGS化してアニメーション適用する映像も公開。詳細はJune 22のSideFXキーノートで発表予定。
- **なぜ重要：** Blender・Maya・Maxと並ぶ主流DCCツールへのネイティブGS対応は業界標準ワークフローへの正式組み込みを意味する。映画・ゲーム・CMなど大規模制作へGSが本格導入される転換点。
- **リンク：** [CG Channel](https://www.cgchannel.com/2026/06/sneak-peek-houdini-22/) ／ [SideFX](https://www.sidefx.com/community/houdini-22-sneak-peek/) ／ [80.lv](https://80.lv/articles/get-a-first-look-at-houdini-22)

---

### ★★★ 11. ComfyUI v0.23.0 — 写真1枚からネイティブでGS生成（TripoSplat統合）[June 1, 2026]
- **概要：** AI画像生成ツールとして世界最大規模のユーザーベースを持つComfyUI v0.23.0で、**GAUSSIANネイティブ型**と**GS操作ノード群**が正式追加。VAST-AI開発の「TripoSplat」（DINOv3 + Flux2 VAE + フロー一致デノイザー + 八叉木Gaussianデコーダーの組み合わせ）をDay 1から統合。1枚の写真をノードに接続するだけで`.ply`, `.splat`, `.spz`, `.ksplat`形式の3DGSアセットが出力される。
- **なぜ重要：** 世界中の何百万ものComfyUIユーザーが今日からGS生成を試せる。外部ツール・プログラミング知識不要。GS生成のメインストリーム化を加速。
- **リンク：** [ComfyUI Blog](https://blog.comfy.org/p/bringing-native-support-for-3d-gaussian) ／ [ComfyUI Docs Changelog](https://docs.comfy.org/changelog)

---

### ★★ 12. 3DGS Render 5.0 for Blender — GSオブジェクトをアーマチュアでアニメーション可能に [June 2026]
- **概要：** KIRI Engine製の無料BlenderアドオンがV5.0に更新。最大の新機能は「プロキシメッシュ経由のアニメーション転送」。従来の3Dキャラクターと同じようにアーマチュア（骨格）でリグを組んで動かし、その変形をGSオブジェクトに焼き付け（Bake）られる。PLYシーケンスとして書き出し、他ソフトへ持ち込み可能。Blender 5.1対応、Apache 2.0ライセンスで無料公開。
- **なぜ重要：** これまでGSは「静止シーン」が主体だったが、標準的なアニメーションワークフローで動くGSキャラクターが作れるようになった。映像・ゲームへの応用が格段に容易化。（現時点では実験的機能、パフォーマンス改善余地あり）
- **リンク：** [CG Channel](https://www.cgchannel.com/2026/06/3dgs-render-5-0-lets-you-animate-gaussian-splats-inside-blender/) ／ [KIRI Engine](https://www.kiriengine.app/3d-tools/3dgs-render) ／ [GitHub](https://github.com/Kiri-Innovation/3dgs-render-blender-addon)

---

### ★★ 13. ArcGIS Enterprise 12.1 — 組織内インフラでGS可視化が初対応 [June 2026]
- **概要：** Esriの企業向け地理情報システム「ArcGIS Enterprise 12.1」がScene ViewerでGaussian Splat Layerをサポート。これまでArcGIS Onlineのみだったが、自社サーバー（オンプレミス）環境でのGS可視化が可能に。インフラ設備・建設現場・都市モデルなどの詳細確認用途で活用できる。
- **なぜ重要：** 政府機関・建設・インフラ分野など「クラウドに上げられない」組織がGSを本格導入できるようになった。測量・GIS分野への普及が加速。
- **リンク：** [Esri ArcGIS Blog](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/announcements/whats-new-in-arcgis-enterprise-12-1) ／ [ArcGIS Pro Docs](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/work-with-gaussian-splat-layers.htm)

---

### ★★ 14. Splatware — 撮影→学習→販売まで一気通貫のGSプラットフォームが正式ローンチ [2026]
- **概要：** ブラウザ完結型のGSエンドツーエンドプラットフォーム「Splatware」が正式サービス開始。スマホ・DSLR・ドローン・360°カメラで撮った写真・動画をアップロードするだけでGSモデルを生成し、マーケットプレイスで販売・ライセンス提供できる。Blender・UE・Unity向けの統合ガイドも提供。無料〜Pro〜Enterprise の料金体系。
- **なぜ重要：** 技術的な参入障壁を一気に下げ、3Dアーティストや測量士がすぐに収益化できる仕組みを提供。GS版のSketchfabとも言える存在。
- **リンク：** [Radiance Fields](https://radiancefields.com/splatware-launches-as-an-end-to-end-gaussian-splatting-platform) ／ [Splatware](https://splatware.com)

---

## 💬 コミュニティ・SNS話題

### ★★★ 15. Apple GS採用でSNS・一般メディアに旋風 [June 8-10, 2026]
- **概要：** WWDCでのApple発表後、Twitter/XでRadiance Fields(@RadianceFields)の投稿が大拡散。TechRadar「これはBlenderより革命的」、Digg「Appleがブロッコリー木を葬った」など一般メディアも相次いで特集。「Gaussian Splatting」というキーワードが技術者以外にも広く認知された転換点となった。Instagramでも#gaussiansplatting タグの投稿が急増中。
- **なぜ重要：** これまで研究者・CG業界向けだったGSが一般消費者に認知され始めた。GS関連ツール・サービスへのユーザー流入増加が期待される。
- **リンク：** [X @RadianceFields](https://x.com/RadianceFields/status/2064043440350888050) ／ [TechRadar](https://www.techradar.com/computing/software/apple-maps-has-a-huge-ios-27-upgrade-on-the-way-for-flyover-that-will-help-you-see-cities-around-the-world-like-never-before-and-users-think-its-down-to-gaussian-splatting-the-next-big-3d-photography-craze) ／ [Digg](https://digg.com/ai/gizhzvon)

---

### ★★ 16. CVPR 2026 Denver コード公開ウェーブ（Week 2）[June 2026]
- **概要：** CVPR 2026（June 3〜8, Denver）の発表に合わせて、GS関連論文のコードが相次いでGitHubに公開。今週公開が確認された主要リポジトリ：FastGS（100秒学習）、Faster-GS（CVPR最適化フレームワーク）、PolarGuide-GSDR（反射シーン対応）等。Awesome3DGS GitHubの CVPR.md リストも随時更新中。
- **なぜ重要：** コード公開により研究成果が即座に実用化・派生研究に繋がる。開発者はこの時期に一気に新手法を試せるチャンス。
- **リンク：** [FastGS GitHub](https://github.com/fastgs/FastGS) ／ [Faster-GS GitHub](https://github.com/nerficg-project/faster-gaussian-splatting) ／ [Awesome3DGS CVPR.md](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md)

---

## 🛠️ 開発者向けインサイト

### 今週すぐ使えるツール
| ツール | 対応環境 | 注目機能 | リンク |
|--------|---------|---------|-------|
| **FastGS** | Python / CUDA | 100秒GS学習、既存コードへの差し込み可能 | [GitHub](https://github.com/fastgs/FastGS) |
| **ComfyUI v0.23.0** | Windows / Mac / Linux | 写真1枚→GSアセット生成、.ply/.spz/.ksplat出力 | [Changelog](https://docs.comfy.org/changelog) |
| **3DGS Render 5.0 (Blender)** | Blender 5.1 | GSオブジェクトにアーマチュアアニメーション | [GitHub](https://github.com/Kiri-Innovation/3dgs-render-blender-addon) |
| **Faster-GS** | CUDA | 2〜5倍高速・低VRAM、4D対応ブランチあり | [GitHub](https://github.com/nerficg-project/faster-gaussian-splatting) |
| **ArcGIS Enterprise 12.1** | Windows Server | 組織内GSレイヤー可視化 | [Docs](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/work-with-gaussian-splat-layers.htm) |

### 今後注目すべき動向
- **Apple GS大量需要化**：iOS 27秋リリースに向け、AppleはMaps用GS処理パイプラインを大規模展開予定。GSアセット・ツール需要が一気に拡大する可能性。
- **Houdini 22キーノート（June 22）**：SideFXが詳細発表予定。映像・VFX業界向けGSワークフローが一気に標準化される可能性大。
- **CVPR 2026論文コード公開ラッシュ継続**：今週末にかけてさらに多数のGS関連コードが公開される見通し。Awesome3DGS CVPR.mdを定期チェック推奨。
- **EvoGS実装待ち**：ストリーミング向けGSとして注目度が高く、OSS実装が出次第即試す価値あり。

---

*レポート生成日時: 2026-06-10 ／ 情報収集ソース: arXiv, CVPR 2026, Radiance Fields, CG Channel, TechRadar, X(Twitter), ComfyUI Blog, SideFX, Esri Blog*
