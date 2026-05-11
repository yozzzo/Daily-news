# 3DGS & 4D生成 デイリーレポート — 2026年5月11日

> 収集日: 2026-05-11 | 新規: 17件（論文7 / ニュース・ツール7 / コミュニティ3）
> ソース: arXiv, Radiance Fields, PC Gamer, Digital Production, PlayCanvas, KIRI Engine, NVIDIA Developer Forums, IBTimes JP, ingamenews.com, Niantic Spatial

---

## 今日のサマリー・注目トレンド TOP 5

1. 🚀 **GS学習高速化レース加速** — 53秒学習（Structure-Aware Densification）＆密度制御廃止10×高速（EDGS/CVPR 2026）と2本立て発表。実用的な学習時間短縮が現実に
2. 🎮 **ゲームへのGS本格採用** — フォトリアルゲーム「Snap & Grab」にGS採用。PC Gamerが「私の新お気に入り」と大特集
3. 📦 **フォーマット整備が加速** — Niantic SPZ V4.0（並列圧縮・SH degree 4対応）＆PlayCanvas SplatTransform 2.0（ボクセル空間解析）が相次いでリリース
4. 🇯🇵 **NECが社会インフラ向けGS技術を発表** — 点群データを90%圧縮しスマホでリアルタイム表示。日本発の産業応用が始動
5. 🖥 **ライトフィールドディスプレイ×GS** — CoherentRaster（SIGGRAPH 2026採択）で3Dグラス不要のディスプレイにGSをリアルタイム表示

---

## 注目論文

### 1. CoherentRaster — ライトフィールドディスプレイ向けリアルタイムGS ⭐ SIGGRAPH 2026採択

- **arXiv**: https://arxiv.org/abs/2605.04509
- **コード**: https://github.com/sgj0402/coherent-raster
- **分野**: ライトフィールドレンダリング・3DGS

**概要**:
3Dグラス不要で立体視できる「ライトフィールドディスプレイ」とGS（3D Gaussian Splatting）を組み合わせる際の最大の課題（隣接視点間の重複計算量）を解決した論文。Cross-view Coherent Attribute Reuse（隣接視点間で属性を共有・使い回す仕組み）とView-coherent Remapping（変形されたGPUメモリ効率を補正する仕組み）により、コンシューマー向けGPUでも高品質かつリアルタイムの描画を実現。SIGGRAPH 2026に採択予定。

**何ができるようになったか**: グラスなしで立体視できるディスプレイ（ライトフィールドディスプレイ）でGSシーンをリアルタイムに高品質表示できるようになった。

**解決した課題**: 多視点を同時表示する際の冗長な計算がボトルネックで、従来はリアルタイム表示が困難だった。

---

### 2. Faster 3DGS via Structure-Aware Densification — 53秒学習を実現

- **arXiv**: https://arxiv.org/abs/2604.28016
- **分野**: 3DGS高速化・密度制御

**概要**:
GSの密度制御（どこにGaussianを追加するか判断するプロセス）を根本から改善した論文。従来の「画面上の勾配（変化の大きさ）」を基準にする曖昧な手法から、テクスチャの空間周波数を多スケールで解析して「高周波テクスチャが多い=Gaussianをもっと細かくすべき」と精密に判定する「構造駆動型」手法に変更。結果としてMip-NeRF360データセットで53秒の学習完了（1.5倍高速化）、SSIM・LPIPSともに最高水準を達成。

**何ができるようになったか**: 1分以内に高品質な3DGSシーンを学習可能になった。

**解決した課題**: 従来の密度制御が「どこを細かくすべきか」を正確に判断できず、過密化や無駄な学習ステップが生じていた問題を解決。

---

### 3. EDGS: Eliminating Densification — 密度制御廃止で10×高速収束 ⭐ CVPR 2026採択

- **arXiv**: https://arxiv.org/abs/2504.13204
- **コード**: https://github.com/CompVis/EDGS
- **分野**: 3DGS高速化・初期化

