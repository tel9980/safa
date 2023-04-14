
<h1 align="center">Semi-Automatic Financial Analysis(safa)</h1>


<p align="center">
    <img alt="GitHub" src="https://img.shields.io/github/license/watalo/safa.svg?color=blue&style=flat-square">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/watalo/safa">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/watalo/safa">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/watalo/safa">
</p>

<p align="center">
本项目旨在为被领导PUA太狠的银行加班🐶节省点时间，多摸点鱼，养点生。</p>
<p align="center">
用财务数据.xlsx直接生成报告模板.docx，剩下的留给自己or交给百度（敬请期待）。
</p>

## 使用说明

### 环境依赖

python环境

> 语言：`python版本 >= 3.8`
> 安装：`git clone https://github.com/watalo/safa.git`
> 依赖：`python -m pip install -r requirements.txt`


ChatGLM-6B
> [参阅THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)
> 也可以直接去[wenda](https://github.com/l15y/wenda)下载网盘的懒人包
> 
> - 因为我的机器显存不够，使用了int4的量化版本模型，在CPU上进行推理，32G内存，跑完6轮推理用了快2个小时。
> `./far/_config.py`中的设置`model='***/model/chatglm-6b-int4'`,本地路径
> 
> - 使用6B版的反而更快，这是什么情况？？因为之前推理过，所有在.cache/中有模型文件，
> `./far/_config.py`中的设置`model='THUDM/chatGLM-6B'`


### 数据准备

- 需要按下表企业财务报表数据完整情况填数据，总共4列(例如:2021|2022|2023|2023M3)
  | 缺失情况 |对应`_text.py`中的模版|填入标记为1的列|备注|
  |:--:|:-:|:-:|-|
  |数据完整| normal|1-1-1-1|成立超3年|
  |缺少第一年数据 | no_year3|0-1-1-1|成立不足3年|
  |缺少第二年数据 | no_year2|0-0-1-1|成立不足2年|
  |缺少第三年数据 | no_year1|0-0-0-1|成立不足1年|
  |当期为年末数据 | all_years|1-1-1-0|报告时间还没出1月报|

- 在`/input/样本1.xlsx`中填写财务数据,<font color="red">如果有缘人懂OCR，可以联系我：</font><link>watalo@163.com</link>
  
> 银行的应该都知道为什么会有这么多奇葩的日期结构吧，如果不知道说明你运气不错，被坑的不多。

### 使用

#### 普通版

- 运行py文件
  - 运行`start.py`
  - 在`/output`中找到生成的🤗`模板.docx`，名字与`.xlsx`文件一样。

- 网页版
  - 运行`webapp.py`启动本地网页后台
  - 浏览器访问：http://127.0.0.1:5000

#### ChatGLM版（推荐使用）
  - 运行`start_aigc.py`
  - 在`/output`中找到生成的🤗`模板.docx`，名字与`.xlsx`文件一样。

## ToDo：
- [x] 项目基本框架
    - [x] 文档结构优化
	- [x] 执行程序：start.py & start_aigc.py
- [x] 标准报告模板：/far
    - [x] 文本模版：_text.py
    - [x] 参数模版：_para.py
- [x] 数据处理模块：
    - [x] 数据读取：_core.py
- [x] UI界面配置：
    - [x] 制作一个简单的webUI界面
- [x] 接入大模型：
  - [x] ChatGLM已成功接入
  - [ ] 优化prompt，完成各版块分析内容生成

## 测试效果

### 整体
- 基本满足的新手摸鱼凑字数的要求了
- 多轮推理之下，越往后，结果越有用

### 分段

#### 资本结构分析

**这段的回复虽然有点罗嗦，但是ChatGLM给出的分析觉得很中肯。不过出现了一些莫名其妙的词。**

  - prompt
    >申请人近三年及最近一期的总资产分别为18,523.79万元、22,805.74万元、22,890.20万元和29,858.36万元；总负债分别为8,598.39万元、11,980.34万元、11,625.73万元和20,519.52万元；资产负债率分别为46.42%、52.53%、50.79%和68.72%。整体来看，申请人资产负债率在0.55上下波动，资产负债结构相对稳定。从债务期限结构看，申请人债务以短期债务为主，流动负债占比高于50%。近三年及最新一期，流动负债分别为1,614.73万元、8,341.09万元、6,348.74万元和16,237.79万元，短期负债占比分别为18.78%、69.62%、54.61%和79.13%。刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)分别为6,375.00万元、4,600.00万元、3,350.00万元和5,500.00万元。刚性负债占比分别为74.14%、38.40%、28.82%和26.80%。短期内需要刚性兑付的债务为3,000.00万元，主要为短期借款3,000.00万元，一年内到期的非流动负债0.00万元。
  - reponse 
    > 从申请人的资产负债结构来看，申请人的资本结构较为稳健。申请人的主要负债为短期债务，短期负债占比高于流动负债占比，表明申请人的主要资本是短期资本，而不是长期资本。在短期内，申请人需要刚性兑付债务，因此需要在短期内大量融资，以应对债务到期。此外，申请人的资产负债率在0.55上下波动，但整体保持在相对稳定的水平。这表明申请人的资产负债比例适中，资本结构合理，可以应对一定范围内的经济波动。申请人的刚性负债占比相对较低，表明申请人的债务风险较小，并且可以通过控制<font color='red'>短期咤融资量</font>来降低债务风险。综上所述，申请人的资本结构较为稳健，短期资本为主，但资产负债率适中，资本结构适度，可以应对一定范围内的经济波动。

