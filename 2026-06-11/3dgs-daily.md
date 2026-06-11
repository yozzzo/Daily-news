# 3DGS & 4D生成 デイリーレポート — 2026-06-11

> 対象期間: 2026-06-01〜2026-06-11 ／ 新規項目: 11件
> 過去掲載済みリスト（past_3dgs.json）と照合済み・重複除外済み

---

## 🔥 今日のハイライト（注目トレンド TOP 5）

1. **Apple、WWDC 2026でApple MapsのFlyoverをGaussian Splattingに移行すると発表** — iOS 27 / macOS 27 / visionOS 27 で秋に展開、史上最大規模の3DGS商用展開へ
2. **visionOS 27 RealityKitにネイティブGS API追加** — Apple Vision Pro向けアプリに3DGSを直接組み込む開発者APIが登場
3. **ComfyUI v0.23 + TripoSplat** — 画像1枚から3DGSを生成するノードが公式サポートに。AI画像生成ツールと3Dが本格融合
4. **EvoGS** — 3DGSのストリーミング配信効率を2.4〜5.5倍改善する新手法。大規模シーンの配信コスト問題に突破口
5. **SIGGRAPH 2026採択「Gaussian Point Splatting」** — 確率的サンプリングで超大規模シーンも高速レンダリング可能に

---

## 🗞️ 業界ニュース

### 1. Apple Maps Flyover、iOS 27でGaussian Splattingに移行
**重要度: ★★★★★（業界史上最大のGS商用展開）**

