# 3DGS / 4D生成 デイリーレポート — 2026年6月15日

## サマリー
- 収集期間: 2026年6月上旬〜中旬
- 新規項目数: **19件**（論文10件 / ニュース6件 / コミュニティ3件）
- 重複除外: `past_3dgs.json` 照合済み

---

## 🔥 今日の注目トレンド TOP5

1. 🍎 **Apple が3DGSをApple Mapsに正式採用**（WWDC 2026） — iOS 27 Flyoverで秋提供予定。GS技術が初めてコンシューマー向け製品に公式採用
2. 🏙️ **都市規模・10億Gaussian再構成が可能に**（Multi-GPU GS） — 現SOTAの25倍規模。マルチGPU PyTorch抽象化で都市全体を街路レベルで3DGS化
3. 🎬 **BlenderでGSをキャラクターのようにアニメーション化**（3DGS Render 5.0） — リグ付きプロキシメッシュからGSに動きを転送 + 再照明対応。無料
4. 🚗 **自動運転向け「未来を予測する4DGS」登場**（Envision4D） — カメラ位置情報なしで走行シーンの未来を3D生成。清華大学＋CUHK発
5. 🎨 **ComfyUI v0.23.0でGS生成がAIワークフローの標準機能に**（TripoSplat） — 1枚の写真から3DGSを生成するノードが公式対応

---

## 📄 注目論文

### 1. Multi-GPU Gaussian Splatting（PyTorch抽象化）
- **arXiv**: https://arxiv.org/abs/2606.11390
- **フィールド**: 大規模・マルチGPU

**何ができるようになったか:** 複数のGPUを連携させて、10億個以上のGaussianを使った「都市スケール」の超精細3D再構成が可能になった。

**課題と解決:** これまでは1台のGPUのメモリ上限があり、大規模シーンの3DGSは不可能だった。PyTorch上の分散処理を3DGS専用に設計し、コード複雑性を隠しながらマルチGPU化。現SOTAの25倍以上（10億超）のGaussianで都市全体を街路レベルの精細さで再構成。

---

### 2. Gaussian Point Splatting（SIGGRAPH 2026採択）
- **論文**: https://momentsingraphics.de/Siggraph2026.html
- **GitHub**: https://github.com/JorisAR/gaussian-point-splatting
- **フィールド**: 確率的レンダリング・超大規模GS
- **発表**: SIGGRAPH 2026（7月20日）

**何ができるようになったか:** 4億2500万個ものGaussianをRTX 4070 Ti SUPER 1枚でリアルタイム表示できるようになった。

**課題と解決:** 従来の3DGSはソート処理とタイルベースレンダリングに依存しており、Gaussian数が増えると処理が遅くなっていた。「各Gaussianからランダムに点をサンプリングし、64ビットアトミック演算でフレームバッファに書き込む」確率的手法でソートもタイルも不要に。数百万スレッドに均等に負荷分散。

---

### 3. Envision4D（4DGS × 自動運転）
- **arXiv**: https://arxiv.org/abs/2606.10656
- **投稿日**: 2026-06-09
- **著者**: 清華大学 + 香港中文大学（深圳）
- **フィールド**: 4DGS・自動運転・フィードフォワード

**何ができるようになったか:** 自動運転車の車載カメラ映像だけで、カメラ位置情報（ポーズ）すら必要とせず、「数秒後の走行シーン」を3Dで予測生成できるようになった。

**課題と解決:** 大きな動きがあるとゴースト（残像）が生じる問題、単純な動き仮定の限界、誤差蓄積の問題を、反復的デノイジングで未来カメラ位置を推定するモジュール・層内時間注意機構・段階的トレーニングで解決。既存手法を大幅に上回る品質を達成。

---

### 4. EvoGS（スケーラブル3Dストリーミング）
- **arXiv**: https://arxiv.org/abs/2606.07179
- **投稿日**: 2026-06-05
- **フィールド**: 3Dストリーミング・LoD

**何ができるようになったか:** 大規模3DGSシーンをWebやモバイルへ効率よくストリーミング配信できるようになった。

**課題と解決:** 既存のLoD方式はGaussianが重複・蓄積しメモリを無駄に消費していた（重複率65%以上）。「Evolutionツリー」というウェーブレット風の親子構造で差分のみを洗練させ、重複率を25%以下に削減。転送量最大2.4倍削減、GPU VRAM最大5.5倍削減。

---

### 5. Ref-DGS（反射対応デュアルGS）
- **arXiv**: https://arxiv.org/abs/2603.07664
- **フィールド**: 反射表面・SIGGRAPH2026
- **発表**: SIGGRAPH 2026（7月19-23日、ロサンゼルス）

