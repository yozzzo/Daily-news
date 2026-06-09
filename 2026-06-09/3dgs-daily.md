# 3DGS & 4D生成 デイリーレポート 📅 2026-06-09

> **本日のサマリー**: 新規 19件（論文 8件 / 業界ニュース 4件 / ツール・コミュニティ 7件）

---

## 🔥 今日の注目トレンド TOP5

1. 🍎 **Apple MapsがGaussian Splatting採用（WWDC 2026）** — iOS 27/macOS 27/visionOS 27で今秋登場。300都市以上をGS技術で3D化。史上最大規模のGS商用展開が現実に
2. 🧮 **CLM (ASPLOS 2026)** — CPUオフロードでGPUメモリ壁を突破。家庭用RTX4090一台で25km²都市の3DGS学習が可能に
3. 🎬 **Houdini 22 がGSリグ＆アニメーション対応を予告** — VFX業界の標準ツールが3DGSを一級市民扱いへ（6/22詳細発表）
4. 🌍 **MapTiler GeoSplats Beta** — 都市スケールGS（10億Splat）をWebGPUでブラウザストリーミング
5. 🔬 **Gaussian Point Splatting (SIGGRAPH 2026)** — ソーティング不要の新レンダリングパラダイム（7/20発表）

---

## 🔬 注目論文

### 1. EvoGS — 進化ツリー型継続階層化GSストリーミング
**重要度: ★★★★★** | `arxiv:2606.07179` | 2026-06-05

**何ができるようになったか**
スマホからハイエンドPCまで、デバイス性能に合わせて自動的に最適な品質でGSをリアルタイムストリーミングできるようになった。

**課題と解決**
従来の3DGSストリーミングは「粗い→細かい」という段階的なレイヤー構造で転送していたため、誤差の蓄積と無駄なGaussianの大量生成（全体の65%以上）が問題だった。EvoGSはウェーブレット変換にインスパイアされた「進化ツリー」構造を導入し、親Gaussianが子Gaussianを連続的に精緻化する仕組みを実現。余剰Gaussianを25%未満に削減し、転送量最大2.4倍・GPU VRAM最大5.5倍の削減を達成した。

- 🔗 https://arxiv.org/abs/2606.07179

---

### 2. Gaussian Point Splatting — ソーティング不要の新レンダリングパラダイム
**重要度: ★★★★★** | SIGGRAPH 2026 | DOI: 10.1145/3811272 | 発表: 2026-07-20

**何ができるようになったか**
3DGSの描画から「ソーティング（Gaussianを奥から手前の順に並び替える処理）」が不要になり、Gaussianが多ければ多いほど効率が上がるという驚きの特性を実現。

**課題と解決**
従来の3DGSレンダリングは毎フレームのソーティング処理がボトルネックとなっていた。GaussianからPixelサイズの不透明な点をサンプリングし、64bitアトミック演算でフレームバッファに直接書き込む「確率的透明度」方式を採用。並列プログラミング原語により計算負荷を均等分散し、Gaussianが増えるほど効率が上がるスケーリングを実現。

- 🔗 論文ページ: https://momentsingraphics.de/Siggraph2026.html
- 💻 GitHub: https://github.com/JorisAR/gaussian-point-splatting

---

### 3. CLM — GPUメモリ壁を破る3DGSのCPUオフロード
**重要度: ★★★★★** | ASPLOS 2026 | NYU | `arxiv:2511.04951`

**何ができるようになったか**
家庭用GPU（RTX4090）一台で、東京23区規模（25km²超）の都市を3DGSで学習・レンダリングできるようになった。

**課題と解決**
都市規模の大シーンを3DGSで学習する際、GPUメモリが致命的なボトルネックとなっていた。CLM（CPU-Offloaded Large-Scale 3DGS）はメモリ消費の大きいGaussianパラメータをCPUに退避し、必要な時だけGPUへロードする方式を採用。RTX4090一台で1億個のGaussian（大都市規模）の学習・レンダリングを実現し、GPU単独比最大6.1倍大きいモデルを扱えるようになった。

- 💻 GitHub: https://github.com/nyu-systems/CLM-GS
- 📰 詳細記事: https://eu.36kr.com/en/p/3607760538895618

---

### 4. HiGS — 階層型リアルタイム3DGSレンダリングアーキテクチャ
**重要度: ★★★★☆** | `arxiv:2606.00352` | 2026-05-29

**何ができるようになったか**
一般向けGPUでも大規模シーンのリアルタイム3DGS描画が可能になった。

