# 3DGS & 4D生成 デイリーレポート — 2026年5月29日

**総件数**: 21件（論文 9件 / ニュース 7件 / コミュニティ・ツール 5件）  
**カバー期間**: 2026年5月16日〜5月29日（`past_3dgs.json` 未掲載の新規項目のみ）

---

## 🔥 今日の注目トレンド TOP 5

1. **Eulerian Gaussian Splatting（Harvard/Google DeepMind）** — 密度化ヒューリスティックを「確率密度の勾配最適化」に刷新。3DGSの根本アルゴリズム改革へ。
2. **Chaos Corona 15 — GS×グローバルイルミネーション** — 市販CGレンダラーが「GSシーンから周囲オブジェクトへ光を反射」を標準機能化。CG×GS統合の壁が崩れた。
3. **Manycore Tech Aholo Viewer OSS — 10億スプラットをブラウザで** — World Labs Spark 2.0の10倍スケール対応OSSビューア。都市規模のGSシーンがWebで閲覧可能に。
4. **Netflix × Volinga — 大作ドラマにGSバーチャルプロダクション本格採用** — マドリードの実街並みをGSでLEDボリュームに取り込み。NetflixクラスでGSが制作標準ツール化へ。
5. **PG-3DGS — 物理機能付き3D生成** — 流体力学・空力学的に機能する3DオブジェクトをGSで生成。工業設計・ロボティクスの新応用分野へ。

---

## 📄 注目論文

### 1. Eulerian Gaussian Splatting using Hashed Probability Pyramids
- **ソース**: arXiv:2605.29136（2026年5月27日）
- **著者所属**: Harvard University / Google DeepMind / Google
- **リンク**: https://arxiv.org/abs/2605.29136
- **重要度**: ★★★★★
- **概要**: ガウシアンの密度化を「手動ルールによる増減」から「学習可能な確率密度分布の勾配最適化」に刷新。Hashed Probability Pyramid（多スケール格子）と制御変量による分散低減を組み合わせ、mip-NeRF 360でSOTA達成かつ3DGS同等の描画速度を維持。アルゴリズムの根本的再設計として研究界への影響大。

### 2. PG-3DGS: 物理目標を満たす3D Gaussian Splatting
- **ソース**: arXiv:2605.11266（2026年5月）
- **リンク**: https://arxiv.org/html/2605.11266v1
- **重要度**: ★★★★
- **概要**: 微分可能物理シミュレーション＋3DGSを結合し、外観損失と物理目標を同時最適化。「注ぎ口から液体が注げるティーポット」「揚力を生む飛行機の翼」を生成。工業設計・ゲーム・ロボティクスへ応用。

### 3. AIR: 自己教師あり・フィードフォワード2D Gaussian Splatting
- **ソース**: arXiv:2605.20820（2026年5月20日）
- **リンク**: https://arxiv.org/abs/2605.20820
- **重要度**: ★★★
- **概要**: 従来1枚ごとにコストの高い最適化が必要だった2DGSを単一ネットワーク推論に圧縮。残差ベース段階的アーキテクチャ＋自己教師あり学習＋量子化でコンパクトなGS保存を実現。画像圧縮・高速配信への応用。

### 4. FaceParts: GS顔アバターの教師なしパーツ分割・編集
- **ソース**: arXiv:2605.13853（2026年5月）
- **リンク**: https://arxiv.org/abs/2605.13853
- **重要度**: ★★★★
- **概要**: ラベルデータなしで「目・鼻・口・耳」単位に顔GSアバターを自動分割。FLAMEアンカーによる別アバターへのパーツ移植が可能。メタバースアバター編集・ゲームキャラカスタマイズへ直接応用。

### 5. DSGS: デコーダサイドGS for 没入型ビデオ
- **ソース**: arXiv:2605.17002（2026年5月16日）
- **リンク**: https://arxiv.org/abs/2605.17002
- **重要度**: ★★★★
- **概要**: 没入型映像ストリーミング時、圧縮テクスチャだけ送りデコーダ側でGSを再構築することで帯域を大幅削減。圧縮ノイズが低周波フィルタとして安定化に寄与するという逆転の発想。VR/ARストリーミングのちらつき問題も解消。

### 6. Underwater360: 水中パノラマGS再構成
- **ソース**: arXiv:2605.26447（2026年5月26日）
- **リンク**: https://arxiv.org/abs/2605.26447
- **重要度**: ★★★
- **概要**: 360度パノラマカメラ＋3DGSで水中シーンを再構成。光の吸収・散乱（参加媒体効果）と球面歪みの両方に対処。サンゴ礁・海底遺跡のVR体験、海洋調査への応用。コード・データセット公開予定。

