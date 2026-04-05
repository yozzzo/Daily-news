# 3DGS & 4D生成 デイリーレポート (2026-04-05)

本日の3D Gaussian Splatting（3DGS）および4D生成に関する最新動向をお届けします。世界中から収集した最新論文、ツール、業界ニュース、コミュニティの話題から、重複を排除した新規項目のみを厳選しています。

## 🌟 今日の注目トレンド

1. **4DGSの実用化とエンタメ導入**：スペインのテーマパークで世界初のリアルタイム4DGSデジタルヒューマンが稼働開始。また、スマホで4DGSを生成・配信できる日本のプラットフォーム「4DGS.jp」が登場しました。
2. **Web・ゲームエンジンでの標準化と最適化**：PlayCanvasがGracia 4DGSをネイティブサポートし、Babylon.jsがV9.1で球面調和関数のダウンサンプリングに対応。Web上での高品質な3DGS再生環境が急速に整っています。
3. **大規模・長尺シーンへの対応**：論文「TRiGS」や「MotionScale」など、数千フレームに及ぶ長尺動画や大規模な動的シーンを効率的に再構成する4DGS技術が次々と発表されています。

---

## 📄 注目論文（Research & Papers）

### [GEMM-GS](https://arxiv.org/abs/2604.02120)
- **分野**: 高速化
- **概要**: テンソルコアを活用したGPU上での3DGS高速化手法。GEMM変換により描画パイプラインを再設計

### [TRiGS](https://arxiv.org/abs/2604.00538)
- **分野**: 4DGS
- **概要**: SE(3)剛体変換を統合した4DGS。1200フレームの長尺動画シーン再構成に対応
- **何ができるようになったか**: これまで難しかった長時間の動的シーン（最大1200フレーム）を、破綻なく高品質に4D再構成できるようになりました。
- **課題と解決策**: 従来の4DGSは短い動画には対応できても、長時間の動きでは計算量や品質が低下する課題がありました。剛体変換（物体の回転や平行移動）を数学的に統合することで、効率的かつ正確に長尺動画を処理できるようになりました。

### [F3DGS](https://arxiv.org/abs/2604.01605)
- **分野**: 分散・マルチエージェント
- **概要**: 連合学習（フェデレーテッドラーニング）を使ったマルチエージェント分散3D再構成
- **何ができるようになったか**: 複数のロボットやドローンが協力して、1つの巨大な3Dマップを安全かつ効率的に作成できるようになりました。
- **課題と解決策**: これまでは全データを1箇所に集めて処理する必要があり、通信量やプライバシーの問題がありました。連合学習（各端末で学習し、結果だけを共有する手法）を用いることで、データを分散させたまま全体マップを構築できるようになりました。

### [Palette-Based Color Grading for 3DGS](https://arxiv.org/abs/2604.01551)
- **分野**: 編集
- **概要**: パレットベースのリアルタイムカラーグレーディング。3DGSシーンをリアルタイムで色調整可能
- **何ができるようになったか**: 3DGSで生成された空間の色合いを、画像編集ソフトのようにリアルタイムで直感的に変更できるようになりました。
- **課題と解決策**: 3DGSのデータは色情報が複雑に絡み合っており、後から色を変えるのが困難でした。パレットベースの色調整手法を導入することで、特定のオブジェクトの色だけを変えたり、全体のトーンを調整したりすることが可能になりました。

### [ARGS](https://arxiv.org/abs/2604.00494)
- **分野**: 生成
- **概要**: 自己回帰型Gaussian Splatting生成フレームワーク。並列プログレッシブデコーディングで高品質3D生成

### [TRACE](https://arxiv.org/abs/2604.01207)
- **分野**: 編集
- **概要**: 接線ベクトルを使った高忠実度3Dシーン編集フレームワーク

### [Director](https://arxiv.org/abs/2604.01678)
- **分野**: 4DGS・人物
- **概要**: インスタンス認識型4DGS。動的シーンで人物パフォーマンスと高品質レンダリングを統合

