# 3DGS & 4D生成 デイリーレポート — 2026年6月1日（月）

**新着件数：論文14件 / 業界ニュース3件 / コミュニティ4件 ＝ 合計 21件**

---

## 🔥 今日の注目トレンド TOP5

1. 🏆 **CVPR 2026 Denver 開幕**（6/3〜6/7）— 3DGS論文80本以上を一挙発表。世界最大のコンピュータビジョン学会開幕週
2. 🪟 **GLINT** — ガラス越しの透明物体を初めてGSでリアルに再現（CVPR 2026 **Oral**）
3. ⚡ **MoVieS** — 動画1本から *1秒以内* に4D動的シーン再構成+3D物体追跡を同時実現
4. 📜 **KHR_gaussian_splatting 批准直前** — KhronosのglTF GS標準がQ2 2026内に正式確定へ
5. 🚀 **SpeeDe3DGS** — 動的3DGSを *13.71×* 高速化・1/10のGaussian数で同等品質

---

## 📄 注目論文（重要度：高）

### GLINT — ガラス・透明物体をGSで完全再現 `CVPR 2026 Oral`

**何ができるようになったか：**
窓ガラス・ショーケース・眼鏡など、これまで3DGSが苦手としてきた「透明物体」を正確に3D再構成できるようになりました。反射と透過の光を物理的に分離して別々にモデル化することで、ガラス越しの室内も、ガラス面の映り込みも、正確に再現します。

**解決された課題：**
3DGSはすべての物体が「不透明」であるかのように扱うため、ガラス素材のある場面では光の曲がり方が破綻していました。GLINTはガラス面を明示的に検出し、その前後の光輸送を別々に学習することでこの限界を打破。建築可視化・小売VR・博物館展示のデジタルアーカイブに直結。

- **arXiv:** https://arxiv.org/abs/2603.26181
- **GitHub:** https://github.com/youngju-na/GLINT

---

### MoVieS — 1秒で4D動的シーンを丸ごと再構成 `CVPR 2026`

**何ができるようになったか：**
スマホで撮影した動画1本から、1秒以内に「3D外観」「ジオメトリ（形状）」「物体の動き追跡」をすべて同時出力。シーンフロー推定や動く物体の自動分離にもゼロショットで対応します。

**解決された課題：**
4D再構成はこれまで数分〜数時間かかる最適化が必要でした。MoVieS はフィードフォワード推論で全工程を統合し、数桁の高速化を実現。スポーツ分析・AR撮影・ロボット知覚への即時応用が可能になります。

- **arXiv:** https://arxiv.org/abs/2507.10065
- **GitHub:** https://github.com/chenguolin/MoVieS

---

### 4DSurf — 動的シーンの「表面」精度を49%向上 `CVPR 2026`

**何ができるようになったか：**
人物や物体が激しく動いているシーンでも、表面形状（ジオメトリ）を高精度かつ時間的に一貫して再構成。大きな変形も複数セグメントに分けて段階的に処理することで対応します。

**解決された課題：**
従来の動的GSは「見た目はきれいだが形状が歪む」問題がありました。4DSurfはSDF（符号付き距離関数）フロー正則化でGaussianの動きを表面変化に合わせ、Chamfer距離で従来比49%/19%改善（Hi4D/CMU Panoptic）。

- **arXiv:** https://arxiv.org/abs/2603.28064

---

### EcoSplat — Gaussian数を自由にコントロールできる最初のフィードフォワードGS `CVPR 2026`

**何ができるようになったか：**
3D再構成に使うGaussianの数を「目標N個」と明示的に指定できる最初のフィードフォワードGS。入力画像が多くなっても爆発的にGaussianが増えず、同等品質を1/10のプリミティブ数で達成。

**解決された課題：**
フィードフォワードGSは入力枚数が増えると視点ごとにGaussianが生成され、不要な重複が発生していました。EcoSplatは重要度スコアリングで不要Gaussianを自動削減。RealEstate10K・ACIDで最高スコア。

- **arXiv:** https://arxiv.org/abs/2512.18692

---

### iLRM — 8枚入力で従来の2枚手法より高品質・計算コスト半減 `CVPR 2026`

**何ができるようになったか：**
多くの写真（8枚）を使いながら、従来の2枚入力手法より高品質な3D再構成を、計算時間は半分以下で実現。2段階アテンション機構で「全体→詳細」の情報統合を効率化。

**解決された課題：**
大規模な3D再構成モデルは入力枚数を増やすと計算量が爆発的に増大する問題がありました。iLRMは二段階のアテンションで多ビュー情報を効率処理し、GS-LRM・DepthSplatを約+3dB上回りながら計算時間は半減。

- **arXiv:** https://arxiv.org/abs/2507.23277
- **GitHub:** https://github.com/Gynjn/iLRM

---

### REALM — 自然言語でGSシーンを「探す・切る・編集する」AIエージェント `CVPR 2026`

