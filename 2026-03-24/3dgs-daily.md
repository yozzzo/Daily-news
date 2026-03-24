# 3DGS & 4D生成 デイリーレポート

**日付:** 2026年3月24日（月）
**対象分野:** 3D Gaussian Splatting / 4D生成 / 動的3Dシーン
**対象地域:** 英語圏 / 日本 / 中国 / ヨーロッパ

---

## 今日の注目トレンド

| 順位 | トレンド | 概要 |
|:---:|:---|:---|
| 1 | 標準フォーマットが一斉に3DGS対応 | OpenUSD v26.03がGSスキーマ導入、glTFにもKHR_gaussian_splatting拡張が提案 |
| 2 | CVPR 2026採択論文が公開 | GSA（異種オブジェクト位置合わせ）とFreeArtGS（関節物体再構成）の2本 |
| 3 | モバイル3DGSが実用レベルに | Mobile-GSがHD 116FPS・4.8MBモデルを達成、スマホでリアルタイム表示 |
| 4 | UE5でGSが本格運用可能に | NanoGSプラグインがNaniteスタイルLODを実現、RTX 20シリーズでも動作 |
| 5 | Embodied AIに3DGS/4DGSが統合 | 51Vision社が3DGS/4DGSベースのロボットAIシステムを発表、株価+6% |
| 6 | 物理シミュレーション付きGSが登場 | GASPがGenesis物理エンジンと統合、CVIU誌に掲載 |
| 7 | カメラ不要の3DGS軽量化 | Camera-Agnostic Pruningで.plyファイルだけから枝刈りが可能に |

---

## 論文（7件）

### 1. F4Splat — 予測的密度化でフィードフォワード3DGSを効率化

**分野:** 3DGS最適化 | **重要度:** 高

フィードフォワード型3DGSの弱点を克服する「予測的密度化」手法。空間の複雑さやマルチビューの重なり具合に応じて、ガウシアンの数を自動的に最適配分する。単純な領域では冗長なガウシアンを減らし、複雑な領域に集中配置することで、少ないガウシアン数でも高品質な3D再構成が可能になった。開発者にとっては、3Dスキャンやビュー合成のメモリ効率と速度が大幅に改善されることを意味する。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.21304)

---

### 2. Camera-Agnostic Pruning — カメラ情報なしで3DGSを軽量化

**分野:** 3DGS圧縮・最適化 | **重要度:** 高

カメラ情報なしで3DGSモデルを軽量化できる画期的な手法。従来の枝刈り（プルーニング）はカメラパラメータが必要だったが、本手法は.plyファイルの属性情報だけで不要なガウシアンを統計的に判定・除去する。属性ベースの近傍記述子とBetaエビデンスモデルを使い、各スプラットの信頼性を評価。ISO/IEC MPEG標準テスト条件で検証済み。3DGSデータの保存・転送・共有が大幅に効率化され、Webやモバイルでの配信が容易になる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.21933)

---

### 3. GSA — 異なるオブジェクト間の3DGS位置合わせ [CVPR 2026]

**分野:** 3DGS位置合わせ | **重要度:** 高

異なるオブジェクト同士の3DGSモデルを自動的に位置合わせできる世界初の手法。例えば、別々にスキャンした2台の異なる車のモデルを、回転・移動・スケールを自動推定して正確に重ね合わせることができる。180度の向き違いや10倍のスケール差にも対応。幾何学的特徴とDINOv2の意味的特徴を組み合わせた2段階のアライメントパイプラインを採用。3Dアセット管理やデジタルツインの構築が格段に楽になる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.21936)

---

### 4. FreeArtGS — 関節物体の自由移動再構成 [CVPR 2026]

**分野:** 関節物体の3D再構成 | **重要度:** 高

ドアやハサミなど関節で動く物体を、スマホの動画1本から高精度に3D再構成できる手法。従来は物体を特定の角度に固定して撮影する必要があったが、自由に動かしながら撮影するだけでOK。単眼RGB-Dビデオ入力のみで、パーツセグメンテーションとジョイント推定を組み合わせて動作。AR（拡張現実）やロボティクスで、現実の物体をデジタル化する作業が劇的に簡単になる。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.22102)

---

### 5. GTSR — 半透明物体の3DGS再構成

**分野:** 半透明物体の3D再構成 | **重要度:** 中

ガラスやろうそく、肌のような半透明な物体を3DGSで正確に再現できる新手法。従来の3DGSは不透明な物体しかうまく扱えなかったが、表面と内部の2種類のガウシアンを使い分け、光の散乱をシミュレーションすることで、半透明素材のリアルタイムレンダリングを実現。フレネル項のブレンディングとDisney BSDFモデルを採用。ゲームやVR、製品ビジュアライゼーションの品質向上に貢献する。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.22036)

---

### 6. GaussianSSC — 自動運転向けセマンティック3D補完

**分野:** 自動運転・セマンティック理解 | **重要度:** 中

自動運転車が周囲の3D空間を「意味的に」理解するための新技術。カメラ画像からガウシアンの特性を活用して、見えていない部分も含めた3D空間全体の物体配置を推定する。トリプレーンガイドによる方向性ガウシアンフィールドとガウシアンアンカリングでサブピクセル画像集約を実現。SemanticKITTIベンチマークで従来手法を+1.8% IoU上回る精度を達成。自動運転の安全性向上やロボットの空間認識に直結する技術。