### [MotionScale](https://arxiv.org/abs/2603.29296)
- **分野**: 4DGS
- **概要**: 大規模動的シーン向けスケーラブル4DGSフレームワーク。CVPR 2026採択

### [Diff3R](https://arxiv.org/abs/2604.01030)
- **分野**: フィードフォワード3DGS
- **概要**: 不確実性認識型微分可能最適化を組み合わせたフィードフォワード3DGS

### [FaCT-GS](https://arxiv.org/abs/2604.01844)
- **分野**: 医療・CT
- **概要**: Gaussian Splattingを使った高速・スケーラブルなCT再構成フレームワーク

### [GS^2](https://arxiv.org/abs/2604.01884)
- **分野**: 圧縮・最適化
- **概要**: グラフベースの空間分布最適化によるコンパクト3DGS。少ないGaussian点数で高品質レンダリング

### [LESV](https://arxiv.org/abs/2604.01388)
- **分野**: 言語+3D
- **概要**: スパースボクセルと言語特徴を融合したオープン語彙3Dシーン理解

### [GeoHCC](https://arxiv.org/abs/2603.28431)
- **分野**: 圧縮
- **概要**: 幾何学的関係を活用した階層的コンテキスト圧縮で3DGSファイルサイズを大幅削減
- **何ができるようになったか**: 3DGSのデータサイズを大幅に圧縮し、スマホやWebでの読み込みを高速化できるようになりました。
- **課題と解決策**: 3DGSはデータ容量が非常に大きくなるのが弱点でした。空間内の点（アンカー）同士の幾何学的な関係性を利用して無駄なデータを省くことで、画質を保ったままファイルサイズを削減することに成功しました。

### [Coko-SLAM](https://arxiv.org/abs/2604.00804)
- **分野**: SLAM・ロボット
- **概要**: コンパクトキーフレーム最適化マルチエージェントGaussian Splatting SLAM。帯域制限環境でのロボット展開に対応

### [EgoSim](https://arxiv.org/abs/2604.01001)
- **分野**: ロボット・シミュレーション
- **概要**: 3DGSを使った自我中心世界シミュレーター。ロボットアームと人間の手のインタラクション動画生成

### [ReSplat](https://github.com/cvg/resplat)
- **分野**: フィードフォワード3DGS
- **概要**: 再帰型フィードフォワード3DGS。レンダリング誤差をフィードバックとして反復的にGaussianを精緻化

---

## 🛠️ 開発者向けインサイト（Tools & Updates）

### [DJI Reality](https://dronedj.com/2026/04/02/dji-reality-drone-3d-mapping/)
- **分野**: ドローン・ビューアー
- **概要**: DJI Terraに統合された無料3Dモデルビューアー。メッシュ・点群・3DGSを即時表示、ログイン不要
- **インサイト**: ドローン最大手のDJIが、無料の3Dモデルビューアーを公開しました。ログイン不要で、ドローンで撮影・生成した3DGSデータや点群データを即座に確認・共有できます。建設や測量現場でのデータ共有が劇的にスムーズになります。

### [DJI Avata 360](https://www.bhphotovideo.com/explora/video/news/dji-announces-the-avata-360-an-8k-360-degree-fpv-drone)
- **分野**: ドローン
- **概要**: DJIの8K 360度FPVドローン。3DGSデータ収集に最適な360度映像を8K/60fpsで撮影可能

### [PlayCanvas + Gracia 4DGS統合](https://80.lv/articles/playcanvas-can-now-load-gracia-s-4d-gaussian-splats)
- **分野**: 4DGS・Webエンジン
- **概要**: オープンソースWebエンジンPlayCanvasがGracia 4DGSをネイティブサポート。ブラウザ上でリアルタイムライティング・シャドウ付き4DGS再生が可能に
- **インサイト**: Webブラウザ上で動くゲームエンジン「PlayCanvas」が、Graciaの4DGS（動く3DGS）に正式対応しました。リアルタイムの光や影の計算も可能になり、Webサイト上で高品質な動的3Dコンテンツを配信するハードルが大きく下がりました。