**何ができるようになったか：**
「赤いソファを青に変えて」「窓を消して」など自然言語の指示だけで、3DGSシーン内の物体を自動で見つけ、切り抜き、置き換えや削除が可能。大規模3D特化の追加学習は不要。

**解決された課題：**
3DGSシーンの編集は専門知識が必要でした。REALMはMLLMエージェントが「全体俯瞰→拡大詳細セグメンテーション」の2段階で精度を確保し、物体除去・置換・スタイル変換をエンドユーザーが操作できるレベルに引き下げます。

- **arXiv:** https://arxiv.org/abs/2510.16410
- **GitHub:** https://github.com/ChangyueShi/REALM-Code

---

### NimbusGS — 霞・雨・雪の悪天候下でも鮮明な3DGS再構成 `CVPR 2026`

**何ができるようになったか：**
霞・雨・雪・それらの混合という4種の悪天候条件でも、正確な3DGS再構成が可能に。ペアデータや大規模事前学習も不要で、あらゆる天候に対してSoTAを達成。

**解決された課題：**
屋外撮影やドローン映像は天候の影響を強く受けますが、既存のGS手法はほぼ晴天前提。NimbusGSは「散乱光の体積的な減衰」と「浮遊粒子の動的残留」を物理モデルで個別に分解し、幾何形状の復元も同時に改善。

- **arXiv:** https://arxiv.org/abs/2603.27228
- **GitHub:** https://github.com/lyy-ovo/NimbusGS

---

### GaussianDWM — 自動運転の「理解」と「生成」を3DGSで統合 `CVPR 2026`

**何ができるようになったか：**
自動運転シーンの3D理解（物体認識・3D視覚接地・計画）と、マルチモーダルなシナリオ生成を1つの3DGSモデルで同時実現。言語特徴をGaussian primitiveに直接埋め込むことで早期モダリティ融合。

**解決された課題：**
既存の自動運転ワールドモデルは「理解」か「生成」の片方しかできず、3D空間の理解能力が欠如していました。GaussianDWMはNuInteract・OmniDriveでSoTA、nuScenesでの時空間生成でも最高性能。

- **arXiv:** https://arxiv.org/abs/2512.23180

---

### Uni3R — カメラ位置なしで3D再構成+言語理解を1パス `CVPR 2026 (Horizon Robotics)`

**何ができるようになったか：**
カメラ位置情報（ポーズ）なしに複数枚の画像から、高品質な3D再構成・セマンティックセグメンテーション・深度推定をすべて1パスで同時出力。RE10K PSNR 25.07、ScanNet mIoU 55.84で最高水準。

**解決された課題：**
3D再構成と意味理解は従来別々のパイプラインで、さらにカメラ位置の事前計算（SfM）が必要でした。Uni3RはCross-View Transformerで一気通貫の処理を実現。Horizon Roboticsによる開発。

- **arXiv:** https://arxiv.org/abs/2508.03643
- **GitHub:** https://github.com/HorizonRobotics/Uni3R

---

### DGGT — カメラ位置情報なしで自動運転4D再構成 `CVPR 2026 (Xiaomi Research)`

**何ができるようになったか：**
通常は「カメラがどこにあるか」を事前に計算（SfM）する必要がある4D動的シーン再構成を、位置情報なし（Unposed）のまま直接実現。カメラポーズ・Gaussian追跡・深度・動きマスク・空背景を1モデルから同時出力。

**解決された課題：**
自動運転向けの4D再構成は入力の前処理コストが高く、ゼロショット汎化も困難でした。DGGTはWaymo・nuScenes・Argoverse2でゼロショット最高性能を達成。Xiaomi Researchが開発。

- **arXiv:** https://arxiv.org/abs/2512.03004
- **GitHub:** https://github.com/xiaomi-research/dggt

---

### STAvatar — ブレた映像から高精細3Dヘッドアバター生成 `CVPR 2026`

**何ができるようになったか：**
手持ちスマホの動画（人物が動いてブレる映像）から、直接ハイクオリティな顔アバターを生成。耳・顎など頻繁に隠れる部分もきれいに復元し、4つのベンチマークで最高スコア。

**解決された課題：**
既存のGSアバター手法は「ブレのないシャープな映像」を前提としており、現実の撮影条件では使いにくい問題がありました。STAvatarはブレの物理モデル+UV空間での時間的密度制御で直接対処。

- **arXiv:** https://arxiv.org/abs/2511.19854

---

### SpeeDe3DGS — 動的3DGSをリアルタイムへ。13.71×高速・10×軽量 _(arXiv 2506.07917)_

**何ができるようになったか：**
人物・スポーツ・車両などの動的シーンをリアルタイムに近い速度でGS処理可能に。13.71×の高速化と1/10のGaussian数を達成しながら、画質は同等水準を維持。

**解決された課題：**
動的GS手法（DeformableGS等）はニューラルモーションフィールドが重くリアルタイム向きでない問題がありました。「時間的感度プルーニング」「グループSE(3)変換」の2モジュールで劇的に軽量化。

- **arXiv:** https://arxiv.org/abs/2506.07917
- **Project:** https://speede3dgs.github.io

