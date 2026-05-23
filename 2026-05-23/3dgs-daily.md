# 🧬 3DGS & 4D生成 デイリーレポート｜2026-05-23

**収集期間**: 2026-05-16〜2026-05-23  
**本日の新着**: 論文6件 / ニュース4件 / コミュニティ・ツール3件（計13件）  
**重複排除**: `past_3dgs.json` との照合済み  

---

## 🔥 今日のハイライト

| # | トレンド | ポイント |
|---|---------|----------|
| 1 | TideGS: 10億プリミティブを1GPUで | スケールの壁を突破、都市規模3DGSへの道 |
| 2 | CVPR 2026直前コードラッシュ | PhysGM・GenWildSplat等が続々公開（6/3〜7 Denver） |
| 3 | Samsung Galaxy XR × Google Maps × GS | XRヘッドセットで1,000以上の場所をGS体験 |
| 4 | Esri May 2026大型GS更新 | 建設・測量ワークフローに深く統合 |
| 5 | PhysGM: 写真1枚→物理4D、1秒以内 | CVPR 2026 Highlight |

---

## 📄 注目論文（重要度：高）

### 1. TideGS — 10億超のGaussianを1枚のGPUで学習

- **arXiv**: [2605.20150](https://arxiv.org/abs/2605.20150) | **投稿**: 2026-05-19
- **プロジェクトページ**: https://sponge-lab.github.io/TideGS/

**何ができるようになったか**  
これまでGPUのメモリ容量（通常24GB）に縛られ、1シーンで学習できるGaussianの数は数百万個程度が限界でした。TideGSはSSD→CPU→GPUという3段階のメモリ階層を活用し、「今見えている視点に必要なGaussianだけGPUに読み込む」という仕組みで、24GB GPU 1枚で10億個以上のGaussianを学習可能にしました。

**解決された課題**  
都市全体・工場内全域といった超大規模シーンの3DGS化は、GPU不足でほぼ不可能でした。分散学習（複数GPU）を使わずに解決したことが最大の革新です。品質も従来の単GPU手法より高く、都市スケールのデジタルツインへの道が開けました。

---

### 2. GenWildSplat — 写真2〜6枚（制約なし）から3DGS生成 [CVPR 2026]

- **arXiv**: [2604.28193](https://arxiv.org/abs/2604.28193)
- **GitHub**: https://github.com/Vinayak-VG/GenWildSplat
- **プロジェクトページ**: https://genwildsplat.github.io/

**何ができるようになったか**  
スマホでランダムに撮影した2〜6枚の写真（照明条件も場所もバラバラでOK）から、約3秒で3D空間を生成します。カメラの位置・向きを事前に計算するSfM処理が不要で、通行人など一時的に映り込んだ障害物も自動除去します。

**解決された課題**  
従来の3DGS生成には「整然と撮影した多数枚の写真」や「SfM前処理」が必要でした。GenWildSplatはこれを不要とし、ライティングの変化にも対応。観光地・ECサイト・不動産などで手軽に3DGSを作れる時代が近づいています。

---

### 3. PhysGM — 写真1枚から物理的に正確な4Dアニメーションを1秒以内で生成 [CVPR 2026 Highlight]

- **arXiv**: [2508.13911](https://arxiv.org/abs/2508.13911)
- **GitHub**: https://github.com/Hihixiaolv/PhysGM

**何ができるようになったか**  
写真1枚を入力するだけで、3DGS表現とその物体の「剛性・質量」などの物理パラメータを同時に予測し、物理シミュレーション（MPM法）を自動実行。1秒以内に物理的にリアルな4Dアニメーション（落下・変形・接触）を生成します。

**解決された課題**  
「物体がどう動くか」の予測には従来、膨大なデータと時間のかかるシーン固有の最適化が必要でした。PhysGMはこれをフィードフォワード（1回の推論）で解決し、CVPR 2026 Highlightに選出。ゲーム開発・ロボット訓練・映画VFXへの応用が見込まれます。

---

### 4. SparseSplat — Gaussianを1.5%に削減しながら高画質を維持 [CVPR 2026]

- **arXiv**: [2604.03069](https://arxiv.org/abs/2604.03069)
- **GitHub**: https://github.com/victkk/SparseSplat-page

**何ができるようになったか**  
テクスチャのない平坦な部分には大きなGaussianを、情報が多い複雑な部分には小さなGaussianを密に配置するエントロピー制御により、必要なGaussianの数を従来比1.5%まで削減しながら高品質なレンダリングを実現しました。

**解決された課題**  
従来のフィードフォワード3DGS手法は「どこでもGaussianを均一に配置」していたため冗長でした。SparseSplatは構造を理解して配置を最適化し、データ量・処理速度の大幅な改善を達成。エッジデバイスやリアルタイムアプリへの実用展開が現実的に。

---

### 5. GS Transcoding from Plenoptic Cloud/Mesh — 元画像なしで既存3DモデルをGS変換

- **arXiv**: [2605.21051](https://arxiv.org/abs/2605.21051) | **投稿**: 2026-05-20

**何ができるようになったか**  
撮影元の写真が手元になくても、すでに存在する3Dポイントクラウドやメッシュファイルをそのまま3DGSへ変換できるエンドツーエンドパイプラインを提案。既存の3D資産（文化財・建物・製品モデル等）を再撮影なしにGS化できます。

**解決された課題**  
3DGSの作成には元の多視点写真が必須でした。膨大な既存3D資産（CADデータ・文化財スキャン・点群データ等）をGS化するには再撮影が必要でしたが、このトランスコーディング手法でその障壁が消えます。

---

### 6. SCOUP — 言語理解3DGSのメモリを1/3に削減

- **arXiv**: [2605.13600](https://arxiv.org/abs/2605.13600)

**何ができるようになったか**  
「このソファはどこ？」などの言語クエリに3Dシーンが答える「3D Language GS」において、CLIPの言語特徴をスパースなコードブックで表現し直すことで、最先端の精度を維持しながら学習メモリを最大3分の1に削減しました。

**解決された課題**  
言語理解機能付き3DGSは処理コストが高く、実用化が難しかった。SCOUPはこれを大幅に効率化し、ロボットの環境理解・施設ナビゲーションへの展開が現実的になります。

---

## 📰 業界ニュース

### 7. Samsung Galaxy XR × Google Maps × Gaussian Splatting

- **ソース**: [Radiance Fields](https://radiancefields.com/samsung-galaxy-xr-to-support-gaussian-splatting-through-google-maps)

Samsung Galaxy XRヘッドセットとGoogle Mapsが連携し、GS（Gaussian Splatting）で表現された現実空間をXRデバイス上で没入体験できる機能が発表されました。マンハッタンだけで1,000以上のロケーションがGSで利用可能。Google MapsのImmersive ViewをXRで体験できる形態で、GSが一般消費者向けに本格展開する重要な一歩です。

---

### 8. Esri ArcGIS Reality Studio May 2026 — GS精度向上アップデート

- **ソース**: [Esri Blog](https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026)

測量・建設業界最大手のEsriが、5月アップデートでArcGIS Reality StudioのGS生成精度を大幅向上。電線・手すり・アンテナなどの細い構造物や密な植生の表現が改善され、デジタルツインとしての実用精度が向上しました。クラウドベースのワークフローにも対応。

---

### 9. Esri Site Scan for ArcGIS May 2026 — クラウドGS生成・1万枚対応

- **ソース**: [Esri Blog](https://www.esri.com/arcgis-blog/products/arcgis/imagery/whats-new-in-reality-mapping-may-2026)

ドローン測量プラットフォーム「Site Scan for ArcGIS」の5月更新で、クラウド上でのGS生成が可能になりました。1ミッションあたり最大1万枚の画像に対応（従来比大幅増）。現場でドローン撮影→クラウドでGS化のエンドツーエンドフローが完成。

---

### 10. XGRIDS LCC Cloud — 商用化へ移行（$800/年）

- **ソース**: [XGRIDS](https://xgrids.com/lcc)

XGRIDS社のクラウドベースSLAM + 3DGS処理サービス「LCC Cloud」が無料ベータから商用化へ移行。年間$800で月250分のクラウド処理が利用可能。PortalCamで撮影したデータをクラウドに上げるだけでGSが生成できるプロ向けワークフローが確立されました。

---

## 💬 コミュニティ・SNS話題

### 11. Real Horizons Spatial Studio — AI Reframe・Spatial Props等を大型アップデート

- **ソース**: [Radiance Fields](https://radiancefields.com/spatial-studio-adds-ai-authoring-layer)

不動産向けGSツアープラットフォーム「Spatial Studio」が大型アップデート。テキストプロンプトで家具・照明・マテリアルを変えられる「AI Reframe（仮想ステージング）」、物体単位のGS生成「Spatial Props」、多言語自動翻訳「Auto Translate」、PlayCanvas LODストリーミング等を追加。GSツアーが単なる写真ビューア以上の価値を提供する方向へ大きく進化中。

---

### 12. houdini-gsplat（Plattipus）— Houdini 21 SolarisにUSD v26.03 GS対応プラグイン

- **GitHub**: https://github.com/plattipus/houdini-gsplat
- **ソース**: [Alliance for OpenUSD Forum](https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921)

Plattipusがオープンソース公開したHoudini 21 Solarisプラグイン。OpenUSD v26.03で追加されたGaussian Splatスキーマ（`ParticleField3DGaussianSplat`）に対応し、カスタムHydraデリゲートとLOPノード3種（PLY Import・Gsplat Instancer・Uruk）を提供。HoudiniのLOPネットワーク内でGSをそのまま扱えるVFXパイプラインが整備されました。

---

### 13. Gauss Cannon v1.2.0 — BlenderプラグインがWorld-Space BVH採用で高速化

- **GitHub**: https://github.com/keshmirian/gauss-cannon

BlenderでGSを操作・レンダリングできる「Gauss Cannon」プラグインがv1.2.0にアップデート。従来の「フレームごとにメッシュ別BVHを再構築」する重い処理から、シーン全体を一括管理する「World-Space BVH」に変更。アニメーション付きGSシーンの処理速度が大幅に改善されました。

---

## 🛠 開発者向けインサイト

### CVPR 2026（6月3〜7日、デンバー）直前コード公開ラッシュ

CVPR 2026（コンピュータビジョン分野の最高峰学会）が約2週間後に迫り、採択論文のコード・学習済みモデルが今週集中して公開されています。特に3DGS関連の注目論文:

- **PhysGM**（CVPR 2026 Highlight）: 写真1枚→物理4D生成 → https://github.com/Hihixiaolv/PhysGM
- **GenWildSplat**（CVPR 2026）: スマホ写真からポーズフリー3DGS → https://github.com/Vinayak-VG/GenWildSplat
- **SparseSplat**（CVPR 2026）: 超軽量フィードフォワード3DGS → https://github.com/victkk/SparseSplat-page

全採択リスト: https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

### TideGSで超大規模シーンへの挑戦が現実的に

TideGSにより「GPU 1枚で都市スケールGS学習」が可能になりました。これまでGPUクラスタが必要だった大規模デジタルツイン構築が、低コストで実験できる時代へ。  
→ https://sponge-lab.github.io/TideGS/

---

*収集元: arXiv / Hugging Face Papers / radiancefields.com / esri.com / xgrids.com / forum.aousd.org / GitHub / Reddit r/GaussianSplatting*
