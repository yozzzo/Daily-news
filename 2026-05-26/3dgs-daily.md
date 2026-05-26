# 3DGS & 4D生成 デイリーレポート｜2026-05-26

> **収集件数：** 21件（論文10件・業界ニュース7件・コミュニティ/ツール4件）  
> **リサーチ対象：** arXiv・Radiance Fields・MDPI・GitHub・CG Channel・Esri Blog等  
> **重複除外：** `past_3dgs.json` との照合済み

---

## 今日の注目トレンド TOP5

1. **TideGS** — 単一GPU（24GB）で **10億以上のGaussians** を学習可能に。大規模シーン再構成が民主化へ
2. **無線通信 × 3DGS 新潮流** — RxGS・OctCGSが登場し、5G/WiFiの電波場マッピングに3DGSが本格活用
3. **Transcoding 3DGS** — 元の撮影画像が不要！既存のポイントクラウド・メッシュを直接3DGSへ変換
4. **Esri May 2026アップデート** — ArcGIS Reality Studio・Site Scanがクラウド対応強化、最大1万枚処理
5. **Netflix「ベルリン」× Volinga** — Netflixドラマが3DGSを使ったLEDバーチャルプロダクションを採用

---

## 注目論文

### 1. TideGS: 10億以上のGaussianを単一GPUで学習

**重要度：★★★★★**  
**URL：** https://arxiv.org/abs/2605.20150  
**分野：** 3DGS最適化・大規模シーン  
**投稿日：** 2026-05-19

**概要：**  
これまで3DGSの大規模化は「GPUメモリの壁」に阻まれていました。一般的なGPU（24GB VRAM）では数千万のGaussianが限界でしたが、TideGSはSSD・ホストメモリ・GPUメモリを階層的に活用する「Out-of-Core最適化」で、なんと**10億以上**のGaussianを1枚のGPUで学習可能にしました。

**解決した課題：**  
GPU VRAMは有限なため大規模3DGSの学習は不可能でした。TideGSはカメラ位置に応じて可視なGaussianだけを動的にロードする「ブロック仮想化」と「軌跡適応型差分ストリーミング」で突破。都市全体・広大な森林といった超大規模シーンの高品質な3D再構成が現実的になります。

---

### 2. RxGS: 受信機も学習する電波場3DGS

**重要度：★★★★**  
**URL：** https://arxiv.org/abs/2605.24290  
**分野：** 無線通信・RF場再構成  
**投稿日：** 2026-05-22

**概要：**  
5GやWiFiの無線電波がどのように空間に広がるかをモデリングする「電波場再構成」に3DGSを応用。従来手法は送信機の位置は学習できても受信機が変わると使えませんでしたが、RxGSは**あらゆる受信機位置に対応する統一モデル**を実現。

**解決した課題：**  
シーン幾何（位置に依存しない部分）と指向性放射（受信機位置に依存する部分）を2段階に分離して学習するアーキテクチャで、固定受信機前提の限界を突破しました。

---

### 3. Transcoding 3DGS: 元の写真なしでGS変換

**重要度：★★★★**  
**URL：** https://arxiv.org/abs/2605.21051  
**分野：** 3DGS変換・互換性  
**投稿日：** 2026-05-20

**概要：**  
3DGSモデルを作るには通常「多視点の写真」が必要ですが、本手法では**既存のポイントクラウドやメッシュ（3Dスキャンデータ）から直接3DGSへ変換**できます。過去に蓄積されたCADデータや3Dスキャン資産をそのままリアルタイム3DGS表示に活用できるようになります。

**解決した課題：**  
カスタム初期化と幾何拘束の組み合わせにより、元の多視点画像なしでも高視覚品質の3DGSが生成でき、従来のSfM初期化より収束も速い。

---

### 4. AIR: 2DGSの反復最適化をネットワーク1回で完了

**重要度：★★★**  
**URL：** https://arxiv.org/abs/2605.20820  
**分野：** 2DGS・フィードフォワード  
**投稿日：** 2026-05-20

**概要：**  
2Dの画像を美しく2D Gaussian Splattingで表現する処理が、何百回もの反復なしにネットワーク1回の推論で完了します。リアルタイムな画像圧縮・超解像への応用が期待されます。

**解決した課題：**  
従来の2DGSは1枚あたり数百ステップの最適化が必要でした。AIRはPredict–Optimize–Distillという3段階学習戦略で反復を予測ネットワークに「圧縮」し、段階的残差アーキテクチャで品質を保ちながら高速化。

---

### 5. OctCGS: 八分木GSで電波伝搭マップを超高効率に構築

**重要度：★★★**  
**URL：** https://arxiv.org/abs/2605.22961  
**分野：** 無線通信・チャンネルナレッジマップ  
**投稿日：** 2026-05-21

**概要：**  
通信基地局と端末の間の電波伝搭（複数回反射を含む）を3DGSで正確かつ高速にシミュレーション。八分木（オクツリー）でシーンを多解像度分割し、各リーフノードにGaussianを配置してマルチバウンス伝搭を明示的にモデリングします。