---

### HRGS — 大規模高解像度シーンをGPU 23GBで鮮明に再構成 _(arXiv 2506.14229)_

**何ができるようになったか：**
街区・工場フロアなど広大かつ高解像度なシーンのGS再構成を、GPUメモリ23GBで既存最高PSNR（25.6dB）を達成。「粗いGaussianを全体に配置→ブロック分割して高精細化」の階層処理で実現。

**解決された課題：**
高解像度の大規模シーンをGSで再構成しようとするとGPUメモリが不足するか、品質が落ちるジレンマがありました。HRGSの階層戦略で両立。

- **arXiv:** https://arxiv.org/abs/2506.14229

---

## 📰 業界ニュース

### CVPR 2026 Denver — 世界最大CV学会がいよいよ開幕（6/3〜6/7）

コンピュータビジョン最大の国際学会 CVPR 2026 が今週デンバーで開幕。4,090論文が採択（前年比+42%）、うち3DGS関連が80本以上。FastGS（100秒学習）がHighlight筆頭、GLINTはOral採択。「4D World Modelsワークショップ」「2nd 4D Visionワークショップ」も6月3〜4日に同時開催。

- **公式サイト:** https://cvpr.thecvf.com/Conferences/2026
- **CVPR 2026 3DGS論文リスト:** https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

---

### KHR_gaussian_splatting — glTF国際標準の正式批准がQ2 2026内に確定

Khronos GroupのglTF向けGaussian Splatting拡張（KHR_gaussian_splatting）の正式批准がQ2 2026内（6月末まで）に予定。位置・向き・スケール・色（球面調和関数）・不透明度をglTFメッシュとして保存する仕様が確定すれば、すべてのglTF対応ビューア・エンジンでGSが自動表示可能に。

- **Khronos公式:** https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release
- **GitHub仕様:** https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_gaussian_splatting

---

### 3DCoat 2026 安定版 — GPU加速テクスチャリングを6月リリース

3DモデリングツールのPilgwayが3DCoat 2026安定版を6月リリース。GPU加速ノードベーステクスチャリングシステムでスマートマテリアルの大幅な高速化を実現。3DCoatTextura 2026も同時リリース。GS再構成後のテクスチャ品質向上ワークフローに直結。

- **CG Channel:** https://www.cgchannel.com/2026/06/pilgway-releases-3dcoat-2026-and-3dcoattextura-2026/

---

## 💬 コミュニティ・SNS話題

### CVPR 2026「4D World Modelsワークショップ」— 生成と再構成の架け橋

Brown Universityが主催する「4D World Models: Bridging Generation and Reconstruction」ワークショップが6月3日開催。4DGS・NeRF・ラジアンスフィールドを使った動的3D世界の生成と再構成を統合するテーマで、VR/AR・ロボティクス向け応用が中心議題。

- https://ivl.cs.brown.edu/4dworldmodels/

---

### CVPR 2026「2nd 4D Visionワークショップ」— 4Dビジョン研究の最前線

6月4日午後に開催される4Dビジョン専門ワークショップ。NeRF・GS・スパシオテンポラル表現の最新研究が集まり、4D再構成の現在地を見渡せる場。

- https://4dvisionworkshop.github.io/

---

### gsplat HiGS推論パス — 公式ライブラリに高速推論モードが追加

nerfstudio/gsplatにHiGS（階層的GS）ベースの推論専用パスが実験的追加。fp16データパッキング＋マクロタイル融合ラスタライゼーションにより、本番環境での低遅延GSレンダリングが可能に。

- https://github.com/nerfstudio-project/gsplat

---

### HoliGS — 長尺動画からEmbodied AIが動く環境を丸ごとGS化 _(arXiv 2506.19291)_

ロボットが歩き回りながら撮影した数分の動画から、背景（静的）＋各オブジェクト（動的・関節あり）をGaussianで分解・再構成。骨格駆動アーティキュレーション＋非剛体変形を可逆ニューラルフローで統合。ロボット操作向けワールドモデルとして活用可能。

- https://arxiv.org/abs/2506.19291

---

## 🛠️ 開発者向けインサイト

1. **今週のGitHub Watch推奨：** GLINT / iLRM / MoVieS / NimbusGS / DGGT / REALM — CVPR 2026で今週コード公開予定
2. **透明物体対応が本格化：** GLINTによりガラス・水面・眼鏡などの透明素材3DGS化が実用圏に。建築・小売・文化財アーカイブへの展開が加速
3. **動的GS高速化のマイルストーン：** SpeeDe3DGS（13.71×高速化）によりモバイル・エッジデバイスへの動的GSデプロイが現実的に
4. **KHR_gaussian_splatting：** 今月中の正式批准に備えてglTFエクスポート対応の準備推奨
5. **gsplat HiGS推論パス：** 本番推論コスト削減のため `--use_gaussian_render_inference_scene` フラグで即ベンチマーク可能

---

*レポート生成：2026-06-01 | リポジトリ: yozzzo/Daily-news*
