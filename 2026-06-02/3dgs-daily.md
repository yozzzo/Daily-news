# 3DGS & 4D生成 デイリーレポート
**日付：2026年6月2日**

---

## 📊 本日のサマリー

- **新規項目数：20件**（論文7件 / ニュース8件 / コミュニティ5件）
- **注目イベント：CVPR 2026 デンバー開幕（6/3〜6/7）** — 今週からGS関連Oral Sessionがスタート！

### 🔥 今日の注目トレンド TOP5

1. **CVPR 2026 開幕**：4,090論文、GS専用Oral Session（6/5）——今週は年間最大のGSコード公開ウィーク
2. **CLM-GS（ASPLOS 2026）**：コンシューマGPU1枚で1億個のGaussian学習——「GPUメモリの壁」を突破
3. **物理統合GS新潮流**：PG-3DGSで「注いで使えるティーポット」を自動生成——見た目だけでない物理機能を持つ3D
4. **Sony XYN × Disguise**：UE不要でGS素材がLEDウォールへ直接——バーチャルプロダクション完全統合パイプライン実現
5. **映画VFX初4DGS採用**：Framestore が映画『Superman』で4DGSを本番採用、200台カメラで約40ショット

---

## 🔬 注目論文（重要度：高）

### 1. CLM-GS｜単一GPUで1億Gaussian学習——「GPUメモリの壁」突破
> ASPLOS 2026 採択 / NYU / [arxiv:2511.04951](https://arxiv.org/abs/2511.04951) / [GitHub](https://github.com/nyu-systems/CLM-GS)

**何ができるようになったか：** これまで大規模3DGS（数千万〜億点規模）の学習には複数の高性能GPUが必要だった。CLM-GSはCPUメモリを活用したオフロード機構により、**RTX 4090 1枚で1億2200万点Gaussian・25km²都市シーン学習**を実現。PSNR=25.15dBと品質も向上。

**解決された課題：** 大規模デジタルツインはGPUメモリ不足が壁だった。「各学習ステップで使うGaussianはシーン全体のごく一部」というスパース性に着目し、アクセス頻度の低い属性をCPUメモリへ動的オフロードすることで突破。Apache 2.0でコード公開済み。

---

### 2. Selfi｜CVPR 2026 Oral — カメラ情報なしで自動改善する再構成エンジン
> CVPR 2026 Oral Session 2C（6/5 13:50〜） / [arxiv:2512.08930](https://arxiv.org/abs/2512.08930)

**何ができるようになったか：** カメラの位置・角度情報（ポーズ）なしで3D再構成し、結果を**自己改善ループで自動的に精度向上**させる。従来のフィードフォワード3DGSより高精度。

**解決された課題：** 既存手法は正確なカメラ情報が前提だった。3D幾何学特徴アライメントを用いた自己改善機構により、未較正の写真群から高品質3Dを生成可能に。CVPR 2026のOral発表（最優秀クラスの発表枠）に採択。

---

### 3. PG-3DGS｜物理機能を持つ3DGS生成——「見た目」から「機能」へ
> [arxiv:2605.11266](https://arxiv.org/abs/2605.11266)

**何ができるようになったか：** ティーポット、飛行機、橋など**「物理的に正しく機能する」形状を自動生成**。生成された3DGSモデルが物理シミュレーションで正常に動作することを保証。「注いで使えるティーポット」「実際に揚力を生む飛行機の翼」が実現例。

**解決された課題：** 既存の3DGS生成は見た目の正確さのみ最適化し、物理機能性を無視していた。微分可能物理シミュレーターと3DGSの統合により、視覚と物理を同時最適化。ゲーム・ロボティクス・CADへの応用が開ける。

---

### 4. P2GS｜都市スケールGSの照明ムラを物理で解消
> Chubu大学 × Turing Inc. / [arxiv:2605.16925](https://arxiv.org/abs/2605.16925)

**何ができるようになったか：** 複数台の異なるカメラで撮影した自動運転データから、**カメラ間の露出・色差を自動補正して物理的に一貫した都市3DGSを再構成**。LDR画像だけからHDR品質のシーンを生成。

**解決された課題：** 自動運転データはカメラごとに露出が異なり「色ムラ」が発生していた。物理的画像形成モデルで一貫性を担保することで、夜でも曇りでも高精度な都市GSが可能に。

---

### 5. Geometry-Grounded Gaussian Splatting｜形状抽出精度No.1——GSの理論を再定式化
> HKUST / [arxiv:2601.17835](https://arxiv.org/abs/2601.17835)

**何ができるようになったか：** Gaussianを「確率的立体（stochastic solid）」として厳密に定義し直し、高精度な深度マップレンダリングと**3D形状（メッシュ）抽出が公開ベンチマークでGS系手法ベスト精度**を達成。

**解決された課題：** GSは美しい画像を生成できるが、正確なメッシュを取り出すことが理論的に難しかった。数学的基盤を再構築することで解決。

---

### 6. GS-DMSR｜動的シーンを96FPSで描画
> Guilin University of Electronic Technology / [arxiv:2601.05584](https://arxiv.org/abs/2601.05584)

**何ができるようになったか：** 動く物体（人・車など）の3D再構成を**合成データセット上で96FPS（RTX 3090）**で実現。学習時間・ストレージも同時削減。

**解決された課題：** 4DGS（動的GS）は高品質か高速かのトレードオフが課題だった。動き度合いを定量解析し重要な部分に計算を集中する適応型戦略で両立。

---

### 7. Fast Converging 3DGS｜1分以内の3DGS再構成
> SIGGRAPH Asia 3DGS Fast Reconstruction Challenge / [arxiv:2601.19489](https://arxiv.org/abs/2601.19489)

**何ができるようになったか：** 撮影した写真から**1分以内に3DGSモデルを再構成**。SLAMベースの高速ポーズ推定→段階的精度向上のパイプラインで速度と品質を両立。現場リアルタイムプレビューへの道を開く。

**解決された課題：** 従来の高品質3DGS再構成には数十分〜数時間かかり、現場でのプレビューが困難だった。

---

## 📰 業界ニュース

### 8. CVPR 2026 Denver 開幕（6/3〜6/7）
> [CVPR 2026公式](https://cvpr.thecvf.com/Conferences/2026)

過去最大規模4,090論文採択（前年比+42%）。GS関連50件以上が発表予定。**6月5日にGaussian Splatting & Reconstruction専用Oral Session 2C**開催。テーマは「World Models」「3Dグラウンディング」「Embodied AI」でGSが中核。今週は年間最多のGSコードが公開される。

---

### 9. Sony XYN × Disguise 直接パイプライン公開
> [Radiance Fields](https://radiancefields.com/sony-s-gaussian-splatting-gets-direct-pipeline-to-disguise) / [Sony XYN公式](https://xyn.sony.net/en/news/2026-spatial-disguise)

Sony XYNとDisguise（バーチャルプロダクションソフト最大手）の統合プラグインが公開。**Sonyカメラ撮影→XYNクラウド処理→Disguise Designer直接読み込み**の完全パイプライン。従来のUnreal Engineを経由するワークフローを不要化。HDR対応・被写界深度・CG合成完備。米国2026年夏から本格提供開始。

---

### 10. Framestore × 映画「Superman」：4DGS本番採用（商業映画世界初）
> [befores & afters](https://beforesandafters.com/2026/02/13/framestore-showcases-the-4d-gaussian-splatting-used-for-superman/) / [Art of VFX](https://www.artofvfx.com/superman-framestore-brings-4d-gaussian-splatting-to-the-big-screen/)

James Gunn監督「Superman」でFramestoreが4DGSを商業映画初本番採用。約200台のカメラでBradley Cooper・Angela Sarafyanの演技を撮影し、**任意の視点からリフレーム可能な4Dホログラム映像として約40ショットを納品**。ポストプロで自由にカメラ角度・焦点距離を変更できた。

---

### 11. Khronos KHR_gaussian_splatting Q2 2026 正式批准
> [Khronos](https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release)

Google・NVIDIA・Apple・Bentley主導で進むglTF 2.0のGS拡張`KHR_gaussian_splatting`がQ2 2026（4〜6月）に正式批准予定。**批准後は世界中のglTF対応ビューア・エンジンでGSが標準サポート**され、3D配信の新定番フォーマットが確立する。

---

### 12. AWE USA 2026（6/15〜18 Long Beach）GS専用セッション
> [AWE公式](https://www.awexr.com/usa-2026/agenda/2104-roundtable-discussions-everything-about-gaussian-s)

世界最大AR/VRイベントAWE USA 2026が6/15〜18にLong Beachで開催。**「Everything About Gaussian Splatting and XR」ラウンドテーブル**開催。4DviewsがUnity/UE向けGSボリュメトリックビデオ完全統合システムを出展。250社以上・5,000人規模。

---

### 13. Netflix：GS Video Coding インターン採用（Fall 2026）
> [Netflix採用ページ](https://explore.jobs.netflix.net/careers/job/790315673635)

Netflixが「Video Algorithms Intern - Video Coding (Gaussian Splatting)」採用を公開。**「GSを将来のストリーミングフォーマット候補として研究し、TV・スマホ・PCへの展開可能性を模索」**という公式ミッション。世界最大動画配信サービスのGS本格検討が確認できる重要シグナル。

---

### 14. Niantic Spatial：シニアGS採用（$257K〜$315K）
> Glassdoor

San Franciscoで「Senior CV Lead: 3D Reconstruction & Gaussian Splatting」を公開。年俸$257K〜$315K。**ポケモンGOのNianticがGSを次世代AR地図技術の中核に据えた戦略的採用。GS専門職の市場価値が急上昇していることを示す。**

---

### 15. Gracia AI：4DGSストリーミングで$1.7M調達
> [TechFundingNews](https://techfundingnews.com/gracia-ai-lands-1-7m-for-ai-powered-ultra-photorealistic-volumetric-videos-for-vr-and-ar/) / [UploadVR](https://www.uploadvr.com/gracia-moving-volumetric-captures-now-streamable/)

ロンドン発スタートアップGracia AIがEWORなどから$1.7M調達。**WebGPUで動的GSをブラウザストリーミング再生**し、Quest 3・Pico 4でも動作。推奨帯域80Mbps・12万splats/フレームのデモ公開中。

---

## 💬 コミュニティ・SNS話題

### 16. 4Dviews AWE 2026：GSボリュメトリック完全統合発表
Unity/Unreal Engine向けの**世界初エンドツーエンドGSボリュメトリックビデオシステム**をAWE USA 2026で公開予定。キャプチャーからGS変換・ゲームエンジン統合まで1社完結。

### 17. Braindance VR：GS採用でVR没入感を刷新
> [BriefGlance](https://briefglance.com/articles/braindances-new-vr-redefines-immersion-with-gaussian-splatting)

BraindanceのVRコンテンツがGS採用で「現実の中にいる感覚」を実現とコミュニティで話題。ゲーム・XRへのGS採用加速を示す先行事例。

### 18. awesome-gaussians GitHub（毎日自動更新論文トラッカー）
> [GitHub](https://github.com/longxiang-ai/awesome-gaussians)

ArXivの3DGS関連論文を毎日自動収集・更新するGitHubリポジトリ。毎朝の論文キャッチアップに必須ツール。

### 19. CLM-GS GitHub公開（Apache 2.0）
> [GitHub nyu-systems/CLM-GS](https://github.com/nyu-systems/CLM-GS)

NYU開発の大規模GS学習システムCLM-GSがApache 2.0で公開。3つの学習戦略（GPUのみ・ナイーブCPUオフロード・CLM方式）を提供。今すぐ試せる。

### 20. CVPR 2026 コード公開ラッシュ（6/3〜6/7）
> [PaperDigest](https://www.paperdigest.org/2026/06/cvpr-2026-papers-with-code-data/)

CVPR 2026期間中に年間最多のGSコードが公開中。FastGS・Faster-GS・Selfi・4C4Dなど50件以上のGS論文コードが今週公開予定。

---

## 🛠 開発者向けインサイト

| # | インサイト | アクション |
|---|-----------|----------|
| 1 | **CLM-GSで大規模GSが自宅GPUに**：25km²都市・1億Gaussian学習がRTX 4090 1枚で可能に | `nyu-systems/CLM-GS` を今すぐクローン |
| 2 | **CVPR 2026コード公開を逃すな**：今週は年間最多のGS論文コード公開週 | [PaperDigest CVPR 2026](https://www.paperdigest.org/2026/06/cvpr-2026-papers-with-code-data/) を毎日チェック |
| 3 | **Khronos批准後対応準備**：KHR_gaussian_splatting正式批准でglTF対応ビューア全対応へ | `.glb`+GS拡張の出力パイプラインを今から整備 |
| 4 | **物理GS時代の到来**：PG-3DGSが示す「視覚＋物理機能」の両立は3D生成の次の地平 | 物理要件のある生成プロジェクトでPG-3DGSを早期評価 |
| 5 | **GS専門スキルのROIが急上昇**：Netflix・Niantic等でGS専門職が年俸$257K〜 | GS実装スキルへの投資タイミングは今 |

---

*レポート作成：2026年6月2日 | ソース：arXiv / CVPR 2026 / CG Channel / Radiance Fields / UploadVR / befores&afters / TechFundingNews / Khronos / Netflix / Glassdoor*