**ソース:**
- [arXiv論文](https://arxiv.org/abs/2603.21487)

---

### 7. 高忠実度アバター再構成 — 3DGSで人間を精密に3D化

**分野:** アバター生成 | **重要度:** 中

人間のアバターを高品質に3D再構成するための新しいタイルベースラスタライゼーション手法。3DGSフレームワークを拡張し、人体の細かいディテール（髪の毛、衣服のしわなど）まで忠実に再現できる。VRミーティングやゲームのキャラクター作成、バーチャル試着などへの応用が期待される。

**ソース:**
- [Springer論文](https://link.springer.com/article/10.1007/s40747-026-02231-5)

---

## 業界ニュース（5件）

### 1. OpenUSD v26.03 がGaussian Splatsスキーマを正式サポート

3D業界の標準フォーマットOpenUSDが、最新バージョンv26.03でGaussian Splatsの専用スキーマ（UsdVolParticleField3DGaussianSplat）を導入した。PLYファイルからUSDへの変換スクリプトも提供され、既存のCG/VFXパイプラインにGaussian Splatsを統合しやすくなる。WebAssemblyビルドサポートも追加され、ブラウザでの表示も視野に。映画・ゲーム・建築など幅広い業界でGaussian Splatsの採用が加速する転換点。

**ソース:**
- [3DVF記事](https://3dvf.com/en/openusd-v26-03-released-an-announcements-that-confirms-the-rapid-rise-of-gaussian-splats/)
- [AOUSD Blog](https://aousd.org/blog/)

### 2. glTF 2.0にKHR_gaussian_splatting拡張が登場（NVIDIA・Google・Adobe支援）

Web3Dの標準フォーマットglTFに、Gaussian Splatting専用の拡張仕様が提案された。NVIDIA、Google、Adobeが支援しており、重複データを最大90%削減できる。WebブラウザやARアプリでGaussian Splatsを直接表示する標準的な方法が確立されつつある。Web開発者にとって大きなインパクト。

**ソース:**
- [LinkedIn投稿](https://www.linkedin.com/posts/sressler_gaussiansplatting-3dgs-computervision-activity-7441907500427386882-3gvo)

### 3. NanoGS: UE5でNaniteスタイルのGaussian Splats LODを実現

NanoGSは、Unreal Engine 5のNaniteシステムと同様のLOD（Level of Detail）、カリング、GPUソートをGaussian Splatsに適用するプラグイン。Tim Chen氏（Moonshine Studio）が開発。RTX 20シリーズのGPUでも数百万のスプラットをリアルタイムレンダリング可能。ゲーム開発者やバーチャルプロダクション制作者が、大規模なGaussian Splatsシーンを実用的に扱えるようになる。

**ソース:**
- [Digital Production](https://digitalproduction.com/2026/03/24/nanogaussiansplats-for-ue5/)

### 4. 51Vision（五一視覚）が3DGS/4DGSベースのEmbodied AIシステム「51Claw」を発表

中国の51Vision社が、3DGS/4DGSを活用したEmbodied AI基盤システム「51Claw」を発表。マルチモーダル空間データから3DGS/4DGSでシーンを再構成し、物理世界のデジタルツインを生成。強化学習でロボットの動作を訓練し、ロボット犬やヒューマノイドロボットに展開済み。Real2Sim2Realの完全なループを実現し、株価は約6%上昇した。

**ソース:**
- [Futunn記事](https://news.futunn.com/en/post/70490715/wuyi-vision-has-developed-and-deployed-the-embodied-ai-base)

### 5. NAB Show: Gaussian Splatting in Production Pipelines パネル

NAB Showで、Gaussian Splattingを実際の映像制作パイプラインで活用している先駆者たちによるパネルディスカッションが開催。Volinga SuiteやそのUnreal Engineプラグインを使った実例が紹介されている。映像制作業界でのGaussian Splatting採用が本格化していることを示す重要なイベント。

**ソース:**
- [NAB Show](https://www.nabshow.com/session/gaussian-splatting-in-production-pipelines-discovering-real-productions-using-3dgs-today/)

---

## コミュニティ・SNS話題（6件）

- **GASP（CVIU掲載）:** Gaussian Splattingと物理エンジン（Genesis, Blender, Taichi）の統合が実現。パラメトリック化されたフラットガウシアンで物理シミュレーション付きGSが可能に
- **Mobile-GS:** モバイル端末でHD解像度116FPS・4.8MBモデルを達成。スマホでのリアルタイム3DGSレンダリングが実用レベルに到達
- **Reddit r/GaussianSplatting:** UE5プラグイン「MLSLabsRenderer」のアップデート報告。AIでペットを3Dモデル化する話題も活発
- **Facebook 3DMakerpro:** 物件訪問から没入型Gaussian Splattingツアーの送信まで1時間で完了できることを紹介。不動産業界での実用化が進行
- **Facebook 3DGSグループ:** 「What The Splat!」Gaussian Splatting構造化コースが開講。初心者版がリリースされ、学習環境が整備
- **LinkedIn Sandy Ressler:** 今週見逃せない5つのGaussian Splatting発表をまとめた投稿が話題

---

*この情報は毎朝自動で収集・配信されます。*
