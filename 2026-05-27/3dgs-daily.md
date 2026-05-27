# 3DGS & 4D生成 デイリーレポート — 2026-05-27

**本日の件数:** 22件（論文8件 / ニュース7件 / コミュニティ7件）

---

## 🔥 今日の注目トレンド
1. **10億個ガウシアンを1枚のGPUで学習** — TideGSが都市スケール再構成の壁を突破
2. **CADソフト「SolidWorks」でGSが動く** — VeesusがMay更新で対応し製造業への本格普及が近づく
3. **HoudiniがUSDネイティブでGS対応** — PlattipusがHoudini Solaris向けプラグインをOSS化
4. **測量・GIS業界が本格採用** — Esriが2大ツールを同時アップデートしクラウドGS生成を解禁
5. **GS同士をブレンドするモーフィングツール登場** — 2つの3DGSキャプチャを滑らかに補間

---

## 📄 注目論文

### 1. TideGS — 10億個のガウシアンを家庭用GPU1枚で学習
- **arXiv:** [2605.20150](https://arxiv.org/abs/2605.20150) (2026-05-19)
- **重要度:** ⭐⭐⭐⭐⭐
- **概要:** これまで都市スケールのGS学習には大量のGPUが必要で、大企業か研究機関しか実施できなかった。TideGSはSSD→CPU→GPUの3段階キャッシュ方式を用い、10億個以上のガウシアンを24GB GPU（RTX 3090相当）1枚だけで学習可能にした。学習中は現在のカメラから見えるガウシアンだけをGPUにロードする仕組みで、街全体のフォトリアル3Dマップが単一マシンで作れるようになる。分散マルチGPU環境のコストと複雑さを丸ごと回避できる点が画期的。

### 2. CLM-GS — 「GPUメモリの壁」を撤廃（ASPLOS 2026）
- **arXiv:** [2511.04951](https://arxiv.org/abs/2511.04951) | **GitHub:** [nyu-systems/CLM-GS](https://github.com/nyu-systems/CLM-GS)
- **重要度:** ⭐⭐⭐⭐
- **概要:** 1億200万個のガウシアンをRTX 4090 1枚で描画・学習可能にする手法。位置や形状など「どのガウシアンが今見えるか」の判定に必要な属性だけをGPUに置き、残りはCPUメモリにオフロード。通信・計算・CPUワークをパイプライン処理で並列化し、VRAM不足を解消する。TideGSと合わせて「大規模GSの民主化」が加速している。ASPLOS 2026採択。

### 3. DSGS — 動画配信を変える「1つのアトラスで完結」するGS
- **arXiv:** [2605.17002](https://arxiv.org/abs/2605.17002) (2026-05-16)
- **重要度:** ⭐⭐⭐⭐
- **概要:** 360度没入型動画向けに、デコード側（視聴端末）でGSを展開する新方式。従来は大容量の3DGSを丸ごとダウンロードする必要があったが、本手法では圧縮された「アトラス（地図）」1枚を送るだけで端末側がリアルタイムに3DGSを復元。既存動画配信インフラをほぼ変えずに没入型3D映像を届けられる。動画ストリーミング業界への影響が大きい。

### 4. RxGS — 電波伝搬をガウシアンで予測
- **arXiv:** [2605.24290](https://arxiv.org/abs/2605.24290) (2026-05-22)
- **重要度:** ⭐⭐⭐
- **概要:** 3DGSの「空間を光で記述する能力」を電波（RF）に応用。送受信機の位置ごとに異なる電波の届き方を、空間共通の形状ガウシアン＋方向依存の放射成分で表現する。1つのモデルで異なる受信機位置すべてに汎化できる点が新しい。6G基地局配置の最適化やチャンネル予測に使える初の受信機汎化型モデル。

### 5. OctCGS — 6G無線通信のチャンネルマップをGSで構築
- **arXiv:** [2605.22961](https://arxiv.org/abs/2605.22961) (2026-05-21)
- **重要度:** ⭐⭐⭐
- **概要:** 環境内のすべての「電波の跳ね返り方」をオクツリー（空間を8分割する木構造）で管理し、それぞれのノードにガウシアンを配置することで、電波がどのように反射・回折して届くかを高精度かつ低コストでモデル化。ニューラルネットによる暗黙的モデルより高速かつ解釈しやすい。6G通信インフラ設計に活用できる。

### 6. GS Transcoding — 3Dモデルを元画像なしでGSに変換
- **arXiv:** [2605.21051](https://arxiv.org/abs/2605.21051) (2026-05-20)
- **重要度:** ⭐⭐⭐
- **概要:** 既存の3Dメッシュやポイントクラウドから、撮影時の元画像を一切使わずにGSモデルを生成するエンドツーエンドパイプライン。ゲームアセットやCADデータをGSに「トランスコード」できるため、膨大な3Dアセット資産をそのままGSで使えるようになる。コンテンツライブラリのGSへの移行コスト削減につながる実用的な手法。

### 7. FaceParts — 顔GSアバターを「パーツ」ごとに編集・差し替え
- **arXiv:** [2605.13853](https://arxiv.org/abs/2605.13853) (2026-05-13)
- **重要度:** ⭐⭐⭐
- **概要:** 3DGSで生成された顔アバターを、目・鼻・口・眉毛などのパーツ単位で自動的に分割し、別のアバターのパーツと差し替えたり、個別に変形したりできる。教師なし（ラベルなし）でパーツ分割できる点が特徴。アニメーション・映画・ゲームのキャラクター制作ワークフローを大幅に短縮できる。

### 8. HarmoGS — 「野生」の撮影データでもきれいなGSを作る
- **概要（Sun Yat-sen University）:** 観光地など複雑な光環境・混雑した場所の画像から3DGSを作るとき、異なる条件の写真同士で勾配が衝突しノイズが乗る問題を「対立勾配の調和（Conflict-Aware Gradient Harmonization）」で解消。雑多な条件で撮影した写真でもきれいなGS再構成が得られる。
- **重要度:** ⭐⭐⭐

---

## 📰 業界ニュース

### 9. Esri Site Scan for ArcGIS — クラウドGS生成が解禁（May 2026）
- **URL:** [What's New in Site Scan (May 2026)](https://www.esri.com/arcgis-blog/products/site-scan/imagery/whats-new-in-site-scan-for-arcgis-q2-2026)
- **重要度:** ⭐⭐⭐⭐⭐
- **概要:** 世界最大のGISベンダーEsriが、測量・建設向けドローンデータ管理ツール「Site Scan for ArcGIS」でGS生成をクラウド処理対応に。1ミッションあたり最大1万枚の画像を処理可能（従来比2倍以上）。専用ハードウェア不要で現場から即GS生成できる。測量・建設・インフラ管理分野での商用普及に決定的なインパクト。

### 10. Esri ArcGIS Reality for ArcGIS Pro — GS品質向上（May 2026）
- **URL:** [What's New in Reality Mapping (May 2026)](https://www.esri.com/arcgis-blog/products/arcgis/imagery/whats-new-in-reality-mapping-may-2026)
- **重要度:** ⭐⭐⭐⭐
- **概要:** GIS・都市計画向け3D解析ツールのGSレンダリング品質が向上。薄い構造物（電線・フェンスなど）や植生の表現精度が上がり、インフラ点検や都市デジタルツインへの活用がより現実的になった。

### 11. Veesus — CAD大手「SolidWorks」でGSが見られる
- **URL:** [Veesus Adds SolidWorks GS Support](https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update)
- **重要度:** ⭐⭐⭐⭐
- **概要:** 点群・GS対応ソフトのVeesusがMayアップデートでSolidWorksプラグインを追加。設計者がCADソフトを離れずにGSキャプチャを3D設計図に重ねて確認できるようになった。製造・建設業界のAS-BIM（現状把握→設計照合）ワークフローへの普及を加速。すでにRhino・Revit・SolidWorks・CloudCompareに対応。

### 12. Houdini-gsplat (Plattipus) — VFXパイプラインにGSがUSDで直結
- **URL:** [AOUSD Forum Post](https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921)
- **重要度:** ⭐⭐⭐⭐
- **概要:** PlattipusがHoudini 21 Solaris向けプラグイン「houdini-gsplat」をOSS化。OpenUSD v26.03のGS専用スキーマを使い、PLYファイルをHoudiniのビューポートでリアルタイム確認→シーン全体に複製配置（O(M+N)メモリ）→外部GS Rendererへエクスポートまでをノードベースで実現。VFXスタジオのパイプライン統合が格段に楽になる。

### 13. Geofront × NHM Vienna — 自然史博物館の宝石を3DGSで修復
- **URL:** [Geofront EU](https://www.geofront.eu/)
- **重要度:** ⭐⭐⭐
- **概要:** オーストリア・ウィーン自然史博物館（NHM Vienna）の依頼でGeofront社がマリア・テレジアの宝石花束を70万個スプラットでデジタル復元。物理的に劣化した葉の部分を学芸員がデジタル上で修復・復元する前例のないユースケース。文化財保存にGSが本格的に使われ始めた証左。

### 14. Geo Week 2026 — 測量・AEC業界でGSが主要テーマに
- **URL:** [Gaussian Splatting at Geo Week 2026](https://radiancefields.com/gaussian-splatting-at-geo-week-2026)
- **重要度:** ⭐⭐⭐
- **概要:** 米国測量・地理空間業界の主要イベント「Geo Week 2026」で3DGSセッションが複数開催。「AIとGaussian Splattingの次」「AECとGISへの影響」など実務者向け討論が盛況。測量会社・GIS企業・建設会社が本格採用検討フェーズに移行していることが明確になった。

### 15. 3DVista 2026.0 — GS搭載の仮想ツアーがフルVR対応
- **URL:** [3DVista Update 2026.0](https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/)
- **重要度:** ⭐⭐⭐
- **概要:** 仮想ツアー作成ツール「3DVista VT Pro 2026」がVRモードに全皮膚コンポーネントと学習機能を追加。GS埋め込みのツアーがMetaQuestなどVRヘッドセットで完全なインタラクティブ体験として楽しめるようになった。不動産・観光・教育向け仮想ツアーの品質が大きく向上。

---

## 💬 コミュニティ・SNS話題

### 16. Lars & Felix — 80台カメラ自動化GS撮影スタジオが欧州ツアー中
- **URL:** [How Lars and Felix Built a Portable Studio](https://radiancefields.com/how-lars-and-felix-built-a-portable-3d-gaussian-splatting-studio)
- **概要:** 80台のカメラリグ、専用GPUボックス、完全自動化パイプライン（画像転送→アライメント→学習→切り出し→共有まで2名で運用）を持ち歩き、欧州各地のイベントで参加者がその場でGSポートレートを受け取れる体験を提供。QRコードを渡すだけでスマホに届く仕組み。GSキャプチャの「民主化」を体現した実例として話題。

### 17. Gaussian Splatting Morphing Tool — 2つのGSキャプチャを滑らかに補間
- **URL:** [Gaussian Splatting Morphing Tool](https://radiancefields.com/gaussian-splatting-morphing-tool-to-blend-between-3dgs-captures)
- **概要:** 2つの.plyファイル（GSモデル）を空間的・色的な類似度で1対1に対応付け、位置・色・回転・スケールをすべて補間してモーフアニメーションを生成するツール。CLIバッチ処理とインタラクティブビジュアライザー両対応。昼夜シーン切り替えや人物の姿勢変化アニメーションなどへの応用が可能。

### 18. "Above the Clouds" — ブルジュ・ハリファをGSでブラウザ完結3D体験
- **URL:** [Above the Clouds WebGPU Showcase](https://www.webgpu.com/showcase/burj-khalifa-gaussian-splatting/)
- **概要:** 開発者Adrian Redが約6週間で制作したブラウザ完結型3D体験サイト。ドバイの霧の中にそびえるブルジュ・ハリファをスクロール駆動で探索できる。霧・もや表現は本物のGSデータをリアルタイム描画（three.js）で実現しており、ポリゴンとGSが同一フレームで共存する事例として注目。

### 19. mediastormDev Blender 3DGS/4DGS Viewer Node — BlenderでGSをネイティブプレビュー
- **URL:** [GitHub: Blender-3DGS-4DGS-Viewer-Node](https://github.com/mediastormDev/Blender-3DGS-4DGS-Viewer-Node)
- **概要:** MediastormがASUSの「雲崗石窟」4DGSプロジェクトで開発したBlender用GSビューアーノードをOSS化。.plyファイルをBlenderのGeometry Nodesで読み込み・プレビューでき、カメラモーションの設計や外部GS Rendererへのエクスポート設定が可能。SIGGRAPH 2025 Real-Time Live! Best in Show受賞のワークフロー。

### 20. Snap & Grab — 3DGSをゲーム描画エンジンに採用した商業タイトル登場
- **URL:** [Gaussian Splatting in Snap & Grab 2026](https://www.ingamenews.com/2026/05/gaussian-splatting-in-snap-grab-2026.html)
- **概要:** スティールスゲーム「Snap & Grab」がGSをゲームレンダリングに採用。通常ポリゴンより大幅に低いリソースでフォトリアルな描画を実現。Snap Inc.のエンジニアが開発参加。ゲームへのGS本格採用が広がりつつある先行事例。

### 21. 4DV.ai × OBSBOT — 60台カメラ4DGSホログラムリグをNABで展示
- **URL:** [Step Inside the Video: 4DV.ai and OBSBOT](https://www.cined.com/step-inside-the-video-4dv-ai-and-obsbot-build-a-60-camera-hologram-rig-for-4d-gaussian-splatting/)
- **概要:** NAB 2026でOBSBOT Tail 2 PTZRを60台使った4DGSボリュームキャプチャリグを展示。4DV.aiのソフトは「フレーム間をスプラットが継続して動く」連続表現を採用し、無限スローモーション・非同期カメラ対応・少ないアーティファクトを実現。1本のLANケーブルで60台を給電＋制御できる運用コストの低さも話題。

### 22. Note.com — Apple SHARP × 4DGS実践レポート（日本語）
- **URL:** [3DGS実用化への道④](https://note.com/onemorevision/n/na10d67125a3c)
- **概要:** AppleのSHARP（1枚の画像から高品質3DGSを生成する技術）と4DGS変換ツールを組み合わせた実践検証記事が日本語で公開。「PostshotでFlipbook式4DGS」と「真の連続4DGS」の違いを初心者向けに解説。日本語圏でのGS技術理解・普及に貢献する良質コンテンツ。

---

## 🔧 開発者向けインサイト

### すぐ使えるツール・ライブラリ

| ツール | 用途 | リンク |
|---|---|---|
| TideGS | 1B+ガウシアン / 単一GPU学習 | [arxiv](https://arxiv.org/abs/2605.20150) / [project](https://sponge-lab.github.io/TideGS/) |
| CLM-GS | 低VRAMでの大規模GS学習 | [GitHub](https://github.com/nyu-systems/CLM-GS) |
| houdini-gsplat | Houdini Solaris USD統合 | [AOUSD Forum](https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921) |
| GS Morphing Tool | GS間の補間・モーフアニメーション生成 | [Radiance Fields](https://radiancefields.com/gaussian-splatting-morphing-tool-to-blend-between-3dgs-captures) |
| Blender-3DGS-4DGS-Viewer-Node | BlenderでGS/4DGSプレビュー | [GitHub](https://github.com/mediastormDev/Blender-3DGS-4DGS-Viewer-Node) |
| CLM-GS (ASPLOS 2026) | CPU+GPU混合で102M Gaussians | [GitHub](https://github.com/nyu-systems/CLM-GS) |

### 対応すべき動向

- **Esri GISエコシステム**: Site Scan・ArcGIS Reality両ツールのMayアップデートで商用ハードル大幅低下。測量・建設・インフラ分野での採用が加速
- **SolidWorks対応（Veesus）**: 製造業での本格採用段階へ。CAD連携ワークフロー整備が急務
- **Houdini USD統合**: VFXパイプラインでの標準化が進行中。PlattipusのOSSが先導
- **TideGS & CLM-GS**: 大規模シーン学習の「GPUメモリの壁」が解消されつつある。都市デジタルツイン・ポイントクラウド処理のコスト革命に注目
- **GS→電波応用 (RxGS/OctCGS)**: 通信インフラ設計へのGS応用が本格化。ニッチだが6G時代に重要になるカテゴリ

---

*レポート生成: 2026-05-27 | ソース: arXiv, Radiance Fields, CG Channel, CineD, Esri Blog, WebGPU Showcase, Note.com, GitHub, AOUSD Forum*