**概要**:
3DGSの学習で最も時間がかかる「Densification（Gaussianを徐々に増やしながら最適化するプロセス）」を根本から廃止した論文。代わりに、最初から複数の学習画像間の対応点を三角測量で密に初期配置し、微細な調整だけで学習を完了させる。結果として収束が10倍速く、使用Gaussian数は半分で同等以上の品質。Gaussianの座標移動距離が従来の1/50に削減された。CompVis（ミュンヘン大学）の研究グループによる成果で、PyTorchコードも公開済み。

**何ができるようになったか**: Gaussianの増殖プロセスなしに、同等品質のシーンを10倍速く学習できるようになった。

**解決した課題**: 密度制御プロセスが3DGS学習の主なボトルネックだった問題を根本から解決。

---

### 4. Fake3DGS — 3DGS操作画像の検出ベンチマーク

- **arXiv**: https://arxiv.org/abs/2604.27590
- **分野**: セキュリティ・フォレンジクス・3DGS

**概要**:
3DGSを使って「見た目にはリアルな、しかし操作された3Dフェイク画像」を系統的に生成し、その検出難易度を測るベンチマーク。形状・外観・空間配置の3種類の操作パターンを定義。従来の2D偽造検出アルゴリズムが3D操作に対してどれだけ脆弱かを実証した。最強の2Dベースラインは混合設定で92.2%の精度だが、クロス編集評価では大幅にドロップする。3D整合性を活用した新しい3D対応検出手法も提案。

**何ができるようになったか**: GS操作によるフォトリアルフェイク画像の系統的な評価が可能になった。

**解決した課題**: 2D偽造検出がGS操作に脆弱だという問題を明示し、3D対応検出手法の必要性を示した。

---

### 5. PAGaS — ピクセル整合1自由度ガウシアン深度推定

- **arXiv**: https://arxiv.org/abs/2604.22129
- **分野**: 深度推定・マルチビューステレオ

**概要**:
3DGSの表現力を「深度推定」に応用した手法。通常の3DGSは高い自由度（位置・スケール・回転・色など）でGaussianを最適化するが、PAGaS（Pixel-Aligned 1DoF Gaussian Splatting）は1ピクセル=1Gaussianとし、動かせる方向をカメラ光軸方向のみ（1自由度）に制限。ピクセルの背投影（カメラ光線）に沿って深度だけを最適化するため、過適合を防ぎながら精密な深度推定が可能。マルチビュー一貫性も担保。ザラゴサ大学・Metaなどの共同研究。

**何ができるようになったか**: GSの表現力を活かした、高精度なマルチビュー深度推定が可能に。

**解決した課題**: 高自由度なGaussian最適化が深度推定で過適合しやすく、一貫性が崩れやすかった問題を解決。

---

### 6. GSsplat — 再学習なしで意味情報つき3D合成

- **arXiv**: https://arxiv.org/abs/2505.04659
- **分野**: 汎用GS・意味理解・フィードフォワード

**概要**:
従来の3DGSはシーンごとに個別の学習が必要だったが、GSsplatは事前学習済みモデルを使い、新しいシーンを見るだけで即座にGSシーンを生成する汎用手法。色情報と意味ラベル（「ここがドア」「ここが机」など）を同時に出力可能。Offset Learning Moduleが幾何的制約を使ってGaussianの位置を精密にグループ管理し、精度と速度を両立。フィードフォワード速度はマルチタスクGSフレームワーク中最速水準。

**何ができるようになったか**: 新しい場所を撮影するだけで、3D構造と意味マップを即座に生成できるようになった。

**解決した課題**: シーンごとの個別学習が必要でリアルタイム用途や大量シーン処理に使えなかった問題を解決。

---

### 7. GSSA-ViT — 気象予測へのGS応用（異色の応用事例）

- **arXiv**: https://arxiv.org/abs/2604.07928
- **分野**: 気象科学・大気科学・GS応用

