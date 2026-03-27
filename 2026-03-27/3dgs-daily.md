# 3DGS & 4D生成 デイリーレポート｜2026-03-27

> **今日のサマリー**: 論文14件・ニュース8件・コミュニティ9件、合計31件の新規情報を収集。最大のトピックは「**OpenUSD v26.03正式リリースでGaussian Splatsが業界標準フォーマットに組み込まれた**」こと。加えてCVPR 2026採択の感情認識トーキングヘッド論文、1本の動画から動的物体を360度再構成する4DGS360、Apple Silicon Mac向けネイティブアプリRadianceKitなど実用化に近い成果が相次いだ。

---

## 注目論文

### 1. SpectralSplats — 「消えてしまう勾配」問題を周波数領域で解決した追跡フレームワーク
**arXiv:2603.24036** | 2026-03-25 | [論文リンク](https://arxiv.org/abs/2603.24036)

3DGSを使ったビデオ追跡では、カメラのズレが大きいと「勾配が消えてしまい最適化が止まる」という根本的な問題があった。SpectralSplatsはこの問題を、空間ドメインではなく**周波数ドメイン（スペクトル）**で監督することで解決する。画像全体を複素正弦波の特徴量（スペクトルモーメント）で表現することで、ピクセルが全く重なっていない状態でも正しい方向への勾配が得られる。既存の損失関数の「差し替え部品」として使えるため、MLPから疎な制御点まであらゆる変形パラメータに対応できる。

**何が解決されたか**: 大きな位置ズレからでも3DGSの追跡が破綻しなくなった。

---

### 2. FilterGS — 大規模シーンのLoD描画を60%高速化する並列フィルタリング
**arXiv:2603.23891** | 2026-03-25 | [論文リンク](https://arxiv.org/abs/2603.23891)

都市規模の大きなシーンを3DGSで描画する際、「Level-of-Detail（距離に応じて詳細度を変える技術）」のツリー構造を逐一たどる処理が描画時間の60%以上を占めていた。FilterGSは2種類の並列フィルタを組み合わせることで、ツリーをたどらずにGaussianを選択できるようにした。さらに「GTC指標」という新しい冗長性評価指標を導入し、不要なGaussian-タイルペアを削減するシーン適応型の縮小戦略を提案。複数の大規模データセットで最高速度を達成しながら画質も維持した。

**何が解決されたか**: 大規模シーンのリアルタイム描画が大幅に高速化された。

---

### 3. EmoTaG — 感情を認識して話す3Dアバターを数秒の動画から生成（CVPR 2026採択）
**arXiv:2603.21332** | 2026-03-22 | [論文リンク](https://arxiv.org/abs/2603.21332)

音声に合わせて3Dの「しゃべる頭部」を生成する技術は急速に発展しているが、既存の少数ショット手法では感情豊かな表情動作でジオメトリが不安定になったり、音声と感情がずれる問題があった。EmoTaGは「FLAME」という3D顔モデルのパラメータ空間で動作を予測することで幾何学的安定性を確保。さらに「Gated Residual Motion Network（GRMN）」が音声から感情的な韻律を捉えつつ、音声だけでは得られない頭部姿勢や上半顔の動きを補完する。数秒の動画だけで個人に適応でき、CVPR 2026に採択された。

**何が解決されたか**: 少ない動画データで感情表現が豊かで安定した3Dトーキングヘッドが生成可能になった。

---

### 4. 4DGS360 — 1本の動画から動的物体を360度再構成
**arXiv:2603.21618** | 2026-03-23 | [論文リンク](https://arxiv.org/abs/2603.21618) | [プロジェクトページ](https://jaewon040.github.io/4dgs360/)

動いている物体を1本の普通のスマホ動画から360度全方位で3D再構成するのは、「見えていない部分の形状があいまい」という問題から難しかった。4DGS360は「3Dネイティブ初期化」で隠れた部分の幾何学的あいまいさを軽減し、独自の3Dトラッカー「AnchorTAP3D」が2D追跡の確信度の高い点をアンカーとして使うことでドリフトを抑制する。新たに作成した「iPhone360」ベンチマーク（訓練視点と135度離れたカメラで評価）でも最高性能を達成。

**何が解決されたか**: 1本の普通の動画から動く物体の360度4D再構成が可能になった。

---

### 5. Inst4DGS — 複数人が動く動画を「誰が誰か」を保ちながら4D再構成
**arXiv:2603.18402** | 2026-03-19 | [論文リンク](https://arxiv.org/abs/2603.18402)

複数の人物が動くシーンを4DGSで再構成する際、「複数カメラ映像でインスタンス（個人）のラベルが一致しない」問題が未解決だった。Inst4DGSは微分可能なSinkhorn層を使った「ラベル順列潜在変数」で、カメラをまたいだインスタンスの対応付けを学習する。これにより個人の同一性を保ちながら時系列で安定した追跡と分解が可能になった。Panoptic StudioデータセットでインスタンスmIoUが0.63→0.91に大幅改善。

**何が解決されたか**: 複数人物が動くシーンでも誰が誰かを保ちながら4D再構成できるようになった。

---

### 6. Fast and Robust Deformable 3DGS — 変形可能3DGSの高速・堅牢化
**arXiv:2603.20857** | 2026-03-21 | [論文リンク](https://arxiv.org/abs/2603.20857)

動的シーンの3DGSは変形処理が重く、ノイズにも弱い問題があった。本論文は高速かつ堅牢な変形可能3DGSを提案し、リアルタイム動的シーン再構成の実用化に近づけた。

---

### 7. Stochastic Ray Tracing for 3DGS — 確率的レイトレーシングで再構成品質を向上
**arXiv:2603.23637** | 2026-03-25 | [論文リンク](https://arxiv.org/abs/2603.23637)

3DGSの再構成において、従来のラスタライズ方式では光の反射・屈折などの複雑な光学現象を正確に表現できなかった。確率的レイトレーシングを3DGSに組み込むことで、より物理的に正確な光学シミュレーションが可能になった。

---

### 8. Pose-Free Omnidirectional GS — カメラ姿勢なしで360度動画を3D化
**arXiv:2603.23324** | 2026-03-25 | [論文リンク](https://arxiv.org/abs/2603.23324)

360度カメラで撮影した動画から3DGSを構築する際、通常はカメラの位置・向き（ポーズ）の事前推定が必要だった。本手法はポーズ推定なしで360度動画から一貫した深度プライアを使って全方位3DGSを構築できる。VR・メタバースコンテンツ制作の簡略化に直結する。

---

### 9. GTLR-GS — LiDARと画像を組み合わせた高精度シーン再構成
**arXiv:2603.23192** | 2026-03-25 | [論文リンク](https://arxiv.org/abs/2603.23192)

自動運転や屋外スキャンでよく使われるLiDARセンサーのデータを3DGSの正則化に活用し、ジオメトリとテクスチャの両方を考慮した高精度なシーン再構成を実現する。

---

### 10. RefracGS — 水面越しの新視点合成
**arXiv（近日公開）** | 2026-03-24

水面のような屈折面を通した映像から新しい視点を合成するのは、光の歪みが複雑で従来手法では困難だった。RefracGSは3Dガウシアンレイトレーシングを使って屈折水面越しの新視点合成を実現。水中撮影・水族館・海洋調査などへの応用が期待される。

---

### 11. Let it Snow! — 3DGSシーンに動的な天気エフェクトを追加
**arXiv:2504.05296** | 更新2026-03-25 | [論文リンク](https://arxiv.org/abs/2504.05296)

静的な3DGSシーンに雪・雨などの動的な天気エフェクトをリアルタイムで追加できるフレームワーク。物理ベースのスコア蒸留（Physics-Guided Score Distillation）を使い、シーン全体に対してパーティクルベースの編集を行う。映画・ゲーム・VRコンテンツ制作での活用が見込まれる。

---

### 12. GaussianPile — 医療スライス画像から3Dボリューム再構成
**2026-03-24**

CTやMRIのスライス画像（断面画像）から3DGSを使ってボリューム再構成を行う統一フレームワーク。医療画像処理への3DGS応用という新しい分野を開拓する。

---

### 13. EmbodiedSplat — ロボットがリアルタイムで3Dシーンを意味理解
**arXiv（近日公開）** | 2026-03-22

ロボットが動きながらリアルタイムで3DGSを構築し、「テーブルはどこか」「椅子はどれか」といったオープンボキャブラリーの意味理解を同時に行うシステム。Embodied AI（身体を持つAI）の実用化に向けた重要な一歩。

---

### 14. Training-Free Instance-Aware 3D Scene Reconstruction — 学習不要でインスタンス認識3D再構成
**arXiv:2603.21166** | 2026-03-22 | [論文リンク](https://arxiv.org/abs/2603.21166)

少数の未整理RGB画像から、追加学習なしで室内シーンを3D再構成しながら個々のオブジェクトを認識・分離するシステム。事前学習モデルの組み合わせだけで実現しており、導入コストが低い。

---

## 業界ニュース

### 15. Gaussian Splat Studio for Cinema 4D — C4Dにネイティブなスプラットワークフローが登場
**2026-03-25** | [製品ページ](https://alphapixel.net/products/c4d-gaussian-splat-plugin/) | [解説記事](https://radiancefields.com/gaussian-splat-studio-brings-procedural-splat-workflows-to-cinema-4d)

Alpha PixelがCinema 4D向けのGaussian Splatプラグイン「Gaussian Splat Studio」を$59.99でリリース。MoGraphエフェクター・フィールド・フォースベースのコントロールを通じてスプラットをC4Dのプロシージャルワークフローに統合できる。アニメーション・分離・歪み・リライトなどの操作がC4D内で完結するようになった。C4D 2024〜2026、Windows/Mac対応。

**何ができるようになったか**: 映像制作者がCinema 4Dを離れずにGaussian Splatsを編集・アニメーション・書き出しできるようになった。

---

### 16. SplatRenderer — UE5で3D/4DGS両対応の無料オープンソースプラグイン
**2026-03-21** | [解説記事](https://radiancefields.com/splatrenderer-plugin-for-unreal-engine) | [YouTube](https://www.youtube.com/watch?v=eeR5QMQA7co)

Dazai Studio製のSplatRendererプラグインがUnreal Engine 5.5〜5.7に対応。3DGSだけでなく4DGSシーンもUE5内でリアルタイム再生できる。完全無料・オープンソースで、独立開発者によるイノベーションの象徴的な事例として注目を集めている。

**何ができるようになったか**: UE5で4DGS（時間軸を持つ動的3Dシーン）がリアルタイム再生可能になった。

---

### 17. NVIDIA Omniverse NuRec — 3DGSパイプラインが一般提供開始（GA）
**2026-03-26** | [解説記事](https://radiancefields.com/nvidia-omniverse-nurec-reaches-general-availability)

NVIDIAの加速型3DGSパイプライン「NuRec」がIsaac LabおよびIsaac Simでの一般提供（GA）を開始。実世界データを取り込んでインタラクティブなシミュレーション環境を再構成・レンダリングするためのgRPC APIも提供。自動運転・ロボティクスのシミュレーション精度向上に直結する。

**何ができるようになったか**: 自動運転・ロボット開発者がNVIDIA製品として安定的にGS技術を利用できるようになった。

---

### 18. Miris — 高忠実度3Dストリーミングの公開ベータ開始
**2026-03-24** | [解説記事](https://radiancefields.com/miris-launches-public-beta-for-high-fidelity-3d-streaming)

3DGSシーンの高品質ストリーミングサービス「Miris」が公開ベータを開始。大容量のGSデータをリアルタイムでウェブ配信する技術の商用化が本格化している。

---

### 19. Khronos Group — glTF Gaussian Splatting ウェビナーを4月7日開催
**2026-03-25** | [解説記事](https://radiancefields.com/khronos-group-announces-gaussian-splatting-webinar)

3Dフォーマット標準化団体KhronosがglTFへのGaussian Splatting統合に関するウェビナーを2026年4月7日に開催予定。glTFの実世界ワークフローへの応用事例も紹介される。標準化の進捗を把握したい開発者は要チェック。

---

### 20. SP-6M — 世界最大の人間頭部スキャンデータセット（82,000スキャン）
**2026-03-26** | [解説記事](https://3dvf.com/en/a-dataset-built-on-ethics-ten24-unveils-82000-human-scans/)

Studio Ten24（3D Scan Storeの制作元）が「SP-6M」を公開。82,000件の高解像度人間頭部スキャンを収録した世界最大のデータセット。倫理的なデータ収集を重視して構築されており、アバター生成・顔認識・医療応用などへの活用が期待される。

---

### 21. World Labs — Gaussian Splatsで物理世界を理解するAI（VentureBeat報道）
**2026-03-21** | [記事リンク](https://venturebeat.com/technology/three-ways-ai-is-learning-to-understand-the-physical-world)

VentureBeatがAIが物理世界を理解する3つの方法を特集。World LabsがGaussian Splatsを使って生成モデルから完全な3D空間環境を構築するアプローチを紹介。ロボットがGSデータに対してレイキャストを行い、メッシュやコライダーなしで手続き的な歩行を実現する事例も報告された。

---

### 22. OpenUSD v26.03 — CG Channel・80.lv等で業界メディアが一斉報道
**2026-03-25** | [CG Channel記事](https://www.cgchannel.com/2026/03/openusd-26-03-adds-support-for-3d-gaussian-splats/) | [80.lv記事](https://80.lv/articles/aousd-has-announced-openusd-v26-03-with-support-for-3d-gaussian-splats)

OpenUSD v26.03へのGaussian Splats対応が、CG Channel・80.lv・3DVF・Digital Productionなど主要CGメディアで一斉に取り上げられた。PLY形式からUSDへの変換、新リファレンスレンダラー「hdParticleField」、WebAssemblyビルドサポートが注目点。業界全体でGSが「標準ツール」として認知されつつあることを示す。

---

## コミュニティ・SNS

### 23. SuperSplat Walk Mode — ブラウザ内でGSシーンを歩き回れる新機能
**2026-03-25** | [Reddit投稿](https://www.reddit.com/r/GaussianSplatting/comments/1s2pewx/)

PlayCanvas SuperSplatに「Walk Mode」が追加された。ボクセルベースの衝突判定を使い、ブラウザ上でGSシーンを一人称視点で歩き回れるようになった。不動産業界での活用が特に注目されており、「アプリ不要でブラウザからGSの物件内覧ができる」と話題になっている。

---

### 24. RadianceKit — Apple Silicon Mac向けネイティブ3DGSアプリ（無料トライアルあり）
**2026-03-26** | [App Store](https://apps.apple.com/de/app/radiancekit/id6760346035) | [公式サイト](https://www.radiancekit.de/)

写真からGaussian Splatsを作成できるMacアプリ「RadianceKit」が登場。Apple SiliconのMetalで直接動作するため、クラウド不要・Python環境不要・NVIDIA GPU不要。写真をドロップしてトレーニングボタンを押すだけの簡単操作で、PLY・SPZ・GLB・Splatなど多形式での書き出しに対応。3日間の無料トライアルあり。

---

### 25. NanoGS GUI Tool — NanoGSをGUIで操作、ファイルサイズ半減・パフォーマンス2倍
**2026-03-26** | [Reddit投稿](https://www.reddit.com/r/GaussianSplatting/comments/1s3fde8/)

NanoGS（Gaussian Splatsのサイズを削減するツール）をGUIで使えるようにしたツールが公開された。単一ファイルとバッチ処理の両方に対応し、視覚的な影響を最小限に抑えながらスプラットのサイズを約半分に削減できる。コマンドライン不要で使えるため、非エンジニアにも扱いやすい。

---

### 26. 4DGS360 Reddit話題 — 1本の動画から動的物体の360度再構成がコミュニティで話題
**2026-03-25** | [Reddit投稿](https://www.reddit.com/r/GaussianSplatting/comments/1s2pewx/4dgs360_360_gaussian_reconstruction_of_dynamic/)

4DGS360論文のプロジェクトページがRedditで共有され、「普通のスマホ動画から動く物体を360度再構成できる」という結果に驚きの声が多数。

---

### 27. ColmapLiDAR App Update 1.2 — iOSアプリのスキャン安定性向上
**2026-03-23** | [Reddit投稿](https://www.reddit.com/r/GaussianSplatting/comments/1s0vy4n/)

iPhoneのLiDARを使って正確なカメラポーズ付きスキャンを行うColmapLiDARアプリがv1.2 Build 6にアップデート。スキャン安定性の向上とバグ修正が行われた。

---

### 28. gsplat-unity — Unity向け3DGSレンダリングパッケージが新規公開
**2026-03-26** | [GitHub](https://github.com/wuyize25/gsplat-unity)

Unity 2021以降に対応した3DGSレンダリングパッケージ「gsplat-unity」が公開された。既存のパイプラインへの統合を容易にする設計で、3DGSオブジェクトのドローコールを正しい順序で挿入できる。

---

### 29. SplatKing + NVIDIA RTX Pro 6000プレゼント企画
**2026-03-25** | [Reddit投稿](https://www.reddit.com/r/GaussianSplatting/comments/1s3cjlt/)

radiancefields.comのMichael氏がiPhone向け無料GSキャプチャアプリ「SplatKing」を紹介しつつ、NVIDIA RTX Pro 6000（VRAM 96GB）のプレゼント企画を実施。SplatKingは0.5xと1xレンズを同時に起動し、シャッタースピード・ISO・ホワイトバランスを手動制御できる。

---

### 30. Awesome-4D-Spatial-Intelligence — 4D空間知能500本論文まとめリポジトリ
**2026-03-23** | [GitHub](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence)

4D空間知能に関する500本以上の論文をまとめたGitHubリポジトリが公開・更新された。3DGS・4DGS・NeRF関連の研究を網羅的に把握したい研究者・開発者向けの必見リソース。

---

### 31. FastGS (CVPR 2026) — 3DGSを100秒でトレーニング
**CVPR 2026採択** | [GitHub参照](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence)

CVPR 2026に採択されたFastGSは、3DGSのトレーニング時間を従来の数十分から**わずか100秒**に短縮する手法。実用化・商用化の大きな障壁だったトレーニング時間問題への直接的な解答として注目される。

---

## 開発者向けインサイト

| 項目 | 内容 | 優先度 |
|------|------|--------|
| OpenUSD v26.03対応 | PLY→USDの変換パイプラインを整備する好機。hdParticleFieldでUSD内のGSをプレビュー可能に | 高 |
| SplatRenderer (UE5) | 無料・OSSで3D/4DGS両対応。UE5プロジェクトへの即時統合を検討 | 高 |
| RadianceKit (Mac) | Apple Silicon環境でのGSトレーニングが可能に。M1〜M4 Macユーザーへの展開機会 | 高 |
| SuperSplat Walk Mode | 不動産・建築向けGSビューアの差別化機能として即活用可能 | 高 |
| Khronos ウェビナー (4/7) | glTF標準化の最新動向を把握する機会。4月7日参加推奨 | 中 |
| NanoGS GUI Tool | 非エンジニア向けGS最適化ツールとして配布・活用可能 | 中 |
| FastGS (CVPR 2026) | 100秒トレーニングが実用化されれば、リアルタイムGS生成パイプラインが現実的に | 高 |

---

*収集日: 2026-03-27 | ソース: arXiv, Hugging Face Papers, Reddit r/GaussianSplatting, CG Channel, VentureBeat, radiancefields.com, GitHub, Instagram, Reddit*