---

### 6. LiDAR × 3DGS で森林デジタルツイン

**重要度：★★★**  
**URL：** https://www.mdpi.com/2072-4292/18/11/1696  
**分野：** 農業・精密林業・デジタルツイン  
**掲載日：** 2026-05-24

**概要：**  
LiDARドローンと航空カメラ映像を融合させ、森林全体を3DGSで精密に再現。木の幹（剛体）と木の葉（非剛体）を「意味的正則化」で別々にモデリングすることで安定した再構成を実現。バイオマス推定・炭素吸収量計測・病害虫監視への活用が可能。

---

### 7. HarmoGS: 野外・雑多な写真でも崩れない3DGS

**重要度：★★★**  
**分野：** 実環境3DGS・勾配ハーモナイゼーション  

**概要：**  
観光地・市街地など品質がバラバラな大量インターネット写真から安定した3DGSを生成。対立する勾配を自動で「調和（ハーモナイズ）」する新しい密度制御で、ノイズや矛盾した情報を自動で整合しクリーンな3D再構成を実現。中山大学（Sun Yat-sen University）の研究。

---

### 8. AdaptSplat: 大規模AIモデルの知識を3DGSに転用

**重要度：★★★**  
**URL：** https://arxiv.org/abs/2605.10239  
**分野：** Foundation Models・フィードフォワード3DGS  

**概要：**  
DINOv2・Depth Anythingなど大規模視覚AIモデル（Vision Foundation Models）の豊かな3D理解の知識を、3DGSのフィードフォワード再構成に組み込む手法。スパースビュー（少ない枚数の写真）から高品質な3DGSを生成できるようになります。

---

### 9. SDTalk: 構造化顔プリオルで自然なGaussianトーキングヘッド

**重要度：★★**  
**URL：** https://arxiv.org/abs/2605.09956  
**分野：** トーキングヘッド・顔アバター  
**投稿日：** 2026-05-11

**概要：**  
音声に合わせて自然に口・表情が動く3DアバターをGaussianで生成。顔の構造的なプリオール（目・鼻・口の位置関係）と二分岐モーション場を組み合わせることで、特定人物に依存せず誰でも適用可能。テレビ会議・デジタルヒューマン応用に即戦力。

---

### 10. ConFixGS: 拡散モデルで自動運転GSを補正

**重要度：★★**  
**URL：** https://arxiv.org/abs/2605.09688  
**分野：** 自動運転・GS補完  
**投稿日：** 2026-05-11

**概要：**  
自動運転用カメラ配置（少数・固定位置）でもフィードフォワードGS再構成が高品質になります。信頼度の低い領域を拡散モデルで補正し、シミュレーション用の高品質シーン再構成を実現。

---

## 業界ニュース

### 1. Esri ArcGIS Reality Studio May 2026 アップデート

**重要度：★★★★**  
**URL：** https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026  

**概要：**  
GIS・測量業界最大手のEsriが3DGSの品質を大幅改善。電線・細い枝・植生など薄い構造物の表現精度が向上し、現実に近い3D再構成が可能に。クラウドベースのワークフローも追加され、大規模データ処理が手軽になりました。

---

### 2. Esri Site Scan for ArcGIS May 2026 — クラウドGS、最大1万枚処理

**重要度：★★★★**  
**URL：** https://www.esri.com/arcgis-blog/products/arcgis/imagery/whats-new-in-reality-mapping-may-2026  

**概要：**  
ドローン測量プラットフォームSite Scan for ArcGISにクラウド上での3DGS生成機能が追加。1ミッションあたり最大10,000枚の画像を処理可能に。建設・インフラ・都市計画での大規模現場3DGS化が現実的になりました。

---

### 3. Veesus May 2026アップデート — SolidWorksでGSを直接操作

**重要度：★★★**  
**URL：** https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update  

**概要：**  
製造業の標準CADソフトSolidWorksで、3DGSデータを直接読み込み・可視化できるようになりました。従来のCADモデルと現実スキャン（3DGS）を同一環境でシームレスに比較・編集可能。工場改修・製品設計・リバースエンジニアリングへの即活用が可能です。

---

### 4. 3DVista 2026.0 — Total VR Mode + 全機能GS対応

**重要度：★★★**  
**URL：** https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/  

**概要：**  
バーチャルツアー作成ツール3DVistaが2026.0で「完全VRモード」を導入。ほぼ全てのUI要素（ボタン・クイズ・タイマー・E-Learningなど）がVRヘッドセット内で動作し、3DGSモデルもVRで完全機能。不動産・観光・教育向けGS活用の新次元へ。

---

### 5. XGRIDS LCC Cloud 商用化 — $800/年でSLAM+GS

**重要度：★★★**  
**URL：** https://radiancefields.com/xgrids-releases-new-lcc-studio-lcc-scan-and-portalcam-firmware  