### 7. RxGS: 受信機汎化型RF信号3DGS合成
- **ソース**: arXiv:2605.24290（2026年5月22日）
- **リンク**: https://arxiv.org/abs/2605.24290
- **重要度**: ★★★
- **概要**: 5G/6G通信シミュレーション向け。従来固定受信機のみ対応だったGSベースRF合成を任意受信機位置に汎化。シーン幾何（受信機非依存）と指向性放射場（受信機依存）を二段構えで学習。

### 8. GScomp-QA: 圧縮GS品質評価データセット
- **ソース**: arXiv:2605.26880（2026年5月26日）
- **リンク**: https://arxiv.org/abs/2605.26880
- **重要度**: ★★★
- **概要**: 乱立するGS圧縮手法を「人間の目で見た品質」で比較する標準ベンチマーク（MOS評価）を構築。GS品質標準化の共通基盤として機能することが期待される。

### 9. ShorterSplatting（CVPR 2026）: ガウシアンリスト短縮で学習高速化
- **ソース**: arXiv:2603.09277 / CVPR 2026
- **GitHub**: https://github.com/MachinePerceptionLab/ShorterSplatting
- **重要度**: ★★★★
- **概要**: アルファブレンディングの重み分布を鋭くするエントロピー制約を導入し、少ない粒子数で高品質を維持しながら学習を大幅高速化。公式コード公開済み。本番環境への導入検討材料に。

---

## 📰 業界ニュース

### 10. Chaos Corona 15 — GSがグローバルイルミネーションに参加
- **ソース**: Chaos / radiancefields.com（2026年5月27日）
- **リンク**: https://radiancefields.com/corona-15-makes-gaussian-splats-participate-in-global-illumination
- **重要度**: ★★★★★
- **概要**: 3ds Max/Blender向け高品質商用レンダラーCoronaがv15で「GSシーンが周囲の3Dモデルへ間接光を反射」を実現。ドローン撮影GSの背景とCG要素の光学的統合が可能に。建築VIZ・映像制作のCGパイプラインに直接インパクト。

### 11. Manycore Tech・Aholo Viewer OSSリリース — 10億スプラット対応
- **ソース**: PR Newswire（2026年5月26日）
- **リンク**: https://www.prnewswire.com/news-releases/manycore-tech-open-sources-3d-gaussian-viewer-ushering-in-the-era-of-the-3d-internet-302781474.html
- **重要度**: ★★★★★
- **概要**: 中国AI企業がブラウザで都市規模（10億スプラット超）のGSシーンを表示できるOSSビューアを公開（MIT）。スマホ・PC・VR全対応。World Labs Spark 2.0の10倍スケール。空間AI APIも同時開放。

### 12. XGRIDS LCC Cloud 商用化 — 年$800でSLAM+3DGSクラウド処理
- **ソース**: radiancefields.com（2026年5月21日）
- **リンク**: https://xgrids.com/lcc
- **重要度**: ★★★★
- **概要**: PortalCamで撮影→クラウドアップロード→SLAM+3DGS全自動処理という「撮るだけ」ワークフローが月250分・年$800で商用化。建設・不動産・デジタルツイン制作のプロが安定利用可能に。

### 13. Netflix「Berlin and the Lady with an Ermine」— VolingaのGSでバーチャルプロダクション
- **ソース**: Volinga / radiancefields.com（2026年5月19日）
- **リンク**: https://web.volinga.ai/how-to-use-gaussian-splats-for-virtual-production/
- **重要度**: ★★★★★
- **概要**: Netflixドラマでマドリードの実写街並みをGSで取り込みLEDボリュームに投影。CGより速くリアルなロケーション感を実現。NetflixクラスのコンテンツにGSが制作標準ツールとして採用された象徴的事例。

### 14. Geofront × NHM Vienna — マリア・テレジア宝石花束を70万スプラットで保存・修復
- **ソース**: radiancefields.com（2026年5月20日）
- **重要度**: ★★★★
- **概要**: オーストリア自然史博物館所蔵の18世紀宝石花束を70万スプラットのGS 3Dモデルとして保存。学芸員がデジタル空間上で退色した葉を修復。物理的な展示品に触れずに研究・修復できるGSの文化財応用の象徴的事例。

### 15. Esri ArcGIS Reality & Site Scan May 2026 — クラウドGS生成・最大1万枚対応
- **ソース**: esri.com（2026年5月）
- **リンク**: https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026/
- **重要度**: ★★★★
- **概要**: GISの世界最大手Esriが5月更新でGS機能を大幅強化。Site Scanはクラウド型GS生成を追加し1ミッション最大1万枚処理可能に。ArcGIS Reality StudioもGS精度向上。

