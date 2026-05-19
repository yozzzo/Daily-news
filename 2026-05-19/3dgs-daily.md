# 3DGS & 4D生成 デイリーレポート
## 2026年5月19日（月）｜23件の新着情報

---

## 📊 今日のサマリー

- **論文**: 10件（CVPR 2026採択8件含む）
- **業界ニュース**: 7件
- **コミュニティ・SNS**: 3件
- **開発者インサイト**: 3件

---

## 🔥 今日の注目トレンド Top 5

1. **CVPR 2026コード公開ラッシュ開始** — 6月・Denver開催を前に採択GS論文80本以上のコードが続々公開
2. **4DGSが"1秒再構成"時代へ** — `MoVieS`（単眼動画から1秒で4D再構成）がCVPR 2026採択
3. **GSが設計・測量業界の標準ツールへ** — Esri・SolidWorks等の主要CAD/GISソフトがGS対応を一斉強化
4. **物理シミュレーション×4DGSの融合加速** — `PhysGM`（1枚の画像から物理特性まで予測する4D大規模モデル）
5. **HoudiniのVFXパイプラインにGSが正式統合** — `houdini-gsplat`（Houdini 21 Solaris向けオープンソースUSD GSプラグイン）公開

---

## 📄 注目論文

### 1. MoVieS — 単眼動画から"1秒"で4D動的シーン再構成
**分野**: 4DGS・動的シーン生成 ｜ **重要度**: ★★★★★
🏆 **CVPR 2026採択**

**概要**: これまで何十分もかかっていた4Dシーン（動く物体を含む3D空間）の再構成が、わずか1秒で完了。スマホ1台で撮った動画を入れるだけで、物体の外見・形状・動きを1つのモデルが同時に推定する。ゼロショットでシーンフロー推定や物体追跡にも対応。ARリアルタイム体験・映像制作の4D化を現実に引き寄せる革新的手法。

**リンク**: https://arxiv.org/abs/2507.10065

---

### 2. PhysGM（Physical Gaussian Model）— 画像1枚から物理シミュを可能にする4D大規模モデル
**分野**: 4D生成・物理シミュレーション ｜ **重要度**: ★★★★★
🏆 **CVPR 2026採択**

**概要**: 1枚の写真を入れるだけで、オブジェクトの3D形状だけでなく「重さ・弾性・摩擦」などの物理特性も同時に予測し、即座にシミュレーション実行できる大規模GS生成モデル。「このカップを落としたらどう壊れるか」をAIが自動生成。ゲーム開発・ロボット訓練の効率を根本から変える可能性がある。

**リンク**: https://arxiv.org/abs/2508.13911

---

### 3. Diff4Splat — テキスト指示1つで画像から4Dシーンを30秒生成
**分野**: 4D生成・テキスト制御 ｜ **重要度**: ★★★★★
🏆 **CVPR 2026採択**

**概要**: 1枚の画像＋テキストプロンプト＋カメラ軌跡を与えるだけで、動きのある4Dシーンを30秒で生成。ビデオ拡散モデル（動画生成AI）の知識を活用し、変形・動きを含む高品質な4DGSを最適化なしで出力する。コード公開済み（GitHub: paulpanwang/Diff4Splat）。

**リンク**: https://arxiv.org/abs/2511.00503

---

### 4. NimbusGS — 雨・霧・雪の悪天候下でも精度を落とさない3DGS
**分野**: 悪天候対応3DGS ｜ **重要度**: ★★★★☆
🏆 **CVPR 2026採択**

**概要**: これまでの3DGSは「晴天・クリーンな映像」が前提だったが、NimbusGSは雨・霧・雪などの天候ノイズをモデル化して除去し、高品質な3Dを再構成する。建設現場・自動運転・インフラ点検など、年間を通じた屋外での常時運用が現実的になる。

**リンク**: https://arxiv.org/abs/2603.27228

---

### 5. GLINT — ショッピングモールのガラス天井も3DGS化できる透明物体対応
**分野**: 透明・半透明物体のGS化 ｜ **重要度**: ★★★★☆
🏆 **CVPR 2026採択**

