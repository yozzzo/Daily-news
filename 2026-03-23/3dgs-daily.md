# 3DGS & 4D生成 デイリーレポート

**日付:** 2026年3月23日（日）
**対象分野:** 3D Gaussian Splatting / 4D生成 / 動的3Dシーン
**対象地域:** 英語圏 / 日本 / 中国 / ヨーロッパ

---

## 今日の注目トレンド

| 順位 | トレンド | 概要 |
|:---:|:---|:---|
| 1 | CVPR 2026に4本採択 | 3DGSの応用範囲が「表面復元」「群衆3D化」「空間認識」「言語検索」に拡大 |
| 2 | スマホでも高品質3D表示 | Matryoshka GSで1つのモデルから全デバイス対応が可能に |
| 3 | 自動運転の仮想空間が進化 | WorldSplat等で道路映像から4D仮想空間を自動生成 |
| 4 | 業界標準化が始動 | Khronos GroupがglTFに3DGSを統合予定 |
| 5 | ゲームエンジンで4倍高速 | NanoGSプラグインでUE5での3DGS表示が4倍以上に |
| 6 | ロボットが空間を記憶 | GSMemでロボットが3DGSで空間を記憶し自律探索 |
| 7 | 都市まるごとデジタルツイン | サンノゼ市全体をリアルタイム3D化、NVIDIA NuRecも正式リリース |

---

## 論文（22件）

### 1. Matryoshka Gaussian Splatting (MGS) — 1つのモデルで全デバイス対応

**分野:** 3DGS最適化 | **重要度:** 高

1つの3Dモデルから「超高画質〜超軽量」まで自由に品質を切り替えられるようになった。これまではスマホ用・PC用と別々にモデルを作る必要があったが、1つのモデルで全デバイスに対応可能に。既存の仕組みを変えずに導入できる点も実用的。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19234)

---

### 2. GSPrior — AIが物体の表面を正確に復元 [CVPR 2026]

**分野:** 表面復元 | **重要度:** 高

写真から3Dモデルを作る際、物体の「表面」をより正確に再現できるようになった。従来の手法では表面がガタガタになりがちだったが、AIが自動で滑らかで正確な表面を推定してくれる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19682)

---

### 3. OnlinePG — ロボットが空間を自動認識して3D地図を作成 [CVPR 2026]

**分野:** 空間認識 | **重要度:** 高

ロボットが部屋の中を見回すだけで「ここはテーブル、あれは椅子」と物体を自動認識しながら3D地図を作れるようになった。しかも学習していない物体でも言葉で指定すれば見つけられる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19193)

---

### 4. CrowdGaussian — 1枚の写真から群衆全員を3D化 [CVPR 2026]

**分野:** 人物復元 | **重要度:** 高

1枚の写真から、写っている群衆全員をそれぞれ独立した3Dモデルとして復元できるようになった。これまでは1人ずつしかできなかったが、渋谷のスクランブル交差点のような混雑シーンでも対応可能に。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=CrowdGaussian)

---

### 5. ReLaGS — 言葉で3D空間を検索 [CVPR 2026]

**分野:** 言語+3D | **重要度:** 高

3D空間の中で「赤いソファの隣にある本棚」のように、言葉で物体の位置関係を指定して検索・認識できるようになった。3Dシーンを言葉で操作する未来に一歩近づいた。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=ReLaGS)

---

### 6. StreetForward — 走行映像から街並みをリアルタイム3D化

**分野:** 自動運転 | **重要度:** 高

走行中の車のカメラ映像から、歩行者や他の車など動くものも含めた街並みの3Dシーンをリアルタイムに再構築できるようになった。自動運転の安全性テストに活用できる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19552)

---

### 7. GSMem — ロボットが空間を「記憶」して自律探索

**分野:** ロボットAI | **重要度:** 高

ロボットが探索した空間を3DGSで「記憶」し、まだ見ていない角度からの景色も想像できるようになった。初めて訪れる場所でも、過去の記憶を活用して効率的に探索・判断できる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19137)

---

### 8. RetimeGS — 4D動画のスロー再生・早送りを自在に

**分野:** 4DGS | **重要度:** 高

動画から作った4D（時間+3D）シーンの再生速度を自由に変えられるようになった。スローモーションや早送りを、映像が破綻することなく滑らかに実現。映画やスポーツ分析に応用可能。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.13783)

---

### 9. SpatioGS — 動きのあるシーンを効率的に3D化

**分野:** 4DGS | **重要度:** 高

