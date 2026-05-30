# 3DGS & 4D生成 デイリーレポート｜2026-05-30

> **配信件数**: 新規20件（論文9件・ニュース6件・コミュニティ/ツール5件）  
> **重複除外**: past_3dgs.json 参照済（前回配信: 2026-05-15）

---

## 🔥 今日の注目トレンド

1. **10億Gaussianの壁が崩れた** — TideGS が SSD/CPU/GPU の階層キャッシュで 10億 Splat を 24GB GPU 1 枚で学習可能に。Aholo Viewer はその規模をブラウザで表示。
2. **言語 × 3DGS が 400 倍高速化** — SCOUP が「自然言語で 3D シーンを操作」する学習コストを劇的削減。
3. **Gaussianが物理エンジンと融合** — PhyGenHOI（テキスト→物理的インタラクション 4D 生成）・Real2Sim（自動運転用物理シミュレーション）が登場。
4. **業界標準ソフトが一斉 GS 対応** — Corona 15（グローバルイルミネーション）、Houdini Solaris（USD V26.03 ネイティブ）、SolidWorks（Veesus）が GS を本格統合。
5. **CVPR 2026 Denver（6/5〜7）目前** — 4,090 本採択（前年比 +42%）。来週から 3DGS 論文コードが怒涛の公開ラッシュ。

---

## 📄 論文（新規9件）

### 1. TideGS — 10億Gaussianを単一GPUで学習
- **URL**: https://arxiv.org/abs/2605.20150
- **投稿日**: 2026-05-19
- **重要度**: ★★★
- **概要**: これまで3DGS学習は「GPUのVRAMに何個乗るか」が上限だった。TideGS は SSD・CPU・GPU を階層型キャッシュとして使い、**10億超の Gaussian を 24GB GPU 1 枚で学習**可能にした。既存の最適化手法（約1億個）の10倍以上。都市丸ごと・工場全体などの超高精細3D化がいよいよ現実的に。プロジェクトページ: https://sponge-lab.github.io/TideGS/

---

### 2. Eulerian Gaussian Splatting (Hashed Probability Pyramids) — densification 不要の新アーキテクチャ
- **URL**: https://arxiv.org/abs/2605.29136
- **投稿日**: 2026-05-27（Harvard / Google DeepMind / Google）
- **重��度**: ★★★
- **概要**: 3DGS 最大の弱点「Gaussian の分裂・削除をヒューリスティックで調整しなければならない」を根本解決。各 Gaussian を「確率密度からのサンプル」として扱い、勾配だけで最適配置を学習。チューニング不要で mip-NeRF 360 最高品質、かつ 3DGS 級の描画速度を両立。

---

### 3. SCOUP（Sparse Code Uplifting）— 言語3DGS 400倍高速化
- **URL**: https://arxiv.org/abs/2605.13600
- **投稿日**: 2026-05-14
- **重要度**: ★★★
- **概要**: 「3Dシーンを自然言語で理解・操作」する Language GS の学習を **400倍高速化**、VRAM は 3分の1 に。言語表現を2D画像領域から疎なコードブックとして学習し、それを3D Gaussianに展開する方式。「赤いソファはどこ？」「3Dで非常口を示せ」のような自然言語×3D理解の実用化が大きく前進。

---

### 4. Sensor2Sensor（Waymo + Johns Hopkins大）— ドラレコ映像→自動運転センサーデータ変換
- **URL**: https://arxiv.org/abs/2605.22809
- **投稿日**: 2026-05-30
- **重要度**: ★★★
- **概要**: 普通のドライブレコーダー映像（カメラ1台）を、自動運転車が必要とする LiDAR + マルチカメラ統合データに変換する拡散モデル。4DGS で実際の AV ログを学習し、一般カメラとの相互変換を実現。YouTube のドラレコ動画が自動運転のトレーニングデータになる可能性を開く。

---

### 5. FaceParts — 顔GSアバターの教師なしパーツ分割・スワップ
- **URL**: https://arxiv.org/abs/2605.13853
- **投稿日**: 2026-05-14
- **重要度**: ★★
- **概要**: 顔の 3DGS アバターを「目・眉・ひげ・口」などパーツ単位で **ラベルなし自動分割**し、異なる人物のパーツを入れ替えられる。FLAME ベースのパーツ転送で精度高く編集可能。メイク・スタイル編集や映像制作での部位別制御に直結。NeRSemble データセット（11名）で検証済み。

---

### 6. PhyGenHOI — テキスト→物理的人間-物体インタラクション 4D ��成
- **URL**: https://arxiv.org/abs/2605.30268
- **投稿日**: 2026-05-28
- **重要度**: ★★
- **概要**: 「サッカーボールを蹴る」等のテキストを入力すると、人体モーション生成 AI（MDM）と物体の材料力学シミュレーション（MPM）が同時最適化され、**物理的に正しい衝撃・変形**を伴う 4D シーンを自動生成。3DGS を統一された微分可能な表現として利用し、Windowed Attraction Loss と Contact-Driven Re-simulation で人体と物体を同期。

---

