# 3DGS & 4D生成 デイリーレポート — 2026年5月12日（火）

> 収集件数: **11件**（論文3 / 業界ニュース5 / コミュニティ3）  
> 過去レポート掲載済み項目を完全除外した新規のみ

---

## 🔥 今日の注目トレンド TOP5

1. **複数ロボット協調GS-SLAM「MAGS-SLAM」初登場** — 複数台カメラ・ロボットが協力して3D地図を作る世界初のマルチエージェントGSフレームワーク（arxiv 2605.10760）
2. **ソニー「XYN」正式発売** — バーチャルプロダクション（LEDウォール撮影）向けのプロ用GS撮影〜生成〜表示の一体型ソリューション。2026年夏 米国提供開始
3. **映画「スーパーマン」に4DGS初採用（Framestore）** — 商業映画世界初の4DGS採用。192台カメラで俳優をボリュメトリックキャプチャし40ショット以上を制作
4. **World Labs「Spark 2.0」—ブラウザで1億Splats以上をストリーミング** — スマホからVRまで全デバイスのWebブラウザで大規模GS世界をLoD+ストリーミング配信。MIT License
5. **リアル写真でFPSゲーム—ブラウザで動くGS-FPSデモが世界的話題** — 本物の場所をGSスキャンしブラウザで動くFPSに変換。Tom's Hardware・PC Gamer・Hacker Newsで報道

---

## 🔬 注目論文（重要度：高）

### 1. MAGS-SLAM: 複数エージェントが協力して3D地図を作る次世代SLAM

