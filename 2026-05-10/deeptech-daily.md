# 毎朝のディープテック便 — 2026-05-10

本日のディープテック便では、**生物×IT、ドローン、脳波/BCI、技術×バイオ、合成生物学、ロボティクス×バイオ**の6分野を横断し、英語圏・日本・中国・イスラエル・インド・ヨーロッパ・シンガポールから最新プロダクト情報を収集しました。past_products.json（約175件）と照合し、過去に紹介済みのプロダクトを完全に除外した上で、実用化の近さ・ニッチな驚き・SF感・常識を覆す度合いを基準にTop10を選出しました。

| 順位 | プロダクト | 企業 | 地域 | 分野 | 成熟度 | 注目ポイント |
|---:|---|---|---|---|---|---|
| 1 | **Amazon Bio Discovery (ABD)** | AWS | 米国 | 生物×IT | 商用運用開始 | 40以上のAI生物基盤モデル＋ラボインザループで創薬を数週間に短縮。MSKで30万分子設計。 |
| 2 | **Sapient Perception ECHO 10Kセンサー** | Sapient Perception | デンマーク | ドローン | 製品発売（5/6発表） | 世界初ドローン専用10K解像度センサー。1億画素で従来100倍の面積をカバー。 |
| 3 | **Distalmotion Dexter ハイブリッド手術ロボット** | Distalmotion | スイス | ロボティクス×バイオ | 商用展開中 | 4分でセットアップ、125平方フィートで稼働。FDA承認3術式、3,000人以上治療済み。 |
| 4 | **Beinao-1（贝脳-1）半侵襲型BCI** | 清華大学等 | 中国 | 脳波/BCI | 臨床試験中 | 硬膜上設置型128ch電極。7名埋込み済み。世界初BCI手術ライブ配信。 |
| 5 | **Starget Pharma AIスマートターゲットラジオリガンド** | Starget Pharma | イスラエル | 技術×バイオ | Phase 1b臨床試験 | AI設計の放射性「誘導ミサイル」で癌細胞のみ攻撃。診断→治療を同一分子で実現。 |
| 6 | **Airbound ロケット型1円ドローン配送** | Airbound | インド | ドローン | パイロット運用中 | 20歳の創業者。テールシッター設計で配送1回0.01ドル目標。医療物流パイロット実施中。 |
| 7 | **テラドローン モジュール型UAV（防衛装備庁受注）** | Terra Drone | 日本 | ドローン | 量産・納入段階 | 国産ドローン300式・1.15億円受注。GPS遮断下でもSLAM自律飛行。1台約38万円。 |
| 8 | **Andromeda Surgical 自律手術ロボット** | Andromeda Surgical | 米国 | ロボティクス×バイオ | 臨床試験中 | 世界初ロボット支援HoLEP実施。タブレット操作＋GPS様体内ナビ。「手術界のテスラ」。 |
| 9 | **Immunai AMICA-OS × AstraZeneca** | Immunai | イスラエル | 生物×IT | 商用サービス | 単一細胞レベル免疫系AIモデル。AZ提携延長$37.5M。バイオマーカー発見を加速。 |
| 10 | **Taxa Technologics Swap（1週間持続デオドラント）** | Taxa Technologics | 米国 | 合成生物学 | 製品発売段階 | マイクロバイオーム遺伝子編集で1塗り1週間持続。体臭低減＋UV吸収＋蚊よけ。 |

## 詳細解説

### 1位: Amazon Bio Discovery (ABD)

**企業・地域:** AWS（米国）
**分野:** 生物×IT
**成熟度:** 商用運用開始（2026年4月15日ローンチ）
**スコア:** 9.5 / 10

AWSが2026年4月15日にローンチしたAIエージェント型創薬プラットフォーム。40以上のAI生物基盤モデルを搭載し、自然言語でモデルを選択・構成し、候補分子の生成・優先順位付けを行える。CRO（受託研究機関）パートナーと連携した「ラボインザループ」により、計算予測→ウェットラボ実験→結果分析→モデル改良の閉ループを実現。Memorial Sloan Kettering Cancer Centerでは約30万の新規抗体分子を設計し、上位10万候補のテストに着手——従来1年かかる工程を数週間に短縮した。Bayer、Broad Institute、Voyager Therapeuticsでも導入済み。NVIDIA、Alphabet/Isomorphic Labs、OpenAI×Novo Nordiskとの「AI創薬プラットフォーム戦争」が本格化する中、AWSのクラウドインフラ優位性を活かした参入として注目度が極めて高い。