### 7. Underwater360 — 水中全方位 3DGS 再構成
- **URL**: https://arxiv.org/abs/2605.26447
- **投稿日**: 2026-05-26
- **重要度**: ★★
- **概要**: 水の屈折・散乱・減衰などの光学特性を 3DGS に組み込み、360 度水中パノラマからのシーン再構成を実現。球面投影の幾何歪みを排除する Omnidirectional GS モジュールと、深度に依存した散乱・減衰を分離するPhysics-based 外観モデルを組み合わせ。海底探査・水中ドキュメンタリーでのリアル 3D 表現が可能に���

---

### 8. Real2Sim — 自動運転用 物理ベース編集可能 4DGS
- **URL**: https://arxiv.org/abs/2605.13591
- **投稿日**: 2026-05-13
- **重要度**: ★★
- **概要**: 実際の走行映像から 4DGS で動的シーンを再構成し、物理シミュレーター（MPM）と連携して「追突」「雨天」等の**コーナーケースシナリオ**を自動生成。現実データ → 物理シミュレーション → 学習データ拡充の完全自動パイプライン。RPI・University of Delaware 共同研究。

---

### 9. Transcoding 3DGS（元画像なしで既存3Dアセット変換）
- **URL**: https://arxiv.org/abs/2605.21051
- **投��日**: 2026-05-20
- **重要度**: ★★
- **概要**: 既存の 3D メッシュや PLY 点群データから**元の撮影画像なしで** 3DGS に変換するパイプライン。カスタム初期化で収束を大幅高速化し、元の点群よりも少ない Gaussian で高品質な GS を生成。何年も前に作られた旧来の 3D アセットをリアルタイム描画可能な GS 形式に変換できる。映画・ゲーム業界のアセット再利用に直結。

---

## 📰 ニュース（新規6件）

### 1. Manycore Tech「Aholo Viewer」オープンソース公開
- **URL**: https://www.prnewswire.com/news-releases/manycore-tech-open-sources-3d-gaussian-viewer-ushering-in-the-era-of-the-3d-internet-302781474.html
- **日付**: 2026-05-26
- **重要度**: ★★★
- **概要**: 中国の Manycore Tech が、**10億 Splat 以上**をブラウザで快適表示できる GS ビューワー「Aholo Viewer」をオープンソース公開。スマホ・PC・VR 対応でインストール不要。チャンク単位 LoD ストリーミングを採用。World Labs Spark 2.0 の10倍規模のシーンを処理可能。都市スケールの 3D Web サービスが現実的に。

---

### 2. Chaos Corona 15 — GS にグローバルイルミネーション対応
- **URL**: https://radiancefields.com/corona-15-makes-gaussian-splats-participate-in-global-illumination
- **日付**: 2026-05
- **重要度**: ★★★
- **概要**: 建築・内装業界標準のレンダラー「Corona 15」が GS に**グローバルイルミネーション**（光の間接反射）を適用可能に。これまで GS はレイトレースの光計算に参加できず「のっぺりした光」になりがちだったが、Corona 15 では GS 環境の光が 3D CG オブジェクトに正しく当たる。スキャンした実空間と 3D CGの融合品質が大幅向上。3ds Max、Blender、Cinema 4D 対応。

---

### 3. XGRIDS LCC Cloud — SLAM+3DGS クラウドサービス正式商用化
- **URL**: https://radiancefields.com/xgrids-open-sources-its-lcc-file-format-aims-to-standardize-3dgs-pipelines
- **日���**: 2026-05-21
- **重要度**: ★★
- **概要**: XGRIDS の LCC Cloud が 5/21 に正式有料サービスへ移行。月 250 分のクラウド処理で年額 800 ドル。LCC Scan スマホアプリで撮影→クラウド処理→GS 出力が完全自動化。専用 PC・GPU 不要。LCC ファイルフォーマット（V2.0）もオープンソース化し、標準フォーマット化を狙う。

---

### 4. Esri ArcGIS Reality Studio + Site Scan May 2026 アップデート
- **URL**: https://www.esri.com/arcgis-blog/products/arcgisrealitystudio/imagery/whats-new-in-arcgis-reality-studio-may-2026
- **日付**: 2026-05
- **重要度**: ★★
- **概要**: 世界最大 GIS プラットフォームが GS 精度を大幅改善。薄い構造物（フェンス・木の枝）や高密度植生の再現精度が向上。クラウド処理ワークフロー対応でスケール制限が撤廃。Site Scan for ArcGIS では 1 ミッション最大 **10,000 枚**まで処理可能に（大型ドローン測量・インフラ点検用途）。

---

### 5. houdini-gsplat（Plattipus）— USD V26.03 対応 Houdini Solaris GS 統合
- **URL**: https://radiancefields.com/houdini-gsplat-brings-usd-native-gaussian-splats-to-houdini-solaris
- **日付**: 2026-05
- **重要度**: ★★
- **概要**: Plattipus 社が Houdini 21 Solaris 向け GS プラグインをオープンソース公開。OpenUSD v26.03 の新 GaussianSplat スキーマ（UsdVolParticleField3DGaussianSplat）を使い、GS を **USD プリムとしてシーングラフに完全統合**。PLY をインポートするだけで Hydra ビューポートにリアルタイム表示。Houdini 上で GS を他の 3D アセットと同等に扱える。

