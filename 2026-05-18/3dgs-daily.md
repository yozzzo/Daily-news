# 3DGS & 4D生成 デイリーレポート — 2026年5月18日（月）

**新着件数**: 論文5件 / ニュース3件 / ツール・コミュニティ2件 = 合計10件

---

## 今日の注目トレンド（Top 5）

1. 🧪 **物理×3DGS融合** — PG-3DGSが「見た目だけでなく物理的に機能する形状」生成を実現（飛行機を3Dプリントして揚力を実験検証）
2. 💾 **GPU 1枚で1億点突破** — CLM-GSがCPU Offloadingで単一RTX4090に25km²都市の3DGS学習を実現（NYU/ASPLOS 2026）
3. 🏗️ **CAD/GIS業界へ本格統合** — SolidWorksとEsri ArcGIS両方へのGS統合が今週同時登場
4. ⚡ **4DGS効率化** — ICLR 2026採択のHybrid 3D-4D GSが静止・動的領域を自動判別し計算コストを大幅削減
5. 🎬 **VFXパイプライン統合強化** — Houdini 21 Solaris向けオープンソースGSプラグイン公開（MIT License）

---

## 🔬 注目論文（重要度：高）

### 1. PG-3DGS — 「物理的に機能する形状」を3DGSで生成

- **分野**: 物理シミュレーション × 3DGS
- **出典**: arXiv:2605.11266（Purdue大学、2026年5月）
- **リンク**: <https://arxiv.org/abs/2605.11266>
- **重要度**: ★★★★★（新しい応用パラダイム）

**何ができるようになったか**
3DGSで「水を注げるポット」や「揚力を生む飛行機の翼」など、見た目だけでなく物理的に機能する3D形状を自動生成できるようになった。

**これまでの課題と解決策**
従来の3DGSは「外見が正確な形状」の最適化のみで、物理的機能は考慮されていなかった。PG-3DGSは微分可能な物理シミュレーターと3DGSを組み合わせ、「液体が流れる」「揚力が発生する」などの物理目標に向けて形状を自動最適化する。

**実証**: 3Dプリントした飛行機（Cessna・B-2スピリット・紙飛行機）で実際に風洞実験を行い、提案手法の形状が既存手法より高い揚力を生むことを確認。

**応用**: ロボット設計・航空部品・医療器具など「機能する3Dアセット」生成の新パラダイム。

---

### 2. AmbiSuR — 光の曖昧さを解決し3DGS表面再構成の精度を向上

- **分野**: 表面再構成・3DGS精度向上
- **出典**: arXiv:2605.12494（2026年5月12日）
- **リンク**: <https://arxiv.org/abs/2605.12494>
- **重要度**: ★★★★（表面精度が製造・医療応用に直結）

**何ができるようになったか**
複数カメラから3Dシーンを復元する際、「光度曖昧性」による形状ノイズを自動補正し、より正確な表面形状を得られるようになった。

**これまでの課題と解決策**
同じ表面が異なるカメラから「違う明るさ」に見える現象（光度曖昧性）が3DGSの表面精度を低下させていた。AmbiSuRはGS表現が本来持つ「制約不足な領域を自己検出する能力」を活用し、曖昧な箇所だけを選択的に補正する。

**応用**: 建築・製造・医療向け精密3D計測、高精度デジタルツイン構築。

---

### 3. Hybrid 3D-4D Gaussian Splatting — 静止・動的領域を自動判別（ICLR 2026採択）

- **分野**: 4DGS・動的シーン再構成
- **出典**: arXiv:2505.13215（ICLR 2026採択）
- **リンク**: <https://arxiv.org/abs/2505.13215>
- **重要度**: ★★★★（4DGS実用化を加速）

**何ができるようになったか**
4DGS（動的シーン向け）の計算コストを大幅削減しながら品質を維持できるようになった。

