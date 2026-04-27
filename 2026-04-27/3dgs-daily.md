# 3DGS & 4D生成 デイリーレポート — 2026-04-27

> **収集日**: 2026年4月27日  
> **対象期間**: 直近7日間（2026年4月20日〜27日）  
> **新規項目数**: 25件（論文9件 / 業界ニュース8件 / コミュニティ・SNS5件 / 開発者向け3件）

---

## 📌 今日の注目トレンド

1. **Splatica × Insta360 × The Verge** — 360度カメラ1台で誰でも3D世界を作れる時代が本格到来
2. **NVIDIA Asset Harvester** — 自動運転ログから3D Gaussian Splatアセットを自動生成、シミュレーション革命
3. **V-Ray 7.3 for 3ds Max** — 業界標準レンダラーがGaussian Splatの「ライト再照明」に対応
4. **YOGO（You Only Gaussian Once）** — 研究から製品レベルへ：予算制御付きの決定論的3DGSフレームワーク
5. **PlayCanvas SplatTransform** — Gaussian Splatをそのままブラウザゲームに変換できるCLIツール登場

---

## 🔬 注目論文（重要度：高）

### 1. YOGO（You Only Gaussian Once）
- **ソース**: [arXiv:2604.21400](https://arxiv.org/abs/2604.21400) | 2026年4月23日
- **分野**: 3DGS最適化・本番環境対応
- **概要**: これまでの3DGSは研究用プロトタイプにとどまり、実際の製品に使うには「どれだけメモリを使うか予測できない」「複数センサーのデータが混在するとノイズが出る」という問題がありました。YOGOはこれを解決するシステムレベルのフレームワークで、**ガウシアンの増加を確率的ではなく決定論的・予算制御式に管理**します。また、超高密度な室内データセット「Immersion v1.0」を公開し、業界標準ベンチマークの「疎すぎる問題」を打破。コードとデータセットの一部は公開済み。
- **何が変わるか**: 「研究室では動くが製品では使えない」という3DGSの最大の壁を突破する可能性。

### 2. WildSplatter
- **ソース**: [arXiv:2604.21182](https://arxiv.org/abs/2604.21182) | 2026年4月23日
- **分野**: フィードフォワード3DGS・野外写真対応
- **概要**: 従来の3DGSは「カメラの位置が既知」「照明が一定」という条件が必要でした。WildSplatterは**カメラパラメータ不明・照明バラバラな野外写真コレクションから1秒以内に3Dシーンを再構成**できます。旅行写真やSNS投稿など、条件が揃っていない写真群から3D化が可能になります。
- **何が変わるか**: 「撮影条件を整えなくても3D化できる」ため、一般ユーザーの写真からの3D生成が現実的に。

### 3. Gaussians on a Diet（高品質メモリ制約付き3DGS学習）
- **ソース**: [arXiv:2604.20046](https://arxiv.org/abs/2604.20046) | 2026年4月21日
- **分野**: エッジデバイス対応・メモリ効率化
- **概要**: 3DGSの学習には大量のメモリが必要で、特に学習初期に「ガウシアンが急増してメモリが爆発する」問題がありました。本手法は**増分プルーニングと適応的補償を交互に行う動的フレームワーク**で、ピークメモリを最大80%削減。NVIDIA Jetson AGX Xavier（組み込みAI向け小型ボード）での学習を実現。
- **何が変わるか**: スマホ・ドローン・ロボットなどの小型デバイスでも3DGS学習が可能になる。

### 4. DualSplat
- **ソース**: [arXiv:2604.21631](https://arxiv.org/abs/2604.21631) | 2026年4月23日
- **分野**: 3DGSロバスト性向上
- **概要**: 人や車など「一時的に映り込む物体」が含まれる画像で3DGSを学習すると、品質が著しく低下する問題がありました。DualSplatは**「再構成の失敗」から逆に疑似マスクを生成する「Failure-to-Prior」パラダイム**を採用し、動的物体を自動的に除外。現実世界の雑然とした環境での3D化精度が大幅向上。
- **何が変わるか**: 街中や人混みでの3D再構成が実用レベルに。

### 5. GraphiXS（Graphical X Splatting）
- **ソース**: [SIGGRAPH 2026論文](https://www.youtube.com/watch?v=a2U9OiMGczQ) | 2026年4月
- **分野**: 4DGS・不確実性モデリング
- **概要**: 4D Gaussian Splatting（動く3Dシーン）における不確実性を**グラフィカルモデル（確率的グラフ構造）**で明示的に扱う新手法。動的シーンの「どこが信頼できてどこが不確かか」を定量化できるようになります。SIGGRAPH 2026採択。
- **何が変わるか**: 4DGSの信頼性・品質評価が可能になり、映像制作・医療・自動運転での応用が広がる。

### 6. WorldStereo（CVPR 2026）
- **ソース**: [GitHub](https://github.com/FuchengSu/WorldStereo) | 2026年4月24日（arxiv更新）
- **分野**: 動画生成×3D再構成
- **概要**: Tencent Hunyuanが開発した**カメラ制御付き動画生成と3D再構成を橋渡しするフレームワーク**。1枚の画像から多視点一貫した動画を生成し、そこからGaussian Splatを含む3D点群を再構成。HY-World 2.0のWorldMirrorと連携。CVPR 2026採択、コード公開済み（スター148）。
- **何が変わるか**: 写真1枚から高品質な3D世界を生成するパイプラインが実用化。

### 7. Splatography（映画制作向け疎多視点動的GS）
- **ソース**: [arXiv:2511.05152v2](https://arxiv.org/html/2511.05152v2) | 2026年4月20日（v2更新）
- **分野**: 4DGS・映画制作
- **概要**: 映画撮影現場では「カメラが少ない」「動きが速い」「テクスチャが難しい」という課題があります。Splatographyは**疎な多視点動的Gaussian Splatting**でこれらの映画制作特有の課題を解決。RTD（リアルタイム動的）テクスチャにも対応。
- **何が変わるか**: 少ないカメラ台数でも映画品質の動的3Dシーン再構成が可能に。

### 8. CryoSplat（ICLR 2026）
- **ソース**: [GitHub](https://github.com/Chen-Suyi/cryosplat) | 2026年4月（ICLR 2026）
- **分野**: 科学応用・クライオ電子顕微鏡
- **概要**: クライオ電子顕微鏡（cryo-EM）は**タンパク質の3D構造を解析する医療・創薬の核心技術**ですが、再構成に時間がかかる問題がありました。CryoSplatはGaussian Splatting kernelをcryo-EM再構成に適用し、CryoDRGNベースのパイプラインに統合。ICLR 2026採択。
- **何が変わるか**: 創薬・医療分野でのタンパク質3D構造解析が高速化・高精度化。

### 9. MS-Splatting（マルチスペクトルGaussian Splatting）
- **ソース**: [Computer Graphics Forum](https://onlinelibrary.wiley.com/doi/10.1111/cgf.70337) | 2026年4月25日
- **分野**: マルチスペクトル・赤外線対応
- **概要**: これまでの3DGSは可視光のみ対応でしたが、MS-Splattingは**可視光と赤外線など不可視スペクトルを統合した多視点一貫再構成**を実現。農業・医療・セキュリティなど、可視光外の情報が重要な分野への応用が開けます。
- **何が変わるか**: 「見えない光」で撮影したデータも3D化できるようになる。

---

## 📰 業界ニュース

### 10. Splatica × Insta360 パートナーシップ（The Verge報道）
- **ソース**: [The Verge](https://www.theverge.com/tech/914730/splatica-gaussian-splats-insta360-antigravity) | 2026年4月24日
- **概要**: 英国スタートアップSplaticaとInsta360が提携。**360度カメラで動画を撮影してアップロードするだけで、翌日には3D Gaussian Splatの仮想空間が完成**するサービスを提供。The Vergeが実際に自宅の庭を3D化してレビュー。不動産・工場・文化財保存など幅広い用途に対応。料金は動画1秒あたり18〜25セント＋月額サブスクリプション。
- **重要度**: ★★★★★（一般消費者向け3DGS普及の転換点）

### 11. Antigravity「Project ETERNAL」発表
- **ソース**: [PR Times](https://prtimes.jp/main/html/rd/p/000000148.000052813.html) / [Petapixel](https://petapixel.com/2026/04/24/antigravity-is-preserving-historical-sites-in-3d-using-its-360-drone/) | 2026年4月23日
- **概要**: Insta360の支援を受けたAntigravityが**世界遺産・文化財を3D Gaussian Splattingで永久保存するグローバルプロジェクト「Project ETERNAL」**を発表。ポンペイ、チヴィタ・ディ・バニョレージョ（イタリア）などを対象に高精度3Dモデルを構築。1,000件の無料アップロード枠を提供。
- **重要度**: ★★★★（文化財保存×3DGSの社会的インパクト）

### 12. Chaos V-Ray 7 Update 3（3ds Max）— Gaussian Splat再照明対応
- **ソース**: [CG Channel](https://www.cgchannel.com/2026/04/chaos-releases-v-ray-7-update-3-for-3ds-max/) | 2026年4月23日
- **概要**: 業界標準レンダラーV-Rayが3ds Max向けにUpdate 3をリリース。**3D Gaussian Splatオブジェクトにシーン内のライトが当たり、再照明（relight）が可能**になりました。アニメーションSplatにも対応。さらにAMD GPUサポートが8年ぶりに復活。
- **重要度**: ★★★★（プロダクションパイプラインへの本格統合）

### 13. NVIDIA Asset Harvester — 自動運転ログから3Dアセット自動生成
- **ソース**: [NVIDIA Research](https://research.nvidia.com/labs/sil/projects/asset-harvester/) / [GitHub](https://github.com/nvidia/asset-harvester/) | 2026年4月21日
- **概要**: NVIDIAが**自動運転車の走行ログ動画から車・歩行者・道路物体の3D Gaussian Splatアセットを自動生成するパイプライン「Asset Harvester」**をオープンソース公開。疎な視点からでも重遮蔽・ノイズに対応し、数秒でシミュレーション用3Dアセットを生成。NVIDIAのNCore・NuRecと直接連携。
- **重要度**: ★★★★★（自動運転シミュレーションの効率化に直結）

### 14. Pixotope × Volinga — ライブ放送向け3DGS統合（NAB 2026）
- **ソース**: [LinkedIn](https://www.linkedin.com/posts/pixotope_nab-2026-pixotope-integrates-volinga-3d-activity-7451914490801184768-vmSR) | 2026年4月21日
- **概要**: バーチャルプロダクションソフトウェアPixotopeがNAB 2026にて**Volinga経由で3D Gaussian Splatting対応を発表**。実際の場所をスキャンして数時間で放送対応の仮想セットを構築できるようになります。スポーツ中継・ニュース番組での活用を想定。
- **重要度**: ★★★★（テレビ放送制作への3DGS本格参入）

### 15. Laval Virtual 2026 — 4DGS特集レポート
- **ソース**: [3DVF](https://3dvf.com/en/redaction/laval-virtual-2026-gaussian-splats-motion-capture-innovations-and-an-industry-in-transition/) | 2026年4月24日
- **概要**: フランスのXR業界イベント「Laval Virtual 2026」で4D Gaussian Splattingが特集。**モーションキャプチャとの統合、プロフェッショナル用途での実用化事例**が多数紹介され、XR業界の転換点として報道。
- **重要度**: ★★★（欧州XR業界での4DGS普及状況）

### 16. DroneDeploy Gaussian Splats ベータ公開
- **ソース**: [DroneDeploy Help](https://help.dronedeploy.com/hc/en-us/articles/36102714208023-Gaussian-Splats) | 2026年4月20日
- **概要**: 建設・農業向けドローン測量プラットフォームDroneDeployが**Aerial Proサブスクライバー向けにGaussian Splatsベータ機能を公開**。ドローン空撮から光リアルな3Dビューを生成し、建設現場レビューに活用できます。
- **重要度**: ★★★（建設・測量業界への3DGS普及）

### 17. KIRI Engine 4.2 — 3DGS to Mesh 3.0リリース
- **ソース**: [X (@KIRI_Engine_App)](https://x.com/KIRI_Engine_App/status/2046882453919236253) | 2026年4月22日
- **概要**: スマホ3DスキャナーアプリKIRI Engineが4.2をリリース。目玉は**3DGS to Mesh 3.0**で、「細い構造物はスキャンできない」という常識を覆し、花・ケーブル・椅子の脚などの薄い構造物の変換に対応。処理速度も約20%向上。
- **重要度**: ★★★★（3DGSのメッシュ変換品質の大幅改善）

---

## 💬 コミュニティ・SNS話題

### 18. PlayCanvas SplatTransform — Gaussian Splatをゲームに変換するCLIツール
- **ソース**: [PlayCanvas Blog](https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/) | 2026年4月22日
- **概要**: PlayCanvasエンジニアが**Gaussian Splatをブラウザで動くFPSゲームに変換する完全チュートリアル**を公開。`splat-transform` CLIツールを使い、衝突判定・ライティング・NPCナビゲーションまで実装。Hacker Newsでも話題に。
- **重要度**: ★★★★（ゲーム開発者向け実用ツール）

### 19. VRChat Gaussian Splatting — SH3対応アップデート
- **ソース**: [lileaLab](https://lilea.net/lab/how-to-use-vrchat-gaussian-splatting/) | 2026年4月25日
- **概要**: VRChatのGaussian Splatting対応（MichaelMoroz製）が**2026年4月アップデートでSH3（球面調和関数3次）に対応**。これにより、より高品質な照明表現でGaussian SplatをVRChatワールドに持ち込めるようになりました。日本語コミュニティでも活発に活用中（鳥取・米子城跡VRなど）。
- **重要度**: ★★★（VRコミュニティへの3DGS普及）

### 20. 360度動画→Gaussian Splat仮想ツアー検証レポート（Reddit）
- **ソース**: [Reddit r/GaussianSplatting](https://www.reddit.com/r/GaussianSplatting/comments/1swgi22/i_tested_360_video_to_gaussian_splat_virtual/) | 2026年4月27日
- **概要**: ユーザーが**360度動画からGaussian Splat仮想ツアーを生成するSpatial Studio（Real Horizons）を実際に検証**したレポートを投稿。「360度動画→Splat生成→仮想ツアー化」のフローが驚くほど簡単になったと話題。
- **重要度**: ★★★（実用ワークフローの普及）

### 21. AirVis — スマホで大規模Gaussian Splatシーンを表示
- **ソース**: [Reddit r/GaussianSplatting](https://www.reddit.com/r/GaussianSplatting/comments/1swjzqd/some_large_gaussian_splat_scenes_scanned_from/) | 2026年4月27日
- **概要**: AirVisアプリを使い、**スマホ数台で撮影した大規模Gaussian Splatシーンをスマホ・MacBook・Quest・Vision Proなど複数デバイスで閲覧**できることを実証したデモが投稿。クロスプラットフォーム対応の実用性が注目。
- **重要度**: ★★★（クロスデバイス3DGS閲覧の普及）

### 22. Gaussian Splatting for VFX — 業界向け解説記事
- **ソース**: [CG Lounge Studio](https://cglounge.studio/journal/gaussian-splatting-for-vfx) | 2026年4月22日
- **概要**: VFXアーティスト向けに**Houdini・Nuke・USDパイプラインへのGaussian Splatting統合方法**を詳解した記事。「2026年初頭時点でNuke 17がネイティブ対応、Houdini 21がテクニカルプレビュー、OpenUSD 26.03が対応済み」という現状を整理。Redditのr/vfxでも話題。
- **重要度**: ★★★★（VFX業界での実用化状況の整理）

---

## 🛠️ 開発者向けインサイト

### 23. Dehaze-then-Splat — 煙・霧のある環境での3DGS
- **ソース**: [arXiv:2604.13589v3](https://arxiv.org/html/2604.13589v3) | 2026年4月23日
- **分野**: ロバスト3DGS・悪条件対応
- **概要**: 火災現場・霧の多い屋外・工場内など**煙や霧がある環境では3DGSの品質が著しく低下**していました。Dehaze-then-Splatは生成的デヘイジング（霧除去）と物理インフォームドGaussian Splatting学習を組み合わせた2ステージパイプライン。NTIRE 2026チャレンジ Track 2向けに開発。
- **活用場面**: 消防・防災・工場監視・悪天候下の自動運転

### 24. PropSplat — 電波伝搬マップの3DGS化（IEEE DySPAN 2026）
- **ソース**: [IEEE DySPAN 2026](https://dyspan2026.ieee-dyspan.org/main-conference-technical-program) | 2026年4月
- **分野**: 無線通信・RF場再構成
- **概要**: 3D Gaussian Splatting技術を**無線電波（RF）の伝搬場の再構成**に応用。地図不要でRF場を3Dモデル化できるため、5G基地局配置最適化・屋内測位・電波干渉解析などに活用できます。
- **活用場面**: 通信インフラ設計・スマートビルディング・IoT

### 25. XGRIDS 3DGS無料ウェビナー（4月28日開催）
- **ソース**: [PR Times](https://prtimes.jp/main/html/rd/p/000000011.000093846.html) | 2026年4月21日
- **概要**: XGRIDS社が**「3DGSって何ができる？」をテーマにした無料ウェビナーを4月28日に開催**。3DGSの基礎から実務活用シーン、スキャンから3DGS生成までのフローを解説。日本語で3DGSを学べる貴重な機会。
- **活用場面**: 3DGS入門者・業務活用を検討中の企業

---

## 📊 今週のトレンドサマリー

| カテゴリ | 件数 | 主なキーワード |
|---|---|---|
| 論文（arXiv・学会） | 9件 | YOGO, WildSplatter, Gaussians on a Diet, DualSplat, GraphiXS, WorldStereo, Splatography, CryoSplat, MS-Splatting |
| 業界ニュース | 8件 | Splatica, Project ETERNAL, V-Ray 7.3, NVIDIA Asset Harvester, Pixotope, Laval Virtual, DroneDeploy, KIRI Engine |
| コミュニティ・SNS | 5件 | PlayCanvas SplatTransform, VRChat SH3対応, 360度仮想ツアー, AirVis, VFX解説記事 |
| 開発者向け | 3件 | Dehaze-then-Splat, PropSplat, XGRIDSウェビナー |

---

*このレポートは自動収集・AI要約により作成されています。各リンクは収集時点で有効であることを確認済みです。*
