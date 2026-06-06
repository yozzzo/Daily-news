# 3DGS/4DGS デイリーレポート 2026-06-06

## サマリー
本日は新着・更新情報を **21件** 収録。**CVPR 2026（デンバー、6月5〜7日）**が本日開幕しており、GS関連論文80件超のコード公開ラッシュが進行中。SIGGRAPH 2026採択論文の公開、Zillow/Netflixなど大企業のGS本格採用、業界標準化の最終段階と、あらゆる面で3DGS/4DGSの「実用化の波」が到達した1日です。

---

## 今日の注目トレンド TOP5
1. 🏆 **CVPR 2026開幕** — GS関連論文80件超が発表・コード公開ラッシュ（6/5〜7日）
2. ⚡ **MoVieS** — 動画から「1秒以内で4D動的シーン再構成」をCVPR 2026で実証
3. 🚀 **HiGS** — 元の3DGSより15.8倍高速なリアルタイムレンダリング手法をarXivに公開
4. 🎯 **Gaussian Point Splatting（SIGGRAPH 2026）** — 4億2500万Splatsをリアルタイム描画、ソーティング不要の革新手法
5. 🏢 **Zillow/Netflixが本格GS採用** — 大企業への実用普及が決定的段階へ

---

## 1. 注目論文（重要度：高）

