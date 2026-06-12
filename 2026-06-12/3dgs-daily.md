# 3DGS & 4D生成 デイリーレポート｜2026年6月12日

**本日の収集件数**: 論文10件 / 業界ニュース5件 / コミュニティ3件 / 開発者向け2件 = **計20件**

---

## 今日の注目トレンド

1. **Apple が3DGS採用を公式発表（WWDC 2026）** — iOS 27 の Apple Maps Flyover が Gaussian Splatting 化。350都市以上に適用、秋リリース予定
2. **CVPR 2026 Denver 閉幕** — 3DGS論文50本超が発表。Selfi(Oral)・Chorus(Oral)・HumanNOVA など注目作多数
3. **映画「Superman」4DGS VFX 技術詳細公開** — Framestore社が196台カメラ・約40ショットへの4DGS適用を解説
4. **ComfyUI v0.23 + TripoSplat** — 1枚の画像から Gaussian Splat 生成が誰でも可能に
5. **NVIDIA らが10億 Gaussian 超で都市規模3D再構成** — 従来比25倍のスケールでデジタルツインが現実に

---

## 1. 注目論文（重要度：高）

### 1-1. HiGS — リアルタイム3DGSレンダリングを最大15.8倍高速化
- **arXiv**: https://arxiv.org/abs/2606.00352（2026年6月1日公開）
- **分野**: 3DGS高速化
- **概要**: 通常の3DGS では「仕分け」と「塗り」を同じ格子サイズで処理するため速度に限界がありました。HiGS（Hierarchically Tiled Gaussian Splatting）はこの2ステップを異なる解像度の格子に分離し、元の3DGS より最大**15.8倍**高速な描画を実現。VR・自動運転など即時応答が必要な場面への活用が期待されます。実験的推論パスがすでに gsplat ライブラリに実装済みです。

### 1-2. EvoGS — 3D映像ストリーミングのデータ量を最大2.4倍削減
- **arXiv**: https://arxiv.org/abs/2606.07179（2026年6月5日公開）
- **分野**: 3DGS ストリーミング・大規模配信
- **概要**: 3DGS を段階的に配信する際、レベルごとに重複データが積み上がる問題がありました。EvoGS は「進化ツリー」（親子構造）でデータを整理し、重複率を65%超から25%未満に圧縮。GPU メモリを最大**5.5倍**、送信データ量を最大**2.4倍**削減しながら高品質な3D映像ストリーミングを実現します。

### 1-3. Multi-GPU GS（NVIDIA・Toronto大学ら） — 10億 Gaussian 超で都市丸ごと3D化
- **arXiv**: https://arxiv.org/abs/2606.11390（2026年6月9日公開）
- **分野**: 大規模3DGS・都市規模再構成
- **概要**: 複数 GPU を束ねる新 PyTorch 仕組みにより、**10億以上**の Gaussian（従来 SoTA の25倍以上）を使った都市規模の3D再構成に成功。街路レベルの細部を持つデジタルツインが現実的なコストで実現できるようになります。NVIDIA・Toronto大学・Vector Institute のチームによる成果です。

### 1-4. LEGS — Laplacian 誘導で画像細部の PSNR 最大+1.68dB
- **arXiv**: https://arxiv.org/abs/2606.07932（2026年6月6日公開）
- **分野**: 3DGS最適化・画質向上
- **概要**: 標準 3DGS は平坦な面も複雑な輪郭も均等に最適化するため細部が甘くなりがちでした。LEGS は「2次微分（Laplacian）」で構造豊かな領域を検出し、重点的に最適化。Tanks&Temples データセットで PSNR を最大**1.68dB**向上。FastGS・FasterGS に組み込んでも効果を発揮する汎用性の高い手法です。

### 1-5. Selfi（CVPR 2026 Oral） — 自己改善型3D再構成エンジン
- **arXiv**: https://arxiv.org/abs/2512.08930
- **発表**: CVPR 2026 Oral（6月5日、Mile High Ballroom, Denver）
- **分野**: フィードフォワード3DGS・自己改善型学習
- **概要**: 複数写真から3Dシーンを生成する際、自分自身の出力を「教師データ」として幾何特徴の整合性を高める手法。ポーズ不明の写真群からでも高品質な Novel View Synthesis を実現し、CVPR 2026 の Gaussian Splatting & Reconstruction セッションで口頭発表されました。

