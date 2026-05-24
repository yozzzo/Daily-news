# 3DGS & 4D生成 デイリーレポート 2026-05-24

> **収集期間**: 2026-05-15〜2026-05-24  
> **新規項目数**: 16件（論文6件、業界ニュース6件、コミュニティ/ツール4件）  
> **重複排除**: past_3dgs.json と照合し、既出項目を完全除外済み  

---

## 今日の注目トレンド TOP 5

1. 🏙️ **TideGS** — 10億Gaussianをシングル24GB GPUで学習可能に。都市スケール3DGSが現実的に
2. ⚡ **NVIDIA vkSplatting 2026.1** — VulkanにレイトレーシングとDLSSを統合。本番実装が本格化
3. 🎮 **PG-3DGS（物理誘導GS）** — 「機能する形状」を生成可能に。ティーポットが注げる3Dモデル
4. 🗺️ **Esri ArcGIS May 2026** — クラウドGS生成＋薄い構造物の精度向上。エンタープライズ採用加速
5. 🎬 **Netflix × Volinga** — マドリードの通りをGSで撮影しLEDステージに投影。映画制作での実用が拡大

---

## スレッド 1：注目論文

### 1. TideGS ⭐⭐⭐⭐⭐
**arxiv: [2605.20150](https://arxiv.org/abs/2605.20150) | 提出: 2026-05-19 | 機関: 香港科技大学ほか**

**何ができるようになったか**  
10億個以上のGaussian Primitive（GS の最小単位の「粒」）を、24GBの単一GPUで学習可能に。従来の上限（約1,100万個）の約90倍のスケール。

**これまでの課題と解決策**  
都市スケールのシーンを3DGSで再構成しようとすると、すぐにGPUのメモリが枯渇していた。TideGSは「今の視点から見える部分だけをGPUに載せる」というキャッシュ方式（SSD→CPU→GPUの階層パイプライン）を採用し、メモリを「作業領域」として活用。分散学習（複数GPU）不要で城や街全体の3DGS再構成が可能に。

- 🔗 [arxiv論文](https://arxiv.org/abs/2605.20150)  
- 🔗 [プロジェクトページ](https://sponge-lab.github.io/TideGS/)

---

### 2. DeG（Density-Sampled Gaussians）— 密度制御による生成3DGS ⭐⭐⭐⭐
**arxiv: [2605.16355](https://arxiv.org/abs/2605.16355) | 提出: 2026-05-08 | 機関: 中国科学院ほか**

**何ができるようになったか**  
テキストや画像から3Dオブジェクトを生成する際に、「Gaussianをどこに配置すべきか」を自動学習する新しい生成フレームワーク。1つの潜在コードから解像度を自由に変えて3Dモデルを出力できる。

**これまでの課題と解決策**  
従来のGS生成モデルはGaussianの配置を固定グリッドで制御していたため、複雑な形状への対応が弱かった。DeGはOctree（空間を再帰的に分割する木構造）上の確率密度関数でGaussianを動的に配置し、細かい部分に自動集中させる。

- 🔗 [arxiv論文](https://arxiv.org/abs/2605.16355)

---

### 3. PG-3DGS（Physics-Guided 3D Gaussian Splatting）— 物理目的を満たすGS ⭐⭐⭐⭐
**arxiv: [2605.11266](https://arxiv.org/abs/2605.11266) | 提出: 2026-05-11 | 機関: Purdue大学**

**何ができるようになったか**  
「見た目がリアル」なだけでなく「物理的に機能する」3Dオブジェクトを生成可能に。例：ティーポットが実際に水を注げる注ぎ口形状、飛行機が実際に揚力を生む翼形状を自動生成。

**これまでの課題と解決策**  
従来のGSはレンダリング（見た目）のみを最適化しており、物理的な機能は考慮されなかった。PG-3DGSは微分可能な物理シミュレーターをGS最適化に組み込み、「見た目の損失」と「物理的損失」を同時に最小化する学習を実現。

- 🔗 [arxiv論文](https://arxiv.org/abs/2605.11266)

---

### 4. GS Transcoding from Point Cloud / Mesh ⭐⭐⭐⭐
**arxiv: [2605.21051](https://arxiv.org/abs/2605.21051) | 提出: 2026-05-20**

**何ができるようになったか**  
元の撮影写真がなくても、既存の3Dモデル（点群・メッシュ）からGaussian Splattingモデルに変換可能に。既存の膨大な3D資産（映画・ゲーム・建築設計データなど）をGSに転用できる。

**これまでの課題と解決策**  
3DGSモデルを作るには通常、同一シーンを複数の視点から撮影した写真が必要だった。この研究は、カスタム初期化と制約付き最適化により、点群やメッシュから直接GSモデルを高品質に生成するパイプラインを提案。

- 🔗 [arxiv論文](https://arxiv.org/abs/2605.21051)

---

### 5. Portals — エッジデバイスで動く4D空間ワールドモデル ⭐⭐⭐⭐
**CVPR 2026 Workshop | プロジェクト公開: 2026-05**

**何ができるようになったか**  
iPhone 14 Proで60fps動作する4D空間ワールドモデルを実現。360度以上のVFXエフェクト、音声コマンドでの操作、セッションをまたいでシーン状態が維持される「永続的な空間」を実装。

**これまでの課題と解決策**  
4DGS（時間軸も含む動的な3DGS）はPC向けでさえ重かった。LOD適応型GS（遠ければ荒く、近ければ細かく）でiOSの制約内に収め、セッション間でシーン状態を保持するアーキテクチャを構築。ARグラス・スマートフォンへの4DGS展開の実証研究として重要。

- 🔗 [プロジェクトページ](https://imclab.github.io/portals-cvpr2026/)

---

### 6. AIR（Amortized Image Reconstruction Framework） ⭐⭐⭐
**arxiv: [2605.20820](https://arxiv.org/abs/2605.20820) | 提出: 2026-05-20 | 機関: 華中科技大学・浙江大学**

**何ができるようになったか**  
1枚の画像を2D Gaussian Splattingで表現する際に、これまで必要だった繰り返し最適化（数百回以上のイテレーション）を、1回のニューラルネットワーク推論に圧縮。

**これまでの課題と解決策**  
2D GSによる画像再構成は質が高いが、画像ごとに個別に最適化が必要で時間がかかった。AIRは「残差（再現できていない部分）からGaussianを段階的に追加する」多段アーキテクチャと「短期最適化→蒸留」戦略で安定した高速化を実現。

- 🔗 [arxiv論文](https://arxiv.org/abs/2605.20820)

---

## スレッド 2：業界ニュース

### 7. NVIDIA vkSplatting 2026.1 — Vulkan GSが本番環境レベルへ ⭐⭐⭐⭐⭐
**Radiance Fields | 2026-05**

NVIDIAのVulkan対応オープンソースGS実装が大幅アップデート。

**主な新機能：**
- **マルチインスタンス**: GSシーンを「部品」として再利用・インスタンス化可能に
- **マルチライト＋レイトレーシング**: ポイント光源・スポット光源・平行光源に対応した硬軟影のリアルタイムレイトレーシング
- **3DGRT統合**: 従来のGSラスタライズとガウシアンベースのレイトレーシングを同一シーン内でハイブリッド利用
- **DLSS Ray Reconstruction**: 自動アンチエイリアス・アップスケーリング・デノイジング

研究用ツールから本番実装に向けたリファレンス実装へと格上げ。ライセンスはApache 2.0。

- 🔗 [Radiance Fields](https://radiancefields.com/nvidia-releases-vulkan-gaussian-splatting-2026.1)

---

### 8. Esri ArcGIS Reality Studio May 2026 — クラウドGS生成と精度向上 ⭐⭐⭐⭐
**Esri Blog | 2026-05**

GIS業界最大手EsriがArcGIS Reality Studioの5月アップデートを発表。

**主な改善：**
- 薄い構造物（フェンス・アンテナ等）、植生、高周波テクスチャのGS精度が大幅向上
- クラウドベースのGS生成ワークフローを追加。仮想マシンやクラウド上で大規模処理が可能に
- 都市環境・複雑なシーンでの再現精度も改善

- 🔗 [Esri Blog](https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026)

---

### 9. Esri Site Scan for ArcGIS May 2026 — ドローン測量GS、1万枚対応 ⭐⭐⭐
**Esri Blog | 2026-05**

ドローン測量向けプラットフォーム「Site Scan for ArcGIS」がクラウドベース3DGS生成に対応。1ミッションあたりの処理画像上限を10,000枚に引き上げ。測量・建設・都市計画でのGS採用の障壁が大幅低下。

- 🔗 [Esri Blog](https://www.esri.com/arcgis-blog/products/arcgis/imagery/whats-new-in-reality-mapping-may-2026)

---

### 10. Veesus May Update：SolidWorksでGS可視化が可能に ⭐⭐⭐
**Radiance Fields | 2026-05**

点群・GS管理プラットフォームVeesusの5月更新でSolidWorks対応を追加。製造・設計エンジニアがCADツールを離れることなく、GS（スプラット）データを直接可視化・操作可能に。次回リリースではレンズフレアと動的シャドウのGS対応、XGRIDS LCC2（大規模屋外GS圧縮フォーマット）への対応も予定。

- 🔗 [Radiance Fields](https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update)

---

### 11. Netflix「ベルリンとエルミタージュの女」× Volinga ⭐⭐⭐⭐
**Volinga | 2026-05**

Netflixの映像制作でVolingaのGaussian Splattingワークフローが実際に採用。スペイン・マドリードのCalle Alcalá（アルカラ通り）を現地でGS撮影し、LEDボリューム（大型LEDスクリーン撮影スタジオ）に投影するバーチャルプロダクションに活用。従来なら実物の背景セットを建設する必要があった部分を、GSによるデジタルツインで代替。制作コストと移動の大幅削減に貢献。

- 🔗 [Volinga](https://web.volinga.ai/)

---

### 12. 3DVista Update 2026.0：Total VR Mode でGS完全VR体験 ⭐⭐⭐
**3DVista Blog | 2026**

バーチャルツアー制作ツール3DVistaの2026.0アップデートで「Total VR Mode」を追加。Gaussian Splattingを含むバーチャルツアーをVRヘッドセットで完全体験可能に。不動産・文化観光・教育分野でのGS活用に向けた重要なアップデート。

- 🔗 [3DVista Blog](https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/)

---

## スレッド 3：コミュニティ・SNS話題

### 13. Lars & Felix：80台カメラのポータブル3DGSスタジオがヨーロッパを巡回 ⭐⭐⭐⭐
**Radiance Fields | 2026-05**

LarsとFelixの2人組が、80台のカメラで構成されたポータブル3DGSスタジオをヨーロッパ各地のイベントに持ち込み運営中。来場者がリグ（カメラフレーム）の中でポーズを取ると、QRコードをスキャンするだけで数分後にGSポートレートをスマホで受け取れる仕組み。GPU搭載ボックスで複数の学習を並列実行し、「スプラット写真館」的な新ビジネスモデルを実証中。

- 🔗 [Radiance Fields](https://radiancefields.com/how-lars-and-felix-built-a-portable-3d-gaussian-splatting-studio)

---

### 14. geofront × ウィーン自然史博物館：マリア・テレジアの宝石ブーケをGSで復元 ⭐⭐⭐
**Radiance Fields | 2026-05-21**

オーストリアの3DGS専門スタジオgeofront（geofront.eu）が、ウィーン自然史博物館（NHM Vienna）の依頼で、マリア・テレジア女帝の宝石ブーケを約70万スプラットでデジタル復元。本来は色あせてしまっていた葉の部分を、GS上でキュレーターがデジタル修復することに成功。実物には手を加えずに修復可能性を検討できるという文化財保存の新手法として注目。

---

### 15. Arrival Space 2026.1：AIがシーンを「見ながら」アシスト ⭐⭐⭐
**Radiance Fields | 2026-05**

GS特化のコラボレーションプラットフォームArrival Spaceが2026.1をリリース。新しいAIプロンプトインターフェースは「マルチモーダルなデフォルト」——ユーザーが見ているシーンをAIも把握した上でアシストする。HDRレンダリングパイプライン、輝度・コントラスト・彩度・ブルームなどのポストプロセス、黒背景でトレーニングしたGSの背景処理改善も追加。

- 🔗 [Radiance Fields](https://radiancefields.com/arrival-space-releases-version-2026.1)

---

### 16. Arrival Space 2026.2：「Vibes」でGSシーンに挙動をAI生成 ⭐⭐⭐
**Radiance Fields | 2026-05**

Arrival Spaceが2026.2もリリース。目玉は「Vibes」機能：テキストプロンプトでシーン内のオブジェクトの挙動（動き・アニメーション・インタラクションなど）をプログラム可能。テンプレートから始めるか、ゼロから生成かを選べ、後から追加のプロンプトで進化させることもできる。GSが「静的な3D再構成」から「AIで挙動を持つインタラクティブキャンバス」へと進化している。

- 🔗 [Radiance Fields](https://radiancefields.com/arrival-space-release-2026.2)

---

## スレッド 4：開発者向けインサイト

### ✅ 今週すぐ使える・試せる技術

| 技術 | 使いどころ | 入手先 |
|------|-----------|--------|
| TideGS | 都市・大規模シーンのGS学習 | [GitHub (予定)](https://sponge-lab.github.io/TideGS/) |
| GS Transcoding | 既存の点群/メッシュ → GS変換 | [arxiv 2605.21051](https://arxiv.org/abs/2605.21051) |
| NVIDIA vkSplatting 2026.1 | Vulkanベースの本番向けGSレンダリング | [NVIDIA GitHub](https://github.com/nvpro-samples/vk_gaussian_splatting) |

---

### 📌 業界標準への対応ポイント

- **Esri ArcGIS + Site Scan May 2026**: GIS・測量・建設案件でのGS採用が急加速。Site Scanが1万枚まで対応したことで、実プロジェクトへの導入障壁が大幅低下。GIS系案件での提案に積極的に組み込む好機。

- **Veesus SolidWorks対応**: 製造業・プロダクトデザインでGSを活用する際の新選択肢。CADソフトとGSのインテグレーションが確実に進んでいる。

- **3DVista 2026.0 VR Mode**: GS仮想ツアーをVRヘッドセットでデモするのが容易に。不動産・観光・文化財分野でのプレゼン価値が向上。

---

### 🔭 注目すべき研究トレンド

1. **物理誘導GS（PG-3DGS）**: 「見た目」だけでなく「機能」も設計できる3D生成が現実に。ロボット工学・製品設計・ゲームへの応用ポテンシャルが高い。

2. **エッジデバイス4DGS（Portals）**: iOSで60fps 4DGSが動くことが実証された。スマホAR/MRアプリ開発者はアーキテクチャを要確認。

3. **スケーラビリティ（TideGS）**: 10億Gaussianの学習がシングルGPU化。今後1〜2年でデジタルツインのスケールが大幅に拡大すると予想される。

---

*レポート生成: 2026-05-24 | ソース: arXiv, Radiance Fields, Esri Blog, NVIDIA, Volinga, 3DVista, scipapermill.com*
