# 3DGS & 4D生成 デイリーレポート｜2026年5月9日

## 概要

| 項目 | 件数 |
|------|------|
| 収集新規件数 | 15件 |
| 論文 | 10件 |
| 業界ニュース | 2件 |
| コミュニティ・ツール | 3件 |
| 重複除外（past_3dgs.json照合）| 多数 |

**今日の注目トレンド：**
- **GaussianGPT**：GPTスタイルのトークン予測で3Dシーンを丸ごと自動生成
- **Ground4D**：悪路・オフロード環境対応の4DGS実時間再構成
- **LeafFit**（Eurographics 2026）：植物スキャン→ゲームエンジン対応メッシュ自動変換
- **EA mesh2splat**：EAが3Dメッシュ→GS即時変換OSSを公開（平均0.5ms以内）
- **UNIGINE 2.21**：産業向けシミュレーションエンジンのGS機能が全面強化

---

## スレッド1：注目論文

### 1. GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation

**分野**：3D生成  
**重要度**：⭐⭐⭐⭐⭐  
**ソース**：[arXiv 2603.26661](https://arxiv.org/abs/2603.26661)  
**著者**：Nicolas von Lützow, Barbara Rössle, Katharina Schmid, Matthias Nießner（TU Munich）  
**HuggingFace**：[Paper page](https://huggingface.co/papers/2603.26661)

**何ができるようになったか**  
ChatGPTが文字をトークンごとに生成するのと同じ仕組みで、3Dシーン全体を自動生成できるようになりました。「新規シーンの生成」「部分的な補完」「シーンを広げた大規模アウトペイント」の3つを単一モデルで実現します。

**これまでの課題と解決法**  
従来の拡散モデルは「シーン全体をまとめて予測」する方式だったため、細かい制御や部分補完が困難でした。GaussianGPTは3DGS素材をトークンに圧縮し順番に予測する方式で、柔軟な生成・補完・拡張を一本化します。

---

### 2. Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes

**分野**：4DGS・自動運転  
**重要度**：⭐⭐⭐⭐  
**ソース**：[arXiv 2605.04435](https://arxiv.org/abs/2605.04435)  
**コード**：[GitHub](https://github.com/wsnbws/Ground4D)  
**投稿日**：2026年5月6日

**何ができるようになったか**  
舗装されていない悪路・山道・建設現場などの複雑な環境でも、車両カメラ映像からリアルタイムに4Dシーン（動く物体も含む）を再構成できるようになりました。自動運転の非舗装路走行や農業ロボットへの応用が期待されます。

**これまでの課題と解決法**  
従来の4DGSフィードフォワード手法は、凹凸が激しい地形や車の揺れ、非剛体の動き（草木の揺れなど）に弱く精度が落ちていました。「ボクセルグランディング」でシーン空間を格子状に分割し、時間的な変化を局所処理して矛盾した観測を解消します。

---

### 3. Lumina-4DGS: Illumination-Robust Four-Dimensional Gaussian Splatting for Dynamic Scene Reconstruction

**分野**：4DGS・自動運転  
**重要度**：⭐⭐⭐⭐  
**ソース**：[MDPI Sensors 2026](https://www.mdpi.com/1424-8220/26/5/1650)  
**PMC**：[Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12987166/)

**何ができるようになったか**  
複数カメラがそれぞれ独自の自動露出・ホワイトバランスで撮影した映像からでも、光の違いを吸収して正確に4D再構成が可能になりました。Waymoデータセットで最新最高性能（PSNR 31.12dB）を達成。

**これまでの課題と解決法**  
従来の4DGSは「均一な露出」を前提としており、カメラごとの光差異を「形状の変化」と誤判断して映像がちらついていました。階層的露出補正＋シーン認識型最適化（Object-Aware SSIM-Gated Optimization）でこれを根本解決します。

---

### 4. LeafFit: Plant Assets Creation from 3D Gaussian Splatting（Eurographics 2026）

**分野**：ゲーム開発・植物3D化  
**重要度**：⭐⭐⭐⭐  
**ソース**：[arXiv 2602.11577](https://arxiv.org/html/2602.11577v1) / [Wiley CGF](https://onlinelibrary.wiley.com/doi/10.1111/cgf.70374)  
**コード**：[GitHub](https://github.com/netbeifeng/leaf_fit)  
**プロジェクトページ**：[LeafFit](https://netbeifeng.github.io/LeafFit/)

**何ができるようになったか**  
植物をスキャンして得たGaussian Splattingデータを、UE5/Unityで使えるゲームエンジン対応の軽量メッシュに自動変換できるようになりました。葉1枚1枚をテンプレート化して使い回し、データ量を桁違いに削減します。

**これまでの課題と解決法**  
3DGSで植物をリアルに再現できても、メッシュ構造がないためゲームの物理演算・ライティング・LOD切り替えが使えませんでした。LeafFitは葉形状を分析して代表テンプレートを作り、差分変形（MLS）で全葉に適用します。

---

### 5. GauScene: Physically Plausible Scene Generation via Language-Guided 3D Gaussian Interaction

**分野**：3D生成・言語AI  
**重要度**：⭐⭐⭐⭐  
**ソース**：[Springer 2026](https://link.springer.com/chapter/10.1007/978-981-95-6960-1_30)

**何ができるようになったか**  
「部屋にボールを置いて」「テーブルの物を左に動かして」といった自然言語の指示だけで、物理法則に従って動く3Dシーンを生成・操作できるようになりました。

**これまでの課題と解決法**  
AIによる3Dシーン生成は「見た目の生成」はできても「物理的に正しい配置か」の検証が困難でした。LLMエージェントが言語を物理力（重力・衝突判定など）に変換し、3DGSシーンに適用します。

---

### 6. Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads

**分野**：農業・3D再構成  
**重要度**：⭐⭐⭐  
**ソース**：[arXiv 2504.06978](https://arxiv.org/abs/2504.06978) / [IEEE Xplore](https://ieeexplore.ieee.org/document/11148022/)  
**プロジェクトページ**：[Wheat3DGS](https://zdwww.github.io/wheat3dgs/)

**何ができるようになったか**  
実際の農業圃場で撮影したマルチビュー映像から、小麦の穂1本1本を3D分離・長さ・幅・体積で自動計測できるようになりました。大規模品種改良・収穫量予測への直接応用が可能です。

**これまでの課題と解決法**  
密集した畑では穂が重なり合い、2Dカメラでは個体識別が困難でした。3DGS＋SAM（Segment Anything Model）を組み合わせて穂を3Dで分離・計測します。NeRFベース手法を凌駕する精度を達成。

---

### 7. A General Framework for Gaussian Splatting-Based Human-Centric Volumetric Videos

**分野**：人物ボリュームビデオ  
**重要度**：⭐⭐⭐  
**ソース**：[Visual Intelligence / Springer](https://link.springer.com/article/10.1007/s44267-026-00111-7)  
**EurekAlert**：[プレスリリース](https://www.eurekalert.org/news-releases/1123975)

**何ができるようになったか**  
人物の動きをカメラで撮影→3DGSで処理→デスクトップ・スマホ・XRデバイスでリアルタイム再生という一貫したパイプラインを実現しました。81台カメラで収録した130シーケンス以上の人物動作データセットも公開。

**これまでの課題と解決法**  
「撮影」「3DGS処理」「クロスプラットフォーム配信」の工具がバラバラで研究から実用への道が断絶していました。本フレームワークがエンドツーエンドで統合し、商用グレードの人物ボリュームビデオを可能にします。

---

### 8. Planar-Guided Gaussian Splatting with Texture-Complexity-Based Initialization

**分野**：3DGS・室内再構成  
**重要度**：⭐⭐⭐  
**ソース**：[MDPI Electronics 15/5/1137](https://www.mdpi.com/2079-9292/15/5/1137)  
**著者**：Zheng A., Yu Z.（2026年3月）

**何ができるようになったか**  
白壁・床・天井など「テクスチャが少ない場所」でも3DGSが正確に室内形状を再現できるようになりました。

**これまでの課題と解決法**  
標準の3DGSはテクスチャの豊富さを頼りにGaussian配置を決めるため、平坦な壁などでは配置が粗くなり品質が落ちていました。Manhattan Frame整合とSAMマスクで平面を検出し、低テクスチャ領域を的確にカバーします。

---

### 9. GTS-SLAM: A Tightly-Coupled GICP and 3DGS Framework for Robust Dense SLAM in Underground Mines

**分野**：SLAM・産業  
**重要度**：⭐⭐⭐  
**ソース**：[MDPI Drones](https://www.mdpi.com/2624-8921/8/4/79)

**何ができるようになったか**  
GPS信号が届かない地下鉱山内でも、ロボット・ドローンがリアルタイムで3Dマップを作りながら自己位置を把握（SLAM）できるようになりました。暗所・粉塵・狭隘な過酷環境に対応しています。

**これまでの課題と解決法**  
既存のSLAMは地上環境前提で、狭空間・少ない特徴点・過酷な照明では性能が大幅に落ちていました。GICPとGaussian Splattingを密結合することで堅牢なマッピングと位置推定を実現します。

---

### 10. Plant3R: Fusing 3D Feature Learning with Gaussian Splatting to Enhance Wheat Plant 3D Reconstruction

**分野**：農業・3D再構成  
**重要度**：⭐⭐⭐  
**ソース**：[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2643651526000373)

**何ができるようになったか**  
カメラのポーズ（位置・向き）情報なしに、複数視点の小麦株画像から高精度3D再構成が可能になりました。事前学習済みモデル（MASt3R）と3DGSを融合したエンドツーエンドのパイプラインです。

**これまでの課題と解決法**  
農業用3D再構成には通常カメラキャリブレーション等の複雑なセットアップが必要でした。Plant3Rはフィードフォワード方式で、現場での手軽な計測を可能にします。

---

## スレッド2：業界ニュース

### 11. UNIGINE 2.21 – Gaussian Splatting Controls が全面拡張

**ソース**：[Radiance Fields](https://radiancefields.com/unigine-2.21-expands-gaussian-splatting-controls) / [UNIGINE公式](https://unigine.com/news/2026/unigine-sdk-2-21-released-new-animation-system-ai-ready-workflow-and-major-performance-gains/) / [CG Channel](https://www.cgchannel.com/2026/04/unigine-2-21-is-out/)  
**リリース**：2026年4月

産業用リアルタイム3Dエンジン「UNIGINE」のv2.21で、Gaussian Splatting関連の機能が大幅強化されました。デジタルツイン・航空シミュレーション・防衛訓練分野で採用される同エンジンで、3DGSがより実用的に使えるようになります。

**主な新機能：**
- レンダリング順序制御：ポストエフェクト後にGSを描画するオプションを追加
- 2Dミップフィルタリング（実験的）：スクリーンサイズに応じたブラー調整
- 3Dアダプティブスムージング：カメラパラメータに基づくGaussianスケーリング
- Splat調整コントロール：シーンごとに色温度・彩度・明度・黒白レベルをチューニング
- クラスタードレンダリング強化：光源204個のテストシーンでGPU/フレーム時間を **21%削減**

---

### 12. Electronic Arts SEED – mesh2splat オープンソース公開

**ソース**：[GitHub](https://github.com/electronicarts/mesh2splat) / [Radiance Fields](https://radiancefields.com/mesh2splat-instant-3d-mesh-conversion-to-3d-gaussian-splatting)

EAのゲーム研究部門「SEED」が、3Dゲームアセット（メッシュ）を **平均0.5ミリ秒以内** でGaussian Splatting形式に変換するオープンソースツールを公開しました。

**特徴：**
- 従来の「撮影→最適化→GS化（数分〜十数分）」という工程が不要
- ラスタライザを直接活用し、3Dジオメトリ・マテリアル・テクスチャからGSを即時生成
- 現在は .glb フォーマットのみ対応
- 付属の3DGS Rendererで変換結果を即確認可能
- 再照明（Relighting）も容易

---

## スレッド3：コミュニティ・SNS話題

### 13. Eurographics 2026 – 3DGS関連採択論文リスト公開

**ソース**：[GitHub Awesome3DGS](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/Accepted.md) / [公式プログラム](https://eg2026.github.io/program/?type=Full+Paper)

欧州最大のCGカンファレンス「Eurographics 2026」で採択された3DGS関連論文の一覧がGitHubで公開されています。LeafFit・GS-2Mを含む複数の実用研究が採択されており、欧州CGコミュニティでの3DGSの主流化が確認できます。

---

### 14. GaussianGPT – Matthias Niessner教授がX（Twitter）でデモ公開

**ソース**：[X/Twitter](https://x.com/MattNiessner/status/2038563326167310507) / [HuggingFace](https://huggingface.co/papers/2603.26661) / [論文](https://arxiv.org/abs/2603.26661)

TU MunichのMatthias Niessner教授がGaussianGPTのデモ動画をX（旧Twitter）で公開。「3DシーンをGPTと同じ方法で生成できる」というコンセプトが話題を呼び、HuggingFace Papersでも高評価を獲得しています。

---

### 15. Wheat3DGS – 農業AI・精密農業コミュニティで急速に拡散中

**ソース**：[プロジェクトページ](https://zdwww.github.io/wheat3dgs/) / [論文](https://arxiv.org/abs/2504.06978)

「畑でカメラを使って撮影するだけで、小麦の穂1本ずつを3D計測できる」という応用研究が農業AI関係者の間で注目されています。オープンソース・プロジェクトページ公開済みで、精密農業コミュニティでの採用が加速中。

---

## スレッド4：開発者向けインサイト

| 動向 | 対象者 | 優先度 |
|------|--------|--------|
| EA mesh2splat 試験導入 | ゲームエンジン開発者 | 🔴 高 |
| UNIGINE 2.21 GS新パラメータ確認 | 産業シミュレーション担当 | 🔴 高 |
| GaussianGPT 論文精読 | 3D生成AI研究者 | 🟡 中 |
| Ground4D コード評価 | ロボット・自動運転エンジニア | 🟡 中 |
| LeafFit パイプライン検証 | ゲーム・CG植物担当者 | 🟡 中 |
| Wheat3DGS / Plant3R 動向把握 | 農業AI・精密農業関係者 | 🟢 低〜中 |

### すぐ使えるリンク集

- [EA mesh2splat GitHub](https://github.com/electronicarts/mesh2splat)
- [Ground4D GitHub](https://github.com/wsnbws/Ground4D)
- [LeafFit GitHub](https://github.com/netbeifeng/leaf_fit)
- [Wheat3DGS プロジェクト](https://zdwww.github.io/wheat3dgs/)
- [UNIGINE 2.21 リリースノート](https://unigine.com/news/2026/unigine-sdk-2-21-released-new-animation-system-ai-ready-workflow-and-major-performance-gains/)