### 1-6. Chorus（CVPR 2026 Oral） — 1モデルでセグメンテーションも VQA も
- **arXiv**: https://arxiv.org/abs/2512.17817
- **発表**: CVPR 2026 Oral
- **分野**: 汎用3DGSシーンエンコーダー・言語理解
- **概要**: SigLIP2・DINOv3・PE-Spatial の3種 AI 教師から知識を蒸留し1つのコンパクトエンコーダーに統合。3DGS シーンに対してセグメンテーション・物体認識・Q&A を単一モデルで処理できます。ScanNet200/Matterport3D などで SoTA を更新しています。

### 1-7. HumanNOVA（CVPR 2026） — 写真1枚から1秒未満でリアルな3Dアバター
- **arXiv**: https://arxiv.org/abs/2606.02573
- **プロジェクトページ**: https://humannova.github.io/
- **発表**: CVPR 2026
- **分野**: 人体3D再構成・アバター生成
- **概要**: 写真1枚からの高品質3D人体アバター生成を**1秒未満**で実現。トリプレーン表現と Gaussian Splatting を組み合わせ、10万件以上のデータで学習。ゲーム・映画・AR/VR のキャラクター制作に直結する実用的な成果です。

### 1-8. BEAST3D — 動物の行動と脳活動を3DGSで空間的に解析
- **arXiv**: https://arxiv.org/abs/2606.02937（2026年6月1日公開）
- **分野**: 動物行動解析・神経科学応用
- **概要**: わずか4台のカメラ映像から動物の3D姿勢を GS で再構成し、どの動きが神経発火を引き起こすかを空間的に特定。単一ベクトルのみで構造が失われる従来手法の限界を突破した、神経科学分野への独自の GS 応用事例です。

### 1-9. AtlasGS — 脳 MRI の超解像・解像度調和に3DGSを応用
- **arXiv**: https://arxiv.org/abs/2606.02961（2026年6月1日公開）
- **分野**: 医療画像・脳MRI超解像
- **概要**: MRI は撮影条件でスライス方向の解像度が大きく異なり比較が困難でした。AtlasGS は等方性 T1 スキャンで3D Gaussian 骨格を学習し、その骨格を T2・FLAIR・DWI など他モダリティの超解像に流用する2段階手法を提案。UK Biobank・GBM・ABCD データセットで SoTA を達成しました。

### 1-10. PolarGuide-GSDR（CVPR 2026 Poster） — 偏光センサーで反射物体をリアルに3D化
- **arXiv**: https://arxiv.org/abs/2512.02664
- **発表**: CVPR 2026 Poster
- **分野**: 3DGS反射・素材表現・偏光センサー
- **概要**: ガラス・金属など強反射物体は GS が最も苦手とする対象。偏光カメラ情報を GS 最適化に直接組み込み、法線推定の曖昧さを解消。鏡面反射と拡散反射の分離で SoTA を達成し、リアルタイム描画速度も維持した初の手法です。

---

## 2. 業界ニュース

### 2-1. 【超大型ニュース】Apple が3DGS を Apple Maps Flyover に採用（WWDC 2026）
- **ソース**: https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade
- **報道**: https://www.techradar.com/computing/software/apple-maps-has-a-huge-ios-27-upgrade-on-the-way-for-flyover
- **概要**: 2026年6月8日の WWDC 基調講演で、Apple は Apple Maps「Flyover」機能（世界350都市以上）に Gaussian Splatting を採用すると発表。建物の細部・木々の形状・スカイスクレーパーのガラスへの光反射まで、従来のメッシュ3Dモデルでは不可能だったリアルな都市景観を提供します。**iOS 27・macOS 27・visionOS 27 として2026年秋リリース予定**。

### 2-2. ComfyUI v0.23 + TripoSplat — 1枚の画像からGS生成が誰でも可能に
- **ソース**: https://radiancefields.com/comfyui-adds-native-3d-gaussian-splat-generation-with-triposplat
- **GitHub**: https://github.com/VAST-AI-Research/TripoSplat
- **概要**: ComfyUI が v0.23.0 で GS 生成をネイティブサポート。Tripo AI（VAST AI）の MIT ライセンスモデル TripoSplat を初日統合し、1枚の RGB 画像から最大**26万2144個の Gaussian**を持つ3Dアセットを直接生成できます。テンプレートライブラリから即利用可能です。

### 2-3. Irrealix — After Effects & Nuke 向け GS プラグイン大型更新
- **ソース**: https://radiancefields.com/irrealix-updates-after-effects-and-nuke-plugin-for-gaussian-splatting
- **概要**: After Effects では GS の色演出・不透明度アニメーションをタイムライン上で直接操作可能に。Nuke では PLY ファイルと4DGS シーケンスの読み込み・複数 GS モデルの一括出力が強化されました。VFX 制作現場への GS 活用がさらに加速します。