動きのあるシーン（人が歩く、車が走るなど）を3D化する際に、「時間と空間の両方」を考慮して最適な密度で描画する新手法。動きの激しい部分をより精密に、静止部分は効率的に処理。

**ソース:**
- [Springer論文](https://link.springer.com/article/10.1007/s00371-026-04442-w)

---

### 10. WorldSplat — 道路映像から4D仮想空間を自動生成

**分野:** 4DGS/自動運転 | **重要度:** 高

実際の道路映像から「時間の流れも含む4D仮想空間」を自動生成できるようになった。自動運転の学習データを大量に作り出せるため、実車テストを減らしてコストと安全性を改善できる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2509.23402)

---

### 11. ReconDrive — 自動運転用4D再構築を大幅高速化

**分野:** 4DGS/自動運転 | **重要度:** 高

自動運転用の道路シーンを、従来より大幅に高速に4D再構築できるようになった。リアルタイムに近い速度で仮想空間を構築でき、シミュレーションの効率が飛躍的に向上。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.07552)

---

### 12. 3D-REGEN — 写真1枚から数秒で編集可能な3Dモデル

**分野:** 3D生成 | **重要度:** 高

写真1枚から数秒で、回転させたり編集したりできる高精度な3Dモデルを自動生成できるようになった。ECサイトの商品3D化やゲーム素材の量産に革命的。

**ソース:**
- [Note.com 日本語解説](https://note.com/toshia_fuji/n/na6249ffcc81d)

---

### 13. Fourier Splatting — より効率的な大規模シーン描画

**分野:** 新表現手法 | **重要度:** 中

3Dシーンを描画する際の基本的な「粒」の表現方法を改良し、より効率的に大規模なシーンを描画できるようにした。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19834)

---

### 14. HUGE-Bench — ドローンAI操縦のテスト環境

**分野:** ドローン | **重要度:** 中

ドローンのAI操縦を評価するためのテスト環境を構築。3DGSで作った実在都市のデジタルツイン上で、ドローンが障害物を避けながら目的地に行けるかなどを検証できる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.19822)

---

### 15. GHOST — 手の動きを高速3D再現

**分野:** 手と物体 | **重要度:** 中

人が物を掴んだり操作したりする動作を、普通のカメラ映像から高速に3D再現できるようになった。VRやロボットの操作学習に活用できる。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=GHOST+Gaussian)

---

### 16. AHOY! — YouTube動画から人物を完全3D化

**分野:** 人物アニメーション | **重要度:** 中

YouTube動画に映っている人物を、他の物に隠れている部分も含めて完全な3Dモデルとして復元し、自由にポーズを変えられるようになった。

**ソース:**
- [プロジェクトページ](https://miraymen.github.io/ahoy/)

---

### 17. Splat2BEV — 自動運転車の鳥瞰図を高精度化

**分野:** 自動運転 | **重要度:** 中

自動運転車が周囲の状況を「真上から見た地図」として正確に把握できるようになった。3DGSを使うことで、従来より正確な鳥瞰図を生成。

**ソース:**
- [プロジェクトページ](https://vulab-ai.github.io/Splat2BEV/)

---

### 18. 月面マッピング with 3DGS — 月の地形をリアルタイム3D化

**分野:** 宇宙 | **重要度:** 中

月面探査ロボットが撮影した画像から、月の地形をリアルタイムに3Dマップ化できるようになった。将来の月面基地建設の計画立案に役立つ。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=Lunar+Gaussian+Splatting)

---

### 19. Polynomial Kernels for GS — 描画品質の改良

**分野:** 最適化 | **重要度:** 中

3DGSの描画品質を、内部の計算方法（カーネル）を改良することで向上させた。同じデータでもより綺麗に表示できるようになる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.18707)

---

### 20. SRGS — 低解像度3DGSを高解像度に変換

**分野:** 超解像 | **重要度:** 中

低解像度の3DGSモデルを高解像度に変換できるフレームワーク。少ないデータからでも高品質な3Dシーンを作れるようになった。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2404.10318)

---

### 21. UniSem — 少数の写真から意味を理解して3D復元

**分野:** 意味理解 | **重要度:** 中

少数の写真から、カメラ位置の情報なしでも「ここは壁、ここは床」と意味を理解しながら3D空間を復元できるようになった。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=UniSem+Gaussian)

---

### 22. SMAL-pets — 犬の写真1枚からリアルな3Dアバター

**分野:** 動物3D化 | **重要度:** 中

犬の写真1枚から、自由にポーズを変えられるリアルな3Dアバターを作れるようになった。ペットのデジタルフィギュアやゲームキャラクターへの応用が期待される。

