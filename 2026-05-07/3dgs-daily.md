# 3DGS/4DGS デイリーレポート｜2026年5月7日（木）

**収集件数：22件**（論文13件・ニュース5件・コミュニティ/ツール4件）  
重複排除済み（`past_3dgs.json` と照合）

---

## 🔥 今日の注目トレンド（Top 5）

1. **Adobe PhotoshopにGS採用** — Photoshop 27.6の「Rotate Object」が内部でGaussian Splattingを活用。2D画像を3D的に回転・合成可能に。一般ユーザーへのGS普及における最大の転換点。
2. **4DGSブラウザ完全ストリーミング時代へ** — DNE×Graciaが4分間の音楽パフォーマンスをブラウザ直接再生で公開。アプリ不要・全デバイス対応。
3. **Cesium 3D Tiles×GS LoD統合** — Microsoftレドモンドキャンパス1億1千万Splatをブラウザでリアルタイムストリーミングするデモが公開。都市スケールのGSが実運用レベルへ。
4. **GETA-3DGS** — GSシーン（数GB）を自動で小さくしつつ品質を保つ初のエンドツーエンド圧縮手法。モバイル・VR展開の壁を突破。
5. **FreeTimeGS++** — 4DGS（動的3D）がなぜ上手くいくのかを初めて体系的に解明。動きの本質的なメカニズムを解析し、より安定・高品質な4DGS基盤を提案。

---

## 📚 注目論文

### 重要度：高

#### 1. GETA-3DGS — 自動プルーニング＋量子化でGSを激小化
- **arXiv**: https://arxiv.org/abs/2605.02086
- **投稿日**: 2026年5月3日
- **分野**: 圧縮・最適化

**何ができるようになったか**  
3DGSシーン1つが数百MB〜数GBと巨大だった問題を解決。不要なGaussian点を自動で間引き（プルーニング）しながら、各属性の数値精度も自動で下げる（量子化）処理を一括自動化。手作業なしで任意のシーンを大幅圧縮できる初の汎用フレームワーク。

**これまでの課題と解決策**  
これまでの圧縮手法はプルーニング・量子化・エントロピー符号化を別々に実施し、現場合わせの調整が必要だった。GETA-3DGSは「レンダリング品質×送受信効率×各Gaussian点の重要度」を統合評価する量子化対応依存グラフ（QADG）を新設計し、自動最適化を実現。

---

#### 2. 2D-SuGaR — CAD品質のメッシュを3DGSから自動生成
- **arXiv**: https://arxiv.org/abs/2605.00569
- **投稿日**: 2026年5月1日
- **分野**: 表面再構成・メッシュ変換

**何ができるようになったか**  
複数視点の画像から幾何学的に正確な3Dメッシュを自動生成。2D Gaussian Splattingに奥行き・法線の事前知識を組み込み、DTUベンチマークでSoTAを達成。3Dスキャン→3Dプリント・ゲームエンジン向けモデルの品質が大幅向上。

**これまでの課題と解決策**  
3DGSで作ったデータをメッシュ変換すると形状がガタガタになりがちだった。深度誘導初期化と3D primitiveへの漸進的移行による「メッシュ・GS共同精細化」で問題を解決。

---

#### 3. FreeTimeGS++ — 「4DGSがなぜ動くのか」を初めて解剖
- **arXiv**: https://arxiv.org/abs/2605.03337
- **投稿日**: 2026年5月5日
- **分野**: 4DGS

**何ができるようになったか**  
4DGS（時間軸を加えた動的3D表現）の構成要素を徹底的に分解・実験し、「動きの時間区分分化」「光学品質と時空間整合性のズレ」など重要な原則を初めて定量的に特定。ゲーテッドマージナリゼーションとニューラル速度場を使った新手法FreeTimeGS++を提案し、安定性・再現性を大幅向上。

**なぜ重要か**  
4DGS実装者が「どの要素が品質に効いているか」を判断できる初の体系的ガイドとなる。

---

#### 4. ELoG-GS — 真っ暗な環境でも正確な3D再構成
- **arXiv**: https://arxiv.org/abs/2604.12592
- **投稿日**: 2026年4月14日（NTIRE 2026チャレンジ採択）
- **分野**: 低照度3D再構成

**何ができるようになったか**  
夜間・地下・医療内視鏡など極低照度で撮影した複数視点映像から高品質な3DGSを生成。学習ベースの点群初期化と輝度誘導型カラー補正を組み合わせたデュアルブランチパイプライン。

**これまでの課題と解決策**  
暗所画像はセンサーノイズ・カラードリフト・特徴点マッチング失敗で従来の3DGSが機能しなかった。明示的な照度復元→再構成のデカップリング方式で安定化。

---

### 重要度：中

#### 5. Light 'em Up — 数枚の写真で暗所3DGS
- **arXiv**: https://arxiv.org/abs/2604.24053
- **投稿日**: 2026年4月27日
- **分野**: 低照度3DGS（Few-Shot）

少数枚の暗所写真から3DGSを構築。人間の視覚の光反射知覚モデル「レティネックス理論」を多スケールで適用し、照明変動を分離。撮影コストを最小化しながら暗所3D化を実現。

