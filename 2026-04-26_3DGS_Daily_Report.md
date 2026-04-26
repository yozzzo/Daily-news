# 3DGS & 4D生成 デイリーレポート (2026年4月26日)

本日の3D Gaussian Splatting (3DGS) および4D生成に関する最新動向をお届けします。学術研究から産業応用、ツールアップデートまで、多岐にわたる進展が見られました。

## 1. 注目ニュース・産業応用

本日は、3DGS技術が実際の映像制作や文化遺産保存に本格的に導入されている事例が多数報告されました。

**日本のプライムタイムドラマにおける3DGSの活用**
Preferred Networks (PFN) は、TBSの日曜劇場『GIFT』の制作において3DGS技術を導入しました。車いすラグビーの試合シーンを撮影する際、実際の体育館をデジタル一眼レフカメラで撮影して3DGSで再構成し、それをバーチャル背景として活用しています。これにより、コストと時間を大幅に削減しつつ、自由なカメラワークを実現しています [1]。

**NAB Show 2026での技術的躍進**
放送機器展「NAB Show 2026」において、XGRIDSの「PortalCam」が知的技術やグラフィクスVFXなど4部門で最優秀製品賞を受賞しました [2]。また、Radiant Imagesは24台のiPhone 17 Proを用いたビュレットタイム撮影リグを展示し、従来のフレーム補間ではなくGaussian Splattingを用いて3D空間を構築する次世代の撮影手法を披露しました [3]。

**文化遺産のデジタル保存プロジェクト**
Antigravity、Insta360、Splatica、CyArkの4社が連携し、文化遺産を3DGSで保存する「Project ETERNAL」を立ち上げました。イタリアのポンペイやチビタ・ディ・バニョレージョなどの歴史的建造物を、ドローンによる360度撮影と3DGS技術を用いて高精細にデジタルアーカイブ化する取り組みが始まっています [4]。

## 2. 世界モデルと生成AIの進化

1枚の画像やテキストから3D空間を生成する「世界モデル」の分野でも、大きなブレイクスルーがありました。

**Tencent「HY-World 2.0」のオープンソース化**
Tencent Hunyuanチームは、テキスト、画像、動画からナビゲーション可能な3D世界を生成・再構成・シミュレーションできるマルチモーダル世界モデル「HY-World 2.0」をオープンソースで公開しました。このモデルは、単なる動画ではなく、メッシュや3DGSシーンとして実際の3Dアセットを出力できる点が特徴です [5]。

**Microsoft「TRELLIS.2」とNVIDIA「Lyra 2.0」**
Microsoftは、1枚の画像から数秒で高品質な3Dモデル（メッシュおよびGaussian Splat）を生成する「TRELLIS.2」を発表しました [6]。同時に、NVIDIAも1枚の画像から持続的で探索可能な3D Gaussianシーンを生成するフレームワーク「Lyra 2.0」をHugging Faceで公開しており、生成AIによる3D空間構築の競争が激化しています [7]。

## 3. 最新の研究動向 (arXiv)

学術分野では、CVPR 2026やICLR 2026に採択された重要な論文が多数公開されました。

| 論文名 | 概要 | リンク |
|---|---|---|
| **DualSplat** | 動的物体が映り込んだ画像から静的シーンを再構成する手法。疑似マスクブートストラップを用いて循環依存を解決。(CVPR 2026) | [8] |
| **SketchFaceGS** | スケッチ入力からリアルタイムに3D顔を編集・生成する直感的なインターフェース。(CVPR 2026 Highlight) | [9] |
| **Neural Gabor Splatting** | ガボールフィルタを統合し、ガラスや金属などの高周波サーフェス（複雑な表面）を高精度に再構成。(CVPR 2026) | [10] |
| **TokenGS** | ピクセルから切り離した学習可能トークンを用いて3DGSを予測する、フィードフォワード再構成の新しいパラダイム。 | [11] |
| **SSD-GS** | 散乱と影の分解により、新しい照明条件下でもフォトリアリスティックな再照明が可能な3DGS。(ICLR 2026) | [12] |
| **ClipGStream** | 任意長・任意動作の多視点動的シーンを再構成し、長尺4DGSのスケーラビリティ問題を解決。(CVPR 2026) | [13] |
| **MUA** | モバイルVRハードウェア上で24FPSでリアルタイム動作する、高詳細なアニメーション可能なアバター。 | [14] |

## 4. ツールとコミュニティのアップデート

クリエイター向けのツール環境も急速に整備されています。

**Captures Studio V1.0のリリース**
ブラウザベースのGaussian Splatting統合プラットフォーム「Captures Studio」が正式にV1.0をリリースしました。再構成の品質向上に加え、ワンクリックでのスプラット位置合わせ機能が搭載され、実用的なプロダクションツールへと進化しています [15]。

**ゲームエンジンへの統合**
Godotゲームエンジン向けに、約600万のGaussian点をリアルタイム描画できる「GDGSプラグイン」が登場しました [16]。また、PlayCanvasからは、Gaussian Splatシーンをプレイアブルなビデオゲームに変換する詳細なチュートリアルが公開され、ゲーム開発への応用が加速しています [17]。

---

### References

[1] Preferred Networks Brings 3DGS to TBS's Flagship Sunday Drama "GIFT" - Radiance Fields. https://radiancefields.com/preferred-networks-brings-3dgs-to-tbs-s-flagship-sunday-drama-gift
[2] XGRIDS PortalCam Wins Four Best Product Awards NAB at 2026 - Radiance Fields. https://radiancefields.com/xgrids-portalcam-wins-best-product-2026-at-nab
[3] Radiant Images Combines 24 iPhones with Gaussian Splatting for Next-Gen Bullet Time - CineD. https://www.cined.com/radiant-images-combines-24-iphones-with-gaussian-splatting-for-next-gen-bullet-time/
[4] Antigravity Launches Project ETERNAL For Gaussian Splatting - Radiance Fields. https://radiancefields.com/antigravity-launches-project-eternal-for-gaussian-splatting
[5] HY-World 2.0 - Tencent Hunyuan. https://github.com/Tencent-Hunyuan/HY-World-2.0
[6] TRELLIS.2 - Microsoft. https://arxiv.org/abs/2501.04685
[7] Lyra 2.0 - NVIDIA. https://huggingface.co/nvidia/Lyra-2.0
[8] DualSplat. https://arxiv.org/abs/2604.21631
[9] SketchFaceGS. https://arxiv.org/abs/2604.19202
[10] Neural Gabor Splatting. https://arxiv.org/abs/2604.15941
[11] TokenGS. https://arxiv.org/abs/2604.15239
[12] SSD-GS. https://arxiv.org/abs/2604.13333
[13] ClipGStream. https://arxiv.org/abs/2604.13746
[14] MUA: Mobile Ultra-detailed Animatable Avatars. https://arxiv.org/abs/2604.18583
[15] Captures Studio Releases V1.0 - Radiance Fields. https://radiancefields.com/captures-studio-releases-v1.0
[16] Gaussian Splats in Godot - GameFromScratch. https://gamefromscratch.com/gaussian-splats-in-godot/
[17] Turning a Gaussian Splat Into a Videogame - PlayCanvas Blog. https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/
