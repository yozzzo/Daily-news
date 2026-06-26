# 3DGS & 4D生成 デイリーレポート 2026-06-26

## サマリー
本日は新規17件(論文7件・業界ニュース4件・コミュニティ/SNS話題3件・開発者向けツール3件)を選出。プロ向けVFXツールへの3DGS本格統合(Autodesk Arnold)、3DGSの弱点だった「見えない部分の穴」を補完するAI技術、日本のKDDI総合研究所による高速化技術などが目立った。なお調査時点でネットワーク経由のページ直接アクセスが一部制限されており、検証可能性に幅があることを正直に申し添える。

## 今日の注目トレンド
1. **プロ向けVFXツールへの3DGS統合が加速**(Autodesk Arnold 7.5.2がGaussian Splat Shaderを正式搭載)
2. **3DGSの「見えない領域」問題にAIが挑む**(NVIDIA「ArtFixer」が観測不足エリアを自動補完)
3. **日本発の高速化技術が登場**(KDDI総合研究所、動画から要点だけ選んで3DGS生成を5倍速く)
4. **カメラポーズ不要・推論一発の3DGS研究が継続**(VG²GTなどフィードフォワード系の改良)
5. **3DGSの異分野クリエイティブ応用が拡大**(ガラス内への3Dプリントなど)

---

## 1. 注目論文(重要度:高)

### VG²GT(Voxel-Gaussian Splatting Visual Geometry Grounded Transformer)
- 分野: フィードフォワード3DGS・カメラポーズ推定
- URL: https://arxiv.org/abs/2606.01573
- 日付: 2026年6月上旬
- 概要: カメラの位置情報が分からない写真の束からでも、シーンごとの個別学習(最適化計算)なしに一発で3D空間を再構成できるようになった。従来のフィードフォワード型3DGSは「カメラの位置が既知である」ことが前提になりがちだったが、ボクセル(立方体状の3D格子)とガウシアンを組み合わせることでこの制約を緩めた。

