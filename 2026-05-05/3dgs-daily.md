# 3DGS & 4D生成 デイリーレポート — 2026年5月5日

**収集件数**: 論文9件・ニュース5件・コミュニティ5件・開発者インサイト5件（重複排除済み）

---

## 🔥 今日の注目トレンド TOP5

1. **Eurographics 2026 開催中**（5/4-8 ドイツ・アーヘン） — GTAvatar・RotGS・GS-2M・LeafFit など注目GS論文が続々発表
2. **Cesium + 3D Tiles に GS の階層的LoD 正式対応** — 都市規模の3DGSデータをリアルタイムストリーミング可能に
3. **GETA-3DGS（arxiv 2605.02086）** — 3DGSファイルを自動で約1/5に圧縮する世界初のend-to-end自動フレームワーク
4. **DNE × Gracia：4分間の4DGS音楽パフォーマンスがブラウザ配信** — ダウンロード・アプリ不要でQuest3・スマホ・PCから視聴可能
5. **Flow4DGS-SLAM（arxiv 2604.22339）** — 動く人・車が混在する環境でカメラ追跡と4D再構成を同時実現

---

## 📚 スレッド1：注目論文（重要度：高）

### 1. GETA-3DGS ★★★★★
- **リンク**: https://arxiv.org/abs/2605.02086
- **投稿**: 2026年5月3日
- **分野**: 圧縮・最適化
- **概要**: 3DGSシーンは1シーンで数百MB〜数GBに達し、スマホ・VRデバイスには大きすぎる問題があった。GETA-3DGSは3DGS対応の量子化認識依存グラフ（QADG）を用いてGaussian点の重要度を自動スコアリングし、プルーニング（枝刈り）と量子化（精度を落とす）を同時最適化。手動しきい値設定なしに約5倍の圧縮を達成する世界初のend-to-end自動フレームワーク。
- **なぜ重要か**: モバイル・VRへのGSコンテンツ配信の最大のボトルネック（データサイズ）を自動で解消。

### 2. Flow4DGS-SLAM ★★★★☆
- **リンク**: https://arxiv.org/abs/2604.22339
- **分野**: 4DGS・SLAM・ロボット
- **概要**: SLAM（ロボット・ARに必須の自己位置推定と地図作成の同時実行技術）は動く物体が多い環境で精度が落ちるという課題があった。本手法は光学フロー（映像内の動きパターン）を使って静的部分と動的部分を自動区別し、4DGS（時間軸も含む3D表現）で動的シーンを再構成することでロバストなSLAMを実現。シンガポール国立大学の研究。

### 3. GTAvatar（Eurographics 2026） ★★★★☆
- **リンク**: https://arxiv.org/abs/2512.09162
- **プロジェクトページ**: https://kelianb.github.io/GTAvatar/
- **分野**: アバター生成・再照明
- **概要**: 通常のGSアバターは球面調和関数で見た目を表現するためPhotoshop等での直接テクスチャ編集が困難だった。GTAvatarはGaussian点をUVテクスチャ空間に埋め込み、アルベド・粗さ・法線マップを分離して保持することで任意照明でのリアルタイム再照明と直感的なテクスチャ編集を両立。1本の動画から高品質アバターを生成可能。Eurographics 2026採択。

### 4. GS-2M（Eurographics 2026） ★★★★☆
- **arXiv**: https://arxiv.org/abs/2509.22276
- **GitHub**: https://github.com/ndming/GS-2M
- **分野**: メッシュ再構成・マテリアル対応
- **概要**: 3DGSからメッシュを抽出する際、鏡面反射が強い部分で形状が崩れる問題があった。GS-2Mはマテリアルの「粗さ」を学習に組み込み、複数視点からの輝度変化を使って自動的に反射成分を分離。事前学習モデル不要で動作し、ガラス・金属など高反射マテリアルに対して水密（穴なし）で滑らかなメッシュを生成。Eurographics 2026採択。