#### 盈利能力分析

**这里就有点搞笑了，直接重复了一大段，还出现一些比较搞笑的评价，虽然有点像我的风格。**

  - prompt
    >申请人营业收入出现波动，最近一年营收出现回落，盈利能力有所波动，前三年分别实现营业收入8,538.76万元、18,367.59万元和9,870.21万元，营业成本6,405.84万元、14,079.19万元和7,522.11万元，毛利率分别为7.21%、10.69%和3.77%，期间费用分别为1,531.75万元、2,316.59万元和1,818.74万元，费用收入比分别为17.94%、12.61%和18.43%，实现净利润559.46万元、922.05万元和333.25万元，净利润率分别为6.55%、5.02%和3.38%。最近一期，申请人实现营业收入10,572.49万元，营业成本7,593.08万元，毛利率11.51%，期间费用合计1,403.11万元，投资收益0.00万元，净利润率12.06%。
  - response
    >根据提供的信息，<font color='red'>申请人的营业收入出现波动，最近一年营收出现回落，盈利能力有所波动。前三年分别实现营业收入8,538.76万元、18,367.59万元和9,870.21万元，营业成本6,405.84万元、14,079.19万元和7,522.11万元，毛利率分别为7.21%、10.69%和3.77%，期间费用分别为1,531.75万元、2,316.59万元和1,818.74万元，费用收入比分别为17.94%、12.61%和18.43%。最近一期，申请人实现营业收入10,572.49万元，营业成本7,593.08万元，毛利率11.51%，期间费用合计1,403.11万元，投资收益0.00万元。</font>
    >从最近一期的财务数据中可以看出，申请人的盈利能力有所提高，净利润率从12.06%上升到12.06%，主要是由于投资收益的增加以及毛利率的提高。但是，与前三年相比，申请人的盈利能力仍然有所波动，最近一年营收出现回落，导致净利润率下降。<font color='red'>赏花赏月赏心</font>，申请人的营业收入和净利润率出现波动得<font color='red'>一塌糊涂</font>，但是最近一期的财务数据表明，申请人的盈利能力有所提高，但仍然存在较大的提升空间。

#### 现金流量分析