**概要**: ガラス面・水面・薄い布など光が複雑に透過する大規模な透明物体を、Gaussian Splatting（3Dの点群表現）で高精度に再現する新技術。従来の3DGSは透明物体が大きな弱点だったが、Gaussian Radiance Transport（GRT）という新しい物理モデルで解決した。

**リンク**: https://arxiv.org/abs/2603.26181

---

### 6. AeroDGS — ドローン空撮×動的4DGSの物理整合再構成
**分野**: 空中撮影・動的4DGS ｜ **重要度**: ★★★★☆
🏆 **CVPR 2026採択**

**概要**: 空中から撮影した動く車・人物・木々などを、物理的に正確な4DGSとして再構成する。ドローン映像特有の視点・動きに対応した最初の本格的な動的GSフレームワーク。ドローン×4DGSの実用化に向けた基盤技術として注目される。

**リンク**: https://arxiv.org/abs/2602.22376

---

### 7. LTGS（Long-Term Gaussian Scene Chronology）— 都市変化を3DGSで"年代記"として記録
**分野**: 長期シーン変化記録 ｜ **重要度**: ★★★★☆
🏆 **CVPR 2026採択**

**概要**: 都市・建物・自然環境が数ヶ月〜数年にわたってどう変化したかを、3DGSで一貫した時系列モデルとして記録・再現する手法。デジタルツイン・都市計画・文化財の経年変化保存への応用が有望。「3DGSで歴史を記録する」という新たな使い方を示した。

**リンク**: https://arxiv.org/abs/2510.09881

---

### 8. 4DSurf — 動く物体から正確なサーフェスメッシュを生成する4DGS
**分野**: 動的シーン・サーフェス再構成 ｜ **重要度**: ★★★★☆
🏆 **CVPR 2026採択**

**概要**: 動く人物・物体を含む動的シーンから、時刻ごとの正確なサーフェス（表面メッシュ）を高品質に再構成する。「見た目はきれいだが面の形状が不正確」という4DGSの弱点を改善。VFX・ゲームでの変形メッシュ生成に直結する研究。

**リンク**: https://arxiv.org/abs/2603.28064

---

### 9. CTRL-GS — 複雑な動きも精度よく再現する階層的4DGS時間分解
**分野**: 4DGS・時間階層分解 ｜ **重要度**: ★★★☆☆

**概要**: 動的シーンを「動画全体→セグメント→フレーム」の3段階で階層的に分解し、残差学習（差分だけを学ぶ効率的手法）を応用したGS再構成。大きな動き・遮蔽・細かい部分が混在する複雑なシーンで特に効果を発揮し、リアルタイムレンダリングと最高品質を両立する。

**リンク**: https://arxiv.org/abs/2505.18306

---

### 10. CLIPGaussian — テキスト1行で2D/3D/4Dをまとめてスタイル変換
**分野**: マルチモーダルスタイル転送 ｜ **重要度**: ★★★☆☆

**概要**: 「ゴッホ風に」「水彩画に」などのテキスト指示や参照画像だけで、2D画像・動画・3Dオブジェクト・4Dシーンを統一的にスタイル変換できる初のフレームワーク。既存のGSパイプラインにプラグイン追加だけで利用可能。コード公開済み（GitHub: kornelhowil/CLIPGaussian）。

**リンク**: https://arxiv.org/abs/2505.22854

---

## 🏢 業界ニュース

### 11. Esri Site Scan Q2 2026 — ドローン映像からクラウドでGS自動生成、最大1万枚対応
**分野**: GIS・ドローン・クラウドGS ｜ **重要度**: ★★★★★

**概要**: GIS業界最大手EsriがSite Scan for ArcGISのQ2 2026アップデートで、ドローン映像から直接クラウド上でGaussian Splatを自動生成する機能を追加。最大10,000枚の画像を処理可能。専用PCなしで建設・インフラ・農業の現場担当者がGSデータを作成できる環境が整った。EU圏はAWS制約で一部対象外。

**リンク**: https://www.esri.com/arcgis-blog/products/site-scan/imagery/whats-new-in-site-scan-for-arcgis-q2-2026