**課題と解決**
3DGSが普及するにつれ、大規模シーンでの一般向けGPUによるリアルタイムレンダリングが課題だった。HiGSは空間分割とラスタライゼーションにそれぞれ異なるスケールを持つ「階層型レンダリングアーキテクチャ」を提案し、品質とレンダリング速度を両立した。

- 🔗 https://arxiv.org/abs/2606.00352

---

### 5. SparseStreet — 自動運転向け高効率街路シーン3DGS
**重要度: ★★★☆☆** | `arxiv:2606.03909` | 2026-06-01

**何ができるようになったか**
自動運転シミュレーション用の街路シーン3DGSのデータ量を大幅削減しながら、動的物体（車・歩行者）の高精度描画を維持。

**課題と解決**
動的物体には高精度が必要だが静的背景には冗長性が高いという非対称性を活用。ノードベースの学習可能プルーニング＋背景圧縮の2段階アプローチで、ストレージコストと描画速度の課題を解決。

- 🔗 https://arxiv.org/html/2606.03909v1

---

### 6. LEGS — ラプラシアン強化GSと非線形損失関数
**重要度: ★★★☆☆** | `arxiv:2606.07932` | 2026-06-06

**何ができるようになったか**
3DGSの再構成画質をPSNR最大+1.68dB改善。

**課題と解決**
通常の3DGS学習は1次微分（勾配）情報のみで品質を最適化するが、構造的な精度が不十分だった。LEGSは2次微分（ラプラシアン＝構造エッジ情報）を活用した非線形重み関数を導入し、細部の構造精度を向上。

- 🔗 https://arxiv.org/abs/2606.07932

---

### 7. BEAST3D — 動物行動解析への3DGS応用
**重要度: ★★★☆☆** | `arxiv:2606.02937` | 2026-06-01

**何ができるようになったか**
マルチカメラ映像から動物の3D姿勢・行動を高精度解析できるようになった。神経科学研究への3DGS応用という新分野を開く。

**課題と解決**
動物行動解析は従来2D映像からの推定に限られていた。BEAST3Dは自己教師あり学習で3D視覚表現を獲得するフレームワークを構築し、ラベルなしのマルチビュー映像からリッチな3D情報を抽出可能にした。

- 🔗 https://arxiv.org/abs/2606.02937

---

### 8. AtlasGS — 脳MRI空間解像度の統一化
**重要度: ★★★☆☆** | `arxiv:2606.02961` | 2026-06-01

**何ができるようになったか**
異なるMRI装置・異なる病院から取得した脳画像を同一品質に揃える「空間解像度調和」に3DGSを応用。臨床データの横断活用が促進される。

**課題と解決**
複数施設のMRIデータは装置の差異から解像度が揃わず、AIモデルの汎化性能が低下していた。共有Gaussian幾何スキャフォールドを基に2段階学習することで装置間の差異を吸収。

- 🔗 https://arxiv.org/abs/2606.02961

---

## 📰 業界ニュース

### 9. Apple Maps、iOS 27でGaussian Splatting採用（WWDC 2026）
**重要度: ★★★★★** | 2026-06-09 発表

**何ができるようになったか**
iPhoneのMapsアプリで、映画品質の3D都市モデルをリアルタイム閲覧できるようになる（今秋iOS 27と同時リリース）。300都市以上が対象。Vision Proでの没入型体験も最適化。

**課題と解決**
従来のフォトグラメトリー（3D都市モデルの標準技術）は「木がドロドロに溶ける」「建物がぼやける」という問題があった。3DGS技術により、航空映像＋AIで超精細な3Dビューを実現。史上最大規模のGS商用展開となる可能性大。

> ⚡ *業界インパクト*: Appleの採用は「Gaussian Splattingが普通のユーザーに届く時代」の到来を意味する。glTF KHR_gaussian_splatting標準化の最終承認（Q2 2026予定）とも重なり、業界標準化に強い追い風。

- 🔗 TechRadar: https://www.techradar.com/computing/software/apple-maps-has-a-huge-ios-27-upgrade-on-the-way-for-flyover-that-will-help-you-see-cities-around-the-world-like-never-before-and-users-think-its-down-to-gaussian-splatting-the-next-big-3d-photography-craze
- 🔗 Radiance Fields: https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade
- 🔗 Engadget: https://www.engadget.com/2189698/everything-announced-at-apples-wwdc-2026-keynote/

---

