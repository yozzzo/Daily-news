# 3DGS & 4D生成 デイリーレポート｜2026-05-22

**本日のサマリー：** 論文5本・ニュース6件・コミュニティ/ツール2件の合計13件を新規紹介。

---

## 📌 今日の注目トレンド

1. **スケールの壁を突破** — TideGSが10億個のGaussianを24GB GPU 1台で訓練可能にした。従来の限界（1,100万個）の90倍以上。
2. **物理シミュレーション×GS** — Real2Simが自動運転で「衝突シーンも含む多様なシナリオ」をリアルなGSで生成可能に。
3. **映像・放送業界への本格展開** — Foundry Nuke StageがGS対応でLED壁バーチャルプロダクションを強化。
4. **GIS/測量の大手EsriがGS全面対応** — ArcGIS Reality Studioがクラウド化・高品質化を大幅アップデート。
5. **製造業CADにもGS** — SolidWorksでVeesus経由のGS可視化が実現、設計現場にGS浸透。

---

## 📚 注目論文（重要度：高）

### 1. TideGS — 10億個のGaussianを1台のGPUで訓練

- **arXiv:** https://arxiv.org/abs/2605.20150
- **投稿日:** 2026年5月19日
- **分野:** 大規模GS・スケーラビリティ

**何ができるようになったか**

これまで3DGSの訓練は、GPUメモリの制約でGaussianの数が最大約1,100万個程度に限られていた。TideGSはこの壁を打ち破り、**24GBのGPU（RTX 4090など家庭用〜ワークステーション級）1台で10億個以上のGaussianを訓練**できるようにした。

**これまでの課題と解決策**

Gaussianの全パラメータをGPU上に常駐させると、大規模シーンはすぐにメモリを使い果たす。TideGSは「今見えているカメラ視点に必要なGaussianだけをGPUに載せ、残りはSSD/RAMに退避する」という仕組みを導入。都市規模など超大型シーンの超高精度再構成が単一GPUで可能になる。

---

### 2. DSGS（Decoder-Side Gaussian Splatting）— 動画圧縮にGSを組み込む

- **arXiv:** https://arxiv.org/abs/2605.17002
- **投稿日:** 2026年5月16日
- **分野:** 動画圧縮・没入型映像配信

**何ができるようになったか**

没入型動画（VR・360度映像）を圧縮・配信する際、これまでは「深度推定」という重い処理が必要だった。DSGSはこれをGS推論に置き換え、**「アトラス（地図）1枚から全視点の映像を生成」**するアプローチを提案。動画デコーダー側にGS推論を組み込むことで、高品質な没入型映像をより小さいファイルサイズで配信できる可能性を示した。

**これまでの課題と解決策**

360度動画などは視点が多く、深度情報の推定が品質のボトルネックだった。「アトラス1枚で全ビューをカバー」するDSGSは、深度推定を不要にしつつ品質を維持する新アーキテクチャ。

---

### 3. Transcoding 3DGS from Plenoptic Point Cloud or Mesh — 元画像なしにGSモデルを作成

- **arXiv:** https://arxiv.org/abs/2605.21051
- **投稿日:** 2026年5月20日
- **分野:** GS変換・既存3Dアセット活用

**何ができるようになったか**

通常、3DGSモデルを作るには元の多視点写真が必要。しかしこの研究は、**既存の3D点群（plenoptic point cloud）やメッシュデータから直接GSモデルに「変換」（トランスコード）するパイプライン**を提案。元画像がなくても3DGSを作れるため、過去に作られた大量の3Dアセットの再利用が可能になる。

**これまでの課題と解決策**

GSは写真から再構成するのが前提だったため、既存の3Dデータとの互換性がなかった。このトランスコード手法により、過去の3Dスキャンデータ・ゲームアセット・BIMデータなどをGS形式に変換できる道が開けた。

---

### 4. Real2Sim — 物理シミュレーション×4DGS×自動運転

