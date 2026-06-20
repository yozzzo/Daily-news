# 3DGS & 4D生成 デイリーレポート 2026-06-20

## サマリー
本日は新規22件(論文5件・業界ニュース7件・コミュニティ/SNS話題7件・開発者向けツール3件)を選出。AWE USA 2026(XR業界カンファレンス)を中心にボリュメトリック映像配信の実用化が進んだほか、CVPR2026関連の高速化研究、手・指の3D/4D再構成、モバイル/Web配信の最適化が目立った。

## 今日の注目トレンド
1. **AWE USA 2026でXR/ボリュメトリック映像の実用化発表が集中**(Apple Vision Pro向け4DGSアプリ、Unity向けGSプラグインなど)
2. **CVPR2026関連の高速化研究が続々**(100秒で3DGS学習完了、4台のカメラだけで4D再構成)
3. **手・指の3D/4D再構成研究が複数登場**(AR/VRグラスのハンドトラッキング市場を見据えた動き)
4. **モバイル・Web配信の最適化が進展**(WebGPUレンダラー、モバイルで30倍圧縮の新コーデック)
5. **ガウシアン技術の異分野応用が拡大**(画像の霞除去、ロボット訓練用シミュレーション環境の自動構築)

---

## 1. 注目論文(重要度:高)

### Intrinsic-GS(Intrinsic 4D Gaussian Segmentation from Scene Cues)
- 分野: 4DGSセグメンテーション
- URL: https://arxiv.org/abs/2606.18623
- 日付: 2026-06-17
- 概要: 動画の中で動いている物体を、人手でラベル付けせずに自動で切り分けられるようになった。これまでは物体ごとに「これは椅子」「これは人」とAIに教え込む(マスク教師あり学習)必要があったが、本手法は形・向き・動きのパターンだけから物体の境界を発見し、教師あり手法(SAM活用のTRASE)と同等の精度を12.5倍速く実現した。

### GASE(Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments)
- 分野: Embodied AI・ロボットシミュレーション
- URL: https://arxiv.org/abs/2606.17520
- 日付: 2026-06-16
- 概要: パノラマカメラで撮った映像から、ロボット訓練用のシミュレーション空間を自動で作れるようになった。これまでロボット学習環境の構築には専門オペレーターと高価な機材が必要だったが、本システムは多視点動画から物体を自動抽出・補完し、現実とのギャップが小さい仮想空間を素早く構築できる。

### Hand-4DGS(Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos)
- 分野: ハンド再構成・AR/VR
- URL: https://arxiv.org/abs/2606.19156
- 日付: 2026-06-17
- 概要: メガネ型カメラ(一人称視点)で撮った映像から、手の動きを3Dでリアルタイムに再現できるようになった。従来は撮影後に時間のかかる最適化計算が必要だったが、フィードフォワード方式(一発の推論で完了する仕組み)により高速化し、AR/VRグラスでの手の動き認識に直結する技術。

### VEPHand(View-Efficient Photometric Hand Performance Capture at Scale)
- 分野: ハンドパフォーマンスキャプチャ
- URL: https://arxiv.org/abs/2606.15966
- 日付: 2026-06-14
- 概要: わずか20台ほどのカメラで、手の精密な動きを高精度キャプチャできるようになった。高品質な手のモーションキャプチャには通常100台規模の専用カメラリグが必要だったが、視点効率を高めたパイプラインによりコストを大幅に下げた。

### Dehaze-GaussianImage(Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation)
- 分野: 画像処理応用(2DGS)
- URL: https://arxiv.org/abs/2606.16163
- 日付: 2026-06-15
- 概要: 2D版のガウシアンスプラッティング技術を使い、霞んだ写真を学習なしでクリアにできるようになった。従来の画像処理はピクセル単位の格子計算(CNN/Transformer)が主流だったが、霞を連続的に変化するガウシアンの集合として捉える新しい発想で画質改善を実現した。

---

## 2. 業界ニュース

### 4Dviews、Unity向けボリュメトリックGaussian Splattingプラグインを発表
- 分野: 映像制作・ゲームエンジン対応
- URL: https://www.cgw.com/Press-Center/News/2026/4Dviews-unveils-Unity-plug-in-for-volumetric-Gau.aspx
- 日付: 2026年6月15〜18日(AWE USA 2026会場発表)
- 概要: Unityゲーム内に、メッシュ(従来の3D形状データ)とGaussian Splat(写実的な点描写)の両方を同時に出力できるようになった。ゲーム開発者が一つのワークフローで両方の3D表現を使い分けられる「デュアル・ボリュメトリック・パイプライン」を業界初で実現。