### [Babylon.js V9.1](https://radiancefields.com/babylon.js-releases-v9.1)
- **分野**: Webエンジン
- **概要**: ダウンサンプリング球面調和関数（SH）生成とランタイムSH次数制御を追加。Webブラウザ上での3DGS品質チューニングが可能に
- **インサイト**: Web3DエンジンのBabylon.jsがV9.1にアップデート。3DGSの光の反射を表現する「球面調和関数（SH）」のデータ量を調整できる機能が追加されました。これにより、スマホなどの低スペック端末ではデータ量を減らして軽くし、PCでは高画質で表示するといった最適化が容易になります。

### [World Labs Marble 1.1 / 1.1 Plus](https://radiancefields.com/world-labs-releases-marble-1.1-and-marble-1.1-plus)
- **分野**: 3D世界生成
- **概要**: テキストから3D世界を生成するMarbleが1.1にアップデート。1.1 Plusは動的に空間を拡張し、より大きな世界を生成
- **インサイト**: テキストから3D世界を生成するAI「Marble」がアップデート。新機能の「1.1 Plus」では、生成する空間の広さをAIが自動で拡張してくれるようになり、より広大な3D空間を一度のプロンプトで作成できるようになりました。

### [SplatRenderer v1.1.0](https://radiancefields.com/splatrenderer-v1.1.0-adds-level-sequencer-for-4dgs-in-unreal-engine-5)
- **分野**: UE5プラグイン・4DGS
- **概要**: UE5のLevel Sequencerで4DGSのキーフレームアニメーション制御が可能に。SplatScale・ScrubFrame・PlaybackSpeedをシーケンサーで直接制御

### [SplataraScan on SideQuest](https://radiancefields.com/splatarascan-arrives-on-sidequest)
- **分野**: VR・スキャン
- **概要**: Meta Quest向けGaussian Splat 3Dスキャナー＆マルチプレイヤービューアーがSideQuestで公開。P2P接続で複数ユーザーが同じGSシーンに同時入場可能

### [Blurry LoD Streaming](https://radiancefields.com/blurry-adds-level-of-detail-streaming-and-revamps-pricing)
- **分野**: ストリーミング
- **概要**: ブラウザ上で4000万以上のSplatシーンをLoD（詳細度）ストリーミングで処理。無料枠が30GBに拡大

### [AR Splat by AR Code](https://ar-code.com/blog/ar-splat-a-new-3d-scanning-to-augmented-reality-solution-based-on-gaussian-splatting)
- **分野**: AR・QRコード
- **概要**: 動画をアップロードするだけでGaussian Splattingベースの3DシーンをAR QRコードとして即時共有

### [COLMAP 4.0](https://radiancefields.substack.com/p/gaussian-splatting-in-march-nvidia)
- **分野**: 3D再構成
- **概要**: 3D再構成の定番ツールCOLMAP 4.0リリース。GLOMAPネイティブサポートを追加

### [vkSplatting 2026.1](https://radiancefields.substack.com/p/gaussian-splatting-in-march-nvidia)
- **分野**: Vulkan・レンダリング
- **概要**: NVIDIAのオープンソースVulkan Gaussian Splattingリファレンス実装が2026年初アップデート

### [fVDB V0.4](https://radiancefields.substack.com/p/gaussian-splatting-in-march-nvidia)
- **分野**: NVIDIAライブラリ
- **概要**: NVIDIAのfVDBがV0.4リリース。MCMCと3DGUTメソッドをライブラリに追加

---

## 📰 業界ニュース（Industry News）

### [Gracia PortAventura 4DGS体験](https://radiancefields.com/gracia-launches-4dgs-experience-at-portaventura-park)
- **分野**: 4DGS・エンターテインメント
- **概要**: スペインのテーマパーク「PortAventura」に世界初のリアルタイム4DGSデジタルヒューマンが登場。恐竜探検をガイドするULUMキャラクター
- **何ができるようになったか**: テーマパークの実際の来場者向けアトラクションに、4DGS技術が導入されました。
- **詳細**: スペインのPortAventuraパークにて、恐竜探検をガイドするデジタルヒューマンが4DGSで描画されています。研究室やWeb上だけでなく、現実のエンターテインメント施設で4DGSが実用化された画期的な事例です。

