# 3DGS & 4D生成 デイリーレポート — 2026-05-21

> 重複排除済み（`past_3dgs.json` 照合）｜前回配信: 2026-05-15

---

## サマリー

| カテゴリ | 件数 |
|---|---|
| 注目論文 | 4件 |
| 業界ニュース | 4件 |
| ツール | 2件 |
| コミュニティ | 2件 |
| **合計** | **12件** |

---

## 今日のハイライト（5選）

1. **LeGS** — Gaussianの「増やす・消す」判断を強化学習（RL）で自動化。長年の職人芸的なパラメータ設定が不要に
2. **Geo Week 2026（5/19開催）** — 測量・GIS業界の最大カンファレンスで3DGSが主役テーマに。NVIDIA・Esri・Cesiumが一堂に
3. **ArcGIS Reality Studio May 2026** — 薄い構造物・植生・細かいテクスチャの再現精度が大幅向上。大規模測量に商用展開
4. **CLM-GS（ASPLOS 2026）** — CPU活用でGPU1枚（RTX4090）に1億個のGaussianを格納・学習できる技術が公開
5. **Plattipus houdini-gsplat** — 映像制作の標準ツール「Houdini 21」がOpenUSD v26.03ベースのGSプラグインをオープンソース化

---

## 注目論文（重要度：高）

### 1. LeGS — 強化学習でGaussianの密度制御を自動化

- **ArXiv**: https://arxiv.org/abs/2605.00408
- **投稿日**: 2026-05-11
- **重要度**: ⭐⭐⭐⭐⭐

**何ができるようになったか**
3DGSでは「どこにGaussianを増やすか・どこを削るか」の密度制御を、これまで研究者が手で設計したルールに頼っていた。LeGSはこの判断をニューラルネットワーク＋強化学習（RL）で完全自動化する。シーンごとに適応的に最適化されるため、複雑な形状でも無駄なGaussianを減らしながら高品質な再構成を維持できる。

**これまでの課題と解決方法**
従来の密度制御（ADCアルゴリズム）は「勾配の大きさ」だけを見て判断するため、複雑な幾何形状や見る角度によって判断が不安定になりやすかった。LeGSは「各Gaussianが品質にどれだけ貢献しているか」を感度分析で数値化し、それを報酬関数としてRLポリシーネットワークが学習する。

---

### 2. FaceParts — 3DGSアバターの顔パーツを自動分解・編集

- **ArXiv**: https://arxiv.org/abs/2605.13853
- **OpenReview**: https://openreview.net/forum?id=OM5kwmiZGj
- **重要度**: ⭐⭐⭐⭐

**何ができるようになったか**
3DGSで作った顔アバターを「眉毛・目・ひげ・まつ毛」などのパーツに自動で分解し、個別に編集したり、別のアバターとパーツを移植したりできる。ラベル付き教師データなし（完全教師なし）で動作する。

**これまでの課題と解決方法**
従来のGS顔編集は2D画像や3Dメッシュを介した間接的なアプローチが主流で、Gaussianドメインで直接パーツ分解する手法がなかった。FaceParts はGumbel-Softmaxを活用した神経網がGaussianの中心・色・不透明度・共分散から直接パーツカテゴリを予測する。NeRSembleデータセット（11人）で検証済み。

---

### 3. CLM-GS — GPU1枚で1億Gaussianを学習する技術（ASPLOS 2026）

- **ArXiv**: https://arxiv.org/abs/2511.04951
- **GitHub**: https://github.com/nyu-systems/CLM-GS
- **プロジェクトページ**: https://tarzanzhao.github.io/CLM-GS/
- **重要度**: ⭐⭐⭐⭐⭐

**何ができるようになったか**
RTX4090 GPU 1枚で1億個のGaussianを学習でき、25km²規模の都市を3DGSで再構成できるようになった。NYUが開発し、ASPLOS 2026に採択、コードも公開済み。36krの中国語メディアでも「GPUメモリの壁を打破」として大きく報じられた。

**これまでの課題と解決方法**
大規模シーン（億単位のGaussian）の学習には複数GPUが必須で、メモリ不足によるOOMエラーが頻発していた。CLMは「位置・形状などの判断に重要な属性だけをGPUに置き、その他の属性をCPUメモリに退避」し、GPU-CPU間通信とGPU計算をパイプライン化してオーバーヘッドを最小化する。

---

### 4. gs-embedding — 3DGSをニューラルネットが扱いやすい統一表現に変換（ICLR 2026）

