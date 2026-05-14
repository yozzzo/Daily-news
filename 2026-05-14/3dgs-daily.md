# 3DGS & 4D生成 デイリーレポート｜2026年5月14日（水）

> **新着9件**（論文2件・ニュース4件（うち重複排除後）・コミュニティ3件）  
> 収集ソース：arXiv、Radiance Fields、Befores & Afters、Tom's Hardware、PC Gamer、Autodesk Blog、Jawset、npj Heritage Science、Hugging Face Papers  
> 重複排除基準：`past_3dgs.json` と照合し既出項目を除外

---

## 📋 今日のサマリー

| # | 名前 | 種別 | 分野 | 重要度 |
|---|------|------|------|--------|
| 1 | MAGS-SLAM | 論文 | ロボット・SLAM | ⭐⭐⭐ |
| 2 | XFreq-GS | 論文 | 無線通信・RF場 | ⭐⭐⭐ |
| 3 | Autodesk VRED 2027 × GS | ニュース | CAD・製造業 | ⭐⭐⭐ |
| 4 | 映画『Superman』× 4DGS Framestore | ニュース | 映像制作 | ⭐⭐⭐ |
| 5 | Postshot V1.1 | ツール | 処理ツール | ⭐⭐ |
| 6 | Dioramix | ツール・コミュニティ | プレゼンツール | ⭐⭐ |
| 7 | GS FPS ブラウザゲーム | コミュニティ | ゲーム開発 | ⭐⭐ |
| 8 | The New Yorker × 3DGS | コミュニティ | フォトジャーナリズム | ⭐⭐ |
| 9 | BSH × VRED 2027 事例 | ニュース | 製造業 | ⭐⭐ |

---

## 🔬 注目論文

### 1. MAGS-SLAM — RGBカメラだけで複数ロボットが協力して3D地図を作れる