### 5. RotGS（Eurographics 2026） ★★★★☆
- **リンク**: https://onlinelibrary.wiley.com/doi/10.1111/cgf.70317
- **分野**: 3DGS最適化・ECサイト応用
- **概要**: 3DGS生成に必須のSfM処理はターンテーブル撮影（物体が回転するパターン）で特徴点追跡が失敗しやすかった。RotGSは「物体が一本の軸を中心に回転している」という幾何的制約を活用し、Gaussian点の動きと光学フローを比較してカメラパラメータを精密推定。製品写真・商品カタログの3DGS化に実用的。マルチカメラシステムへの拡張も提案。Eurographics 2026採択。

### 6. LeafFit（Eurographics 2026） ★★★☆☆
- **arXiv**: https://arxiv.org/abs/2602.11577
- **GitHub**: https://github.com/netbeifeng/leaf_fit
- **分野**: 植物GSアセット化・ゲームエンジン
- **概要**: 植物は葉が複雑に重なるため3DGSデータが非常に重くなり、ゲームエンジンでは使えなかった。LeafFitは個々の葉をセグメント化し、代表的な葉形状をテンプレートにしてMLS（Moving Least Squares）変形で全葉にフィッティング。実行時はバーテックスシェーダーで計算するため追加ストレージ不要。データサイズを大幅削減しつつパラメータ編集も可能。Eurographics 2026採択。

### 7. ELoG-GS ★★★☆☆
- **リンク**: https://arxiv.org/abs/2604.12592
- **分野**: 低照度3DGS再構成（NTIRE 2026）
- **概要**: 低照度環境（夜間・地下・暗い室内）での3DGS生成はノイズで点群の初期化が崩壊するという課題があった。ELoG-GSはVGGT深度推定＋ボクセル融合で頑健な点群を初期化し、Retinexformerで低照度補正した後に二重ブランチアーキテクチャで再構成。NTIRE 2026チャレンジ（CVPR 2026付随）への提出論文。

### 8. Sparse-View 3DGS in the Wild ★★★★☆
- **リンク**: https://arxiv.org/abs/2604.27422
- **分野**: スパースビュー・実世界GS
- **概要**: 少ない写真（スパースビュー）から、観光地のように人が写り込む野外環境でも高品質なGSを生成する新しいパイプラインを提案。Diffusionモデルで動く邪魔なものを除去しながら、スパース領域はGaussian複製戦略で補完。観光地・公共空間スキャンなど実世界での応用に特化した実用的な研究。

### 9. BiSplat-WRF ★★★☆☆
- **リンク**: https://arxiv.org/abs/2604.25945
- **分野**: 無線通信・RF場再構成
- **概要**: Wi-Fi・5Gミリ波などの電波強度分布の3Dモデル化は従来レイトレーシングが必要で計算コストが高かった。BiSplat-WRFは平面型GS（Planar GS）でRF電磁場を再構成し、電波の反射・散乱・回折などの周波数依存効果を物理的に正確にモデル化。NB-IoT/Wi-Fi/ミリ波の混在環境に対応。通信インフラ設計・電波計測に応用可能。

---

## 📰 スレッド2：業界ニュース

### 1. Eurographics 2026 開催中（5/4-8、ドイツ・アーヘン）
- **公式**: https://eg2026.github.io/
- 欧州最大のコンピュータグラフィックスカンファレンスが今週開催中。GS関連論文4本（GTAvatar・RotGS・GS-2M・LeafFit）が採択されており、GS技術が学術カンファレンスの主要テーマとして定着。コードはGitHubで順次公開中。

### 2. Cesium May 2026リリース：GS + 3D Tilesの階層的LoD対応
- **LoDブログ**: https://cesium.com/blog/2026/04/27/3d-gaussian-splats-lod/
- **5月リリース**: https://cesium.com/blog/2026/05/01/cesium-releases-in-may-2026/
- Cesium ionに写真をアップロードするだけでLoD付きGSタイルセットを自動生成。CesiumJS・Cesium for Unreal（v2.26.0）対応。`KHR_gaussian_splatting`+`KHR_gaussian_splatting_compression_spz`の2つのglTF拡張も実装済み。都市スキャン〜サブセンチメートル精細データのリアルタイムストリーミングが実用段階に。