| 項目 | 内容 |
|------|------|
| **arxiv** | [2605.10760](https://arxiv.org/abs/2605.10760) |
| **投稿日** | 2026/05/11 |
| **重要度** | ★★★★★ |
| **分野** | SLAM・Embodied AI・マルチエージェント |

**何ができるようになったか**  
複数台のカメラ・ロボットが「チームを組んで」同時に3DGSベースの地図を作れるようになった。RGBカメラのみで動く世界初のマルチエージェントGSフレームワーク。

**課題と解決**  
従来のGS-SLAMは1台のカメラ専用。広い空間や複雑な環境では1台では時間がかかりすぎる問題があった。MAGS-SLAMは複数エージェントのデータを幾何学的・外観的に一貫した形で統合するアーキテクチャを設計。カメラ追跡精度・画像品質・学習効率で既存手法を上回ることを実証。

**技術キーワード**: RGB専用（深度センサー不要）、マルチエージェント、分散3DGS、Embodied AI

---

### 2. AdpSplit: 学習を9〜22%高速化するドロップイン置換演算子

| 項目 | 内容 |
|------|------|
| **arxiv** | [2605.06876](https://arxiv.org/abs/2605.06876) |
| **投稿日** | 2026/05/07 |
| **重要度** | ★★★★☆ |
| **分野** | 3DGS最適化・高速化 |

**何ができるようになったか**  
既存の3DGS学習コードの「分割処理」を1つ入れ替えるだけで、学習時間を9.2〜22.3%短縮できるようになった。

**課題と解決**  
3DGSでは「Gaussianをどこで増やすか」（Densification）が画質に直結するが、従来は固定ルールで分割。AdpSplitはL1ピクセル誤差の統計から分割数と初期パラメータを自動決定。Scaffold-GS、Mip-Splattingなど複数の主要パイプラインへのドロップイン置換として検証済み。

**技術キーワード**: Adaptive Splitting, Drop-in Replacement, Densification高速化

---

### 3. Flow4DGS-SLAM: 動く物体を光の流れで分離する4D動的SLAM

| 項目 | 内容 |
|------|------|
| **arxiv** | [2604.22339](https://arxiv.org/abs/2604.22339) |
| **投稿日** | 2026/04/24 |
| **重要度** | ★★★★☆ |
| **分野** | 4DGS・動的SLAM |

**何ができるようになったか**  
人や車が動いている「動的な場面」でもカメラの動きと物体の動きを正確に分離しながらリアルタイムで3Dシーンを再構成できるようになった。

**課題と解決**  
動的シーンでのSLAMは「動いているのはカメラか物体か」の区別が難しく精度が落ちる問題があった。Flow4DGS-SLAMはオプティカルフロー（フレーム間の動きのパターン）からカメラの自己運動モデルをフィッティングし、静的・動的Gaussianを分離管理。

**技術キーワード**: Optical Flow, Dynamic SLAM, 4DGS, カテゴリ非依存モーションマスク

---

## 📰 業界ニュース

### 4. Sony XYN™ Spatial Capture — プロ向けGSバーチャルプロダクションが現実に

| 項目 | 内容 |
|------|------|
| **発表日** | 2026/04/15（NAB Show 2026） |
| **提供開始** | 2026年夏（米国向け） |
| **重要度** | ★★★★★ |
| **ソース** | [Radiance Fields](https://radiancefields.com/sony-xyn-launches-spatial-capture-solution-with-gaussian-splatting) / [Sony公式](https://sony.mediaroom.com/2026-04-15-Sony-Electronics-Announces-the-Launch-of-XYNs-Spatial-Capture-Solution-for-Professionals-Generating-High-Quality-3DCG-Assets-from-Real-World-Spaces) |

**何ができるようになったか**  
ソニーがバーチャルプロダクション（映画・ドラマ・CMのLEDウォール撮影）に特化したGS一体型ソリューションを正式発売。スキャン→GS生成→LEDウォール表示まで一気通貫。

**3つのツールで構成**
- **XYN Spatial Scan Navi**: スマートフォンアプリ。SonyαカメラとAR連携して撮影をガイド
- **XYN Spatial Scan（クラウド処理）**: ソニー独自アルゴリズムで高品質GSアセットを生成
- **XYN Spatial Renderer Plugin**: LEDウォール向け専用レンダラー。再照明・被写界深度・色補正対応

**業界への影響**  
ソニーというカメラ最大手がGSを製品として正式に位置づけ。映画制作・バーチャルプロダクションでのGS採用が加速する可能性が高い。

---

### 5. World Labs Spark 2.0 — WebブラウザでGaussian Splats 1億粒超をストリーミング

| 項目 | 内容 |
|------|------|
| **リリース日** | 2026/04/14 |
| **重要度** | ★★★★★ |
| **ソース** | [World Labs Blog](https://www.worldlabs.ai/blog/spark-2.0) / [GitHub](https://github.com/sparkjsdev/spark) |

**何ができるようになったか**  
THREE.jsベースのオープンソースGSレンダラー「Spark」がv2.0に。LoD（距離に応じた詳細度制御）とストリーミングシステムを搭載し、スマホからPC・VRまで全デバイスのブラウザで1億粒超のGS世界をリアルタイム表示可能になった。

**技術ポイント**
- WebGL2対応でブラウザだけで動作（インストール不要）
- MIT License完全無料
- PLY・SPZ・SPLAT・KSPLAT等の主要フォーマット対応
- Hacker NewsでShow HNとしてトレンド入り

---

### 6. Framestore × 映画「スーパーマン」— 4DGSが商業映画に世界初採用

| 項目 | 内容 |
|------|------|
| **記事日** | 2026/02/13 |
| **重要度** | ★★★★★ |
| **ソース** | [befores & afters](https://beforesandafters.com/2026/02/13/framestore-showcases-the-4d-gaussian-splatting-used-for-superman/) / [The Art of VFX](https://www.artofvfx.com/superman-framestore-brings-4d-gaussian-splatting-to-the-big-screen/) |

**何ができるようになったか**  
VFXスタジオFramestoreが映画「スーパーマン」でクリプトン星の親からのホログラムメッセージを4DGSで制作。商業映画で4DGSが採用された世界初事例。

**撮影・制作の詳細**
- Infinite Realities社の球状Deus Capture Stage（192台カメラ）で俳優を24fps・全方向キャプチャ
- 自社GPUクラスターで数日間学習、24fps PLYシーケンスとして出力
- 40ショット以上を4DGSで最終納品
- ポスプロで任意アングルからの再撮影が可能という革命的なワークフロー

**業界への影響**  
「撮影後に仮想カメラを自由に動かせる」映画VFXの新時代。今後の映画・TV制作でのGS標準採用が急加速する可能性。

---

### 7. Wicked Engine — OSSゲームエンジンがGaussian Splatsのネイティブ対応追加

| 項目 | 内容 |
|------|------|
| **発表日** | 2026/03/09 |
| **重要度** | ★★★★☆ |
| **ソース** | [Radiance Fields](https://radiancefields.com/wicked-engine-adds-native-gaussian-splat-rendering) / [GitHub](https://github.com/turanszkij/WickedEngine) |

**何ができるようになったか**  
MIT LicenseのオープンソースゲームエンジンWicked Engineが、PLYファイルをドラッグ&ドロップするだけでGSをエディタ内に読み込み・レンダリングできるようになった。従来のポリゴンメッシュとGSの混合シーンも実現可能。

**意義**: 完全無料のゲームエンジンでのGS対応が実現し、インディーゲーム・研究・プロトタイプ開発での活用障壁が大幅低下。

---

### 8. Atlux λ 2.1 Live — UE5内で仮想3DスキャニングスタジオをGSパイプラインに直結

| 項目 | 内容 |
|------|------|
| **リリース日** | 2026/03/02 |
| **重要度** | ★★★☆☆ |
| **ソース** | [CG Channel](https://www.cgchannel.com/2026/03/unreal-engine-visualization-plugin-atlux-%CE%BB-2-adds-atlux-%CE%BB-live/) / [公式サイト](https://atlux.one/) |

**何ができるようになったか**  
UE5向けプラグインAtlux λが2.1にアップデート。新機能「Atlux λ Live」でUE5シーンをリアルタイムでGS用COLMAPデータに変換するランタイム版が追加。

**ワークフロー**: UE5シーン設計 → Atlux λでカメラ配置・レンダリング → COLMAPデータ → Postshot/LichtFeld StudioでGS生成 → 完成

---

## 💬 コミュニティ・SNS話題

### 9. SuperSplat PWA対応アップデート — PLYファイルをダブルクリックで即起動

| 項目 | 内容 |
|------|------|
| **日付** | 2026/05/12（本日） |
| **重要度** | ★★★★☆ |
| **ソース** | [PlayCanvas Blog](https://blog.playcanvas.com/a-faster-supersplat-with-pwa-support/) / [SuperSplat](https://superspl.at/) |

**何ができるようになったか**  
PlayCanvas製の無料GS編集ツール「SuperSplat」がPWA（Progressive Web App）対応に。PLYファイルを右クリック→「SuperSplatで開く」またはダブルクリック起動が可能に。GPU処理も大幅刷新で数百万Splatsでもスムーズ動作。

---

### 10. ブラウザで動くGS-FPSゲームデモが世界的大バズり

| 項目 | 内容 |
|------|------|
| **日付** | 2026/04/22 |
| **重要度** | ★★★★★ |
| **ソース** | [PlayCanvas Blog](https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/) / [Tom's Hardware](https://www.tomshardware.com/software/programming/developer-creates-a-basic-first-person-shooter-game-using-gaussian-splats-and-you-can-play-it-for-free-in-your-browser) / [Hacker News](https://news.ycombinator.com/item?id=47876071) |

**何ができるようになったか**  
Snap社エンジニア Yakov Sumygin氏が、現実の場所をGSでスキャンし、FPSゲームのステージに変換するデモを公開。物理コライダー・AIナビメッシュ・NPC（ビヘイビアツリー）を完備したゲームがブラウザで無料でプレイ可能。

**なぜ話題に？**  
「スキャンした場所がそのままゲームになる」という体験が強烈で、ゲーム・VFX・不動産・観光業など幅広い業界に刺さった。

---

### 11. The New Yorker誌がGSをジャーナリズムに活用 — ファクトチェックも通過した「生成AIでないGS」

| 項目 | 内容 |
|------|------|
| **重要度** | ★★★☆☆ |
| **ソース** | [Radiance Fields](https://radiancefields.com/gaussian-splatting-at-the-new-yorker) |

**何ができるようになったか**  
米誌The New Yorkerのビジュアル特集エディター Sam Wolson氏が、著名アーティスト Lorna Simpsonの肖像作品をGSSで制作し誌面に掲載。

**課題と解決**  
The New Yorkerは世界最高レベルのファクトチェック基準を持ち、「AI生成メディア」は掲載不可。GaussianSplattingはリアルキャプチャ技術のため「現実の記録」として認められ掲載が実現。ジャーナリズムへのGS本格進出の世界初事例。

---

## 🛠️ 開発者向けインサイト

### 今すぐ試せるツール

| ツール | 用途 | リンク |
|--------|------|--------|
| AdpSplit | 学習9〜22%高速化（ドロップイン置換） | [arxiv](https://arxiv.org/abs/2605.06876) |
| Spark 2.0 | Webで大規模GSストリーミング（MIT） | [GitHub](https://github.com/sparkjsdev/spark) |
| Wicked Engine | OSS ゲームエンジンでGS対応（MIT） | [GitHub](https://github.com/turanszkij/WickedEngine) |
| SuperSplat | ブラウザでPLY編集（PWA対応） | [superspl.at](https://superspl.at/) |

### 今週の注目動向

| テーマ | 動向 | アクション |
|--------|------|----------|
| 🎬 映画VFX | Framestore/Supermanで4DGSが映画標準へ | VFXパイプラインへの4DGS組み込みを検討 |
| 🎮 ゲーム開発 | Wicked Engine + GS FPSデモで実用性証明 | PlayCanvas/Wicked EngineでのGS採用を検討 |
| 📡 Webデプロイ | Spark 2.0で大規模GS場面をWebに配信可能 | WebサービスへのGS統合にSpark 2.0を採用検討 |
| 🤖 ロボット/AI | MAGS-SLAMでマルチロボット協調3Dマッピングが現実に | Embodied AIプロジェクトへの応用を検討 |
| 📷 バーチャルP | Sony XYNでLEDウォール向けGSが製品化 | 映像制作クライアント向けにSony XYNを提案 |

---

*レポート生成日: 2026-05-12*  
*収集ソース: arXiv, Radiance Fields, CG Channel, Tom's Hardware, PC Gamer, Hacker News, befores&afters, The Art of VFX, Sony Press Release, World Labs Blog, PlayCanvas Blog*