### Anchored Temporal Gaussian Splatting(ATGS)
- 分野: 動的シーン再構成・ボリュメトリックビデオ
- URL: SIGGRAPH 2026採択論文(MrNeRF/Janusch Patasによる紹介ポスト: https://x.com/janusch_patas/status/2041880058722226334)
- 日付: 2026年6月
- 概要: 長時間の動画(数十秒〜分単位)でも、人物や物体の3D動画(ボリュメトリックビデオ)を破綻なく再構成できるようになった。従来の4DGSはシーケンスが長くなるほど形状がブレやすかったが、時間方向の「アンカー(基準点)」を導入することで長時間でも安定させた。

### SceneGen(Single-Image 3D Scene Generation in One Feedforward Pass)
- 分野: シーン生成・単一画像からの3D化
- URL: https://github.com/Mengmouxu/SceneGen
- 日付: 3DV 2026採択
- 概要: 1枚の写真から、複数の物体が配置されたシーン全体を一回の推論だけで3D化できるようになった。従来は物体ごとに繰り返し最適化計算が必要で時間がかかっていたが、推論一発(フィードフォワード)方式により大幅に高速化した。

### GS-SVIR(3D Gaussian Splatting for Inverse Rendering with Spatially Varying Illumination)
- 分野: インバースレンダリング(逆光学計算)
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0097849326001329
- 日付: 2026年6月
- 概要: 場所によって光の当たり方が違う複雑な照明環境でも、3DGSデータから「材質」と「光源」を分離して取り出せるようになった。これにより撮影後にライティングを自由に変更する(リライティング)精度が向上する。

### 一般化非指数型Gaussian Splatting(Generalized Non-Exponential Gaussian Splatting)
- 分野: 3DGS基礎理論の拡張
- URL: https://arxiv.org/pdf/2603.02887
- 日付: 2026年3月(継続して引用が増加)
- 概要: 通常のGaussian Splattingは「ガウス分布(釣鐘型のなめらかな形)」だけで物体表面を表現するが、これをより柔らかい/硬いエッジなど多様な形状表現に対応する分布族に一般化した。素材や形状の表現力が広がり、より忠実な見た目の再現につながる。

### Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation
- 分野: 動的シーン高速化
- URL: https://openreview.net/forum?id=V83a0sPhRl
- 日付: 2026年
- 概要: 静止部分は軽量な3D表現、動く部分だけ4D表現を使うという「使い分け」によって、動画全体を4D化するより大幅に計算・メモリを節約できるようになった。背景は動かないのに毎フレーム再計算していた無駄を解消した。

### Hardware-Rasterized Ray-Based Gaussian Splatting
- 分野: VR/ARハードウェア最適化
- URL: https://arxiv.org/pdf/2503.18682
- 日付: 2026年(VR/AR向け実装が進展)
- 概要: VR/ARヘッドセットのGPUで使われる「レイベース(光線単位)」の描画方式に3DGSを最適化し、専用ハードウェアの能力をフル活用できるようになった。スマホ向けGPUでもヘッドセット内でのリアルタイム3DGS表示に近づく技術。

---

## 2. 業界ニュース

### Autodesk、Arnold 7.5.2でGaussian Splat Shaderを正式搭載
- 分野: VFX・プロ向け3Dレンダラー
- URL: https://www.cgchannel.com/2026/06/autodesk-releases-arnold-7-5-2-with-support-for-gaussian-splatting/
- 日付: 2026年6月
- 概要: 映画・CM制作で使われるプロ向けレンダラー「Arnold」に3DGSデータを直接取り込み、シーン内のライトで自然に再照明できる機能が標準搭載された。これまで3DGSデータはプロのVFXパイプラインに持ち込むのが難しかったが、本機能で実写スキャンとCG照明を組み合わせた制作が容易になる。

### NVIDIA、見えない部分を自動で補完するAI「ArtFixer」を発表
- 分野: 3DGS品質改善・AI補完
- URL: SIGGRAPH 2026論文ベース(報道: kotaku.com/nvidia-art-fixer-ai-gaussian-splatting-hallucination-ram-prices-2000709422)
- 日付: 2026年6月
- 概要: 3DGSは撮影時に死角だった部分が穴や歪みとして残る課題があったが、AIが「ここには何があるはずか」を推測して自然に埋められるようになった。撮影漏れがあっても完成データの見栄えを保てるため、撮影の手間・時間を減らせる。

### KDDI総合研究所、動画から要点だけ選んで3DGS生成を5倍高速化する技術を開発
- 分野: 3DGS生成高速化・日本企業
- URL: https://www.kddi-research.jp/newsrelease/2026/062401.html
- 日付: 2026年6月24日
- 概要: 動画をそのまま全部使うのではなく、3Dモデル生成に本当に必要なフレームだけをAIが選び出すことで、3DGSモデルの生成時間を5倍速くできるようになった。これまでは撮影した動画の全フレームを使う必要があり処理時間が課題だったが、本技術により実用的な処理時間まで短縮した。

### scipapermill、3DGS応用の最新動向を総括する解説記事を公開
- 分野: 業界動向まとめ
- URL: https://scipapermill.com/2026/06/13/gaussian-splatting-takes-flight-from-real-time-humans-to-planetary-scenes-and-beyond/
- 日付: 2026年6月13日
- 概要: リアルタイムの人物キャプチャから惑星規模の地球規模シーンまで、3DGSの応用範囲がスケールを問わず広がっている現状を整理した解説記事。技術の使われ方の全体像を把握するのに役立つ。

---

## 3. コミュニティ・SNS話題

### GIGAZINE、3DGSデータをガラスの中に3Dプリントする作品を紹介
- 分野: クリエイティブ応用
- URL: https://gigazine.net/news/20260624-3dgs-in-glass/
- 日付: 2026年6月24日
- 概要: 3DGSで撮影したデータを、まるで本物をガラスの中に閉じ込めたような立体物として3Dプリントする事例が話題になった。デジタルの3DGSデータが物理的な記念品・アート作品として「持ち帰れる」形に変換される、異分野応用として注目された。

### MomentsInCG(X)、64bitアトミック演算による超大規模シーンの実時間描画を紹介
- 分野: レンダリング技術・コミュニティ話題
- URL: https://x.com/MomentsInCG/status/2057458023619035341
- 日付: 2026年6月
- 概要: 巨大な3DGSシーンを描画する際、ピクセル単位の計算競合(複数のガウシアンが同じピクセルを同時に書き込もうとする処理の衝突)を、64bitアトミック演算という仕組みで効率よく解消する技術が紹介され、CGコミュニティで話題になった。大規模都市・屋外シーンのリアルタイム表示を後押しする技術。

### Qiita、週次の3DGS関連技術メモが公開
- 分野: 開発者向け情報まとめ・日本語コミュニティ
- URL: https://qiita.com/youtoy/items/a4aa112286d7306b981c
- 日付: 2026年6月上旬
- 概要: MeshSplatting、TripoSplat、Cosmosなど複数の3DGS関連ツールの動向をまとめた日本語の技術メモがQiitaで公開され、国内エンジニアの情報収集の手がかりとなっている。

---

## 4. 開発者向けインサイト(すぐ使えるツール・対応すべき動向)

### gsplat(nerfstudio-project)、メインブランチで新機能を続々追加
- 分野: 開発ツール・CUDAライブラリ
- URL: https://github.com/nerfstudio-project/gsplat
- 概要: 多くの3DGSプロジェクトの基盤として使われるCUDA高速化ライブラリ「gsplat」のメインブランチで、HiGS推論レンダリング、CUDA MCMC(モンテカルロ最適化)、AccuTile、LiDARラスタライズなどの開発が進行中。次の正式リリースを待たずに最新機能を試したい開発者は要チェック。

### PlayCanvas SuperSplat v2.28.0がリリース
- 分野: ブラウザベース3DGS編集ツール
- URL: https://github.com/playcanvas/supersplat
- 日付: 2026年6月24日
- 概要: インストール不要でブラウザから3DGSデータを編集・最適化・公開できるエディタ「SuperSplat」が新バージョンに更新された。継続的に機能追加が行われており、Web完結の3DGS編集環境として実務での採用が進んでいる。

### MrNeRF/LichtFeld-Studio v0.5.3がリリース
- 分野: C++/CUDAネイティブ3DGS訓練・編集アプリ
- URL: https://github.com/MrNeRF/LichtFeld-Studio
- 日付: 2026年6月24日
- 概要: 3DGSの訓練・編集・自動化・エクスポートまでを担うネイティブアプリ「LichtFeld-Studio」が更新され、Vulkanビューアの改善・VRAM使用量の削減・Asset Manager機能が追加された。Pythonプラグイン経由でMCP(他のAIツールとの連携)にも対応しており、パイプライン自動化を検討する開発者に有用。

---

## 取材手法に関する注記
今回の調査では、調査時点でネットワークプロキシの一部制限により、arXiv・ニュースサイトなど多くのページへの直接アクセスができず、検索結果のスニペット(抜粋)を主な根拠とした項目が含まれる。GitHubリポジトリについては直接アクセスで内容を確認済み。すべてのURLは実在する検索結果・リポジトリに基づくものであり、架空の項目は含めていない。

*本レポートは過去配信済み項目(past_3dgs.json、386件)と照合し、重複を完全に排除した新規項目のみで構成しています。*