- **arXiv:** https://arxiv.org/abs/2605.13591
- **投稿日:** 2026年5月（中旬）
- **分野:** 自動運転・物理シミュレーション・4DGS

**何ができるようになったか**

**4DGS（時間軸を加えた4次元のGaussian Splatting）と物理シミュレーション技術（MPMソルバー）を組み合わせ**、「衝突事故」「急ブレーキ後の挙動」など現実では収集困難なシーンを物理的にリアルなGSで生成できる。カメラ映像から現実のドライブシーンを再構成し、そこで物理的に正確な事故シミュレーションを行うことが可能。

**これまでの課題と解決策**

自動運転AIの学習には大量の「危険シーン」データが必要だが、実際の事故データは少ない。Real2Simは現実シーンをGSで再構成してから物理エンジンで動かし、インスタンス（車・歩行者）ごとに編集・シミュレーション可能にした。

---

### 5. SCOUP — 3D言語GS、訓練メモリを3分の1に削減

- **arXiv:** https://arxiv.org/abs/2605.13600
- **投稿日:** 2026年5月（中旬）
- **分野:** 言語GS・効率化・オープン語彙3D理解

**何ができるようになったか**

「この棚にコップはある？」のようなテキスト質問に3DGSが答えられる「言語GS」の訓練コストを大幅削減。**LangSplatV2比で訓練メモリを約3分の1**に抑えながら、同等の精度・速度を維持。シーンごとの意味的3D再構成が数時間から数分規模に短縮。

**これまでの課題と解決策**

高次元の言語埋め込みを数百万個のGaussianに紐付けるには膨大なメモリと時間が必要だった。SCOUPは2D画像空間でコードブック（埋め込みの辞書）を学習してから3DGSに紐付けるアプローチで、3D空間での直接学習を省略しメモリを大幅削減した。

---

## 📰 業界ニュース

### 6. Esri ArcGIS Reality Studio May 2026アップデート

- **URL:** https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026
- **分野:** GIS・測量・クラウド

世界最大のGISソフトウェア企業EsriがArcGIS Reality Studioをアップデート。GS出力品質が向上し、特に**細い構造物・植生・高周波テクスチャ**の表現精度が上がった。クラウドワークフロー対応で大規模プロジェクトをクラウドVM上で処理可能になり、品質保証（QA）機能も追加。測量・建設・インフラ管理でのGS実用化が大きく加速する。

---

### 7. Esri Site Scan for ArcGIS May 2026 — クラウドGS生成＋1万枚対応

- **URL:** https://www.esri.com/arcgis-blog/products/arcgis/imagery/whats-new-in-reality-mapping-may-2026
- **分野:** ドローン測量・クラウドGS

Esriのドローンデータプラットフォーム「Site Scan for ArcGIS」がクラウドベースの3DGS生成に対応。**1回のミッションあたりの処理上限が1万枚**に引き上げられた。現場でドローンを飛ばしてアップロードするだけで高品質なGSが得られるワークフローが確立。

---

### 8. 3DVista 2026.0 — GS統合VRが完全機能化（Total VR Mode）

- **URL:** https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/
- **分野:** バーチャルツアー・VR・不動産・観光

バーチャルツアーソフト3DVistaの2026.0アップデートで「**Total VR Mode**」が登場。これまでVRモードは機能が限定的だったが、今回からほぼすべてのUI・インタラクション・Eラーニング機能がVRで動作する。3DGSモデルをVR内でフル活用でき、不動産・観光・教育分野のVRツアー制作が劇的に簡単になる。

---

### 9. Foundry Nuke Stage更新 — LED壁でGS対応・バーチャルプロダクション強化

- **URL:** https://digitalproduction.com/2026/05/13/foundry-expands-nuke-stage-for-led-walls/
- **分野:** 映像制作・バーチャルプロダクション・ICVFX

ハリウッドなどで使われる合成ソフトNukeのバーチャルプロダクション版「Nuke Stage」が更新。**GSシーンをリアルタイムでLED壁（大型LED背景）に映し出しながら撮影**できる。NotchLC動画再生・GS対応・現場メタデータ記録（Vault）・USD対応を一体化。Amazon MGMの映画「The Thomas Crown Affair」でも採用予定。映像制作へのGS本格導入が一歩前進。