- **arXiv**: [2605.10760](https://arxiv.org/abs/2605.10760)
- **提出日**: 2026年5月11日
- **著者機関**: ETH Zürich ほか国際共同チーム
- **フルタイトル**: MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction

**何ができるようになったか**

これまでのロボット用3DGSマッピング（SLAM）は、LiDARや深度カメラ（RGB-Dセンサー）が必要でした。今回の「MAGS-SLAM」は**普通のRGBカメラだけ**を使い、しかも**複数のロボットが同時に協力**してフォトリアルな3D地図を作成できる、世界初の連携フレームワークです。

**これまでの課題と解決策**

- 深度センサーは重く・高価で・屋外では精度が低下するため、ロボットの軽量化・低コスト化の障壁だった
- 各ロボットが独立してローカルの3DGSサブマップを構築し、**コンパクトな「要約情報」だけ**を他ロボットに送信する方式を採用
- 深度なしのスケール曖昧性問題を、ジオメトリ・外観の両面からのループ検出で解消
- 既存の複数のRGB-Dベースラインと同等以上の性能をRGBのみで達成

**応用可能性**: 倉庫ロボット・工場点検ドローン群・建設現場マッピング

---

### 2. XFreq-GS — 携帯電波の「見えない3D地図」を複数周波数帯で同時に作る

- **arXiv**: [2605.11432](https://arxiv.org/abs/2605.11432)
- **提出日**: 2026年5月12日
- **フルタイトル**: XFreq-GS: Cross-Frequency Wireless Radiation Field Reconstruction with 3D Gaussian Splatting

**何ができるようになったか**

Gaussian Splattingを**無線通信の電波場（RF場）再構成**に応用。従来手法は1つの周波数帯しか扱えなかったが、本研究では**異なる周波数帯（例：4G/5G/Wi-Fi）の電波強度マップを共通の3D幾何学情報から同時に生成**できるようになった。

**これまでの課題と解決策**

- 既存手法は各周波数帯に対して別々にモデルを学習する必要があり、計算コストが高かった
- 共有の3D幾何学形状に「周波数適応型RF属性」を付与する独自表現「AOS（Adaptive Orthographic Splatting）」を開発
- 各Gaussianプリミティブが複数周波数の電波挙動を同時に保持

**応用可能性**: 基地局配置最適化・ビル内電波デッドスポット検出・通信インフラのデジタルツイン

---

## 📰 業界ニュース

### 3. Autodesk VRED 2027 × Gaussian Splatting — 自動車・製造業の本格導入が始まった

- **発表**: 2026年4月16日
- **BSH事例公開**: 2026年5月8日
- **公式URL**: [What's New in Alias and VRED 2027](https://blogs.autodesk.com/design-studio/2026/04/16/whats-new-in-alias-and-vred-2027/)
- **BSH事例**: [BSH Adopts Gaussian Splats in VRED 2027](https://blogs.autodesk.com/design-studio/2026/05/08/bsh-adopts-gaussian-splats-in-vred-2027-for-high-fidelity-visualization/)

**何ができるようになったか**

Autodesk VREDはVW・BMW・メルセデス等の自動車メーカーを中心に広く使われているCAD可視化ソフト。このVREDが**Gaussian Splat（PLYファイル）のネイティブインポートと表示に対応**。

- PLYファイルをインポートしてCADモデルと同一シーンに配置できる
- GSシーンとCADモデルが**影を落とし合う**インタラクション
- VulkanによるGPUレイトレーシングで高速レンダリング
- GSオブジェクトを剛体物理シミュレーションに組み込める

**BSH（ボッシュ/シーメンス家電）の採用事例**

「製品を置く部屋の背景を3DGSでスキャンするだけで、製品と周囲の反射・影をリアルに合成できる」→ 家電・家具・インテリア業界の可視化ワークフローを大幅短縮

---

### 4. 映画『Superman』で4D Gaussian Splattingが長編映画に初登場 — Framestore × Infinite Realities

- **記事**: [Framestore showcases the 4D Gaussian Splatting used for 'Superman'](https://beforesandafters.com/2026/02/13/framestore-showcases-the-4d-gaussian-splatting-used-for-superman/) — Befores & Afters, 2026年2月13日
- **Art of VFX**: [Superman: Framestore Brings 4D Gaussian Splatting to the Big Screen](https://www.artofvfx.com/superman-framestore-brings-4d-gaussian-splatting-to-the-big-screen/)
- **Radiance Fields**: [Gaussian Splatting in Superman](https://radiancefields.com/gaussian-splatting-in-superman)

**何ができるようになったか**

VFXスタジオFramestoreが映画『Superman』のクリプトン星の両親のホログラムシーン**約40ショット**に4D Gaussian Splattingを採用。**4DGSが長編映画のファイナルピクセルVFXとして初めて本格活用された**。

**制作プロセス**

1. Infinite Realitiesの球形「Deus Capture Stage」に**192台のカメラ**を設置
2. ブラッドリー・クーパーとアンジェラ・サラフィアンを24fpsで撮影（2分のパフォーマンス）
3. 機械学習で各視点から4DGSを学習 → PLYシーケンスとしてHoudini（GSOPSプラグイン使用）に取り込みVFX仕上げ
4. 撮影後にカメラアングル・焦点距離を自由に変更可能

> *「まるで実写映像のように見えるのに、完全に制御可能なパフォーマンスが手に入る」* — VFXスーパーバイザー Stephane Ceretti

---

### 5. Postshot V1.1 リリース（Jawset）— VRプレビュー・測光補正・新選択ツール追加

- **リリースノート**: [Postshot User Guide Release Notes](https://www.jawset.com/docs/d/Postshot+User+Guide/Release+Notes)
- **ダウンロード**: https://www.jawset.com/builds/postshot/windows/（Windows専用・全プラン無料）

**主要アップデート**

| 機能 | 内容 |
|------|------|
| 🥽 VRヘッドセットプレビュー | エディタからVRデバイスで直接GSシーンを確認 |
| 📸 Photometric Compensation | 複数カメラ間の露出・色温度のばらつきを自動補正 |
| 🖱 新選択ツール | ラッソ選択・矩形選択を追加 |
| 📁 フォーマット拡張 | Pix4D OPF形式・SPZシーケンス対応 |

Photometric Compensationは、ドローン航空撮影や不動産スキャンなど「異なる時間帯・照明環境で撮影した写真を混ぜる」ユースケースで特に効果大。

---

## 💬 コミュニティ・SNS話題

### 6. ブラウザでGSのFPSゲームが動く！— Tom's Hardware & PC Gamer が大きく報道

- **Tom's Hardware**: [Developer creates a basic first person shooter game using Gaussian splats](https://www.tomshardware.com/software/programming/developer-creates-a-basic-first-person-shooter-game-using-gaussian-splats-and-you-can-play-it-for-free-in-your-browser)
- **PC Gamer**: [This photorealistic FPS runs in browser thanks to 'Gaussian Splatting'](https://www.pcgamer.com/hardware/this-photorealistic-fps-runs-in-browser-thanks-to-gaussian-splatting-which-is-now-my-new-favorite-thing/)
- **PlayCanvas解説**: [Turning a Gaussian Splat Into a Videogame](https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/)
- **開発者**: Iakov Sumygin（Snap Inc エンジニア）

**技術的な革新**

Gaussian Splattingの根本的欠点「見た目だけで物理的実体がない（壁をすり抜ける）」問題を解決した実装事例。

- 廃墟の実写GSScanから**衝突判定コリジョンメッシュを自動生成**
- ベイクしたライティンググリッドでNPCキャラに光を当てる
- Recastナビメッシュで8体のNPCが経路探索
- 合計**68MB**の完全なFPSゲームがブラウザで無料プレイ可能
- PlayCanvasプロジェクト全体はオープンソース公開

---

### 7. The New Yorker が3DGSをフォトジャーナリズムに活用

- **Radiance Fields記事**: [Gaussian Splatting at the New Yorker](https://radiancefields.com/gaussian-splatting-at-the-new-yorker)
- **担当者**: Sam Wolson（Visual Features Editor, The New Yorker）

The New Yorkerが3DGSを使った**初の主要報道メディア事例**。NY周年記念号でアーティスト Lorna Simpsonのポートレートを空間的に探索できる形式で公開。「GSはAI生成ではなく実際の現場記録から構築されるため、ファクトチェックの観点で説明しやすい」と評価。

---

### 8. Dioramix — GSシーンを「プレゼン資料」にする新ツール、Webサイト公開

- **Radiance Fields**: [Olli Huttunen Announces Dioramix](https://radiancefields.com/olli-huttunen-announces-dioramix)
- **IK3D紹介**: [Dioramix — Olli Huttunen Just Built the Storytelling Tool](https://ik3d.fr/dioramix-olli-huttunen-just-built-the-storytelling-tool-gaussian-splats-have-been-begging-for/)
- **開発者**: Olli Huttunen（フィンランド）

Gaussian Splattingで作った3Dシーンに**注釈・ボタン・画像カルーセル・動画・PDFを埋め込んで**インタラクティブなプレゼンテーションを作れるブラウザツール。「PowerPoint for 3D models」と表現される。Webサイト公開済み・エディターはベータ開発中。

---

## ⚙️ 開発者向けインサイト

### 🔴 今すぐ対応すべき動向

1. **Autodesk VRED 2027 GS対応** — 製造業・自動車クライアントがいる場合、PLY形式でのGSデータ納品ワークフロー整備を検討。CADモデルとGSシーンの合成による「デジタルモックアップ」の需要が急増予測。

2. **Postshot V1.1 無料アップデート** — Photometric Compensationにより、ドローン撮影・不動産スキャンなど「複数条件の写真が混在する案件」の品質向上。Windows環境なら即アップデート推奨。

### 🟡 参考になるアーキテクチャ

3. **MAGS-SLAM** — 「各エージェントがローカルサブマップを構築し、コンパクトな要約だけを共有する」アーキテクチャは、分散3Dスキャン・マルチカメラネットワーク設計に応用可能。コード公開予定。

4. **GS × インタラクティブゲーム** — Iakov SumyginのPlayCanvasプロジェクトはオープンソース。「コリジョンメッシュ生成→ライティングベイク→NPCナビメッシュ」実装の参考に。

### 🟢 視野に入れておく動向

5. **XFreq-GS** — 通信インフラ・スマートビルディング・IoT環境マッピングで「電波の死角を3D可視化」するニーズへの対応技術として注目。

6. **Dioramix** — 不動産・文化財・教育向け「GSシーンをわかりやすく見せる」ツール市場が拡大中。ベータ版登録を検討。

---

## 📎 ソース一覧

| # | タイトル | URL |
|---|---------|-----|
| 1 | MAGS-SLAM arXiv | https://arxiv.org/abs/2605.10760 |
| 2 | XFreq-GS arXiv | https://arxiv.org/abs/2605.11432 |
| 3 | Autodesk VRED 2027 発表 | https://blogs.autodesk.com/design-studio/2026/04/16/whats-new-in-alias-and-vred-2027/ |
| 4 | BSH × VRED 2027 事例 | https://blogs.autodesk.com/design-studio/2026/05/08/bsh-adopts-gaussian-splats-in-vred-2027-for-high-fidelity-visualization/ |
| 5 | Superman Framestore B&A | https://beforesandafters.com/2026/02/13/framestore-showcases-the-4d-gaussian-splatting-used-for-superman/ |
| 6 | Superman Art of VFX | https://www.artofvfx.com/superman-framestore-brings-4d-gaussian-splatting-to-the-big-screen/ |
| 7 | Gaussian Splatting in Superman | https://radiancefields.com/gaussian-splatting-in-superman |
| 8 | Postshot Release Notes | https://www.jawset.com/docs/d/Postshot+User+Guide/Release+Notes |
| 9 | GS FPS Tom's Hardware | https://www.tomshardware.com/software/programming/developer-creates-a-basic-first-person-shooter-game-using-gaussian-splats-and-you-can-play-it-for-free-in-your-browser |
| 10 | GS FPS PC Gamer | https://www.pcgamer.com/hardware/this-photorealistic-fps-runs-in-browser-thanks-to-gaussian-splatting-which-is-now-my-new-favorite-thing/ |
| 11 | PlayCanvas FPS Tutorial | https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/ |
| 12 | GS at The New Yorker | https://radiancefields.com/gaussian-splatting-at-the-new-yorker |
| 13 | Dioramix Radiance Fields | https://radiancefields.com/olli-huttunen-announces-dioramix |
| 14 | Dioramix IK3D | https://ik3d.fr/dioramix-olli-huttunen-just-built-the-storytelling-tool-gaussian-splats-have-been-begging-for/ |