**概要：**  
XGRIDSのLCCクラウドが正式商用化。月250分の処理枠でSLAMと3DGSの生成をクラウドで完全自動化。年間$800 USDというサブスク価格。高スペックなPCなしで本格的な3DGS制作が可能な時代へ。

---

### 6. Netflix「ベルリン」— VoligaのGSでLEDバーチャルプロダクション

**重要度：★★★**  
**URL：** https://web.volinga.ai  

**概要：**  
2026年5月15日配信開始のNetflixドラマ「ベルリンと貴婦人」（Money Heistシリーズ）が、マドリードの実際の街並みをVoligaの3DGSワークフローでLEDバーチャルプロダクション用の背景として使用。主要エンタメコンテンツで3DGSが実証されました。

---

### 7. NHM Vienna × Geofront — 70万Gaussiansで宝石を復元

**重要度：★★**  
**URL：** https://radiancefields.com/  

**概要：**  
オーストリア・ウィーン自然史博物館（NHM Vienna）所蔵のマリア・テレジアの宝石飾りを70万Gaussiansでデジタル化。色褪せた葉の部分をキュレーターがデジタル上で修復・復元。文化財保存×3DGSの先進的な事例。

---

## コミュニティ・ツール

### 1. houdini-gsplat（Plattipus）— Houdini SolarisでOpenUSD GS統合

**重要度：★★★★**  
**URL：** https://github.com/plattipus/houdini-gsplat  

**概要：**  
OpenUSD v26.03で標準化された3DGSスキーマをHoudini Solaris（USDベースのVFXパイプライン）で直接使えるオープンソースプラグイン。カスタムHydraデリゲート・USDイメージングアダプタ・3つのLOPノード（PLY読み込み・インスタンス化・レンダリング）を含みVFXスタジオのGSワークフロー統合を大幅に簡略化します。MITライセンス。

---

### 2. Gaussian Splat Morphing Tool（Felix Hirt）— GS間の滑らかな変形

**重要度：★★★**  
**URL：** https://github.com/feel3x/Gaussian_Splat_Morpher  

**概要：**  
複数の3DGSモデル間を滑らかにモーフィング（変形）できるオープンソースCLIツール。位置・色・回転・スケール全てを補間し、「工事前」→「工事後」のシームレスな変化映像などを自動生成。SLERPで滑らかな回転補間。MITライセンス。

---

### 3. PlayCanvas SOG（Spatially Ordered Gaussians）— 95%容量削減のWebフォーマット

**重要度：★★★**  
**URL：** https://blog.playcanvas.com/playcanvas-open-sources-sog-format-for-gaussian-splatting/  

**概要：**  
GS向けの新圧縮フォーマット「SOG」がオープンソースで公開。400万Gaussiansのシーンが元の1GB PLYから**42MB（約95%削減）**に圧縮可能。位置を16bit量子化+対数座標系で格納、回転を26bit四元数エンコード。WebPロスレスでパック。完全オープンソースで任意エンジンに組み込み可能。

---

### 4. ShorterSplatting CVPR 2026 — 公式コード公開

**重要度：★★**  
**URL：** https://github.com/MachinePerceptionLab/ShorterSplatting  

**概要：**  
CVPR 2026採択論文「より短いGaussianリストで3DGS学習を高速化」の公式実装がGitHubで公開。スケールリセットとエントロピー正則化でGaussianの数を減らしつつ品質を維持し、学習を効率化。既存フレームワークへのプラグイン形式での組み込みも可能。

---

## 開発者インサイト

### すぐ使えるツール・コード

| ツール | 用途 | URL |
|--------|------|-----|
| ShorterSplatting | 3DGS学習高速化 | https://github.com/MachinePerceptionLab/ShorterSplatting |
| Gaussian Splat Morphing Tool | GS間モーフィング映像生成 | https://github.com/feel3x/Gaussian_Splat_Morpher |
| houdini-gsplat | Houdini/USD GS統合 | https://github.com/plattipus/houdini-gsplat |
| PlayCanvas SOG | Web配信GS圧縮フォーマット | https://blog.playcanvas.com/playcanvas-open-sources-sog-format-for-gaussian-splatting/ |

### 今後対応すべき動向

1. **測量・建設業界** — EsriクラウドGSの波。「ドローン映像→クラウド→3DGS→CAD比較」ワークフローが標準化しつつある
2. **製造業** — Veesus×SolidWorksはCADへのGS統合の幕開け。CATIAやCreoへの波及に注目
3. **無線通信インフラ** — RxGS・OctCGSで5G/WiFi電波場マッピングへのGS活用が本格化
4. **超大規模GS** — TideGSで「都市全体のGS」が現実的に。デジタルツイン・スマートシティ分野での先行投資機会
5. **エンタメ制作** — Netflix実績が示す「現地ロケ→GS背景」の代替コスト効果。日本映像制作会社での採用検討価値が高まる

---

*レポート生成：2026-05-26 | 次回更新予定：2026-05-27*