### Gracia AI、Apple Vision Pro向け初の4D Gaussian Splattingアプリを公開
- 分野: XR・映像配信
- URL: https://www.uploadvr.com/gracia-moving-volumetric-captures-now-streamable/
- 日付: 2026年6月(AWE USA 2026にて発表)
- 概要: Apple Vision Proで、歩き回って視聴できる無料の4D動画コンテンツが25シーン以上見られるようになった。従来のボリュメトリック動画は通信容量が課題だったが、動きの差分だけを圧縮する技術で帯域を10倍以上削減し、配信を現実的にした。

### Radiant Images、次世代ボリュメトリック撮影システム「Meridian 4D」を発表
- 分野: 映像制作・ボリュメトリックキャプチャ
- URL: https://www.awexr.com/blog/awe-usa-2026-major-product-launches-new-immersive-experiences-and-industry-announcements
- 日付: 2026年6月16日頃
- 概要: iPhone 17 Pro 56台を同期させた持ち運び可能な撮影リグで、24時間以内に4D動画化できるようになった。従来は据え置き型の巨大スタジオが必要だったが、5G同期と軽量化によりロケ撮影が可能になった。

### MultiSet AI、世界初の「3DGS-to-VPS」パイプラインを発表
- 分野: 自己位置推定・AR/VPS
- URL: https://www.multiset.ai/post/world-first-3dgs-to-vps
- 日付: 2026年6月(AWE USA 2026)
- 概要: Gaussian Splatで撮った3Dデータを、そのまま位置認識(VPS=スマホやARグラスが「今どこにいるか」を把握する仕組み)の地図として使えるようになった。これまでLiDARなど専用スキャナーで別途データを作る必要があったが、撮影データをそのまま転用できることでコストと手間を削減した。

### OwnXR、AIによるGaussian Splat生成を組み込んだXRコンテンツ制作プラットフォームを発表
- 分野: コンテンツ制作・AI生成
- URL: https://www.awexr.com/blog/awe-usa-2026-major-product-launches-new-immersive-experiences-and-industry-announcements
- 日付: 2026年6月(AWE USA 2026)
- 概要: 3Dモデリングの専門知識がなくても、AIが自動でXRコンテンツ用のGaussian Splatを生成できるようになった。専門スキルの壁がXRコンテンツ制作のハードルだったが、AI生成により誰でも制作に参加できるようになる。

### アクティブリテック、3DGSデータ閲覧用の自社開発Webビューアを発表(日本)
- 分野: 建設・インフラ点検・日本企業
- URL: https://prtimes.jp/main/html/rd/p/000000015.000093846.html
- 日付: 2026年5月(直近動向として収載)
- 概要: ブラウザだけで3DGSデータを見られる、専用ソフト不要のビューアが日本企業から登場。建設・点検現場では専用ソフトのインストールやライセンス管理が障壁だったが、Webブラウザ対応で現場でのデータ共有が容易になった。

### UWA(UHD World Association)、業界初の3DGS向け空間イメージング標準と新コーデック「EGSC」を発表
- 分野: 業界標準・圧縮コーデック
- URL: https://uhd-world-association.com/news/uwa-releases-the-industrys-first-spatial-imaging-standard-to-foster-ecosystem-development/
- 日付: 2026年6月
- 概要: スマホでも「見た目はロスレス」な品質を保ちながら、3DGSデータを最大30倍圧縮できる新しい業界標準が登場した。これまで3DGSデータは容量が大きくモバイル配信が難しかったが、業界団体が定めた新コーデックによりモバイルでも実用的な配信が可能になる見込み。

---

## 3. コミュニティ・SNS話題

### FastGS(100秒で3DGSを学習・CVPR2026 Highlight)
- 分野: 開発ツール・学習高速化
- URL: https://github.com/fastgs/FastGS
- 日付: CVPR2026 Highlight選出
- 概要: 3DGSの学習(撮影データから3D空間を作る処理)が、わずか100秒で完了するようになった。従来は数分〜数十分かかっていた学習を、視点間の一致性を使った効率的な処理で2〜6倍高速化。

### Faster-GS(3DGS最適化を再分析・改善するフレームワーク・CVPR2026)
- 分野: 研究フレームワーク
- URL: https://github.com/nerficg-project/faster-gaussian-splatting
- 日付: 2026年6月時点で活動継続中
- 概要: 研究者が手元のPCで3DGSの研究コードを2〜5倍速く、少ないメモリで動かせるようになった。再現・拡張しやすい設計のため、学術コミュニティでの採用が進んでいる。