### 3. Unigine 2.21：GSカラーコントロール大幅強化
- **リリースノート**: https://unigine.com/news/2026/unigine-sdk-2-21-released-new-animation-system-ai-ready-workflow-and-major-performance-gains/
- **Radiance Fields**: https://radiancefields.com/unigine-2.21-expands-gaussian-splatting-controls
- 産業・防衛シミュレーション向け3DエンジンUnigine v2.21にGSシーンへの色・彩度・明るさ・コントラストのパーシーン調整機能を追加。CPUフレーム時間12.5%削減など全体的な性能改善も同梱。

### 4. DNE × Gracia：4分間4DGS音楽パフォーマンスをブラウザ配信
- **CG Channel**: https://www.cgchannel.com/2026/04/dne-and-gracia-release-4-minute-streamable-4dgs-performance/
- **80.lv記事**: https://80.lv/articles/gaussian-splatting-videos-can-now-be-streamed-like-regular-videos
- 歌手Amy Mayの4分間フルパフォーマンス（4DGS）をWebGPUベースでブラウザ配信。ダウンロード不要・アプリ不要でQuest3・Pico4・スマホ・MacのWebGPUから視聴可能。4DGSコンテンツが「普通の動画」と同じ感覚で配信できることを実証。

### 5. OctaneRender 2026.3リリース
- **CG Channel**: https://www.cgchannel.com/2026/04/otoy-releases-octanerender-2026-3/
- 業界標準GPUレンダラーOctaneRenderがGS対応（パストレース・シャドウ・反射映り込み）を維持しながらv2026.3へアップデート。ネットワークレンダリングでのバーチャルテクスチャが使用可能に。

---

## 💬 スレッド3：コミュニティ・SNS話題

1. **Eurographics 2026コミュニティ盛り上がり** — RotGS（ターンテーブル対応）とLeafFit（植物アセット化）がReddit/Twitter/Xで「実用性が高い」と評価が集まっている
2. **DNE×Gracia音楽パフォーマンス視聴レポートが拡散** — 「アプリなし・ダウンロードなし・4分間フルパフォーマンスがブラウザで動いた」という体験レポートが各SNSで拡散
3. **Cesium LoD対応がAEC・GIS業界に波及** — 建設・エンジニアリング・GISコミュニティでデジタルツイン活用の議論が急増
4. **「Decoupled Reprojection Consistency」GS失敗診断ツールに注目** — EG 2026採択のGSデバッグ支援論文がコミュニティから実務的に評価
5. **NTIRE 2026 RealX3D結果公開** — 極低光量3D復元チャレンジ結果サマリー（https://arxiv.org/abs/2604.04135）に複数のGSアプローチが参加したことが判明

---

## 🛠 スレッド4：開発者向けインサイト

1. **【今すぐ試せる】Cesium ion：GS + LoD タイルセット生成** — 写真アップロードのみでLoD付きGSタイルを自動生成。CesiumJS・UE5対応
2. **【要ウォッチ】GETA-3DGS自動圧縮** — コード公開待ちだが手動設定不要のGS圧縮フレームワーク。モバイル・VRGSアプリ開発者は注目
3. **【今週チェック】EG 2026論文コード公開** — GS-2M・LeafFitはGitHub公開済み。GTAvatar・RotGSも今週中に公開予定の可能性
4. **【重要動向】4DGS Webストリーミングスタックの台頭** — Gracia WebGPU + PlayCanvas + Quest3対応で4DGS配信インフラが整備されつつある
5. **【実務応用】RotGS：ターンテーブル撮影で製品3DGS化を自動化** — ECサイト・製品展示向けの3DGS化パイプライン構築に活用検討を

---

*Generated: 2026-05-05 | Sources: arXiv, Eurographics 2026, CG Channel, Radiance Fields, Cesium Blog, 80.lv*