**概要**:
緯度経度グリッドの各点をGaussianの中心として扱い、大気場（気温・湿度・気圧など）の任意解像度スケールダウン（粗い予測を細かい解像度に変換すること）と気象予測を実現するGSSA-ViT（3D GS-based Scale-Aware Vision Transformer）フレームワークを提案。GS技術が気象・気候科学分野に進出した注目論文。

**何ができるようになったか**: GSの表現力を気象データの高解像度化・予測精度向上に活用可能になった。

**解決した課題**: 気象モデルの解像度変換が従来手法では不連続で品質が低かった問題を解決。

---

## 業界ニュース・ツール

### 8. PlayCanvas SplatTransform 2.0 公開（2026年5月11日）

- **出典**: https://digitalproduction.com/2026/05/11/playcanvas-updates-splattransform-to-2-0/
- **コード**: https://github.com/playcanvas/splat-transform
- **分野**: GS処理ツール・CLIライブラリ

**概要**:
GSシーンの編集・変換CLIツール「SplatTransform」が2.0にメジャーアップデート。主な変更点：
- **ボクセルグリッド導入**: シーンの3D空間を格子状（ボクセル）に分割して構造解析。ナビメッシュ生成などのゲーム・インタラクション用途に応用可能
- **GPU処理フィルター**: `filterFloaters`（孤立したノイズGaussianを除去）・`filterCluster`（まとまりのないGaussianを除去）をGPUで高速実行
- **URL直接入力対応**: ローカルダウンロード不要でリモートGSファイルを処理
- **losslessメッシュ変換**: meshoptimizerを廃止し、平面マージパスに変更してロスレスを実現

**何ができるようになったか**: 単なるファイル変換ツールからGS空間の「インテリジェント解析ツール」に進化。ゲームのナビメッシュ生成やシーン整理が自動化可能に。

---

### 9. Niantic SPZ V4.0 リリース

- **出典**: https://radiancefields.com/niantic-spatial-releases-spz-v4.0
- **GitHub**: https://github.com/nianticlabs/spz
- **分野**: GS圧縮フォーマット

**概要**:
NianticのオープンソースGS圧縮フォーマット「SPZ」がV4.0に更新。主な改善点：
- 圧縮速度3〜5倍向上、ロード速度1.5〜2倍向上
- GZipから6並列ZSTDストリームに移行（属性クラスごとに1ストリーム、並列処理で高速化）
- SH（球面調和関数）degree 4に対応。より精密な視点依存色表現が可能に
- 1000万点の上限を撤廃。数千万GaussianのAEC・測量スケールシーンにも対応
- SH量子化ビット数を3〜8bitで可変設定可能（5bitが実用バランス）

**何ができるようになったか**: GS圧縮ファイルの読み書きが大幅高速化。大規模シーンも扱えるようになった。

---

### 10. KIRI Engine 3DGS Blender addon v4.1

- **出典**: https://radiancefields.com/kiri-engine-releases-v4-1-of-free-3dgs-blender-plugin
- **GitHub**: https://github.com/Kiri-Innovation/3dgs-render-blender-addon
- **分野**: Blenderプラグイン・GS編集

**概要**:
Blender用3DGSレンダリングアドオンがv4.1に更新。Blender 4.5対応。EeveeエンジンとのネイティブGS統合は現時点でこのアドオンが唯一。複数GSオブジェクトを同一シーンに配置可能。HQ Splatモードで静止画の高品質レンダリングも対応。色調整ツール（彩度・明度・コントラスト等）内蔵。Apache 2.0ライセンスで商用利用無料。

**何ができるようになったか**: Blender上でGSシーンを直接レンダリング・編集・書き出し可能に。

---

### 11. Splatrograph API — セットアップ不要のGS変換サービス

- **出典**: https://radiancefields.com/splatrograph-api-for-gaussian-splatting
- **サービス**: https://splatrograph.com
- **分野**: GS APIサービス・クラウド処理