---

### 6. Veesus May 2026 — SolidWorks で GS 可視化・XGRIDS LCC2 対応
- **URL**: https://radiancefields.com/veesus-adds-solidworks-gaussian-splatting-support-in-may-update
- **日付**: 2026-05
- **重要度**: ★★
- **概要**: 点群・GS 統合ビューワー Arena4D が SolidWorks プラグインに GS 表示を追加。製造業での設計 CAD データと実空間スキャン（GS）の重ね合わせが同一ソフトで実現。レンズフレア・動的シャドウの GS 対応や XGRIDS LCC2 フォーマットサポートも同梱。

---

## 🛠️ コミュニティ・ツール（新規5件）

### 1. 360 Splat Pro v1.2.5 — GPU 高速化 + Insta360 RAW 写真対応
- **URL**: https://radiancefields.com/360-splat-pro-v1.2.5-gpu-friendly-alignment-and-insta360-raw-photo-support
- **重要度**: ★★
- **概要**: 360 度映像から GS を生成する定番ツールの新バージョン。GPU フレンドリーモードで位置合わせが大幅高速化。Insta360 の `.insp` RAW 写真フォーマットに新対応し、動画だけでなく**静止画のマルチ枚撮影からも 3DGS 生成**が可能に。$44.99 買い切り、v1.x 系アップデート無償。

---

### 2. Gaussian Splatting Unity VR Plugin — VR 対応追加
- **URL**: https://radiancefields.com/gaussian-splatting-unity-plugin-gets-vr-support
- **重要度**: ★★
- **概要**: Aras Pranckevičius 氏のオープンソース Unity GS プラグインに VR 対応が追加（Ninjamode 氏の PR がマージ）。Meta Quest 3 で 72fps 達成には 50 万 Gaussian 以下が推奨。Unity 6 LTS 対応。VR コンテンツでの GS 活用がより手軽に。

---

### 3. 3DVista 2026.0「Total VR Mode」— GS を完全 VR 対応
- **URL**: https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/
- **重���度**: ★★
- **概要**: バーチャルツアー作成ツール 3DVista がアップデート。これまで VR では省略されていた UI スキン・eラーニング機能が完全対応し、**GS + 従来パノラマ混合のツアーが VR ヘッドセットで完全体験可能**に。不動産・観光・文化財 VR ツアーへの応用が加速。

---

### 4. Gaussian Splatting Morphing Tool — 2 シーン間ブレンド（MIT ライセンス）
- **URL**: https://radiancefields.com/gaussian-splatting-morphing-tool-to-blend-between-3dgs-captures
- **重���度**: ★
- **概要**: 2 つの GS シーンを滑らかにモーフィング・ブレンドするツールがオープンソース公開。異なる時刻に撮影した同じ場所の GS を繋いでタイムラプス的演出が可能。映像制作・イベント演出・季節変化の可視化などへの活用が期待。GitHub クローンのみでインストール（MIT License）。

---

### 5. CVPR 2026 Denver（6/5〜7）— 3DGS 論文コード公開ラッシュ目前
- **URL**: https://cvpr.thecvf.com/Conferences/2026
- **重要度**: ★★★
- **概要**: 来週開催の CVPR 2026 に **4,090 本が採択**（前年比 +42%）。3DGS 関連では FastGS（100 秒学習）・EDGS（densification 廃止）・EmbodiedSplat（Open-Vocabulary 3D 理解）など多数の論文コードが公開予定。今後 2 週間は特に要チェック。

---

## 💡 開発者向けインサイト

### 今すぐ試すべきもの
- **TideGS** — 大規模シーン開発者向け。10億Splat学習アーキテクチャが今後の標準設計に
- **SCOUP** — Language GS 実装者向け。400倍高速化で実用コストが現実的に
- **houdini-gsplat** — Houdini ユーザー向け。USD v26.03 GS スキーマのリファレンス実装として最速
- **Aholo Viewer** — Web GS プラットフォーム開発者向け。10億Splat対応のアーキテクチャを参照

### 対応すべき変化
1. **CVPR 2026 コード公開ラッシュ（6/5〜）** — 2週間で GitHub の GS トレンドが大幅刷新
2. **物理 × GS** — MPM との統合が次世代標準になりつつある（PhyGenHOI, Real2Sim）
3. **USD v26.03 × GS スキーマ** — パイプライン設計時はUSDネイティブ対応を前提に
4. **クラウド GS の価格競争** — XGRIDS LCC Cloud（年$800）商用化。競合価格帯を把握
5. **既存 3D アセットの GS 変換** — Transcoding 3DGS で旧資産の GS 移行が現実的に

---

*レポート生成: 2026-05-30 | ソース: arXiv, Radiance Fields, PR Newswire, CG Channel, Esri Blog, 3DVista, CVPR*