- **ArXiv**: https://arxiv.org/abs/2509.22917
- **GitHub**: https://github.com/cilix-ai/gs-embedding
- **プロジェクトページ**: https://cilix-ai.github.io/gs-embedding-page/
- **重要度**: ⭐⭐⭐

**何ができるようになったか**
3DGSのGaussianパラメータを「サブマニフォールドフィールド（SF）埋め込み」と呼ばれる統一的な特徴量に変換し、ニューラルネットが3DGSを理解・処理しやすくする。3D編集・生成・分類などのタスクの精度が向上する。

**これまでの課題と解決方法**
3DGSの各Gaussianは位置・スケール・回転・球面調和係数など異種混合なパラメータを持ち、ニューラルネットに直接入力すると「Gaussianの順序が変わっても同じシーン」という非一意性の問題が生じた。SF埋め込みは連続的なサブマニフォールド場としてこの問題を解決し、均質で微分可能な表現を提供する。

---

## 業界ニュース

### 5. Geo Week 2026 — 地理空間最大カンファレンスを3DGSが席巻（5月19日）

- **Radiance Fields レポート**: https://radiancefields.com/gaussian-splatting-at-geo-week-2026
- **セッション情報**: https://www.geo-week.com/session/ai-gaussian-splatting-and-what-comes-next/

米国コロラド州で開催されたGeo Week 2026に、NVIDIA・Esri（ArcGIS）・Cesium・XGRIDS・Hexagonが登壇しGSを大々的にアピール。「AEC・GIS業界へのGS影響」と「AI・GSと次のステップ」の2セッションで円卓議論が行われた。Michael Rubloff（Radiance Fields編集長）がファシリテーターを担当。測量・デジタルツイン・AEC業界でのGS採用が加速していることを示すマイルストーン的イベントとなった。

---

### 6. ArcGIS Reality Studio May 2026 — 薄構造物・植生のGS品質が向上、クラウドワークフロー対応

- **公式ブログ**: https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026

Esriが5月リリースのArcGIS Reality StudioでGaussian Splatの品質を大幅強化。これまで苦手だった「電線・フェンス・木の葉・建物の細部」の再現精度が向上。クラウドベースのエンドツーエンドワークフロー（VM＋クラウドホスト入力）に対応し、企業が大規模プロジェクトをオンプレ不要でクラウド処理できるようになった。品質保証（QA）機能も追加され、テスト工数を削減。大手地理情報企業がGSを本格的に商用パイプラインに組み込んだ象徴的なリリース。

---

### 7. Esri Site Scan May 2026 — クラウドGS生成 & 1ミッション1万枚上限に拡大

- **公式**: https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026

ドローン測量向け「Site Scan for ArcGIS」の5月版でクラウド上でのGS生成に対応。1ミッション当たりの処理画像上限を10,000枚に引き上げ（従来比大幅増）。現場写真を大量にアップロードするだけでGSが自動生成されるため、建設・インフラ・防災での大規模現場デジタル化が手軽に。

---

### 8. Hexagon CityMapper-3 — GS対応航空マッピングシステム「City Splatter」がGeo Weekに登場

- **プレスリリース**: https://hexagon.com/company/newsroom/press-releases/2026/next-gen-leica-citymapper-3-increases-efficiency-for-airborne-urban-and-regional-mapping
- **GeoWeekニュース**: https://www.geoweeknews.com/news/hexagon-unveils-next-generation-mapping-solutions-at-geo-week-2026

Hexagon（Leica Geosystems）が次世代航空マッピングシステム「CityMapper-3」を発表。3カメラ垂直配置で従来比3倍の幅の地域を1フライトでカバー。GS生成モードを搭載し、社内では「City Splatter」と呼ばれている。都市規模のデジタルツインをGS形式で直接生成できる航空機搭載センサーとして、Geo Week 2026で存在感を示した。

---

## ツール

### 9. Plattipus houdini-gsplat — Houdini 21 SolarisでOpenUSD v26.03のGSスキーマに対応（OSS）

- **GitHub**: https://github.com/plattipus/houdini-gsplat
- **OpenUSDフォーラム**: https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921
- **公開時期**: 2026-05中旬（約1週間前）