**概要**:
イタリア・ボローニャ発のGS APIサービス「Splatrograph」が話題。開発者Mazeyar Moeiniが自宅のM4 Mac Mini 1台でBrushバックエンドを動かし、複数画像からGSシーンを生成するAPIを無料提供。COLMAP不要・CUDA不要・環境構築不要でブラウザから即利用可能。

**何ができるようになったか**: 技術知識なしでも写真→GS変換をAPIで自動化。プロトタイプ開発に即活用可能。

---

### 12. NVIDIA 3DGRUT — USDZ対応でIsaac Sim 5.0と連携

- **出典**: https://radiancefields.com/nvidia-adds-usdz-support-to-3dgrut-and-beta-for-omniverse-and-isaac-sim
- **GitHub**: https://github.com/nv-tlabs/3dgrut
- **分野**: ロボット開発・シミュレーション・GS

**概要**:
NVIDIAの3DGRUT（3D Gaussian Ray Tracing × Unscented Transform のハイブリッド描画ライブラリ）がUSDZ形式への出力に対応。Omniverse Kit 107.3・Isaac Sim 5.0のベータ機能としてGSシーンをロボットシミュレーター内で直接レンダリング可能に。PLY→USDZ変換スクリプト（`ply_to_usd.py`）も提供。

**何ができるようになったか**: GS撮影した実環境をNVIDIAのロボット開発環境に直接持ち込み、合成学習データとして活用できるようになった。

---

### 13. NEC — 社会インフラ向けGS技術を開発（日本初）

- **出典**: https://jp.ibtimes.com/nec-develops-ai-technology-lighter-3d-infrastructure-models-100858
- **出典2**: https://www.telecompaper.com/news/nec-develops-ai-based-technology-to-compress-and-enhance-3d-digital-twin-data--1570586
- **分野**: インフラ管理・デジタルツイン・日本

**概要**:
NECが独自AI×GSで点群（3Dスキャナーが出力する大量の座標点データ）をリアルに見える高品質3Dに変換する技術を開発。4.4GBの点群データを316MBに（90%圧縮）しながら、ボルトや構造物の細部も精密に再現。スマホ・通常PCでリアルタイム表示が可能。大量の撮影画像不要で既存インフラの点群データから直接変換できる点が特徴。道路・橋・電力設備などの遠隔点検・デジタルツインに応用予定。

**何ができるようになったか**: 道路・橋・設備などのインフラをGSで可視化し、スマホから遠隔でリアルタイム点検できるようになった。

---

### 14. 3D Printing × Gaussian Splatting — GS→物理3D印刷が現実に

- **出典**: https://radiancefields.com/3d-printing-gaussian-splatting
- **分野**: 製造・デジタルファブリケーション・GS

**概要**:
DreamPrintingがVolumetric Printing Primitives（VPP）という新しい変換フレームワークで、GS/NeRFデータを直接3Dプリント命令に変換する技術を発表。通常の3Dプリントは表面形状だけを印刷するが、VPPは内部の密度・光散乱・半透明性まで物理プリンタで再現。毛皮の柔らかさ、雲の淡さ、ガラスの透明感なども印刷可能に。GS/NeRF表現の両方に対応。

**何ができるようになったか**: GS/NeRFで撮影した実物を、見た目そのまま物理的に3Dプリントできるようになった。

---

## コミュニティ・SNS話題

### 15. SplatStream — CUDA不要VulkanネイティブGSレンダラー

- **出典**: https://radiancefields.com/splatstream-pushes-vulkan-based-gaussian-splatting-beyond-vkgs
- **分野**: GSレンダリング・オープンソース

**概要**:
開発者Park氏によるGSレンダラー「SplatStream」がコミュニティで注目。vkgs（Vulkan版GS）の後継だが、CUDA・PyTorch依存ゼロで設計し直されたクリーンな実装。Windows・Linux・macOS Apple Siliconの3プラットフォームで動作。Python APIはgsplatと互換性があり、最小限の変更で既存コードを移行可能。「学習フレームワークに依存しない推論・表示専用」という設計思想が評価されている。