---

#### 6. EvFlow-GS — イベントカメラでブレ映像から3Dを高精度復元
- **arXiv**: https://arxiv.org/abs/2604.22183
- **投稿日**: 2026年4月22日
- **分野**: モーションブラー除去

動く被写体をカメラで撮影すると発生する動きブレを、イベントカメラ（微小な光変化を高速検出するセンサー）とオプティカルフロー（映像中の動き情報）で克服。スポーツ・工場ライン・自動運転への応用が期待。

---

#### 7. Splats in Splats++ — 3DGSへの見えない透かし入れ
- **arXiv**: https://arxiv.org/abs/2604.15862
- **投稿日**: 2026年4月15日
- **分野**: セキュリティ・ステガノグラフィ（透かし）

3DGSデータに見えない形で別の3D/4Dコンテンツや識別情報を埋め込む（ステガノグラフィ）技術。著作権保護・改ざん検知への応用。元シーンの画質をほぼ損なわず、攻撃耐性も高い。

---

#### 8. SFGS — 単眼動画から全身アバターを高精度生成
- **arXiv**: https://arxiv.org/abs/2604.09324
- **投稿日**: 2026年4月9日
- **分野**: アバター生成

スマートフォン1台の動画から、服・手・全身が自然に動く3Dアバターを生成。時間変化を捉えるヘックスプレーンと空間情報を捉えるトリプレーンを組み合わせ、手の細かい動きや衣服変形も正確に表現。

---

#### 9. Sparse-View 3DGS in the Wild — 現実の少枚数写真から高品質3D
- **arXiv**: https://arxiv.org/abs/2604.27422
- **投稿日**: 2026年4月28日
- **分野**: スパースビュー3DGS

写真が数枚しかない（スパースビュー）リアルな屋外環境でも、歩行者・車など邪魔な物体が映り込んでいても正確に3DGSを生成する手法。実際の撮影環境に即した現実的なパイプライン。

---

#### 10. Generalizable 3DGS Semantic Coding — リアルタイム没入映像通信へ
- **arXiv**: https://arxiv.org/abs/2604.25330
- **投稿日**: 2026年4月28日
- **分野**: 映像通信・意味的圧縮

3DGSを意味的に圧縮してリアルタイムで送受信する技術。メタバース・XRライブ配信など低遅延で高品質な3D映像通信の実現に向けた重要ステップ。

---

#### 11. Instant Colorization of Gaussian Splats — 2D情報を3DGSに逆投影
- **arXiv**: https://arxiv.org/abs/2604.17155
- **投稿日**: 2026年4月17日
- **分野**: 編集・再照明

通常のGSレンダリングは「3D→2D」だが、本手法は逆に「2Dの色・特徴量・セグメンテーション情報を3DGSに即時反映」させる。シーンの再照明・スタイル変換・セグメンテーションを統一パイプラインで実現。

---

#### 12. GS-2M — 反射物体でも高精度メッシュ（Eurographics 2026）
- **arXiv**: https://arxiv.org/abs/2509.22276
- **GitHub**: https://github.com/ndming/GS-2M
- **発表**: Eurographics 2026
- **分野**: 材質対応メッシュ再構成

金属・ガラスなど反射の強い物体の3D再構成はこれまで困難だった。材質パラメータ（粗さ・反射率）を学習に組み込み、高品質メッシュを生成。事前学習モデルに依存しない独自の粗さ推定法を提案。

---

#### 13. Scene-Agnostic Object-Centric GS — シーンを超えて物体を認識
- **arXiv**: https://arxiv.org/abs/2604.09045
- **投稿日**: 2026年4月10日
- **分野**: 物体中心表現・Embodied AI

これまでの3DGSの物体認識は「このシーン専用」だった。スロットアテンションを使った「物体コードブック」を学習することで、シーンが変わっても一貫した物体識別が可能に。Embodied AIやロボットへの応用が広がる。

---

## 📰 業界ニュース

#### 14. Adobe Photoshop 27.6「Rotate Object」— GSが一般ユーザーへ
- **CG Channel記事**: https://www.cgchannel.com/2026/04/adobe-releases-photoshop-27-6/
- **Adobe Research**: https://research.adobe.com/news/new-photoshop-feature-rotate-2d-objects-in-three-dimensions/
- **発表日**: 2026年4月28日

Photoshopの新機能「Rotate Object」が内部でGaussian Splattingを活用。2D写真に写った物体を一時的に低解像度のGS 3Dモデルに変換し、任意角度に回転後、高解像度2D画像に戻す仕組み。使用にはジェネレーティブクレジット（1回20クレジット）が必要。何百万もの一般ユーザーが初めてGS技術に触れる歴史的なマイルストーン。

---

#### 15. Cesium 3D Tiles × GS LoD — 都市規模3DGSがブラウザへ
- **Cesiumブログ**: https://cesium.com/blog/2026/04/27/3d-gaussian-splats-lod/
- **発表日**: 2026年4月27日