### Selfi — 自己改善型3D再構成エンジン（CVPR 2026 オーラル）
- **重要度**: ★★★★★
- **出典**: [arXiv 2512.08930](https://arxiv.org/abs/2512.08930) | [CVPR 2026 Oral（6月5日発表）](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: カメラ設定情報も深度データも何も不要 — 「普通の写真の束」だけから高品質なGaussian Splatting（3D空間）を生成できる技術。VGGT視覚基盤モデルのバックボーンを使い、自己教師あり学習で特徴の3D一貫性を向上させる。CVPR 2026でオーラル（全採択論文の上位数%に相当）に選ばれた注目作。
- **これまでの課題 → 解決策**: 高品質3D再構成にはカメラキャリブレーションや深度センサーが必要だった。Selfiは「生の写真集」だけで高品質3Dシーンを再構成でき、スマホ撮影画像などあらゆる入力に対応する。

---

### MoVieS — 1秒以内で4D動的シーン合成（CVPR 2026）
- **重要度**: ★★★★★
- **出典**: [arXiv 2507.10065](https://arxiv.org/abs/2507.10065) | [GitHub](https://github.com/chenguolin/MoVieS) | [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: 1本の動画から外観・形状・動きを同時に学習し、約0.93秒で「4Dシーン（時間軸付き動的3D空間）」を再構成する手法。動体セグメンテーションやシーンフロー推定もゼロショットで対応。
- **これまでの課題 → 解決策**: 4D（動的3D）再構成には数時間〜数十時間かかっていた。MoVieSは0.93秒でほぼリアルタイムの4D合成を実現し、ロボット・AR/VR・自動運転への即時適用が現実になった。

---

### HiGS — 15.8倍高速化されたリアルタイム3DGS（arXiv 2606.00352）
- **重要度**: ★★★★★
- **出典**: [arXiv 2606.00352](https://arxiv.org/abs/2606.00352)
- **概要**: 3DGSのレンダリングボトルネックを「空間分割」と「ラスタライズ（描画）」で別々のタイルサイズを使う2階層アーキテクチャで解決。元の3DGSと比べて最大**15.8倍**の高速化を達成し、他の全ラスタライザを上回る画質を維持する。商用GPUで大規模シーンをリアルタイム描画できるようになる。
- **これまでの課題 → 解決策**: シーンが密集・複雑になるほどGPUの処理が特定タイルに集中し、描画が遅くなるボトルネックがあった。HiGSは密度の高い領域の処理を多くのGPUコアに均等分散させることで、大規模シーンでも安定した超高速描画を実現した。

---

### Gaussian Point Splatting — SIGGRAPH 2026 採択：4億Splatsをリアルタイムで
- **重要度**: ★★★★★
- **出典**: [プロジェクトページ](https://momentsingraphics.de/Siggraph2026.html) | [GitHub](https://github.com/JorisAR/gaussian-point-splatting)
- **概要**: **4億2500万個**のGaussianをNVIDIA RTX 4070 Ti SUPERでリアルタイム描画できる新手法。従来必須だった「ソーティング（Gaussianを奥から手前に並べ直す処理）」を不要にし、64-bit atomicsを使った確率的サンプリングで各Gaussianから点をサンプリングして描画する。ACM Transactions on Graphics（SIGGRAPH 2026）に採択。
- **これまでの課題 → 解決策**: 超大規模シーン（数億Gaussian）はソーティングの計算コストでリアルタイム描画が不可能だった。Gaussian Point Splattingはソーティングレス・LoD（詳細度切り替え）不要の全く新しい設計で、スケール問題を根本から解決した。HackerNewsでも話題沸騰中。

---

### DSD-GS — 10分学習・700+ FPS の動的GS（CVPR Findings 2026, arXiv 2605.30863）
- **重要度**: ★★★★
- **出典**: [arXiv 2605.30863](https://arxiv.org/html/2605.30863v1) | [GameDev News](https://gamedev.net/news/3653/)
- **概要**: 動的シーン（人が動く・車が走るなど）を「動く部分」と「動かない部分」に分解し、静止部分への不要な計算をスキップする手法。RTX 5090で**700 FPS超**（1352×1014解像度）・**10分で学習完了**・COLMAP（前処理ツール）不要。
- **これまでの課題 → 解決策**: 動的シーンの3DGSは「全Gaussianが時間変化する」前提で計算負荷が高く、学習に数時間・描画も低フレームレートだった。DSD-GSは不要な再計算を排除し、学習速度・描画速度・ストレージを同時に改善した。

---

### GaussianDWM — 自動運転用Gaussian世界モデル（CVPR 2026）
- **重要度**: ★★★★
- **出典**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: 自動運転シミュレーション用に、センサーデータから高忠実度な「3D Gaussian世界モデル」を構築し、未見のシナリオでの合成データ生成に利用する手法。多様な運転シナリオを高品質に生成できる。
- **これまでの課題 → 解決策**: 自動運転テスト用の「リアルな仮想シーン」を大量生成することが難しかった。GaussianDWMはGSベースの世界モデルで、様々な運転シナリオを高速・高精度に生成可能にした。

---

### Diff4Splat — テキスト指定で4D動的シーンを生成（CVPR 2026）
- **重要度**: ★★★★
- **出典**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: テキストプロンプトや参照画像から、制御可能な4Dシーン（時間と空間を持つ動的3D空間）を生成する拡散モデルベースの手法。遅延空間の再構成を使い、時空間一貫性を高品質に保つ。
- **これまでの課題 → 解決策**: 「動く3D空間」をテキスト指定で生成するのは品質・一貫性の両面で困難だった。Diff4Splatは4D生成に直感的なテキスト制御を持ち込み、映像制作・VFX・コンテンツ生成への応用を広げた。

---

### NimbusGS — 雨・霧・雪が混在した悪天候でも高精度3DGS（CVPR 2026, arXiv 2603.27228）
- **重要度**: ★★★
- **出典**: [arXiv 2603.27228](https://arxiv.org/pdf/2603.27228) | [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: 雨・霧（haze）・雪が複合した天候条件でも高品質な3Dシーン再構成を実現する統一フレームワーク。各種天候の光学的ノイズを考慮したGS学習で、PSNR・SSIMともに既存手法を上回る。
- **これまでの課題 → 解決策**: 通常の3DGSは晴天時の映像を前提としており、悪天候下では画質が大幅低下していた。NimbusGSは悪天候に適応した学習を行い、屋外ロボット・自動運転・インフラ監視への実用応用を広げた。

---

### AeroDGS — 空撮映像から物理整合した4D再構成（CVPR 2026）
- **重要度**: ★★★
- **出典**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: ドローン空撮映像から、物理的に一貫した動的4Dシーンを再構成する手法。空撮特有の撮影条件（広角・俯瞰・急な視点変化）に対応した物理整合4D再構成を実現。
- **これまでの課題 → 解決策**: 空撮映像からの4D再構成は物理法則との整合が困難だった。AeroDGSはドローン映像に特化した設計で、インフラ点検・測量・都市モデリングへの応用範囲を広げた。

---

### BEAST3D — 動物行動分析に3DGSを初応用（arXiv 2606.02937）
- **重要度**: ★★★
- **出典**: [arXiv 2606.02937](https://arxiv.org/abs/2606.02937)
- **概要**: 実験室の多視点カメラ映像から、ラベルなしで動物の3D姿勢・行動を自己教師あり学習するフレームワーク。GS（Gaussian Splatting）を使って他視点から見た映像を微分可能レンダリングで再構成し、同時に動物と背景を分離する。カメラ4台という少視点でも高精度。
- **これまでの課題 → 解決策**: 動物行動研究では膨大な手動ラベリング（どの部位がどこにあるかの注釈付け）が必要で研究コストが高かった。BEAST3Dはラベルなしで自動的に3D姿勢・行動を学習でき、神経科学・行動生物学研究の大幅加速が期待される。

---

### AtlasGS — 脳MRI異機種間の解像度統一化にGSを応用（arXiv 2606.02961）
- **重要度**: ★★★
- **出典**: [arXiv 2606.02961](https://arxiv.org/abs/2606.02961)
- **概要**: 異なるMRIスキャナー・施設間で解像度が異なる脳MRI画像を、Gaussian Splatting（共有Gaussian幾何）を使って統一的に比較・解析できるようにする手法。2段階学習でスキャナー間の構造一貫性を確保。
- **これまでの課題 → 解決策**: 異なる病院・機器で撮影したMRI画像は解像度・品質が異なり、大規模研究での比較が困難だった。AtlasGSはGSを「3D空間の共通表現」として使うことで、異機種MRIを統一的に扱える。

---

### SparseStreet — 軽量・リアルタイムの自動運転向け街路GS（arXiv 2606.03909）
- **重要度**: ★★★
- **出典**: [arXiv 2606.03909](https://arxiv.org/html/2606.03909v1)
- **概要**: 自動運転向け街路シーンのGaussian再構成を「ノード認識プルーニング」と「背景圧縮」で大幅軽量化し、リアルタイム描画速度を達成した圧縮フレームワーク。WaymoとnuScenesデータセットで検証。品質を維持したままGaussian数を大幅削減。
- **これまでの課題 → 解決策**: 街路シーンは数十万〜数百万個のGaussianが必要でストレージが巨大化し、車載コンピュータでのリアルタイム処理が困難だった。SparseStreetは実用レベルのリアルタイム描画を実現した。

---

### HRGS — メモリ効率型の超高解像度3DGS（arXiv 2506.14229）
- **重要度**: ★★★
- **出典**: [arXiv 2506.14229](https://arxiv.org/abs/2506.14229)
- **概要**: 超高解像度シーン（大型建物・都市スケール）のGS再構成のメモリスケーラビリティ問題を、「粗→細」の階層的ブロック最適化で解決。低解像度でグローバルGaussianを先に構築し、後からブロック単位で高解像度に詳細化する。
- **これまでの課題 → 解決策**: 超高解像度対応には単一GPUのメモリ（VRAM）に収まらない量のデータが必要でクラッシュが頻発していた。HRGSは並列ブロック分割でメモリを均等配分し、任意サイズの高解像度シーンを安定して再構成できるようにした。

---

### PersistGS — 「物体が隠れても消えない」物理ベース4D GS（CVPR 2026 Workshop）
- **重要度**: ★★★
- **出典**: [CVPR 2026 Workshop on Generative 3D Reconstruction](https://cvpr.thecvf.com/Conferences/2026)
- **概要**: 物体が一時的にフレームアウトしても「消えない」という物理的永続性（Object Permanence）を4D GS（動的Gaussian Splatting）に組み込む手法。微分可能な物理シミュレーションをGSと統合。
- **これまでの課題 → 解決策**: 既存の4D GSは物体が隠れた瞬間にその情報が失われ、再登場時に位置がずれる問題があった。PersistGSは物理的な動き予測を組み込み、遮蔽時も物体の位置を正確に保持し続けられる。

---

## 2. 業界ニュース

### CVPR 2026 デンバー 本日開幕（6月5〜7日）
- **出典**: [CVPR 2026 公式サイト](https://cvpr.thecvf.com/Conferences/2026) | [FastGS Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_FastGS_Training_3D_Gaussian_Splatting_in_100_Seconds_CVPR_2026_paper.html)
- **概要**: コンピュータビジョン最大の国際会議がコロラド州デンバーで開幕（6/5〜7日）。採択論文数は4,090件（前年比42%増）。GS関連論文は80件以上が採択。FastGS（100秒で3DGS学習完了）がHighlight表彰。Selfi（自己改善型3D再構成）がOral発表。
- **なぜ重要か**: GS分野の最新研究が一気に公開されるタイミング。実装・コードが続々公開中で、開発者にとって一大チャンス。

---

### glTF KHR_gaussian_splatting — Q2 2026の業界標準批准が目前
- **出典**: [Khronos 公式アナウンス](https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release) | [UploadVR](https://www.uploadvr.com/khronos-moves-to-integrate-gaussian-splatting-into-gltf-3d-format/)
- **概要**: Khronos GroupによるglTF 2.0のGaussian Splatting拡張（KHR_gaussian_splatting）が、Q2 2026批准の最終段階に。Google・NVIDIA・Apple・Bentley Systems・Niantic・Cesium・Esriが支持。批准後はThree.js・Babylon.js・Unity・UE5等でGSがネイティブに扱えるようになる。
- **なぜ重要か**: 正式標準になれば「GSファイル = 普通の3Dファイル」として扱われ、あらゆるツール・プラットフォームで相互運用可能になる。CGI・CAD・GIS・ゲームエンジン全体に波及する業界的転換点。

---

### Netflix が Gaussian Splatting 専門職を3ポジション採用中
- **出典**: [The Future 3D](https://www.thefuture3d.com/blog/state-of-gaussian-splatting-2026/)
- **概要**: NetflixがロサンゼルスとLos GatosでVideo Coding（Gaussian Splatting）専門のインターンを計3ポジション公募中。映像ストリーミングへのGS統合を本格的に準備しているとみられる。
- **なぜ重要か**: 世界最大の映像配信サービスがGSを「動画符号化の未来」として位置づけているシグナル。GSが動画配信の標準技術に組み込まれる可能性を示す。

---

### Zillow SkyTour で Gaussian Splatting が不動産に本格上陸
- **出典**: [Lidar News](https://lidarnews.com/zillow-3d-tours-with-gaussian-splatting/)
- **概要**: 不動産プラットフォーム最大手のZillowが「SkyTour」機能でGS（Gaussian Splatting）を正式採用。ドローン映像から建物外観を3D化し、ユーザーがブラウザから自由に視点変更・フライスルーできる体験を提供。
- **なぜ重要か**: Zillowは月間1億以上のユニークユーザーを持つ米国最大の不動産サイト。一般消費者がGSを意識せずに体験する初の大規模事例であり、不動産業界全体への波及が予測される。

---

### Splatware — エンドツーエンドGSクラウドプラットフォームが正式ローンチ
- **出典**: [Radiance Fields](https://radiancefields.com/splatware-launches-as-an-end-to-end-gaussian-splatting-platform) | [Splatware 公式](https://splatware.com/)
- **概要**: スマホ・ドローン・DSLRで撮影した写真・動画をアップロードするだけで、GS生成〜編集〜公開〜販売まで全てブラウザ上で完結する「Splatware」が正式公開。Blender・UE・Unity向け連携も提供。内蔵マーケットプレイスで3Dアセットの販売も可能。
- **なぜ重要か**: 「GS制作に専門知識不要」を実現するクラウドプラットフォームが登場。クリエイター・非エンジニアがGSコンテンツを作成・収益化できる新しい市場が開かれた。

---

## 3. コミュニティ・SNS話題

### Hacker News で「Gaussian Point Splatting」が話題沸騰
- **出典**: [Hacker News スレッド](https://news.ycombinator.com/item?id=48396792) | [プロジェクト](https://momentsingraphics.de/Siggraph2026.html)
- **概要**: SIGGRAPH 2026採択論文「Gaussian Point Splatting」が1日前（6/5）にHacker Newsに投稿され、「ソーティング不要の意義」「4億Gaussian超をリアルタイム描画」に驚きの声が集中している。
- **何が話題か**: 技術コミュニティが「3DGSレンダリングのアーキテクチャ転換点」と位置づけて議論。今後のゲームエンジン・リアルタイムレンダリングエンジンの設計に影響する可能性を指摘する声が多い。

### CVPR 2026 — 採択GS論文のコード公開ラッシュ（進行中）
- **出典**: [GitHub Awesome3DGS CVPR.md](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md)
- **概要**: CVPR 2026開幕（6/5〜）に合わせ、採択された80件超のGS論文のコードが続々とGitHubで公開されている。FastGS・MoVieS・DSD-GS・Selfi・GaussianDWMなど高影響力論文の実装が入手可能になった。
- **何が話題か**: 実装コミュニティで「今週が3DGSコード入手の一大タイミング」として認識されており、各リポジトリのGitHubスターが急増中。

---

## 4. 開発者向けインサイト（今すぐ使えること・対応すべき動向）

| 優先度 | アクション | 詳細 |
|:---:|:---|:---|
| 🔴 高 | **CVPR 2026コードを今すぐ入手** | FastGS（100秒学習）・MoVieS（1秒4D合成）・DSD-GS（10分学習・700FPS）などハイパフォーマンス実装が公開中 |
| 🔴 高 | **glTF KHR_gaussian_splatting対応を準備** | Q2批准が目前。Three.js・Babylon.js・Unity/UE5での実装の先行検証を開始するタイミング |
| 🟡 中 | **HiGS/Gaussian Point Splattingを評価** | リアルタイムGSアプリ開発者向け。15.8倍高速化・ソーティング不要の新実装が入手可能 |
| 🟡 中 | **Splatwareを試す** | ノーコード/ローコードでGSコンテンツを作りたい場合のクラウドソリューション。エンタープライズ導入の検討対象に |
| 🟢 低 | **悪天候対応GS（NimbusGS）を把握** | 屋外ロボット・自動運転・インフラ点検など「現実世界でのGS」利用を想定するなら要注目 |

---

## 収録アイテム一覧（past_3dgs.json 更新分）
| No | 名前 | 種別 | 分野 |
|:---:|:---|:---:|:---|
| 1 | Selfi | 論文 | 3DGS再構成・自己教師あり |
| 2 | MoVieS | 論文 | 4DGS・高速合成 |
| 3 | HiGS | 論文 | 3DGS高速化・レンダリング |
| 4 | Gaussian Point Splatting | 論文 | SIGGRAPH・確率的レンダリング |
| 5 | DSD-GS | 論文 | 4DGS・動的静的分解 |
| 6 | GaussianDWM | 論文 | 自動運転・世界モデル |
| 7 | Diff4Splat | 論文 | 4D生成・テキスト制御 |
| 8 | NimbusGS | 論文 | 悪天候3DGS |
| 9 | AeroDGS | 論文 | 空撮4D再構成 |
| 10 | BEAST3D | 論文 | 生命科学・動物行動分析 |
| 11 | AtlasGS | 論文 | 医療・脳MRI |
| 12 | SparseStreet | 論文 | 自動運転・街路GS |
| 13 | HRGS | 論文 | 高解像度・省メモリ |
| 14 | PersistGS | 論文 | 物理4DGS・物体永続性 |
| 15 | CVPR 2026 Denver 開催 | ニュース | カンファレンス |
| 16 | glTF KHR_gaussian_splatting Q2批准直前 | ニュース | 標準化 |
| 17 | Netflix GS採用強化 | ニュース | 大企業採用 |
| 18 | Zillow SkyTour GS正式採用 | ニュース | 不動産・消費者向け |
| 19 | Splatware エンドツーエンドGSプラットフォーム | ニュース | クラウドツール |
| 20 | HackerNews Gaussian Point Splatting 話題 | コミュニティ | SNS |
| 21 | CVPR 2026 GS論文コード公開ラッシュ（本番後） | コミュニティ | カンファレンス |

---
*生成日時: 2026-06-06 | リサーチソース: arXiv, CVPR 2026, SIGGRAPH 2026, Hacker News, Radiance Fields, Khronos, The Future 3D, Lidar News, GameDev News*
