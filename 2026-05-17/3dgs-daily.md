# 3DGS & 4D生成 デイリーレポート
**2026-05-17（日）**

---

## サマリー

今日は「物理シミュレーション×3DGS」の波が一気に押し寄せた一日。炎・弾性変形・頭部アバターに物理則を組み込む論文が複数登場し、単なる「見た目の再現」から「現実と同じ動きができる3D」へ技術が進化しつつあることが鮮明になりました。一方、業界では Esri・Veesus・3DVista など従来の測量・VR系ツールが続々とGSネイティブ対応を発表し、「専門家が使うプロツール」としての市場が急速に拡大しています。glTF標準規格の正式承認も目前となり、ブラウザ・ゲームエンジン・CADツール間でGSアセットをやり取りする未来が現実味を帯びてきました。

---

## 注目トレンド5選

1. **物理統合3DGSの本格化** — 炎・布・頭部アバターに物理シミュレーションを組み込む論文が集中。「見た目だけでなく動きも本物」な3Dへ
2. **測量・GIS業界のGS標準採用加速** — Esri Site Scan・ArcGIS Reality・PIX4Dに続き、Veesus × SolidWorksが統合。製造業・インフラ業界へ波及
3. **glTF KHR_gaussian_splatting 正式承認目前** — Q2 2026中に採択される見通し。ブラウザ～CAD～ゲームエンジン横断でGSが流通可能に
4. **フィードフォワード3DGSの精度向上** — AnchorSplatが3D幾何事前情報を活用し、カメラポーズ推定精度を大幅改善。実用化フェーズへ
5. **VRネイティブGS体験の普及** — 3DVista Total VR Mode・SuperSplat 2.5のMITライセンス化により、VR対応GSコンテンツの作成コストが激減

---

## 注目論文

### 1. AmbiSuR — 光学的あいまいさを解消するサーフェス再構成
**何が変わったか**: 鏡面反射や半透明物体など「光が複雑に絡む場所」では、従来の3DGSはどうしても形状がぼやけていました。AmbiSuRは「この点は反射光か直接光か」という光学的なあいまいさを明示的にモデル化することで、ガラス越しの物体や濡れた路面でも正確なサーフェスを取れるようになりました。
**なぜ重要か**: 自動車・精密機器・宝飾品など反射面の多い工業製品のデジタルツイン精度が飛躍的に向上します。
🔗 https://arxiv.org/abs/2605.12494

### 2. PG-3DGS — 物理ガイドで「生成した3DGS」を破綻させない
**何が変わったか**: テキストや画像から3DGSを生成すると、物理的にありえない形状（宙に浮いた破片、つぶれた壁）が生まれがちでした。PG-3DGSは物理シミュレーションを生成プロセスに組み込み、重力・剛体衝突を守りながら3DGSを出力します。
**なぜ重要か**: ゲーム・映像制作での自動シーン生成ワークフローで「物理的に破綻したアセット」を手動修正する工程がなくなります。
🔗 https://arxiv.org/html/2605.11266v1

### 3. FieryGS — リアルタイムで炎を3DGSに合成（ICLR 2026）
**何が変わったか**: 炎・煙は形が常に変わり、光を透過・吸収・散乱するため3D表現が極めて難しい対象でした。FieryGSはパーティクルベースの物理シミュレーションとGaussian Splatを組み合わせ、既存3DGSシーンに炎を物理的に正しく「貼り付ける」ことを可能にしました。
**なぜ重要か**: VFX・ゲーム開発でロケ撮影シーンへの炎合成コストが大幅削減。消防訓練シミュレータなど安全教育用途にも展開可能です。
🔗 https://pku-vcl-geometry.github.io/FieryGS/

### 4. PhysHead — 物理シミュレーション対応のGaussianヘッドアバター（CVPR 2026）
**何が変わったか**: 従来のGSアバターは「見た目は本人そっくり」でも、髪が空気抵抗を無視して動いたり、皮膚が物体を貫通したりする問題がありました。PhysHeadは頭部アバターに有限要素法（FEM）ベースの物理シミュレーションを統合し、髪・皮膚の物理的に正しい動きを実現します。
**なぜ重要か**: メタバース・VRコンコースでのアバター品質が向上。医療シミュレーション（術前計画など）への応用も期待されます。
🔗 https://arxiv.org/abs/2604.06467

### 5. AnchorSplat — 3D幾何事前情報でフィードフォワードGSを安定化（CVPR 2026）
**何が変わったか**: 数枚の写真から瞬時に3DGSを生成するフィードフォワード手法は、カメラポーズが少し狂うと大きくずれる欠点がありました。AnchorSplatは「3D空間の幾何的制約」をアンカーとして使い、ポーズ推定ずれを補正しながら安定した3DGSを生成します。
**なぜ重要か**: スマートフォンで撮影した数枚の写真からほぼリアルタイムに高精度な3D空間を生成できるようになります。
🔗 https://arxiv.org/abs/2604.07053

### 6. In Depth We Trust — 信頼性の高い深度監督でGS品質を向上（CVPR 2026）
**何が変わったか**: 深度センサーや単眼深度推定を使ってGSの学習を補助する手法は多数ありますが、センサーノイズや推定誤差が品質を下げる問題がありました。この研究は「どの深度情報が信頼できるか」を自動的に評価し、信頼度の高い情報だけを監督に使う仕組みを提案しました。
**なぜ重要か**: LiDARを使わない低コスト3D再構成でも、LiDAR並みの精度に近づくことができます。
🔗 https://arxiv.org/abs/2604.05715

---

## 業界ニュース