---

### 10. XGRIDS LCC Cloud 商用化 — SLAM+GS完全クラウド処理

- **URL:** https://xgrids.com/lcc
- **分野:** クラウドGS処理・SLAM・デジタルツイン

3D再構成専用カメラPortalCamのメーカーXGRIDSが、SLAM（位置推定）＋3DGS再構成をすべてクラウドで完結するサービス「**LCC Cloud**」を商用化。月250分の処理枠で年間800ドル。現場でスキャンしてアップロードするだけで高品質な3DGSが得られるため、専門エンジニア不要で3DGSデジタルツインが作れる。

---

### 11. Veesus × SolidWorks — 製造業CADでGS可視化が実現

- **分野:** 製造業CAD・デジタルツイン・設計レビュー

3D点群・GS可視化ソフトVeesusがSolidWorks（製造業で最も使われるCADソフトの一つ）に対応。**設計者がSolidWorks内で現実の3DGSシーンと設計モデルを並べて確認**できるようになった。工場・建設・製造業でのデジタルツイン活用が一歩前進し、設計→現場検証ワークフローへのGS統合が始まった。

---

## 🌐 コミュニティ・ツール

### 12. houdini-gsplat（Plattipus）— HoudiniでUSD/GS統合プラグインをOSS公開

- **URL:** https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921
- **分野:** Houdini・USD・VFXパイプライン

Plattipusがオープンソースで公開した「**houdini-gsplat**」は、3DコンポジットソフトHoudini 21のSolaris（USD）環境でGaussian Splattingを扱えるプラグイン。OpenUSD v26.03の新スキーマ（ParticleField3DGaussianSplat）に基づき、HydraレンダラーとLOP（Light Operator）ノードでGSをUSDパイプラインに完全統合。VFXスタジオでのGS活用が加速する見込み。

---

### 13. GaussianWorld SceneSplat-49K — 4万9千シーン・261億Gaussian、世界最大GSデータセット公開

- **URL:** https://huggingface.co/datasets/GaussianWorld/scene_splat_49k
- **分野:** データセット・3DGS研究・言語GS

GaussianWorldプロジェクトが、**4万9千シーン・261億個のGaussianを収録した世界最大の3DGSデータセット「SceneSplat-49K」**をHugging Faceで公開。ScanNet++・DL3DV-10K・HoliCityなど複数のソースから室内〜屋外まで多様なシーンをカバー。AI研究者が3DGSを用いた物体認識・言語理解・シーン理解の研究に活用できる。

---

## 💡 開発者向けインサイト（すぐ使えるアクション）

| 優先度 | アクション | 理由 |
|--------|-----------|------|
| ★★★ | **TideGSの実装を確認する** | 大規模シーン対応が必要なプロジェクトで即戦力。論文にSSD/RAM階層化の実装詳細あり |
| ★★★ | **EsriのGS対応を把握する** | ArcGIS Reality Studio + Site Scanのアップデートは、ドローン測量→GS出力ワークフローの主流化を示す。GIS業界クライアントへの提案に必須 |
| ★★ | **houdini-gsplatを検証する** | OpenUSD v26.03準拠でVFXパイプラインへの統合が容易。今後の業界標準ワークフローになりうる |
| ★★ | **Veesus SolidWorks対応を製造業クライアントに紹介** | 製造・設備管理でのGS導入の先駆け。工場・インフラ管理へのGS展開のきっかけになる |
| ★ | **GaussianWorld SceneSplat-49Kを研究用途に活用** | 世界最大のGSデータセット。言語GS・シーン理解の研究に直接使える |

---

*レポート生成日: 2026-05-22*
*データソース: arXiv, radiancefields.com, CG Channel, Digital Production, Esri Blog, 3DVista, XGRIDS, Foundry, OpenUSD Forum, Hugging Face*