### 10. Houdini 22 — 3DGSのリグ＆アニメーション対応を予告
**重要度: ★★★★☆** | 2026-06 | SideFX / CG Channel

**何ができるようになったか**
VFX業界の標準ソフトHoudiniで、リアルな3DGSスキャン映像にリグを設定してアニメーションを加えることが可能になる予定（6月22日基調講演で詳細発表）。

**課題と解決**
3DGSはこれまで「静止した場面のスキャン」に強く、動かすことが困難だった。Houdini 22のネイティブ対応により、既存のVFX・CG制作ワークフローにGSを自然に組み込める環境が整う。Copernicus（2D/3D画像処理）・キャラアニメ・シミュレーション・USDワールドビルディングとの統合も強化予定。

- 🔗 https://www.cgchannel.com/2026/06/sneak-peek-houdini-22/

---

### 11. MapTiler GeoSplats Beta — 都市スケールGSのWebGPUストリーミング開始
**重要度: ★★★★☆** | 2026-06 | MapTiler

**何ができるようになったか**
地図上でドローン・スキャナーで取得した建物や都市全体の3DGSをGoogleマップのように操作しながら閲覧できる。10億Splat規模のシーンをブラウザでリアルタイム表示。

**課題と解決**
都市スケールの3DGSはデータ量が巨大でブラウザ配信が困難だった。衛星地図と同様のタイル分割方式でGSをストリーミング、WebGPUでのリアルタイムレンダリングを実現。ドローン・手持ちスキャナー・モバイルマッピングシステムのデータから直接作成・配信できる。

- 🔗 https://www.maptiler.com/geosplats/
- 🔗 デモ: https://labs.maptiler.com/geosplats/

---

### 12. CVPR 2026 Denver — FastGSがHighlight賞受賞・コード公開ラッシュ
**重要度: ★★★☆☆** | 2026-06-03〜08 | Denver, CO

**概要**
採択4,090本（前年比+42%）の中、3DGS関連論文が多数。「FastGS（100秒で3DGS学習）」がCVPR 2026 Highlight賞＋Compute Gold Star受賞。CVPR 2026 Open Accessでコードが一斉公開中。

- 🔗 CVPR 2026 Highlights: https://cvpr.thecvf.com/virtual/2026/events/Highlights2026
- 🔗 FastGS (GitHub): https://github.com/fastgs/FastGS
- 🔗 Open Access: https://openaccess.thecvf.com/content/CVPR2026/html/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.html

---

## 🛠 コミュニティ・ツール

### 13. SuperSplat — WebGPU計算シェーダー＋ストリームLOD対応
**重要度: ★★★★☆** | PlayCanvas | 2026-06

**何ができるようになったか**
ブラウザ上で1000万Gaussian以上の超大規模シーンをLODストリーミングで高速閲覧。スマホでも快適に動作。

**変更内容**: ソーティング処理をCPUワーカーからGPU計算シェーダーへ完全移行。新「Streamed SOG」フォーマットを導入し、デバイス性能に合わせた自動品質調整を実現。

- 🔗 https://blog.playcanvas.com/new-in-supersplat-webgpu-and-streaming-bring-huge-performance-wins/
- 🌐 https://superspl.at/

---

### 14. VkSplatting 2026.2 — Phong廃止・GGX PBRマテリアル＋パストレーシング
**重要度: ★★★☆☆** | NVIDIA | 2026-06

**変更内容**: 旧来のPhong照明→GGXベースPBR（物理ベースレンダリング）へ置換。IBL環境マップ・自動露出・パストレーシング（MIS付き）・GLBメッシュ合成を追加。3DGSシーンに映画品質の物理照明を適用できる。

- 💻 https://github.com/nvpro-samples/vk_gaussian_splatting

---

### 15. KIRI Engine 3DGS Render 5.0 for Blender — Blender 5.1完全対応
**重要度: ★★★☆☆** | KIRI Engine | 2026-06

**変更内容**: Blender 5.1完全対応（旧バージョン非対応）、100以上のバグ修正。Edit/Renderの2モード、SH属性除去機能（ファイルサイズ削減）、UV編集モディファイアー追加。無料公開継続。

- 🔗 https://radiancefields.com/kiri-engine-ships-3dgs-render-5.0-for-blender
- 💻 https://github.com/Kiri-Innovation/3dgs-render-blender-addon

---

### 16. SplatKing 1.0.2 — iPhoneでLiDARデータをCOLMAP直接エクスポート
**重要度: ★★★☆☆** | Radiance Fields | 2026-06