VFX・映像制作の業界標準ツール「Houdini 21」のSolarisステージ（USDベース）にGSを直接組み込めるオープンソースプラグイン。OpenUSD v26.03で策定された公式GSスキーマ（`UsdVolParticleField3DGaussianSplat`）をネイティブ実装し、Hydraデリゲート・USDImagingアダプター・3つのLOPノード（PLYインポート・GSインスタンサー・Uruk）を提供。PLYファイルをインポートしてビューポートでリアルタイム確認し、シーン全体にインスタンス化できる。Plattipus Research and Production Labが公開。

---

### 10. SuperSplat — ソフトウェア帰属・コリジョン生成・GPUヒストグラムの3機能追加

- **PlayCanvas Blog**: https://blog.playcanvas.com/new-in-supersplat-software-attribution-collision-generation-and-histogram/

PlayCanvasのブラウザ型GS編集ツール「SuperSplat」の新機能:
- **ソフトウェア帰属**: 作品ページにどのツールで作ったか明記（Postshot・Polycam・LichtFeld Studio等対応）
- **コリジョン生成**: ワンクリックで3DシーンのAI衝突判定データを自動生成（室内/屋外/物体の3プリセット）。コマンドライン不要でSplatTransform 2.0を活用
- **GPUヒストグラム**: 数百万個のGaussianの統計を瞬時にGPU並列計算。ヒストグラムをドラッグして選択範囲を直感的に指定可能に

---

## コミュニティ・SNS話題

### 11. Gaussian Splat Morpher — GS同士をモーフィングするCLIツールがOSS公開

- **GitHub**: https://github.com/feel3x/Gaussian_Splat_Morpher
- **Radiance Fields紹介**: https://radiancefields.com/gaussian-splatting-morphing-tool-to-blend-between-3dgs-captures
- **制作者**: Felix Hirt

2つ以上の.plyファイルを入力すると、位置・色・回転・スケール全てを空間＆色の類似度でマッチングし、滑らかに補間するモーフィング動画を生成するCLIツール。MIT License。コマンドラインとリアルタイムインタラクティブビジュアライザーの2モード。回転補間にはスレープ（Slerp）を使用。「花が咲く瞬間」「季節の移ろい」「建物の経年変化」といった表現が手軽に制作可能に。

---

### 12. 3DVista — 圧縮GS（SPZ形式）対応でバーチャルツアーの読み込みが高速化

- **Radiance Fields**: https://radiancefields.com/3dvista-adds-compressed-3dgs-and-spz-support

不動産・観光向けバーチャルツアー作成ツール「3DVista VT Pro」がSPZ（球面調和係数圧縮GS形式）に対応。PLYと比べてファイルサイズが大幅に小さくなり、モバイル端末での3DGSツアー読み込みが高速化。KhronosグループのglTF GS標準圧縮形式（`KHR_gaussian_splatting_compression_spz`）の普及がバーチャルツアー市場にも波及しつつある動きとして注目。

---

## 開発者向けインサイト

### 今すぐ試せるOSSリリース

| ツール | 概要 | リンク |
|---|---|---|
| CLM-GS | GPU1枚で1億GS学習（NYU・ASPLOS 2026） | https://github.com/nyu-systems/CLM-GS |
| houdini-gsplat | Houdini 21 SolarisでGS＋USD | https://github.com/plattipus/houdini-gsplat |
| gs-embedding | 3DGSの統一表現（ICLR 2026） | https://github.com/cilix-ai/gs-embedding |
| Gaussian Splat Morpher | GS間モーフィングCLI | https://github.com/feel3x/Gaussian_Splat_Morpher |

### 対応すべきトレンド

1. **SPZ形式の採用を検討** — Khronos標準の圧縮GS形式SPZを3DVista・Niantic SPZなどが採用済み。WebやモバイルでGSを配信するなら今後の主流フォーマット
2. **ArcGIS/PIX4D統合で測量ユーザー層が急拡大** — 専門技術なしでもGSを生成できる環境が整備され、測量・建設業界からの需要が急増する可能性
3. **Houdini × OpenUSD × GS連携が本格化** — VFXパイプラインへのGS統合を考えている場合、v26.03のUSDスキーマに早めに対応することで先行優位
4. **CVPR 2026（6/3〜7, Denver）直前** — 50件超のGS論文が発表予定。来週以降にコードとプロジェクトページが大量公開される見込み
5. **LeGSでRL×3DGS密度制御研究が加速** — 自動密度制御は論文数が急増している分野。実装コードの公開を注視

---

*配信日: 2026-05-21 | 作成: Claude Code (AI) | ソース: arXiv, Radiance Fields, Esri Blog, Geo Week News, GitHub*