### Esri Site Scan Q2 2026 — クラウドGS生成・1万枚対応
ドローン測量プラットフォームの最大手 Esri Site Scan が Q2 2026 アップデートで Gaussian Splatting のクラウド生成を正式サポート。1万枚超の写真でも処理できるスケーラブルな設計で、大規模インフラ・土木工事現場でのGS活用が現実的になりました。
🔗 https://community.esri.com/t5/site-scan-blog/site-scan-q2-2026-faster-reality-mapping-at-scale/ba-p/1691379

### Esri ArcGIS Reality May 2026 — GS品質の継続改善
GIS業界標準ソフトウェアの ArcGIS Reality が 2026年5月アップデートでGS生成品質を大幅改善。建築・インフラ向けデジタルツイン構築でのGS採用がさらに加速する見通しです。
🔗 https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/generate-gaussian-splats-using-arcgis-reality-mapping.htm

### Geo Week 2026 — GS専門セッションが2つ開催
アメリカ最大の地理空間・測量イベント Geo Week 2026（2月）でGaussian Splatting専門セッションが2つ開催され、AEC（建築・土木・建設）業界への本格導入事例が多数発表されました。業界団体への浸透が顕著です。
🔗 https://radiancefields.com/gaussian-splatting-at-geo-week-2026

### Veesus × SolidWorks — CAD設計の世界にGSが進出
ポイントクラウド可視化の Veesus が SolidWorks との統合を発表。CADソフトウェア上でGS化したリアル環境を直接参照しながら設計・検証できるようになります。製造業のデジタルツイン活用で大きなインパクトが予想されます。
🔗 https://www.veesus.com/point-cloud-plugins/

### glTF KHR_gaussian_splatting — Q2 2026に正式承認目前
Khronos Group が 3D標準フォーマット glTF の Gaussian Splatting 拡張仕様「KHR_gaussian_splatting」を Q2 2026 内に正式採択する見通しを示しました。承認後はブラウザ・ゲームエンジン・CADツール間でGSアセットを標準的にやり取りできるようになります。
🔗 https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release

### Plattipus houdini-gsplat — Houdini 21 向けオープンソースGSプラグイン
VFXパイプラインの中核ツール Houdini 21 向けに USD ベースの Gaussian Splatting レンダリングプラグイン「houdini-gsplat」がオープンソースで公開されました。OpenUSD v26.03 の GS スキーマに準拠しており、Solaris（Houdiniのルックデブ環境）からネイティブにGSをレンダリングできます。
🔗 https://forum.aousd.org/t/gaussian-splat-rendering-for-houdini-solaris-built-on-usd-v26-03/2921

---

## ツール・コミュニティ

### SuperSplat 2.5 — 色調整ツール搭載 & MITライセンスビューア公開
PlayCanvas 製のブラウザベースGS編集ツール SuperSplat が v2.5 に更新。色調整・露出補正ツールが追加され、撮影条件の異なるGSシーンのトーン統一が容易になりました。また付属ビューアが MIT ライセンスで公開され、誰でも自由にカスタマイズ・商用利用できます。
🔗 https://radiancefields.com/supersplat-2-5-released

### Gaussian Splatting Morphing Tool（Felix Hirt）— 2つのGSシーンを滑らかにブレンド
独立開発者の Felix Hirt 氏が2つのGSキャプチャーを滑らかにモーフィング（補間）するインタラクティブツールを公開。旅行地の「昼↔夜」「夏↔冬」切り替えや、建設前後の比較ビジュアライゼーションなど、クリエイティブな活用が期待されます。
🔗 https://radiancefields.com/gaussian-splatting-morphing-tool-to-blend-between-3dgs-captures

### 3DVista 2026.0 Total VR Mode — GS完全VR対応
バーチャルツアー制作ツール 3DVista が 2026.0 アップデートで「Total VR Mode」を導入。GS でキャプチャした空間を Meta Quest・PSVR などのスタンドアロン VR ヘッドセットで没入体験できます。不動産・観光・文化施設向けの VR ツアー制作コストが大幅に下がります。
🔗 https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/

---

## 開発者向けインサイト

### 今週の重要な実装ポイント

**1. 物理統合3DGSの実装アプローチ**
今週の論文群（FieryGS・PG-3DGS・PhysHead）に共通するのは「物理シミュレーション出力をGSSの変形パラメータ（回転クォータニオン・スケール）にマッピングする」アプローチです。FEM や MPM（Material Point Method）の出力座標を Gaussian の位置・形状に反映するアダプタ層の設計が鍵となります。

**2. AnchorSplat の幾何アンカー手法**
AnchorSplat は MASt3R や DUSt3R などの幾何推定モデルからスパースな3Dアンカー点を抽出し、フィードフォワードGS生成時のアテンション機構の位置エンコーディングとして使います。既存のフィードフォワードGSフレームワーク（Splatt3R 等）への統合が比較的容易です。

**3. glTF KHR_gaussian_splatting 仕様の先読み**
RC（Release Candidate）段階にある KHR_gaussian_splatting 拡張は、Gaussian パラメータ（位置・スケール・回転・不透明度・SH係数）を glTF バッファビューとして格納します。現時点でも Cesium・PlayCanvas・three.js の実装を参考に対応を進められます。正式採択後の移行コストを最小化するには、今から内部フォーマットを仕様書の型定義に揃えておくことを推奨します。

**4. Esri/測量業界向け統合のポイント**
Esri Site Scan と ArcGIS Reality は どちらも OGC CDB / OpenUSD ベースのエクスポートに対応しています。GS を測量ワークフローに組み込む場合、座標系（EPSG コード）の明示的な付与と、GS バウンディングボックスの地理座標への変換が最初のボトルネックになります。

---

*レポート生成日: 2026-05-17 | 対象期間: 2026-05-15 以降の新着情報*
*重複チェック: past_3dgs.json (280件以上) との照合済み*