---

### 12. ArcGIS Reality May 2026 — 植生・細部構造のGS生成精度が大幅向上
**分野**: GIS・測量・GS品質向上 ｜ **重要度**: ★★★★☆

**概要**: 同月リリースのArcGIS Reality for ArcGIS Proアップデートで、GS生成の忠実度が向上。植生・薄い構造物・複雑な形状など、従来のメッシュが苦手だった対象物のGS化品質が改善。測量・建設のデジタルツイン精度がさらに上がる。

**リンク**: https://www.esri.com/arcgis-blog/products/arcgis-pro/3d-gis/how-to-create-the-best-gaussian-splats-in-arcgis-reality

---

### 13. Emergent Vision Technologies NAB 2026 — 36カメラ×NVIDIA DGX Sparkで"ライブ4DGS"実演
**分野**: ライブ4DGS・映像制作 ｜ **重要度**: ★★★★★

**概要**: 高速カメラメーカーのEmergent VisionがNAB 2026で、36台の100GigEカメラ（ZENITH）とNVIDIA DGX Sparkを組み合わせた「EROSアレイ」によるライブ4DGS収録・表示システムを世界初披露。マーカーレスモーションキャプチャと4DGSをリアルタイムで統合。スポーツ中継・ライブエンタメへの応用を示した。

**リンク**: https://www.tvtechnology.com/production/emergent-vision-unveils-4d-gaussian-splatting-and-high-speed-cameras

---

### 14. Plattipus houdini-gsplat — Houdini 21 SolarisでUSD×GSがネイティブ対応
**分野**: HoudiniプラグインUSD GS ｜ **重要度**: ★★★★★

**概要**: オープンソースの「houdini-gsplat」プラグインが公開。HoudiniのSolaris（USDベースの高度なコンポジットツール）でGSデータをネイティブに扱えるように。OpenUSD v26.03のGS標準スキーマを実装し、カスタムHydraレンダラーとLOPノード3種（PLY Import・Gsplat Instancer・Uruk）を提供。VFXパイプラインへの本格統合を可能にする重要な一歩。

**リンク**: https://github.com/plattipus/houdini-gsplat

---

### 15. Veesus × SolidWorks — 設計CADの画面でGSを可視化できるように
**分野**: 製造業CADとGS融合 ｜ **重要度**: ★★★★☆

**概要**: 製造業向けGSビューアのVeesusがSolidWorks（世界最大級のCADソフト）との統合を実現。設計エンジニアがCADデータと並行して、実際の製造現場や完成品のGSデータを同じ画面で確認できるようになった。設計と現物確認のギャップをなくす、産業向けGSの新活用法として注目。

**リンク**: https://www.thefuture3d.com/blog/state-of-gaussian-splatting-2026/

---

### 16. 3DVista 2026.0 「Total VR Mode」— VRヘッドセット内でGSモデルが完全動作
**分野**: VRバーチャルツアー×GS ｜ **重要度**: ★★★★☆

**概要**: バーチャルツアープラットフォーム3DVista がバージョン2026.0をリリース。新機能「Total VR Mode」により、VRヘッドセット内でGSモデルがカスタムスキンと完全統合されて動作。Eラーニング機能もVR内で利用可能になり、不動産内覧・観光案内・教育分野の仮想体験が次のステージへ。SOGフォーマット採用でGLBより最大10倍軽量。

**リンク**: https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/

---

### 17. Geo Week 2026 — 建設・GIS業界でGSが主役議題に
**分野**: AEC・GIS・カンファレンス ｜ **重要度**: ★★★★☆

**概要**: 測量・地理情報業界の主要カンファレンス「Geo Week 2026」でGSが主要テーマとして登場。NVIDIA・XGRIDS・Esri・Cesiumの担当者が「AEC・GIS産業でのGSの影響」「AIとGSの次の展開」をパネル討論。Cintooがリコー製360度カメラ（THETA X）と連携したGSソリューションも披露。GISとGSの融合が業界標準として認識される転換点となった。

**リンク**: https://radiancefields.com/gaussian-splatting-at-geo-week-2026

---

