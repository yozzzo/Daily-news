# 3DGS & 4D生成 デイリーレポート 2026-06-13

> 対象期間：2026-06-12〜2026-06-13 ／ 新規掲載件数：20件（論文7・ニュース4・ツール1・コミュニティ8）

---

## 今日の注目トレンド

1. **SIGGRAPH 2026 向けGS論文が続々プレプリント公開** — Gaussian Point Splatting（4.25億ガウシアンをリアルタイム表示）、Ref-DGS（反射面GS）がプレプリントで確認
2. **KIRI Engine 3DGS Render 5.0** — BlenderでGaussian Splatsをアニメーション化できる初のワークフロー（無料・6月11日）
3. **NVIDIA Isaac Sim 6.0 正式GA** — ロボット開発シミュレーターにGSが標準統合（6月4日）
4. **Gleanmer SoC（VLSI 2026）** — わずか6mWでリアルタイム3DGS。ドローン・IoT・ARグラスへの道
5. **Netflix GS職インターン募集** — 「未来のストリーミングフォーマット」としてGSを研究するPhDインターン公募

---

## スレッド1：注目論文（重要度：高）

### 1. Gaussian Point Splatting（SIGGRAPH 2026）
**RTX 4070 Ti SUPERで4億2500万ガウシアンをリアルタイム表示**

- **何が変わったか：** 従来のGSは大規模シーンになるほどソート（並び替え）処理が重くなり、数億ガウシアンのリアルタイム表示は実質不可能だった。確率的サンプリングで点を描画する本手法は「ソート不要」を実現し、フル解像度でのリアルタイム表示を達成。
- **仕組み：** 各ガウシアンからピクセルサイズの不透明な点をランダムサンプリングし、64-bit原子操作でフレームバッファに積む。GPU負荷が均等化され、スケールアップが容易。
- **ソース：** https://momentsingraphics.de/Siggraph2026.html | https://github.com/JorisAR/gaussian-point-splatting

---

### 2. Ref-DGS: Reflective Dual Gaussian Splatting（SIGGRAPH 2026）
**反射が多い物体（ガラス・金属・鏡）の3DGS再構成が大幅改善**

- **何が変わったか：** 反射面を含む物体は従来のGSで最難関の一つ。レイトレーシング（重い処理）なしで、高速なラスタライゼーションのまま反射を精密再現。
- **仕組み：** シーンを「幾何学ガウシアン」と「局所反射ガウシアン」に分割し、近距離・遠距離の反射を独立にモデリング。物理ベースの適応型シェーダーで統合。
- **ソース：** https://arxiv.org/abs/2603.07664

---

### 3. SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting（ICML 2026 Spotlight）
**2D画像処理と3D GS を統一した「ソフトスプラッティング」フレームワーク、ICML Spotlight採択**

- **何が変わったか：** 2Dビジョンモデルと3D GS表現の間のギャップを統一的に解消。機械学習タスク（検出・セグメンテーション）への3DGS活用の幅が広がった。
- **ソース：** ICML 2026 Proceedings

---

### 4. Beyond Heuristics: Learnable Density Control for 3DGS（ICML 2026）
**ガウシアンの密度制御を経験則からデータ駆動型学習へ**

- **何が変わったか：** 「どこにガウシアンを追加/削除するか」は従来ヒューリスティック（経験則）で決まっていた。本手法は学習で最適密度制御を実現し、品質・効率のトレードオフを改善。
- **ソース：** ICML 2026 Proceedings

---

### 5. HeroGS: Hierarchical Guidance for Robust 3DGS under Sparse Views（CVPR 2026）
**少枚数の写真でも破綻しない3DGS再構成**

- **何が変わったか：** 高品質3DGSには通常多数の写真が必要。HeroGSは少枚数（スパースビュー）でも、背景が崩れず高品質な再構成を維持。
- **仕組み：** 画像・特徴量・パラメータの3レベルで階層的ガイダンスを適用。少ない監督信号を擬似的な密な信号に変換して全体を正則化。
- **ソース：** https://arxiv.org/pdf/2603.01099

---

### 6. DirectFisheye-GS: Native Fisheye Input in GS（CVPR 2026）
**魚眼カメラ映像をそのまま3DGS化——歪み補正不要に**

- **何が変わったか：** ドライブレコーダー・監視カメラ・VR180カメラ等の広角「魚眼映像」は従来、歪み補正してからGS化する必要があった。本手法は魚眼のままクロスビュー最適化で3DGS再構成が可能。
- **ソース：** CVPR 2026 Open Access

---

### 7. SparseStreet: Sparse GS for Real-Time Street Scene Simulation（ICMR 2026・6月16-19日）
**自動運転シミュレーター向けスパースGSで道路シーンをリアルタイム再構成**