**何ができるようになったか:** 金属・ガラス・水面など鏡面反射する素材を含む場所を、高品質かつ高速に3D再構成できるようになった。

**課題と解決:** 反射の精度を上げるにはレイトレーシングが必要で計算コストが高かった。「形状Gaussian」と「局所反射Gaussian」の2層構造に加え、遠方反射用グローバル環境フィールドを組み合わせることで、ラスタライズベースの高速パイプラインのまま反射を忠実再現。

---

### 6. LEGS（ラプラシアン強化GS）
- **arXiv**: https://arxiv.org/abs/2606.07932
- **投稿日**: 2026-06-06
- **著者**: 中国科学院 長春光学精密機械物理研究所
- **フィールド**: 画質最適化・構造検出

**何ができるようになったか:** 細かいエッジや輪郭がシャープに再構成できるようになった。

**課題と解決:** 標準3DGSの損失関数は平坦な領域も細かい構造も同じ扱いで輪郭がぼけやすかった。「ラプラシアン演算子（2次微分）」で構造を検出し、細かい部分に重点を置いた非線形損失関数に変更。レンダリングパイプライン自体は変更不要。

---

### 7. SparseStreet（街路シーン用Sparse GS）
- **arXiv**: https://arxiv.org/abs/2606.03909
- **フィールド**: 街路シーン・圧縮・自動運転
- **発表**: ICMR '26（6月16-19日、アムステルダム）

**何ができるようになったか:** 自動運転向け街路3DGSを学習可能な枝刈りで大幅圧縮し、実用的なサイズに削減できるようになった。

**課題と解決:** 従来の街路向け3DGSはデータ量が膨大で実用上の障壁だった。ノードベースの学習可能枝刈りで視覚的に重要な領域を保ちながら無駄なGaussianを削除。

---

### 8. HiGS（階層型リアルタイム3DGS描画）
- **arXiv**: https://arxiv.org/abs/2606.00352
- **フィールド**: リアルタイム描画・階層アーキテクチャ

**何ができるようになったか:** 大規模シーンでもリアルタイム描画品質を維持できる階層的なアーキテクチャが登場した。

**課題と解決:** 大規模シーンでのリアルタイム描画は速度とクオリティのトレードオフが問題だった。階層的レンダリングアーキテクチャで両立を図る新手法。

---

### 9. Point Cloud Upsampling for 3DGS
- **arXiv**: https://arxiv.org/abs/2606.00450
- **フィールド**: 初期化改善・品質向上

**何ができるようになったか:** 3DGSの入力となる点群を事前に高密度化する最適な手法を系統的に評価・整備。初期化品質向上で最終的な3DGS品質と収束速度を改善。

**課題と解決:** 3DGSの品質は初期点群の密度に依存するが最適な手法が不明確だった。線形補間・スプライン・MLS等を比較し実践的なガイドラインを提供。

---

### 10. Unifying Appearance Codes and Bilateral Grids（自動運転GS外観統一）
- **arXiv**: https://arxiv.org/abs/2506.05280
- **フィールド**: 自動運転・外観統一

**何ができるようになったか:** 自動運転の多眼カメラ間で生じる色・露出のバラつきを補正し、整合性の高い3DGSを生成できるようになった。

**課題と解決:** 自動運転データは複数カメラの外観差が3DGS品質を低下させていた。外観コードとバイラテラルグリッドを統合した表現で一括補正。

---

## 📰 業界ニュース

### 11. Apple Maps Flyover が3DGSへ移行（WWDC 2026）★最重要
- **発表日**: 2026年6月8日
- **ソース**: https://radiancefields.com/apple-maps-flyover-is-getting-a-gaussian-splatting-upgrade
- **MacRumors**: https://www.macrumors.com/2026/06/08/apple-maps-flyover-ios-27/

**何ができるようになったか:** iPhone・Mac・Vision ProのFlyover機能が3DGSによる超リアルな3D都市に刷新される。航空映像＋Vision Intelligence（AI）で「ハイパーリアルな3D都市」を350都市以上で提供予定。提供開始: 2026年秋（iOS 27 / macOS 27 / visionOS 27同時リリース）。

**なぜ重要か:** Appleが消費者向けプロダクトに3DGSを初めて正式採用。GS技術が「ニッチな研究」から「主流インフラ」へ移行するターニングポイント。

---

### 12. 3DGS Render 5.0 for Blender リリース（June 11）
- **ソース**: https://www.cgchannel.com/2026/06/3dgs-render-5-0-lets-you-animate-gaussian-splats-inside-blender/
- **開発**: Kiri Innovations / 無料