## 💬 コミュニティ・SNS話題

### 18. CVPR 2026 Denver — GS論文80本以上採択確定、コード公開ラッシュ開始
**概要**: 6月開催のCVPR 2026（デンバー）でGaussian Splatting関連論文が80本以上採択されたことが確認。MoVieS・PhysGM・Diff4Splat・NimbusGSなど今週以降コードを公開し始める論文が急増中。コミュニティでは「GS論文のCVPR比率がこんなに高いのは前例がない」と話題。

**リンク**: https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

---

### 19. GSOPs 2.6 — HoudiniのGS編集ツールがVFX現場で"標準ツール"化
**概要**: HoudiniユーザーのGSコミュニティで、GSOPs（Gaussian Splatting Operators）が事実上の標準ツールとして定着。今回のPlattipus houdini-gsplatプラグインとの組み合わせでHoudini内のUSD GSパイプラインが完成形に近づき、「VFXパイプラインにGSをいれるならHoudiniが最有力」という評価がコミュニティで固まりつつある。

**リンク**: https://radiancefields.com/platforms/gsops

---

### 20. 3DVista 2026.0 Total VR — 建築・観光・不動産でGS仮想ツアーが本格普及へ
**概要**: 3DVista 2026.0リリースを受けて、建築・観光・不動産のGS+バーチャルツアー活用が加速。SOGフォーマット採用でGLBより最大10倍軽量な体験が可能となり、スマホでも快適に動作するGS仮想ツアーの事例がコミュニティで多数共有されている。VR×GSの実用事例として「Casa Cascada」ツアーのデモがSNSで話題に。

**リンク**: https://www.3dvista.com/en/blog/update-2026-0-total-vr-mode/

---

## 🛠️ 開発者向けインサイト

### 21. 【今すぐ試せる】Esri + Cesium でのドローン→GS→Web配信パイプライン
Esri Site Scan Q2（クラウドGS生成）＋Cesium 3D Tiles LOD GS（先月対応）の組み合わせで、ドローン撮影→クラウドGS生成→Webブラウザ配信のエンドツーエンドパイプラインが初めて構築可能になった。特に建設・インフラ・都市計画の担当者は「自社ドローン映像→ArcGIS→Cesiumビューア」という即座に実践できるフローが実現した。ArcGIS Reality for ArcGIS Proのベストプラクティスガイドも公開されているため、今週中に試験導入を開始できる。

**リンク**: https://www.esri.com/arcgis-blog/products/arcgis-pro/3d-gis/how-to-create-the-best-gaussian-splats-in-arcgis-reality

---

### 22. 【VFX開発者必見】Houdini USD × GS パイプライン構築の最短経路
Plattipus houdini-gsplat（OpenUSD v26.03準拠）＋GSOPs 2.6の組み合わせで、Houdini内でGSをUSDアセットとして完全に扱えるようになった。パイプラインのポイント：①PLY ImportノードでGSデータをUSDに取り込む→②Gsplat Instancerで配置・編集→③Urukノードで最終出力。OpenUSD v26.03スキーマ準拠のため、他のDCCツール（Blender/Maya）との連携も今後期待できる。

**リンク**: https://github.com/plattipus/houdini-gsplat

---

### 23. 【CVPR 2026 注目実装ウォッチリスト】フィードフォワード4DGSの実装が今週から加速
CVPR 2026（6月・Denver）を前に、4DGS関連の論文コード公開が今週から本格化。特に注目すべき実装：
- `MoVieS` — 1秒4D再構成、動画→4DGSの最速ルート（今週公開予定）
- `Diff4Splat` — テキスト制御4D生成、コード公開済み（GitHub: paulpanwang/Diff4Splat）
- `PhysGM` — 物理対応4D生成、ゲーム・ロボット開発者は要チェック
- `NimbusGS` — 悪天候対応、屋外デジタルツインの実用化に直結

Awesome3DGSのCVPR.mdを定期チェックして最新のコード公開情報をフォローするのがおすすめ。

**リンク**: https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

---

*レポート生成日: 2026-05-19 | リポジトリ: yozzzo/Daily-news*