**这段分析比较有专业范儿了，甩锅的本领很不错**

  - prompt
    > 申请人前三年分别实现净现金流入585.19万元、-1,212.94万元和-657.98万元。其中：经营活动现金净流入0.00万元、0.00万元和0.00万元；投资活动现金净流入-64.53万元、-767.08万元和-81.12万元；筹资活动现金净流入1,899.13万元、-2,692.72万元和-1,616.07万元。
  - response
    > 根据提供的信息，可以分析申请人的前三年分别实现净现金流入585.19万元、-1,212.94万元和-657.98万元。其中：经营活动现金净流入0.00万元、0.00万元和0.00万元；投资活动现金净流入-64.53万元、-767.08万元和-81.12万元；筹资活动现金净流入1,899.13万元、-2,692.72万元和-1,616.07万元。从现金流入角度来看，申请人的前三年都有净现金流入，但是投资活动现金净流入和筹资活动现金净流出的差异较大，这可能与申请人的业务类型和市场环境有关。投资活动现金净流入可能表明申请人在进行某些投资，这些投资可能获得了一定的收益，从而推动了现金流入。筹资活动现金净流出可能表明申请人在筹资方面遇到了一些困难，可能是因为融资需求不足或筹集的资金不能用于经营活动。需要注意的是，以上分析仅仅是根据提供的信息进行的推测，实际情况可能因各种因素而有所不同。

#### 资产质量分析

**挑不出来什么毛病，虽然是废话文学**

  - prompt
    >申请人近三年流动资产分别为8,211.13万元、9,112.60万元、7,986.31万元和14,010.99万元，在总资产构成中流动资产占比分别44.33%、39.96%、34.89%和46.92%。上年末，主要资产构成为固定资产、应收账款、存货、无形资产、应收票据，在总资产构成中的占比分别为52.09%、14.13%、14.02%、12.98%、2.95%。
  - response
    > 申请人的资产质量可以通过总资产和总负债来衡量。根据提供的信息，申请人近三年流动资产在总资产构成中占比逐渐增加，表明申请人的流动性资产质量较高，资产变现能力更强。同时，上年末主要资产构成中固定资产、应收账款、存货、无形资产、应收票据的占比也较低，表明申请人的资产质量相对较高，资产结构相对稳健。然而，需要注意的是，申请人的资产构成中仍然存在一些不确定性，例如无形资产和应收票据等资产的价值难以确定，可能会对资产质量产生影响。另外，申请人的总资产构成中流动资产占比相对较高，可能意味着申请人的资产存在一些短期风险，需要通过合理的资产配置来平衡风险。综合来看，申请人的资产质量较好，但需要结合具体的情况进行分析和评估。

#### 流动性分析

**有很多重复prompt的内容，不过综上所述的内容就够了**

  - prompt
    >申请人近三年及最近一期流动比率分别为5.09、1.09、1.26和0.86，三年平均值为2.07，较年初变化-0.40；申请人近三年及最近一期速动比率分别为3.65、0.84、0.75和0.39，三年平均值为1.41，较年初变化-0.36。
  - reponse
    > 根据 starch的分析，流动比率和速动比率是衡量公司流动性的两个重要指标。以下是对申请人的分析：流动比率申请人的近三年及最近一期流动比率分别为5.09、1.09、1.26和0.86，平均值为2.07。可以看出申请人的流动比率相对较高，但较年初变化均为-0.40。这意味着申请人具有良好的流动性，可以迅速变现其资产和负债。速动比率申请人的近三年及最近一期速动比率分别为3.65、0.84、0.75和0.39，平均值为1.41。速动比率也相对较高，但较年初变化均为-0.36。速动比率表明申请人可以快速转换流动资产为现金或其他流动资产，以满足短期需求八点。综上所述，申请人具有良好的流动性，其流动比率和速动比率均相对较高。但是，需要注意的是，这些指标不能完全反映申请人的流动性，还需要结合其他指标综合考虑。




## bug：

- [x] 2023/04/14: prompt中未添加数据
- [x] 2023/04/13: response中出现了'\r\n'，与python-docx的add_paragraph()冲突



## 最后
<br>
<img src="./img/taomi.png" width="300"/>
<br>
如果觉得本项目有点帮助,you can buy me a coffee.