### 2-4. Cesium ion June 2026 — メッシュ生成なしで GS のみのパイプライン構築が可能に
- **ソース**: https://cesium.com/blog/2026/06/01/cesium-releases-in-june-2026/
- **概要**: Cesium ion の再構成ワークフローを改善。GS 単独パイプラインが組めるようになりました。CesiumJS 1.142・Cesium for Unreal 2.27.0・Cesium for Unity 1.23.3 も同時更新。GIS・デジタルツイン分野での活用コストが下がります。

### 2-5. Framestore「Superman」4DGS 技術詳細公開 — 映画史上初の本格活用
- **ソース**: https://radiancefields.com/gaussian-splatting-in-superman
- **詳細記事**: https://beforesandafters.com/2026/02/13/framestore-showcases-the-4d-gaussian-splatting-used-for-superman/
- **概要**: VFX大手 Framestore が**196台のマシンビジョンカメラ**で Bradley Cooper らを48fps 収録し、Postshot で Ultra品質（約2000万 Splat）の動的 Splat シーケンスに変換。約40ショットに適用した完全パイプラインを詳解。「照明の全方向エネルギーを丸ごと記録した動く写真」と評されています。

---

## 3. コミュニティ・SNS話題

### 3-1. CVPR 2026 Denver 閉幕 — 3DGS関連論文50本超が発表・コード公開ラッシュ
- **ソース**: https://cvpr.thecvf.com/virtual/2026/events/Highlights2026
- **概要**: CVPR 2026 がコロラド州デンバーで6月3〜7日に開催。3DGS 関連だけで50本以上の論文が発表・コード公開され、「Gaussian Splatting & Reconstruction」専用 Oral セッションも設置。FastGS（CVPR Highlight + Compute Gold Star 受賞）、Selfi（Oral）、Chorus（Oral）などが注目を集めています。

### 3-2. Apple WWDC 発表で GS コミュニティが大騒ぎ
- **ソース**: https://x.com/RadianceFields/status/2064043440350888050
- **概要**: WWDC 直後に「Gaussian Splatting is coming to Apple Maps」の X 投稿が急拡散。「Apple が Google より先に実装」「iOS 標準に初めて GS が組み込まれた歴史的瞬間」として話題となり、TechRadar 等主流メディアも「次の大きな3D写真トレンド」として特集記事を掲載しました。

### 3-3. Framestore「Superman」YouTube 動画 & fxguide ポッドキャストで4DGS 技術論が拡散
- **YouTube**: https://www.youtube.com/watch?v=Pxd-q3ECBPs
- **記事**: https://www.artofvfx.com/superman-framestore-brings-4d-gaussian-splatting-to-the-big-screen/
- **概要**: Framestore 制作のメイキング動画が VFX 業界で大きな反響。fxguide ポッドキャスト「Krypto, crystals & cutting-edge gaussian splats」でも技術者インタビューが公開。196台カメラリグから Houdini・Nuke を使ったパイプライン全体が詳解されています。

---

## 4. 開発者向けインサイト

### 4-1. ArcGIS Enterprise 12.1 — 企業内ネットワークで GS Layer が利用可能に
- **ソース**: https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/work-with-gaussian-splat-layers.html
- **概要**: Esri の ArcGIS Enterprise 12.1 で GS レイヤーのシェアリングに対応。オンプレミス環境での GS シーン活用が可能になり、測量・インフラ管理・都市計画分野で「イントラネット型デジタルツイン」として GS を活用する道が開きます。

### 4-2. gsplat ライブラリに HiGS 推論パスが実験的実装
- **GitHub**: https://github.com/nerfstudio-project/gsplat
- **概要**: Nerfstudio の gsplat ライブラリに HiGS の推論専用パスが実験的追加。fp16 シーンパッキング + マクロタイル融合ラスタライゼーションで低遅延レンダリングを実現。**既存の学習済みモデルをそのまま**高速推論に切り替えられます。

---

## 重複排除メモ
- 照合元: `past_3dgs.json`（最終更新: 2026-05-30）
- 新規項目のみ収録済み
- 過去カバー済みで除外した主な項目: FastGS（2026-03-27掲載）、EDGS（2026-05-11掲載）、Esri ArcGIS Reality Studio May 2026（2026-05-30掲載）等