**これまでの課題と解決策**
4DGSは動きのない背景（壁・床）にも高コストな4D表現を割り当てるため計算リソースの大半が無駄になっていた。このハイブリッド手法は最初に全て4DGSで表現し、「時間的に変化しない」ガウス点を自動検出して軽量な3DGSに変換。動く部分だけ4Dを維持する。

**結果**: トレーニング時間・メモリを大幅削減しながら品質は同等以上を維持。

**応用**: スポーツ・イベント・ライブパフォーマンスなど動的シーンの効率的な4D再構成。

---

### 4. CLM-GS — CPUをバッファにして単一GPUで都市スケール3DGS学習（ASPLOS 2026）

- **分野**: 大規模3DGS・システム最適化
- **出典**: arXiv:2511.04951（ASPLOS 2026発表、NYU研究チーム）
- **リンク**: <https://arxiv.org/abs/2511.04951>
- **GitHub**: <https://github.com/nyu-systems/CLM-GS>
- **重要度**: ★★★★★（民主化インパクト大）

**何ができるようになったか**
一般向けGPU（RTX4090）1枚で102百万個のガウス点・25km²規模の都市を3DGSで学習できるようになった。

**これまでの課題と解決策**
大規模シーンの3DGS学習はGPUメモリが最大のボトルネックで、高価なサーバーGPUクラスタが必須だった。CLM-GSは「現在見えているガウス点の選択」に必要な位置・形状だけをGPUに保持し、残りの属性（色・輝度係数）をCPUメモリにオフロード。GPU↔CPU間通信を計算とオーバーラップさせることで速度を維持。

**応用**: 都市デジタルツイン・大型施設の精密3D化コストが劇的低下。単一高性能GPUサーバーで運用可能に。

---

### 5. Gaussian Blending (AAAI 2026) — アルファブレンディングの数学的基礎を再設計

- **分野**: 3DGSレンダリング基礎理論
- **出典**: AAAI 2026採択
- **GitHub**: <https://github.com/1207koo/gaussian_blending>
- **重要度**: ★★★★（基礎理論の修正で広範に影響）

**何ができるようになったか**
ガラス・水・煙・髪など透明・半透明な物体の3DGS表現品質が向上した。

**これまでの課題と解決策**
3DGSのレンダリングは「ガウス点を奥から手前に積み上げて最終色を計算する」アルファブレンディングに依存するが、この標準手法には長年見過ごされてきた理論的矛盾がある。これが透明物体の品質低下の根本原因だった。Gaussian Blendingはアルファブレンディングの数学的定式化を根本から再考し、理論的に整合性のある新手法を提案。

**応用**: ガラス・液体・煙などの難物体が含まれるシーン全般の3DGS品質改善に広く波及。

---

## 📰 業界ニュース

### 6. Esri ArcGIS Reality & Site Scan Q2 2026 — 測量・GIS・ドローン業界でGSが標準機能化

- **出典**: Esri Community（2026年5月）
- **リンク**: <https://community.esri.com/t5/site-scan-blog/site-scan-q2-2026-faster-reality-mapping-at-scale/ba-p/1691379>

世界最大手GISプラットフォームEsriが2026年Q2に3DGS関連の大型アップデートを2連発。

- **ArcGIS Reality for ArcGIS Pro（5月版）**: 植生・細構造（柵・配管等）を含む複雑な表面でのGS忠実度が大幅向上
- **Site Scan for ArcGIS Q2 2026**: ドローン計測データからクラウド上でGSを自動生成する機能を新搭載。1ミッション最大10,000枚の画像処理に対応

**インパクト**: AEC（建築・エンジニアリング・建設）・インフラ管理・測量の現場でGSが「当然の選択肢」になるフェーズに突入。Esriが標準化を主導することで業界全体への普及が加速する。

---

### 7. Plattipus houdini-gsplat — Houdini 21 Solaris向けオープンソースGSプラグイン公開（2026-05-14）

- **出典**: Alliance for OpenUSD Forum
- **リンク**: <https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921>
- **GitHub**: <https://github.com/plattipus/houdini-gsplat>

**何ができるようになったか**
Houdini 21 SolarisのUSDパイプライン上でGSを標準的な素材として扱えるようになった。