**何ができるようになったか:** BlenderでGaussian Splatをリグ付き3Dキャラクターのようにアニメーション化。アーマチュアで動かしたプロキシメッシュの変形をGSに自動転送。ライティング転送・再照明・4DGSエクスポート（PLYシーケンス）も追加。Blender 5.1対応。

---

### 13. ArcGIS Enterprise 12.1 が GS レイヤーを正式サポート
- **ソース**: https://www.esri.com/arcgis-blog/products/arcgis-enterprise/announcements/whats-new-in-arcgis-enterprise-12-1

**何ができるようになったか:** 組織内設置型GISシステムのScene ViewerでGaussian Splatデータを直接可視化・共有できるようになった。配管・アンテナ等の極細構造にも対応。

---

### 14. Chaos Vantage 3.3.0 — リアルタイムレイトレーサーにGS再照明追加
- **ソース**: https://radiancefields.com/chaos-vantage-3-brings-gaussian-splatting-support

**何ができるようになったか:** リアルタイムレイトレースレンダラー「Chaos Vantage」上でGaussian SplatをV-Rayライトで照らせるようになった。GS固有の「ライティング固定」問題を解消。

---

### 15. Cesium ion June 2026 — メッシュ生成なしでGSパイプライン実行可能に
- **ソース**: https://cesium.com/

**何ができるようになったか:** 3D再構成ジョブでメッシュ生成ステップをスキップし、Gaussian Splat単独のシンプルなパイプラインで処理できるようになった。処理時間・コストの大幅削減。

---

### 16. CVPR 2026 Denver（6月3〜7日）— 3DGS関連コード公開ラッシュ
- **ソース**: https://cvpr.thecvf.com/Conferences/2026
- **GS論文リスト**: https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/blob/main/2026/CVPR.md

**何ができるようになったか:** FastGS（100秒でGS学習、Highlight賞）・Faster-GS（2〜5倍高速）・EDGS等の多数の3DGS論文コードが正式公開。全体4,090採択（前年比42%増）。

---

## 💬 コミュニティ・SNS話題

### 17. ComfyUI v0.23.0 TripoSplat — 1枚の写真→3DGSがAIワークフローの標準機能に
- **ソース**: https://radiancefields.com/comfyui-adds-native-3d-gaussian-splat-generation-with-triposplat
- **ComfyUI Blog**: https://blog.comfy.org/p/bringing-native-support-for-3d-gaussian

**何ができるようになったか:** ComfyUI v0.23.0でネイティブの「GAUSSIAN型」と操作ノード群が公式追加。写真1枚をアップロードするだけで3DGSを生成し、3Dパイプラインに直接出力。

---

### 18. Irrealix After Effects / Nuke プラグイン アップデート
- **ソース**: https://radiancefields.com/irrealix-updates-after-effects-and-nuke-plugin-for-gaussian-splatting

**何ができるようになったか:** After EffectsとNukeでGaussian Splatをリアルタイムにインポート・操作・レンダリングできる機能が強化。4DGS（PLYシーケンス）対応・深度パス出力追加。

---

### 19. Splatworld — GS仮想世界を自律生成するオープンソースツール（MIT License）
- **ソース**: https://radiancefields.com/splatworld-explores-autonomous-generation-of-gaussian-splat-environments

**何ができるようになったか:** テキストや画像からGaussian Splatの仮想世界を自動生成・共有できるMITライセンスのオープンソースツール。World Labsの商用ツールに対して無料で誰でも試せる選択肢として注目。

---

## 🛠️ 開発者向けインサイト

1. **ComfyUI v0.23.0でGS生成が標準化** — `pip install --upgrade comfyui` 後、テンプレートライブラリからTripoSplatを選択するだけで即使用可能
2. **3DGS Render 5.0（Blender無料アドオン）** — 既存リグ付きキャラクターワークフローをそのままGSに適用できる初の実用ツール。https://www.kiriengine.app/3d-tools/3dgs-render
3. **CVPR 2026 FastGS / Faster-GS コードが公開** — 既存3DGSパイプラインを2〜5倍高速化。ドロップイン差し替え可能
4. **ArcGIS Enterprise 12.1でエンタープライズGS展開が可能** — 政府・企業向けのGS提案時機
5. **Cesium ionのメッシュフリー化でパイプライン簡略化** — GS専用ジョブ設定で処理コストを削減
6. **注視すべき今後のイベント**: SIGGRAPH 2026（7月19-23日、LA）でGaussian Point SplattingとRef-DGSが発表予定