**主要ソース:**
- [pharmaphorum: Amazon launches its AI drug discovery platform](https://pharmaphorum.com/news/amazon-launches-its-ai-drug-discovery-platform)
- [About Amazon: AWS launches AI tool to speed drug discovery research](https://www.aboutamazon.com/news/aws/aws-amazon-bio-discovery-ai-drug-research)
- [GEN: AWS Launches Amazon Bio Discovery Agentic AI](https://www.genengnews.com/topics/artificial-intelligence/aws-launches-amazon-bio-discovery-agentic-ai-to-accelerate-drug-development/)

### 2位: Sapient Perception ECHO 10Kセンサー

**企業・地域:** Sapient Perception（デンマーク）
**分野:** ドローン
**成熟度:** 製品発売（2026年5月6日発表）
**スコア:** 9.3 / 10

世界初のドローン専用10K解像度センサー「ECHO」。1フレームあたり1億画素（従来のドローンセンサーの200万画素と比較して約100倍）で、同一解像度のまま100倍の面積をカバーできる。ECHO（10Kセンシングフロントエンド）、FORGE（オンボード処理モジュール）、IGNITE（エッジAIフレームワーク）の3要素で構成され、地上の処理設備や高帯域データリンク不要でドローン上で直接10K画像を処理する。デンマーク・ウクライナの防衛スタートアップDropla Techと提携し、地雷検知・監視のためのUAVシステムを開発中。€2M pre-seed調達済み。

**主要ソース:**
- [PR Newswire: Sapient Perception Launches ECHO](https://www.prnewswire.com/news-releases/sapient-perception-launches-echo-the-first-10k-sensor-purpose-built-for-uavs-delivering-up-to-100x-greater-area-coverage-at-full-operational-resolution-302763457.html)
- [DRONELIFE: Sapient Perception Launches 10K Drone Sensor](https://dronelife.com/2026/05/06/sapient-perception-10k-drone-sensor/)
- [ArcticStartup: Denmark's Sapient Perception secures €2M](https://arcticstartup.com/sapient-perception-raises-e2m-pre-seed/)

### 3位: Distalmotion Dexter ハイブリッド手術ロボット

**企業・地域:** Distalmotion（スイス・ローザンヌ）
**分野:** ロボティクス×バイオ
**成熟度:** 商用展開中
**スコア:** 9.1 / 10

世界初かつ唯一の「ハイブリッド手術ロボット」を謳うDexter。わずか125平方フィート（約11.6㎡）のスペースで稼働し、標準ドアフレームを通過可能で、標準電源コンセントに接続し、4分以内にセットアップ完了。FDA承認を3術式（鼠径ヘルニア修復、胆嚢摘出、子宮摘出）で取得し、全世界で3,000人以上の患者を治療済み。Series Gで$150Mを調達し、米国のASC（外来手術センター）への展開を加速中。手術ロボットの「da Vinciの巨大さ」問題を根本から覆す小型・移動式アプローチが革新的。

**主要ソース:**
- [Distalmotion公式: DEXTER](https://www.distalmotion.com/dexter)
- [MassDevice: FDA clears Distalmotion Dexter for hysterectomy](https://www.massdevice.com/fda-clears-distalmotion-dexter-surgical-robot-hysterectomy/)
- [MedTech Dive: Distalmotion raises $150M](https://www.medtechdive.com/news/distalmotion-funding-round-asc/805864/)

### 4位: Beinao-1（贝脳-1）半侵襲型BCI

**企業・地域:** 清華大学 / 中関村フォーラム展示（中国）
**分野:** 脳波/BCI
**成熟度:** 臨床試験中（7名埋込み済み）
**スコア:** 9.0 / 10

中国独自開発の半侵襲型BCI。脳の保護膜（硬膜）の上に設置し、脳組織を貫通しないためリスクを低減しつつ、128チャネルの超薄型電極アレイで手の運動領域の神経信号を取得する。7名の脊髄損傷患者に埋め込み済みで全員回復し、運動機能・発話機能の改善を確認。2026年4月15日には世界初のBCI手術ライブストリーミングを実施。Beinao-2が2026年中に臨床検証を開始予定で、今後1年で50〜100名への拡大を計画。NEO（Neuracle社、商業承認済み）とは異なる独立したシステム。

**主要ソース:**
- [CGTN: China completes first live-streamed Beinao No.1 BCI surgery](https://news.cgtn.com/news/2026-04-15/China-completes-first-live-streamed-Beinao-No-1-BCI-surgery-1MmwHSLYfQs/p.html)
- [Xinhua: China's BCI development shifts into high gear](https://english.news.cn/20260328/514d1649035b4af88c84d0add1d36372/c.html)
- [technology.org: China's Coin-Sized Brain Chip](https://www.technology.org/2026/03/23/chinas-coin-sized-brain-chip-is-closing-the-gap-with-elon-musks-neuralink/)

### 5位: Starget Pharma AIスマートターゲットラジオリガンド（STR）

**企業・地域:** Starget Pharma（イスラエル・Ness Ziona）
**分野:** 技術×バイオ
**成熟度:** Phase 1b臨床試験
**スコア:** 8.8 / 10

世界初のAI駆動型放射性分子エンジニアリングプラットフォームを開発。癌細胞のユニークな受容体をAIで特定し、精密に結合する「スマートターゲットラジオリガンド（STR）」を設計する。革新的なのは「セラノスティクス」アプローチ——まず同じ分子でPET画像診断を行い、腫瘍への取り込みを確認してから、より強力なアイソトープに切り替えて治療する。Series Aで$18M調達（累計$38M）。MD Anderson Cancer Centerで臨床試験を開始し、ルイジアナのCMITと製造パートナーシップも締結。

**主要ソース:**
- [CTech: Israeli biotech Starget secures $18 million Series A](https://www.calcalistech.com/ctechnews/article/s1bzrqmd11l)
- [Globes: Israeli oncology treatment co Starget Pharma raises $18m](https://en.globes.co.il/en/article-israeli-oncology-treatment-co-starget-pharma-raises-18m-1001535720)
- [Cancer Focus Fund: Starget Pharma Phase 1b](https://www.cancerfocusfund.com/news/blog-template-khsw7-ya6zk-hf3cr-fj2sw-8bbze)

### 6位: Airbound ロケット型1円ドローン配送

**企業・地域:** Airbound（インド・ベンガルール）
**分野:** ドローン
**成熟度:** パイロット運用中
**スコア:** 8.6 / 10

15歳で創業し、現在20歳のNaman Pushpが率いるインドのドローンスタートアップ。カーボンファイバーフレームのテールシッター（ロケットのように垂直発射）設計で、従来の20分の1のコストで配送を実現。1台の製造コストは$2,000、現在の1回あたり配送コストは₹24（約$0.27）で、2026年末までに₹5（約$0.05）への引き下げを目指す。ベンガルールのNarayana Healthと医療物流パイロットを実施中（血液サンプル、医療検査等を1日10件配送）。$8.65Mのシード資金を調達済み。2027年中頃に1日100万件配送を目標とし、その後米国市場へ進出予定。

**主要ソース:**
- [TechCrunch: India's Airbound bags $8.65M](https://techcrunch.com/2025/10/14/indias-airbound-led-by-20-year-old-bags-8-65m-to-work-toward-one-cent-drone-deliveries-at-scale/)
- [BusinessWire: Airbound Secures $8.65M Seed Funding](https://www.businesswire.com/news/home/20251013510274/en/Bengaluru-Based-Airbound-Secures-$8.65M-Seed-Funding-and-Contract-With-Narayana-Health-to-Enable-One-Cent-Drone-Deliveries)
- [Flying Mag: Tesla-Backed Startup Aims for 1-Cent Drone Deliveries](https://www.flyingmag.com/tesla-backed-airbound-1-cent-drone-delivery/)

### 7位: テラドローン モジュール型UAV（防衛装備庁受注）

**企業・地域:** Terra Drone株式会社（日本）
**分野:** ドローン
**成熟度:** 量産・納入段階（2026年9月納入予定）
**スコア:** 8.5 / 10

防衛装備庁より国産ドローン「モジュール型UAV（汎用型）教育用」300式を受注。総額1億1543万4000円（1台あたり約38万円）。昼間用カメラ、赤外線センサー、教育用特殊モジュールなどを共通プラットフォームに換装可能なモジュール設計を採用。産業点検分野で実績のある自己位置推定技術（SLAM）を搭載し、GPS電波が遮断される電子戦環境下でも自律飛行を維持できる。参入障壁の高い防衛分野において、本格参入から短期間で初受注を実現した点が注目される。

**主要ソース:**
- [PR TIMES: テラドローン、防衛装備庁より国産ドローン300式・1.15億円を受注](https://prtimes.jp/main/html/rd/p/000000414.000020194.html)
- [ITmedia NEWS: 防衛装備庁、国産ドローン300台を1.1億円で導入へ](https://www.itmedia.co.jp/news/articles/2605/09/news024.html)
- [DroneWiki: テラドローンが防衛装備庁より受注](https://drone-wiki.net/media/news20260508/)

### 8位: Andromeda Surgical 自律手術ロボット

**企業・地域:** Andromeda Surgical（米国・サンフランシスコ / YC）
**分野:** ロボティクス×バイオ
**成熟度:** 臨床試験中（ASTRA試験）
**スコア:** 8.3 / 10

世界初のロボット支援HoLEP（RoLEP™）手術を、チリのUniversidad Católicaで実施し、ASTRA臨床試験を開始。タブレットベースの操作インターフェースと、人体内をGPSのようにナビゲートする空間ナビゲーションシステムを搭載。Richard Wolf（内視鏡画像・手術器具）およびQuanta System（ホルミウムレーザー）との戦略提携を発表。Y Combinator出身で、「手術界のテスラ」として、数千症例のデータからAIが手術判断を支援する「スーシェフ（sous surgeon）」機能を開発中。

**主要ソース:**
- [Andromeda Surgical公式](https://www.andromedasurgical.com/)
- [DeviceTalks: Can Andromeda create an autonomous surgical robot?](https://www.devicetalks.com/can-andromeda-create-an-autonomous-surgical-robot-ceo-damiano-makes-case-here-and-devicetalks-west/)
- [Y Combinator: Andromeda Surgical](https://www.ycombinator.com/companies/andromeda-surgical)

### 9位: Immunai AMICA-OS × AstraZeneca

**企業・地域:** Immunai（イスラエル創業 / 米国）
**分野:** 生物×IT
**成熟度:** 商用サービス
**スコア:** 8.1 / 10

2026年5月7日発表。単一細胞解像度の大規模臨床免疫学データセットとAI基盤モデルを統合した「AMICA-OS」で、人間の免疫システムをモデリング。AstraZenecaとの提携を3度目の拡大で2027年まで延長し、最大$37.5Mを受領可能に。腫瘍学の臨床開発におけるバイオマーカー発見、患者層別化（どの患者が臨床試験に参加すべきか）、投与量最適化に活用。2025年には炎症性腸疾患（IBD）研究にも拡大しており、$85Mの別契約も締結。

**主要ソース:**
- [Jerusalem Post: Immunai expands AstraZeneca cancer collaboration](https://www.jpost.com/business-and-innovation/tech-and-start-ups/article-895531)
- [CTech: AstraZeneca expands AI partnership with Immunai](https://www.calcalistech.com/ctechnews/article/bkhaclqcwe)
- [Fierce Biotech: AstraZeneca extends AI immuno-oncology pact with Immunai](https://www.fiercebiotech.com/medtech/astrazeneca-extends-ai-immuno-oncology-rd-pact-immunai)

### 10位: Taxa Technologics Swap（1週間持続デオドラント）

**企業・地域:** Taxa Technologics（米国）
**分野:** 合成生物学
**成熟度:** 製品発売段階
**スコア:** 8.0 / 10

皮膚マイクロバイオーム工学を基盤にした、1回の塗布で1週間持続するデオドラント「Swap」。棚安定性のあるプロバイオティクスクリームで、体臭低減に加えてUV吸収と蚊よけの多機能を実現。亜種レベルの遺伝子編集で、皮膚マイクロバイオームの特定代謝経路を精密に制御する独自技術を持つ。B2B遺伝子工学プラットフォームとしても化粧品・バイオテック企業向けに展開。合成生物学が実験室を出て日用品の棚に並ぶ象徴的プロダクト。

**主要ソース:**
- [Taxa Technologies公式](https://www.taxatech.com/)
- [SynBioBeta: Personal Hygiene's Renaissance, Brought to You by Synthetic Biology](https://www.synbiobeta.com/read/personal-hygienes-renaissance-brought-to-you-by-synthetic-biology)
- [nss G-Club: Summer 2026 Deodorants: microbiome innovations](https://www.nssgclub.com/en/beauty/44938/summer-2026-deodorants-microbiome-whole-body-skincare)

## トレンド所感

本日の10選を俯瞰すると、3つの大きな潮流が見える。

**1. AI創薬プラットフォーム戦争の本格化。** Amazon Bio Discovery（1位）のローンチにより、AWS、NVIDIA（BioNeMo）、Alphabet（Isomorphic Labs）、OpenAI（GPT-Rosalind / Novo Nordisk提携）の4大テックが揃い踏みとなった。クラウドインフラ、GPU、AIモデル、データセットのどこで差別化するかがプラットフォーム選択の鍵になる。Immunai（9位）のような「免疫系特化AIモデル」のバーティカルプレイヤーが大手製薬と直接契約を獲得している点も見逃せない。

**2. ドローンの多極化と専門化。** Sapient Perception（2位）の10Kセンサー、Airbound（6位）の1円配送、テラドローン（7位）の防衛用国産ドローンと、用途・地域・価格帯が一気に多様化している。ドローン＝「空飛ぶカメラ」の時代は終わり、「センシングプラットフォーム」「物流インフラ」「国防資産」としての分化が加速している。

**3. 手術ロボットの民主化。** Distalmotion（3位）の「4分セットアップ・どこでも使える」コンセプトとAndromeda Surgical（8位）の「タブレット＋AI自律支援」は、da Vinci一強だった手術ロボット市場に新しいゲームルールを持ち込んでいる。大型病院の専用ルームから、外来手術センターやグローバルサウスへの展開が現実化しつつある。