### 16. Veesus May 2026 — SolidWorks GS対応・レンズフレア・動的影を追加
- **ソース**: radiancefields.com（2026年5月）
- **リンク**: https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update
- **重要度**: ★★★
- **概要**: CAD設計者がSolidWorks環境を離れずにGSを確認できるプラグインを追加。レンズフレア＋動的影でフォトリアルな提案資料作成も可能。製造・設計業界へのGS普及を後押し。

---

## 💬 コミュニティ・SNS話題

### 17. houdini-gsplat — USD-native GS for Houdini 21 Solaris（MITライセンス）
- **ソース**: Alliance for OpenUSD Forum
- **リンク**: https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921
- **重要度**: ★★★★
- **概要**: Houdini 21のSolaris内でGSをネイティブレンダリングできる初のプラグイン（MIT）。PLYをインポートするだけでUSD v26.03スキーマ準拠プリムとして配置可能。VFXパイプラインへのGS統合のリファレンス実装として重要。

### 18. 大塚商会 × STUDIO55 — 3DGS建設DXワークショップ 大阪開催（日本）
- **ソース**: 大塚商会公式（2026年5月21日）
- **リンク**: https://www.otsuka-shokai.co.jp/event/region/26/w0521cad/
- **重要度**: ★★★
- **概要**: SLAMスキャナ＋GS技術で現場調査を5時間→1時間に短縮するデモを大阪で実演。日本の建設・リノベーション業界でGS実務活用が急加速していることを示す。

### 19. TREND-POINT 3DGS出力オプション — 2026年6月16日リリース予告（日本）
- **ソース**: ASCII.jp（2026年5月）
- **リンク**: https://ascii.jp/elem/000/004/402/4402852/
- **重要度**: ★★★
- **概要**: 国内建設・測量会社に広く普及している点群処理ソフト「TREND-POINT」（福井コンピュータ）に3DGS出力オプションが6月16日登場予定（12万円/税別）。日本の建設測量ワークフローへのGS統合が本格化。

### 20. 「GS: From Billion-Scale Worlds to Intelligent Robot Hands」解説記事拡散
- **ソース**: SciPaperMill（2026年5月23日）
- **リンク**: https://scipapermill.com/2026/05/23/gaussian-splatting-from-billion-scale-worlds-to-intelligent-robot-hands/
- **重要度**: ★★★
- **概要**: 都市スケールデジタルツインからロボットハンド制御まで、GS技術の最新応用範囲を俯瞰する解説記事。SNSで広く拡散中。技術の全体像を短時間で把握するエントリーポイントに最適。

### 21. Splatware — GS生成・編集・販売をブラウザで一括完結するプラットフォーム
- **ソース**: splatware.com
- **リンク**: https://splatware.com/
- **重要度**: ★★★
- **概要**: 2026年2月ローンチ後コミュニティで継続的に話題。スマホ/DSLR/ドローン/360カメラ映像→GS生成→ブラウザ編集→マーケットプレイスで販売というワンストップフロー。Blender・UE・Unity連携パス付き。

---

## 🛠 開発者向けインサイト

### 高優先度（今すぐ評価・検討）
- **Aholo Viewer（MIT OSS）** — 1億スプラット超のWebシーン表示が必要なら即評価。https://www.prnewswire.com/news-releases/manycore-tech-open-sources-3d-gaussian-viewer-ushering-in-the-era-of-the-3d-internet-302781474.html
- **Chaos Corona 15** — 建築VIZ・映像制作パイプラインへのGI統合を検討。https://www.chaos.com/corona/whats-new
- **houdini-gsplat** — Solaris/USDベースVFXパイプライン向け。Houdini 21.0.559+、MIT。

### 中期対応（今月中に調査）
- **Eulerian GS（2605.29136）** — 次世代GS密度化の方向性を左右する基盤論文。要ウォッチ。
- **Esri ArcGIS Reality / Site Scan May 2026** — GISパイプライン×GS案件を持つ場合は最新機能確認を。
- **XGRIDS LCC Cloud** — LiDAR×GS再構成アウトソースの選択肢として年$800のコスト感を確認。

### 実装前に読むべき論文
- **PG-3DGS（2605.11266）** — 物理制約付きGS設計の先行事例。
- **ShorterSplatting（2603.09277）** — 本番環境向け学習高速化。公式コード公開中。https://github.com/MachinePerceptionLab/ShorterSplatting
- **FaceParts（2605.13853）** — アバター・メタバース製品向け顔パーツ分割。

### 🇯🇵 日本市場向け情報
- **TREND-POINT GS出力オプション**（6月16日リリース予定）https://ascii.jp/elem/000/004/402/4402852/
- **大塚商会×STUDIO55ワークショップ**実施済み（5月21日）https://www.otsuka-shokai.co.jp/event/region/26/w0521cad/

---

*レポート生成日: 2026年5月29日 | 次回重複排除のため past_3dgs.json を更新済み*