- **何が変わったか：** 少ないフレーム・粗いセンサーデータから自動運転用の高品質道路シーン3Dを再構成。ラベルなし圧縮でも精度を維持。
- **ソース：** https://arxiv.org/html/2606.03909v1

---

## スレッド2：業界ニュース

### 8. NVIDIA Isaac Sim 6.0 GA + NuRec GS 標準搭載（June 4, 2026）
**「ロボット開発環境にGSが完全統合——スマホで撮った空間がそのままロボット訓練場に」**

Isaac Sim 6.0 が正式GA（一般提供開始）。NuRec（Gaussian Splatting ライブラリ）が標準搭載され、スマートフォンで撮影した実際の環境を数分でロボット学習用シミュレーション空間に変換できる。OpenUSDとGS形式に対応し、物理シミュレーションとGSの連携が可能に。

倉庫・工場・医療施設でのロボット自動化コストが大幅に下がる見込み。

- **ソース：** https://radiancefields.com/nvidia-s-isaac-sim-6.0-ships-with-nurec-gaussian-splatting

---

### 9. KIRI Engine 3DGS Render 5.0 for Blender リリース（June 11, 2026）
**「無料プラグインが初めてBlenderでのGSアニメーション化を実現」**

Blender用GS専用プラグインの最新版。最大の新機能は「プロキシメッシュ→GSモーション転写」で、通常の3DキャラクターアニメーションをGSに反映してPLYシーケンスとして書き出せる。Blender 5.1対応・完全無料。現時点でExperimental（実験的）。

- **ソース：** https://www.cgchannel.com/2026/06/3dgs-render-5-0-lets-you-animate-gaussian-splats-inside-blender/

---

### 10. Gleanmer: 6mW SoC でリアルタイム3DGS（VLSI 2026）
**「超低消費電力チップでGSリアルタイム処理——ドローン・IoT・ARグラスへの普及加速」**

VLSI 2026で発表。わずか6mW（ミリワット）の消費電力でリアルタイム3D Gaussian Occupancy Mappingを実現するSoCチップ。スマートウォッチやARグラス・小型ドローンなど電力制約デバイスへのGS展開への大きな一歩。

---

### 11. ICMR 2026（アムステルダム、6月16-19日）GS関連セッション予定
**「マルチメディア検索の国際会議でGS論文が複数発表予定」**

SparseStreet（自動運転GS）を含む複数のGS関連論文がICSR 2026で発表予定。6月16〜19日、アムステルダム開催。

---

## スレッド3：コミュニティ・SNS話題

### 12. Netflix がGS専門映像コーデック研究インターン募集（Fall 2026）
**「Netflixが3DGSを"次世代ストリーミング形式"として本格研究開始のシグナル」**

職種名：Video Algorithms Intern - Video Coding (Gaussian Splatting)。TV・スマホ・ストリーミングデバイスへのGSデリバリー実現を目指すPhDレベルのインターン（24週間）。採用があれば、将来的に現在の.mp4のようにGS形式での映像配信が実現する可能性を示唆。

- **ソース：** https://explore.jobs.netflix.net/careers/job/790315673635-video-algorithms-intern-video-coding-gaussian-splatting-fall-2026-los-gatos-california-united-states-of-america

---

### 13. 日本公園のGSキャプチャが海外専門メディアで紹介（Masayuki Sugimoto氏）
日本在住のMasayuki Sugimoto氏が撮影した公園のGaussian Splattingキャプチャが LiDAR News 等で紹介。スノーグローブ型の球体ビューワーで日本庭園を内部から探索できる独自の表示方式が国際的に注目を集めた。

- **ソース：** https://lidarnews.com/japanese-park-3d-gaussian-splatting/

---

### 14. Pixel Lab 古代アセット3DGSモデルパック 無料公開（June 8, 2026）
歴史的遺物・古代建築物の3DGSモデルパックが無料配布。文化財アーカイブ・ゲーム・映像制作での活用が期待される。

- **ソース：** https://www.toolfarm.co.jp/blogs/news/free-ancient-assets-3d-gaussiansplat-modelpack

---

### 15. AirGS: Real-Time 4D Gaussian Streaming（INFOCOM 2026）が注目
**「ネットワーク越しにリアルタイム4D GS配信を実現」**

IEEE INFOCOM 2026で発表されたAirGSは、Free-Viewpoint Video（任意視点映像）をリアルタイムで4DGSストリーミングする手法。動画ストリーミングと3D表現の融合が着実に進んでいる。

---

### 16. GRTX: Efficient Ray Tracing for 3D Gaussian Rendering（HPCA 2026）
**「GPUハードウェアレベルでのGSレイトレーシング高効率化」**