3D TilesとGSを組み合わせ、数億個のSplatを持つ超大規模シーンをLoD（詳細度）技術でブラウザからリアルタイムストリーミング可能に。実証例：MicrosoftがBentley Systemsと協力してレドモンドキャンパス全体（約3.7㎢、1億1千万Splats）を配信。glTF `KHR_gaussian_splatting`標準と連携。

---

#### 16. DNE × Gracia — 4DGS音楽パフォーマンスがブラウザで4分間フル配信
- **CG Channel**: https://www.cgchannel.com/2026/04/dne-and-gracia-release-4-minute-streamable-4dgs-performance/
- **発表日**: 2026年4月

Digital Nation Entertainment（DNE）の多視点撮影ステージとGraciaの4DGS処理パイプラインを組み合わせ、4分間の音楽パフォーマンスを4DGSとしてリアルタイム配信。ダウンロードもアプリも不要でスマホ・PC・VRヘッドセット全対応。WebGPUによるブラウザ描画。

---

#### 17. 3DISE Conference Prague — GS専門カンファレンス（第2回）開催
- **公式サイト**: https://3dise.com/
- **開催日**: 2026年5月5〜6日・プラハ

Gaussian Splatting・フォトグラメトリ・レーザースキャン・没入型技術を専門とする会議の第2回目。パネル「Gaussian Splattingは技術・クリエイティブ産業をどう変えるか」も実施。GS専門のカンファレンスの確立と産業界への浸透を示す重要なシグナル。

---

#### 18. XGRIDS 新型カメラ プラハで発表
- **公式サイト**: https://www.xgrids.com/portalcam
- **発表日**: 2026年5月6日（3DISE Conference会場）

3DGS専用ハンドヘルドカメラの新世代モデルが3DISEカンファレンスにてプラハで発表。LiDAR＋4カメラシステムで歩きながら建物全体を数分でGS化。インスタント処理対応。

---

## 💬 コミュニティ・SNS話題

#### 19. Arrival Space — オフラインモード追加
- **URL**: https://radiancefields.com/platforms/arrival-space
- **発表日**: 2026年5月6日

社会型3DGSプラットフォーム「Arrival Space」がオフラインモードを追加。ネット環境なしでもGSコンテンツの閲覧・管理が可能に。建設現場・地下施設・ネット不安定な現場での活用が広がる。

---

#### 20. 3DGS公式コードベース — トレーニング速度2.7倍高速化
- **GitHub**: https://github.com/graphdeco-inria/gaussian-splatting

元祖3DGSの公式実装に大型アップデート。Taming-3DGSとFused SSIMを統合し、デフォルト設定で1.6倍、Sparse Adamオプティマイザ使用時は2.7倍のトレーニング高速化を達成。Depth Regularization（奥行きマップを活用してフローターを除去する機能）も追加。最も広く使われるGSの基盤実装なので影響範囲が広い。

---

#### 21. Splats under Pressure — エッジデバイスでのGS電力効率を初調査
- **arXiv**: https://arxiv.org/abs/2604.07177
- **投稿日**: 2026年4月

スマートフォン・組み込みGPUなど「低予算GPU」でのリアルタイム3DGS描画における、フレームレート・消費電力・1フレームあたりのエネルギーを体系的に計測・分析した初の研究。IoTやウェアラブルへの展開に向けた重要なベースライン。

---

#### 22. OctaneRender 2026 正式GA — 商用パストレーサー初のネイティブGS対応
- **Radiance Fields**: https://radiancefields.com/octanerender-2026-released-and-2027-roadmap-announced

OTOYのOctaneRender 2026が正式リリース。Splatが他のオブジェクトに影を落とす・反射に映り込む・屈折を通して見える、といった物理ベースの光計算が可能に。.PLYと.SPZファイル形式をサポート。KhronosのglTF＋Splat標準化ワーキンググループにも参加。

---

## 🛠️ 開発者向けインサイト

### 今すぐ使えるもの

| ツール・論文 | 用途 | リンク |
|---|---|---|
| 3DGS公式コードベース（Sparse Adam） | トレーニング2.7倍高速化 | [GitHub](https://github.com/graphdeco-inria/gaussian-splatting) |
| Cesium + glTF KHR_gaussian_splatting | 都市スケールGSのLoD配信 | [Blog](https://cesium.com/blog/2026/04/27/3d-gaussian-splats-lod/) |
| Arrival Space offline mode | ネットなし環境でのGS活用 | [Platform](https://radiancefields.com/platforms/arrival-space) |

### 近く使えるようになるもの（コード公開待ち）

- **GETA-3DGS**: モバイル向けGS自動圧縮パイプライン
- **2D-SuGaR**: GS→高精度メッシュ変換
- **FreeTimeGS++**: 安定した4DGS学習基盤

### 今後の注目イベント

- **glTF KHR_gaussian_splatting 正式批准** — Q2 2026予定（Khronos Group）
- **3DISE Conference プラハ** — 5/5〜6（開催中・資料公開待ち）
- **CVPR 2026** — 6月開催予定（FastGS・4C4Dなど採択論文が発表）

---

*レポート生成：2026-05-07 | データソース：arXiv, CG Channel, Cesium Blog, Radiance Fields, Adobe Research, GitHub*