### Mobile-GS(モバイル端末向けリアルタイム3DGS・ICLR2026)
- 分野: モバイル最適化
- URL: https://github.com/xiaobiaodu/mobile-gs
- 日付: 2026年6月時点で更新継続
- 概要: スマートフォンの限られた処理能力でも、3DGSをリアルタイムに描画できるようになった。モバイルアプリへの実装に直結する技術として注目。

### VolSplat(ボクセル整列予測によるフィードフォワード3DGS)
- 分野: 3D再構成手法
- URL: https://github.com/ziplab/VolSplat
- 日付: 2026年継続更新中
- 概要: 画像から直接3Dガウシアンを予測する際に、シーンの複雑さに応じて精度を自動調整できるようになった。フィードフォワード型3DGSの精度とマルチビュー間のズレという課題を解決。

### AnySplat(無制約視点からのフィードフォワード3DGS・ACM TOG)
- 分野: カメラポーズ不要の再構成
- URL: https://github.com/InternRobotics/AnySplat
- 日付: ACM TOG掲載、2026年も活発に拡張中
- 概要: カメラの位置情報が分からない、適当に撮った写真の束からでも、一回の処理で3D空間を再構成できるようになった。従来はカメラの正確な位置・角度情報が必要だったが、推定と再構成を同時に行うことでハードルを下げた。

### 4C4D(4台のカメラで4D Gaussian Splatting・CVPR2026)
- 分野: 4D生成・動的シーン再構成
- URL: https://github.com/yangzf-1023/4C4D
- 日付: CVPR2026採択
- 概要: わずか4台のカメラだけで、高精度な4D(時間変化する3D)シーンを再構成できるようになった。透明度の変化を扱う新しい数式(Neural Decaying Function)を導入し、少ない視点でも幾何形状を正しく学習できるようにした。低コストな4Dキャプチャの実用化に近づいたと評価されている。

### note.com 日本語3DGS解説記事が拡散
- 分野: 教育コンテンツ・日本語コミュニティ
- URL: https://note.com/onemorevision/n/nf73fe74fb41e
- 日付: 2026年(継続的に拡散)
- 概要: 3DGSの仕組みと最新フォーマット(SOG)を「ちゃんと理解する」ための入門記事が日本語コミュニティで拡散。技術初心者向けに分かりやすく解説し、建設・点検分野での活用記事とも連携。日本国内での技術理解の土台づくりに貢献している。

---

## 4. 開発者向けインサイト(すぐ使えるツール・対応すべき動向)

### NVIDIA Vulkan Gaussian Splatting 2026.1
- 分野: 開発ツール・レンダリングSDK
- URL: https://radiancefields.com/nvidia-releases-vulkan-gaussian-splatting-2026.1
- 概要: Vulkan(グラフィックスAPI)上で3DGSをネイティブに高速描画できる公式SDKが登場。自作レンダラーやゲームエンジン開発者は、これを使えばクロスプラットフォームな3DGS描画基盤をゼロから作らずに済む。

### PlayCanvas Engine 2.19.0(WebGPUレンダラー+Streamed SOG)
- 分野: Web技術・配信最適化
- URL: https://blog.playcanvas.com/new-in-supersplat-webgpu-and-streaming-bring-huge-performance-wins/
- 日付: 2026年6月3日
- 概要: WebGPUによる新レンダラーと、ストリーミング配信に最適化された圧縮フォーマット(Streamed SOG)が搭載され、スマホでもサクサク3DGSをWeb表示できるようになった。大容量データの一括読み込みが必要だった課題を、詳細度(LOD)に応じた段階読み込みで解決。

### Facepunch、s&box向けGaussian Splatライブラリを公式リリース
- 分野: ゲーム開発・実験的機能
- URL: https://radiancefields.com/facepunch-ships-gaussian-splat-library-for-s-box
- 日付: 2026年6月上旬
- 概要: Garry's Modの後継ゲームエンジンs&boxに、リライティング機能付きのGaussian Splat描画ライブラリが公式アカウントから実験的機能として追加された。インディーゲーム開発者がコミュニティ製の3DGSコンテンツをゲーム内に組み込みやすくなった。

---

*本レポートは過去配信済み項目(past_3dgs.json)と照合し、重複を排除した新規項目のみで構成しています。*