**ソース:**
- [arXiv検索](https://arxiv.org/search/?query=SMAL-pets)

---

## 業界ニュース（10件）

### 1. Voxelmaps: サンノゼ市のリアルタイム都市デジタルツイン

サンノゼ市全体を3DGSで丸ごとデジタルコピーし、リアルタイムに更新される「都市のデジタルツイン」が実現。都市計画や災害シミュレーションに活用される。

**ソース:**
- [USA Today](https://www.usatoday.com/press-release/story/28507/voxelmaps-launches-real-time-city-digital-twin-for-san-jose-powered-by-nvidia-ai/)

### 2. Khronos Group: 3DGSデータのglTF標準化を推進

3Dデータの世界標準フォーマット「glTF」に3DGSが統合される予定。異なるソフトウェアやプラットフォーム間で3DGSデータを自由にやり取りできるようになる。

**ソース:**
- [Khronos Group](https://www.khronos.org/events/gaussian-splats-use-cases-next-steps-for-gltf-standardization)

### 3. NanoGS: UE5で3DGSを4倍速く表示する無料プラグイン

ゲームエンジンUnreal Engine 5で3DGSを高速表示できる無料プラグインが登場。ミドルクラスのGPUでもフレームレートが4倍以上に。映画VFX大手DNEGも高く評価。

**ソース:**
- [CG Channel](https://www.cgchannel.com/2026/03/free-plugin-nanogs-puts-nanite-style-gaussian-splatting-in-unreal-engine/)
- [GitHub](https://github.com/TimChen1383/NanoGaussianSplatting)

### 4. NVIDIA Omniverse NuRec 正式リリース

NVIDIAの3D開発プラットフォーム「Omniverse」のNuRecが正式版に。センサーデータから3DGSを使ったシミュレーション環境を自動構築できる。

**ソース:**
- [MEXC News](https://www.mexc.co/en-IN/news/955733)

### 5. LichtFeld-Studio: 3DGS統合ワークステーション（OSS）

3DGSの学習・確認・編集・書き出しを1つのアプリで完結できるオープンソースツールが公開。

**ソース:**
- [GitHub](https://github.com/MrNeRF/LichtFeld-Studio)

### 6. VentureBeat: AIが物理世界を理解する3つの方法にGSを紹介

大手テックメディアが「AIが物理世界を理解する3つの方法」の1つとしてGaussian Splattingを特集。

**ソース:**
- [VentureBeat](https://venturebeat.com/technology/three-ways-ai-is-learning-to-understand-the-physical-world)

### 7. France TV: 映画制作を変革するリアルタイム3D

フランスの公共放送がGaussian Splattingを「映画制作を変革する技術」として紹介。

**ソース:**
- [France TV](https://www.francetelevisions.fr/et-vous/le-lab/en/open-innovation/real-time-3d-is-revolutionising-filmmaking-53885)

### 8. Connect Tech: エッジAIでデジタルツインを自動構築

現場のカメラ映像からリアルタイムにデジタルツインを自動構築するワークフローをデモ。

**ソース:**
- [Connect Tech](https://connecttech.com/connect-tech-ctai-labs-demo-deployable-physical-ai-workflow/)

### 9. 欧州投資家がGaussian Splatting関連スタートアップに注目

欧州の投資家がGaussian Splatting技術を活用するスタートアップに積極投資。

**ソース:**
- [The Robot Report](https://www.therobotreport.com/investor-makes-case-europe-new-frontier-physical-ai/)

### 10. 中国・峰瑞資本が3DGS関連ハードウェアスタートアップに出資

中国のVCファンドが3DGS技術を活用したインテリジェントハードウェアのスタートアップに出資。

**ソース:**
- [36Kr](https://eu.36kr.com/en/p/3734855815184390)

---

## コミュニティ・SNS話題（8件）

- **Reddit r/GaussianSplatting:** データ削減ツールの議論が活発
- **GitHub NanoGS:** UE5向け高速3DGSレンダラーがトレンド入り
- **Twitter/X KIRI Engine:** スマホで3Dスキャン→メッシュ変換
- **TikTok:** 3DGSでデジタルツインを作る動画がバズり中
- **Instagram SXSW 2026:** 4Dボリュメトリック映像のデモが話題
- **Facebook DeoVR:** VRプラットフォームが3DGS対応を予告
- **GitHub fast-gaussian-rasterization:** 高速描画エンジンがトレンド入り
- **Note.com:** 3D-REGENとRetimeGSの日本語解説記事が公開

---

*この情報は毎朝自動で収集・配信されます。*