OpenUSD v26.03の新スキーマ「UsdVolParticleField3DGaussianSplat」をベースに、独自HydraレンダリングデリゲートとLOP3ノード（PLY Import・Gsplat Instancer・Uruk）を実装。VFXスタジオが既存のHoudini/USDパイプラインにGSを組み込める。

**インパクト**: 映像制作現場へのGS定着が加速。MIT Licenseで即導入・改変可能。

---

### 8. Veesus × SolidWorks — CAD設計ソフトにGaussian Splatが入り込む

- **出典**: Veesus / Radiance Fields
- **リンク**: <https://www.veesus.com/point-cloud-plugins/>

**何ができるようになったか**
Veesusプラグイン経由でSolidWorksにGSモデルを直接統合・閲覧可能になった。製造業・建設業・造船業の設計者が普段使うSolidWorksの中でGSを参照しながら設計できる。

VeesusはRhino（GS対応済み）・SolidWorks・Revit・CloudCompareにプラグインを展開中。「現場スキャン → GS生成 → CAD設計」の一貫ワークフローが成立。

---

## 🛠️ コミュニティ・ツール

### 9. Gaussian Splat Morpher — GS間をなめらかにモーフィング（MIT License）

- **出典**: GitHub
- **リンク**: <https://github.com/feel3x/Gaussian_Splat_Morpher>

**何ができるようになったか**
2つ以上のGSキャプチャ（.plyファイル）を入力するだけで、シームレスなモーフィング動画を自動生成できる。

Felix Hirtが開発。空間的・色的類似性でガウス点を対応付け、位置・色・スケール・回転を球面線形補間（Slerp）でなめらかに補間。CLIでバッチ生成 / GUIスライダーでリアルタイムプレビューの両方に対応。

**活用例**: 工事前後・季節変化・製品改良の比較動画、展示向けトランジション演出。MIT Licenseで即商用利用可能。

---

### 10. CVPR 2026直前コード公開ラッシュ — 重要論文リポジトリが続々オープン

CVPR 2026（2026年6月3-7日、デンバー）まで約2週間。今週の注目コード公開:

- <https://github.com/nyu-systems/CLM-GS>（大規模3DGS学習・ASPLOS 2026）
- <https://github.com/1207koo/gaussian_blending>（アルファブレンディング再設計・AAAI 2026）
- <https://github.com/fastgs/FastGS>（100秒でGS学習・CVPR 2026 Highlight）
- <https://github.com/plattipus/houdini-gsplat>（Houdini 21 Solaris GS統合・MIT）

CVPR 2026ではGaussian Splatting関連論文が50件以上発表予定。独自実装・追試・応用実験を始める絶好のタイミング。

---

## 💡 開発者インサイト（今日すぐ活用できること）

| カテゴリ | アクション | リンク |
|---------|-----------|-------|
| 大規模シーン学習 | `nyu-systems/CLM-GS` で単一GPU・都市スケール学習に挑戦 | https://github.com/nyu-systems/CLM-GS |
| モーフィング動画制作 | `feel3x/Gaussian_Splat_Morpher` でBefore/After GS比較動画を即生成 | https://github.com/feel3x/Gaussian_Splat_Morpher |
| VFXパイプライン | `plattipus/houdini-gsplat` をHoudini 21 SolarisのUSDワークフローに試験導入 | https://github.com/plattipus/houdini-gsplat |
| 物理機能検証 | PG-3DGS（2605.11266）でロボット部品・製品の機能的形状生成を検討 | https://arxiv.org/abs/2605.11266 |
| 4DGS効率化 | Hybrid 3D-4D GS を動的シーン撮影プロジェクトに適用し計算コスト削減 | https://arxiv.org/abs/2505.13215 |
| レンダリング品質向上 | `gaussian_blending` で透明・半透明物体の表現品質を改善 | https://github.com/1207koo/gaussian_blending |

---

*レポート生成: 2026-05-18 | 次回: 2026-05-19*