HPCA 2026（コンピュータアーキテクチャのトップ会議）に採択。ハードウェア側からGSレンダリングを高速化する専用アーキテクチャ設計。GPU製造会社が実装すれば、将来のGPUでGSがより効率的に動作することを意味する。

---

### 17. CVPR 2026 Denver 閉幕後、GS関連コード公開が続く（〜June 13）
CVPR 2026（Denver、6/3-7）閉幕後も採択論文のコードがGitHubで続々公開中。

HeroGS・DirectFisheye-GS・REArtGS++などを今すぐ試せる。

- **ソース：** https://openaccess.thecvf.com/CVPR2026

---

## スレッド4：開発者向けインサイト（すぐ使えるツール・対応すべき動向）

### 18. 【今すぐ試せる】KIRI Engine 3DGS Render 5.0 セットアップ手順
BlenderでGSをアニメーション化したい開発者向けのチェックリスト：
- ✅ Blender 5.1 以上を用意（旧版では動作不可）
- ✅ [KIRI Engineプラグイン](https://www.kiriengine.app/3d-tools/3dgs-render) を無料インストール
- ✅ GS化したい対象にアーマチュア（ボーン）付きプロキシメッシュを用意
- ✅ アニメーションを設定し、「Bake to PLY Sequence」で書き出し
- ⚠️ 現時点でExperimental。高密度GSでは処理時間に注意

---

### 19. 【動向チェック】 Netflix + SIGGRAPH でGSが「ストリーミング配信フォーマット」へ
Netflix採用がシグナルするトレンド：
- GSが映像コーデックの候補として真剣に検討され始めた
- AirGS（INFOCOM 2026）など、ネットワーク配信向けGS論文が増加中
- 将来の動画配信プラットフォームはGS形式に対応する必要が生じる可能性
- 今のうちにGSの配信フォーマット（.splat, .spz, .ksplat）に慣れておくと有利

---

### 20. 【ハードウェア注目】 超低消費電力GSチップ Gleanmer（VLSI 2026）
6mWという超低消費電力でのGS処理は、以下への展開を示唆：
- **ARグラス** — バッテリー制約を克服してGSの常時表示が可能に
- **農業用ドローン** — エッジでGS処理してリアルタイム圃場3D化
- **産業IoTセンサー** — 工場インフラのリアルタイム3D異常検知

---

## 参照リンク一覧

| タイトル | タイプ | ソース |
|---|---|---|
| Gaussian Point Splatting | SIGGRAPH 2026 | [link](https://momentsingraphics.de/Siggraph2026.html) |
| Ref-DGS | SIGGRAPH 2026 | [arxiv](https://arxiv.org/abs/2603.07664) |
| SplAttN | ICML 2026 Spotlight | ICML 2026 |
| Beyond Heuristics | ICML 2026 | ICML 2026 |
| HeroGS | CVPR 2026 | [arxiv](https://arxiv.org/pdf/2603.01099) |
| DirectFisheye-GS | CVPR 2026 | [CVPR](https://openaccess.thecvf.com/CVPR2026) |
| SparseStreet | ICMR 2026 | [arxiv](https://arxiv.org/html/2606.03909v1) |
| NVIDIA Isaac Sim 6.0 | ニュース | [link](https://radiancefields.com/nvidia-s-isaac-sim-6.0-ships-with-nurec-gaussian-splatting) |
| KIRI 3DGS Render 5.0 | ツール | [CG Channel](https://www.cgchannel.com/2026/06/3dgs-render-5-0-lets-you-animate-gaussian-splats-inside-blender/) |
| Gleanmer SoC | VLSI 2026 | VLSI 2026 |
| Netflix GS インターン | コミュニティ | [link](https://explore.jobs.netflix.net/careers/job/790315673635-video-algorithms-intern-video-coding-gaussian-splatting-fall-2026-los-gatos-california-united-states-of-america) |
| 日本公園GS（Sugimoto氏） | コミュニティ | [LiDAR News](https://lidarnews.com/japanese-park-3d-gaussian-splatting/) |
| Pixel Lab 古代アセット | コミュニティ | [link](https://www.toolfarm.co.jp/blogs/news/free-ancient-assets-3d-gaussiansplat-modelpack) |
| AirGS（INFOCOM 2026） | 論文 | INFOCOM 2026 |
| GRTX（HPCA 2026） | 論文 | HPCA 2026 |
| CVPR 2026 Open Access | コミュニティ | [link](https://openaccess.thecvf.com/CVPR2026) |

---

*生成日時: 2026-06-13 / ソース: arXiv, CVPR 2026 Open Access, Radiance Fields, CG Channel, NVIDIA Developer, LinkedIn, LiDAR News*