**何ができるようになったか**: PyTorchやCUDAなしで、あらゆるOSでGSシーンを高速レンダリング可能に。

---

### 16. 「Snap & Grab」— 商業ゲームにGS採用 / PC Gamer絶賛

- **出典**: https://www.ingamenews.com/2026/05/gaussian-splatting-in-snap-grab-2026.html
- **分野**: ゲーム開発・商業活用・GS

**概要**:
ブラウザ対応のヒストゲーム「Snap & Grab」が全ゲーム環境をGS表現で構築し、フォトリアルな映像をブラウザで実現。従来の3Dメッシュより大幅に低コストで実写級の画質を実現した点が評価され、PC Gamerやingamenews.comなど主要ゲームメディアが相次いで紹介。Snap Inc.のソフトウェアエンジニアIakov Sumygin氏が開発。

**何ができるようになったか**: ゲームエンジン不要、GS技術だけでインタラクティブなフォトリアルゲームをブラウザで実現。

---

### 17. PC Gamer「Gaussian Splatting is my new favourite thing」— 一般メディアへの波及

- **出典**: https://www.pcgamer.com/hardware/gaussian-splatting-is-my-new-favourite-thing-so-i-hassled-an-ex-epic-artist-to-tell-me-everything-he-knows-about-the-low-cost-photo-real-rendering-technique/
- **分野**: メディア普及・コミュニティ拡大

**概要**:
ゲームメディア最大手のひとつPC Gamerが元Epic Gamesアーティストにインタビューする形でGS技術を大特集。低コストでフォトリアルを実現する革命的技術として、技術者以外の一般ゲームファンに向けて解説。LifeboatニュースにもシンジケートされSNSで拡散中。

**何ができるようになったか**: GS技術が「プロ・研究者専用」という認識から、一般ゲームファン層に広まりつつある転換点。

---

## 開発者向けインサイト

### すぐ使えるツール一覧

| ツール | 用途 | リンク |
|--------|------|--------|
| SplatTransform 2.0 | GS点群のボクセルフィルタリング・ノイズ除去 | `npm i -g @playcanvas/splat-transform` |
| Niantic SPZ V4.0 | PLYより10倍小さく3〜5倍高速な圧縮フォーマット | https://github.com/nianticlabs/spz |
| KIRI Engine Blender Addon v4.1 | Blender 4.5でGSをEeveeレンダリング | https://github.com/Kiri-Innovation/3dgs-render-blender-addon |
| EDGS | 3DGS学習を10×高速化（CVPR 2026採択） | https://github.com/CompVis/EDGS |
| Splatrograph API | 環境構築なし写真→GS変換API（現在無料） | https://splatrograph.com |
| NVIDIA 3DGRUT | GS→USDZ変換 → Isaac Sim 5.0で直接利用 | https://github.com/nv-tlabs/3dgrut |

### 対応すべき動向

**優先度：高**
- **SPZ V4.0への移行検討**: 既存のPLY/GZip運用を見直すタイミング。特に1000万点超の大規模シーンは効果大
- **EDGS + Structure-Aware Densification**: 3DGS学習高速化研究が急進展中（53秒〜10×高速化）。本番パイプラインへの統合検討を

**優先度：中**
- **NVIDIA Isaac Sim 5.0 beta × GS**: GS→USDZ変換でロボット合成データパイプラインに組み込みやすくなった
- **ライトフィールド対応の調査**: CoherentRasterがSIGGRAPH採択。グラス不要3Dディスプレイ向けGSが実用化段階へ

**優先度：中長期**
- **Fake3DGSによるセキュリティ課題**: GSフォレンジクス対策・利用規約整備の検討を開始
- **GS × 3Dプリント**: 製品プロトタイプ・文化財複製など新しいユースケースへの応用検討

---

*本レポートはyozzzo/Daily-newsリポジトリで管理されています。*