**変更内容**: デバイス上でLiDARデータをCOLMAP形式で直接エクスポート可能に。デュアルレンズ（広角＋超広角）同時撮影、4K/30fps HEVC、手動ISO・シャッター・ホワイトバランス制御を搭載。現場でプロ品質の撮影セットアップが完結。

- 🔗 https://radiancefields.com/radiancefields.com-announces-gaussian-splatking-for-mobile-capture
- 📱 App Store: https://apps.apple.com/us/app/gaussian-splatking/id6759175085

---

### 17. StorySplat 2.4 — プロンプト仮想ステージング＆LCC2ネイティブ対応
**重要度: ★★★☆☆** | StorySplat | 2026-06

**変更内容**: テキストプロンプト入力で部屋のレイアウト変更・家具配置を行う「仮想ステージング」機能と、XGRIDS独自フォーマット「LCC2」のネイティブインポートを追加。不動産・建築分野での実用性が大幅向上。

- 🔗 https://docs.storysplat.com/

---

### 18. Facepunch — s&box向け公式Gaussian Splatライブラリ公開
**重要度: ★★★☆☆** | Facepunch（Garry's Mod制作元） | 2026-06

**何ができるようになったか**
ゲームエンジン「s&box」内でリアルな3DGSスキャン素材を「歩ける・衝突できる」3Dオブジェクトとして使用可能に。

**概要**: May 2026ハックウィーク産の公式ライブラリ。PLY/SOGファイル読み込み、シーン照明受け（シャドウ対応）のリアルタイムレンダリング、衝突メッシュ自動生成を実装。ゲーム開発でのGS活用の新事例。

- 🔗 https://radiancefields.com/facepunch-ships-gaussian-splat-library-for-s-box
- 🌐 https://sbox.game/

---

### 19. PlayCanvas Engine 2.13 — WebGSplat描画の精度・制御性向上
**重要度: ★★☆☆☆** | PlayCanvas | 2026-06

**変更内容**: ColorRampレンダリングモード（深度・密度を色で可視化）追加、カメラ移動時の球面調和関数（Spherical Harmonics）再評価、統合GSplat用シェーダーパイプラインの簡略化。Web上でのGS描画がより細かく制御可能に。

- 🔗 https://radiancefields.com/playcanvas-engine-2-13-expands-unified-gsplat-performance-and-customization

---

## 💡 開発者向けインサイト

### すぐ試せるもの

| ツール | 用途 | リンク |
|--------|------|--------|
| SuperSplat WebGPU版 | 大規模GS（1000万Gaussian超）のブラウザLODストリーミング | https://superspl.at/ |
| Gaussian Point Splatting | ソーティング不要の新レンダラー | https://github.com/JorisAR/gaussian-point-splatting |
| CLM-GS | 単一GPUでの大規模（都市スケール）3DGS学習 | https://github.com/nyu-systems/CLM-GS |
| KIRI Engine 3DGS Render 5.0 | Blender 5.1向け必須アップデート | https://github.com/Kiri-Innovation/3dgs-render-blender-addon |
| MapTiler GeoSplats Beta | GIS×3DGS都市スケールWebGPU配信 | https://www.maptiler.com/geosplats/ |

### 中期で対応すべき動向

1. **Apple Maps GS採用による標準化圧力**: AppleのiOS 27採用はglTF KHR_gaussian_splatting拡張の最終承認（Q2 2026予定）と時期が重なる。独自フォーマット依存は早めに解消し、glTF/USDベースの相互運用性対応を進めるべきタイミング。

2. **WebGPU時代の本格到来**: SuperSplat・PlayCanvas・MapTilerがWebGPUへ本格移行。ブラウザベースGSアプリはWebGLではなくWebGPUを主ターゲットにするタイミング。

3. **Houdini 22 GS対応（6/22詳細発表）**: VFX・映像制作パイプラインを持つチームは要チェック。GSリグ・アニメーションがHoudini標準サポートになれば、既存CGワークフローへのGS統合ハードルが一気に下がる。

4. **都市スケール3DGSの実用化フェーズ入り**: CLMとMapTiler GeoSplatsにより「都市スケールGS」が現実的に。建設・インフラ・自動運転分野では、従来LiDARベースのデジタルツイン構築をGSに置き換える検討フェーズに入る時期。

---

*レポート生成日時: 2026-06-09*  
*収集ソース: arXiv, Radiance Fields, CG Channel, TechRadar, Engadget, 9to5Mac, GitHub, MapTiler, PlayCanvas Blog, Radiance Fields Substack*