### [Cesium KHR_gaussian_splatting実装](https://radiancefields.substack.com/p/gaussian-splatting-in-march-nvidia)
- **分野**: 標準化
- **概要**: CesiumJS 1.139とCesium for Unreal v2.23.0にglTF KHR_gaussian_splatting拡張のサポートが実装。地理空間・インフラ可視化での3DGS標準化が加速

### [4DGS.jp（IZUTSUYA）](https://prtimes.jp/main/html/rd/p/000000027.000138121.html)
- **分野**: 日本・4DGS
- **概要**: 日本のIZUTSUYAがスマホ1台で4DGSデータを数十秒で生成・投稿・視聴できる空間映像配信プラットフォーム「4DGS.jp」を発表
- **何ができるようになったか**: 専門知識がなくても、スマホ1台で動く3D空間（4DGS）を撮影・生成し、世界中に配信できるようになりました。
- **詳細**: 日本のIZUTSUYAが発表したプラットフォーム。スマホで被写体の周りを回るように動画を撮るだけで、クラウド上で数十秒で4DGSデータに変換されます。YouTubeのように誰もが空間映像を投稿・視聴できる「空間映像の民主化」を目指しています。

### [共同通信3DGS大分火災検証](https://www.sanyonews.jp/article/1895966)
- **分野**: 日本・報道
- **概要**: 共同通信と一橋大が1781枚の航空写真から3DGSで大分火災現場を立体化。JIMA賞グランプリ受賞
- **何ができるようになったか**: 災害現場の状況を、写真ではなく「歩き回れる3D空間」として報道・記録できるようになりました。
- **詳細**: 共同通信と一橋大学が、大分県の火災現場を1781枚の航空写真から3DGSで立体化。この取り組みが日本インターネット報道協会（JIMA）賞のグランプリを受賞し、ジャーナリズムにおける3DGSの有用性が高く評価されました。

### [大日本印刷 伏見稲荷大社3DGSメタバース化](https://www.newprinet.co.jp/%E5%A4%A7%E6%97%A5%E6%9C%AC%E5%8D%B0%E5%88%B7%E3%80%80%E5%A4%A7%E9%98%AA%E3%83%BB%E9%96%A2%E8%A5%BF%E4%B8%87%E5%8D%9A%E3%81%A7%E4%BC%8F%E8%A6%8B%E7%A8%B2%E8%8D%B7%E5%A4%A7%E7%A4%BE%E3%82%92%E3%83%A1)
- **分野**: 日本・文化財
- **概要**: 大日本印刷が大阪・関西万博で伏見稲荷大社を3DGSでメタバース化。高精度・低コストなデジタル化を実現

### [Arcturus スポーツ放送ラジアンスフィールドインタビュー](https://radiancefields.com/inside-arcturus-how-radiance-fields-are-reshaping-volumetric-sports-broadcasts)
- **分野**: スポーツ放送
- **概要**: Arcturusがラジアンスフィールドを使ったボリュメトリックスポーツ放送の実用化について詳細インタビュー

---

## 🌐 コミュニティ・SNS話題（Community & Social）

### [Corridor Crew「THIS is the Biggest Thing Since CGI」](https://www.youtube.com/watch?v=X8yRlA7jqEQ)
- **分野**: YouTube・啓発
- **概要**: VFX解説チャンネルCorridor Crewが4D Gaussian Splattingを「CGI以来最大の革命」と紹介。大きな話題に
- **話題のポイント**: チャンネル登録者数600万人を超える大人気VFX解説YouTubeチャンネル「Corridor Crew」が、Gaussian Splattingを特集。「CGI（コンピュータグラフィックス）の登場以来、最大の革命だ」と絶賛し、一般層にも3DGSの認知が爆発的に広がるきっかけとなっています。