- **何ができるようになったか**: AppleのマップアプリFlyover機能（350都市以上を鳥瞰3D表示）が、秋リリースのiOS 27 / macOS 27 / visionOS 27で3DGSベースに刷新される。樹木の形・ガラスへの光の映り込みまで再現した超リアルな都市3D表示が可能になる。
- **これまでの課題と解決**: 従来のフォトグラメトリー（写真から3Dモデルを作る手法）では建物がぼやけ、木がぐにゃっとしたアーティファクトが生じていた。3DGSに移行することで、空撮映像とAIが組み合わさり精密な3Dシーンを高速に生成できる。Appleは「今まで見たことのない世界の都市の様子が見られる」と表現。
- **注目ポイント**: Appleはステージで「Gaussian Splatting」とは一言も言わなかったが、技術の内容はまさにそれ。GoogleマップがNeRF系技術でImmersive Viewを展開する中、AppleがGSで先手を打った形。史上最大規模のGS商用展開とも言える。
- **ソース**: [TechRadar](https://www.techradar.com/computing/software/apple-maps-has-a-huge-ios-27-upgrade-on-the-way-for-flyover-that-will-help-you-see-cities-around-the-world-like-never-before-and-users-think-its-down-to-gaussian-splatting-the-next-big-3d-photography-craze) / [Radiance Fields](https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade)

---

### 2. visionOS 27 RealityKitにGaussian Splatting APIが追加
**重要度: ★★★★☆（開発者向け・Apple Vison Pro展開加速）**

- **何ができるようになったか**: Apple Vision Pro向け開発フレームワーク「RealityKit」にネイティブGS描画APIが追加。これにより、開発者がアプリ・ゲーム内に3DGSシーンをそのまま組み込めるようになった。フィジカル空間照明、布シミュレーション、残響メッシュも同時追加。
- **これまでの課題と解決**: 従来はサードパーティツールを使って間接的にGSをVision Proで表示するしかなかった。公式APIにより高パフォーマンス・高品質なGSが標準で使える環境が整った。
- **注目ポイント**: 開発者ドキュメントも公開済み。WWDC26セッション「Explore advances in RealityKit」で詳細解説。
- **ソース**: [Apple Developer Docs](https://developer.apple.com/documentation/visionos/gaussian-splats-on-visionos) / [WWDC26セッション](https://developer.apple.com/videos/play/wwdc2026/279/)

---

### 3. 3DGS Render 5.0 for Blender — スキャンしたキャラをBlender内でアニメ可能に
**重要度: ★★★★☆（CG制作者に即使えるツール更新）**

- **何ができるようになったか**: KIRI Engineが開発するBlender向けGS描画プラグイン「3DGS Render」が v5.0にメジャーアップデート。リアル人物スキャン（GS）にリグを使ったアニメーションを適用できるようになった。Mixamoのアニメーションをスキャンキャラクターに転送してPLYシーケンスとして書き出し、SuperSplatなど他ツールで再生可能。4DGS出力にも対応。
- **これまでの課題と解決**: これまで3DGSは「静止したシーン」しか表現できず、アニメーション制作への組み込みが難しかった。プロキシメッシュ経由でアニメーション情報をGSに焼き込む手法で、ハードルが大きく下がった。
- **注意**: 現時点では実験的機能でパフォーマンスは未最適化。Blender 5.1対応。無料配布。
- **ソース**: [CG Channel](https://www.cgchannel.com/2026/06/3dgs-render-5-0-lets-you-animate-gaussian-splats-inside-blender/) / [Digital Production](https://digitalproduction.com/2026/06/11/lets-animate-splats-in-3dgs-render/)

---

### 4. ComfyUI v0.23 + TripoSplat — 画像1枚から3DGSをワンクリック生成
**重要度: ★★★★☆（AI生成ワークフローと3Dの本格融合）**

- **何ができるようになったか**: AI画像生成ツール「ComfyUI」のv0.23（2026年6月1日リリース）で、Tripo AI開発のオープンソースモデル「TripoSplat」がデイ0サポートされた。1枚の画像をComfyUIのノードにつなぐだけで、自動的に3DGSアセットが出力される。キャラクター・小道具・スタイライズドオブジェクトに特に強い。MITライセンスでオープンソース（ローカル実行可能）。
- **これまでの課題と解決**: 3DGS生成には専用ツールや複数の手順が必要だった。ComfyUIとのネイティブ統合で、画像生成→3D変換が同一ワークフロー内で完結できるようになった。
- **技術補足**: DINOv3 + Flux2 VAEで画像を符号化し、フローマッチングデノイザー＋オクツリーデコーダーで3DGSを出力する仕組み。
- **ソース**: [ComfyUI Blog](https://blog.comfy.org/p/bringing-native-support-for-3d-gaussian) / [Radiance Fields](https://radiancefields.com/comfyui-adds-native-3d-gaussian-splat-generation-with-triposplat)

---

## 📄 注目論文

### 5. EvoGS — ストリーミング3DGSの冗長データを1/3以下に削減
**重要度: ★★★★★ | 分野: 大規模配信・ストリーミング**

- **arXiv**: [2606.07179](https://arxiv.org/abs/2606.07179) ／ 提出日: 2026年6月5日
- **何ができるようになったか**: 3DGSを「進化ツリー（Evolution Tree）」と呼ぶ階層構造で整理し、親から子へのウェーブレット的な細部精細化によって連続的にLoD（画質レベル）を変えながら配信できる手法。冗長なSplatを65%超から25%未満に削減、転送データ量を最大2.4倍・GPU VRAMを最大5.5倍削減。
- **これまでの課題と解決**: これまで3DGSを大規模シーンでストリーミングすると膨大なデータ転送とメモリ消費が問題だった。EvoGSはスマホ〜高性能PCまで帯域に応じて品質を段階的に変えながら滑らかに表示できる仕組みで、実用的なWebでの3DGS配信に道が開けた。

---

### 6. HiGS — 大きいタイル×小さいタイルの二段構えで3DGSの並列描画を最適化
**重要度: ★★★★☆ | 分野: リアルタイムレンダリング高速化**

- **arXiv**: [2606.00352](https://arxiv.org/abs/2606.00352) ／ 提出日: 2026年5月29日
- **何ができるようになったか**: 3DGSのレンダリングで、粗いマクロタイル（空間の仕切り）と細かいレンダータイルを分離した「階層タイル型」アーキテクチャを採用。密度が高い領域を多くのGPUスレッドに分散させることで、従来の1サイズタイルより並列効率が大幅向上。
- **これまでの課題と解決**: 従来は空間分割とピクセル描画が同じタイルサイズで縛られており、密なシーンほど特定のタイルに処理が集中してGPUが余ってしまっていた。HiGSで処理の偏りを解消し、リアルタイム性能を底上げ。
- **著者**: Dawid Pająk, Martin Bisson, Rodolfo Lima

---

### 7. BEAST3D — たった4視点の映像から動物の行動を3D解析
**重要度: ★★★☆☆ | 分野: 生物・行動科学応用**

- **arXiv**: [2606.02937](https://arxiv.org/abs/2606.02937) ／ 提出日: 2026年6月1日
- **何ができるようになったか**: ラボで複数カメラ（最低4台）で撮影した動物映像から、ラベルなし（自己教師あり）で3D姿勢・動作・背景を分離して学習できるフレームワーク「BEAST3D」。GS描画で自己監督的に3D表現を学ぶため、手動アノテーションが不要。
- **これまでの課題と解決**: 動物の3D行動解析は手動ラベル付けが膨大で、汎用3Dモデルはラボ映像の少数視点設定に対応できなかった。BEAST3Dはカメラパラメータを直接使い4視点という少数映像で3D構造を再構成できる。神経科学・行動実験への応用が期待される。

---

### 8. AtlasGS — 脳MRI画像の解像度を複数撮影装置間で自動統一
**重要度: ★★★☆☆ | 分野: 医療画像・マルチサイト研究**

- **arXiv**: [2606.02961](https://arxiv.org/abs/2606.02961) ／ 提出日: 2026年6月1日
- **何ができるようになったか**: 病院間で異なるMRI装置から得た脳スキャン画像の解像度を、GSベースの共有幾何学スキャフォールドを使って統一する手法「AtlasGS」。UK Biobank, GBM（脳腫瘍）, ABCDデータセットで最先端の再構成精度を達成。
- **これまでの課題と解決**: 多施設研究ではMRI解像度がバラバラで比較研究が困難だった。GS由来の幾何学情報を複数モダリティで共有することで、任意視点から一貫した高解像度画像を生成できる。
- **応用**: グリオブラストーマ（脳腫瘍）・FLAIR・DWIなど複数撮影モダリティに対応。

---

### 9. SparseStreet — 自動運転シミュレーション向けにGSのストレージを大幅削減
**重要度: ★★★★☆ | 分野: 自動運転・ストレージ効率化**

- **arXiv**: [2606.03909](https://arxiv.org/abs/2606.03909)
- **何ができるようになったか**: 自動運転の走行シーンを3DGSで再構成する際、冗長なGaussianを刈り込む「スパース化」により、リアルタイム再生に必要なストレージを大幅削減しながら高品質なシーン再構成を維持。
- **これまでの課題と解決**: 自動運転シミュレーション向けGSは映像品質は高かったが、保存データ量が巨大すぎてエッジデバイスやオンボード使用に向かなかった。SparseStreetで実用的なストレージサイズに圧縮できる。

---

### 10. LEGS — 二階微分で画像の「輪郭・エッジ」をGS最適化に取り込み
**重要度: ★★★☆☆ | 分野: GS最適化・テクスチャ品質**

- **arXiv**: [2606.07932](https://arxiv.org/abs/2606.07932) ／ 提出日: 2026年6月6日（中国科学院長春光機所）
- **何ができるようになったか**: 通常の損失関数（ピクセルの色差）に加え、画像の「エッジや輪郭の構造情報」を示す「ラプラシアン」という二次微分情報を非線形ウェイトで損失に組み込む手法「LEGS」。細かいテクスチャの再現精度が向上。
- **これまでの課題と解決**: 標準の3DGSは平坦な領域も精細な領域も同じように最適化するため、エッジの再現が甘くなりがちだった。LEGSは「エッジが多い場所をより重視して学習する」仕組みで、シャープな境界線が復元できるようになった。

---

### 11. Gaussian Point Splatting — SIGGRAPH 2026採択：確率的サンプリングで超大規模シーンを高速描画
**重要度: ★★★★☆ | 分野: 大規模シーンレンダリング**

- **発表**: SIGGRAPH 2026（2026年7月20日登壇予定）
- **何ができるようになったか**: GaussianをピクセルサイズのPointとして確率的にサンプリングし、64ビットアトミック演算でフレームバッファに合成する新レンダリング手法「Gaussian Point Splatting」。Gaussianの数に対してスケールしやすく、超大規模シーンでも高速描画が可能。
- **これまでの課題と解決**: 従来の3DGSレンダリングはGaussianの数が増えるほどタイルソートのコストが上昇し、巨大シーンで処理が重くなる問題があった。確率的サンプリング＋アトミック合成で、大量のGaussianを持つシーンでもGPU効率を保てる。
- **ソース**: [SIGGRAPH 2026発表ページ](https://momentsingraphics.de/Siggraph2026.html)

---

## 💬 コミュニティ・SNS話題

### Apple Maps発表でSNS大盛況
**分野: コミュニティ反響**

- WWDC 2026のキーノート後、X（旧Twitter）では「Appleが3DGSをマップに採用した」という投稿が拡散。Radiance Fields公式アカウントも即座にシェア。
- Redditでは「GoogleマップのImmersive ViewはNeRF系だったのにAppleがGSで先手を打った」という論考が活発に展開。iOS 27ベータでFlyoverの一部都市が低品質に戻る問題も話題に（移行作業中のため）。
- 「Appleが3DGSを使う=技術のメインストリーム入りを証明」という声が多数。
- **ソース**: [X/RadianceFields](https://x.com/RadianceFields/status/2064043440350888050) / [Digg](https://digg.com/tech/gizhzvon)

---

## 🛠️ 開発者向けインサイト

### すぐ使えるツール・対応すべき動向

| # | トピック | 優先度 | アクション |
|---|---------|--------|-----------|
| 1 | **Apple RealityKit GS API (visionOS 27 Beta)** | 🔴 高 | Vision Pro向けコンテンツ開発者はWWDC26セッション確認・ベータ実装開始を推奨 |
| 2 | **ComfyUI v0.23 + TripoSplat (MIT/無料)** | 🔴 高 | 画像→3DGS変換ワークフローに即組み込み可。ローカル実行可 |
| 3 | **3DGS Render 5.0 for Blender (無料)** | 🟡 中 | スキャンキャラのアニメーション制作に試験導入可 |
| 4 | **EvoGSの手法** | 🟡 中 | 大規模3DGSシーンをWeb配信したいチームは論文実装を追うべき |
| 5 | **Apple Maps GS展開 × Google対応動向** | 🟡 中 | 地図・都市デジタルツイン関連事業者は競合の動向を継続ウォッチ |

---

## 📊 今週のソマリー

| カテゴリ | 件数 |
|---------|------|
| 論文（新規） | 7件 |
| 業界ニュース | 4件 |
| コミュニティ・SNS | 1件 |
| **合計** | **11件** |

---

*本レポートはarXiv、Radiance Fields、CG Channel、TechRadar、Apple Developer、Engadget等の公開情報をもとに作成。past_3dgs.jsonにより過去紹介済み項目は除外済み。*
