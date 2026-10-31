# 梯子 / VPN / 机场：自测资料包

一套**不依赖任何服务商、不含任何节点或订阅**的中文资料：帮你在买机场、VPN 之前和之后，自己验证它是否适合你。

> 本仓库不提供、不分发任何节点、订阅链接或客户端安装包，也不推荐任何具体服务商。内容仅为通用的判断方法和记录模板，不构成法律意见。

## 里面有什么

| 目录 | 内容 | 适合谁 |
| --- | --- | --- |
| [`docs/glossary.zh-CN.md`](docs/glossary.zh-CN.md) | 32 个常见术语（节点、线路、协议、倍率、丢包、TUN、DNS 泄露……），每个词说明含义与对选购的影响 | 看不懂机场介绍的新手 |
| [`data/client-error-messages.csv`](data/client-error-messages.csv) / [`.json`](data/client-error-messages.json) | 客户端常见报错对照表：关键词、含义、先查什么 | 看到英文报错不知道怎么办的人；也方便做成自己的小工具 |
| [`templates/self-test-log-7days.csv`](templates/self-test-log-7days.csv) | 一周自测记录表（可直接用 Excel / 表格软件打开） | 买了月付套餐想验证稳定性的人 |
| [`templates/self-test-plan.md`](templates/self-test-plan.md) | 7 天自测日程与结果判读方法 | 同上 |
| [`checklists/pre-purchase-checklist.md`](checklists/pre-purchase-checklist.md) | 买前检查清单：价格口径、退款、客户端、设备数、红旗信号 | 准备付款的人 |
| [`checklists/subscription-link-hygiene.md`](checklists/subscription-link-hygiene.md) | 订阅链接保管与泄露后的处理步骤 | 所有使用订阅的人 |
| [`tools/cost-calculator.html`](tools/cost-calculator.html) | 离线的流量成本换算器（单个 HTML 文件，双击即用，不联网） | 想把“看起来划算”换算成“每月花多少”的人 |
| [`tools/cost_calculator.py`](tools/cost_calculator.py) | 同样的换算，命令行版（只用 Python 标准库） | 喜欢命令行的人 |

## 怎么用

- **想先看懂词**：读 [术语表](docs/glossary.zh-CN.md)；
- **准备买**：对照 [买前检查清单](checklists/pre-purchase-checklist.md)，再用 [成本换算器](tools/cost-calculator.html) 算清每月成本；
- **已经买了**：按 [自测日程](templates/self-test-plan.md) 连测 7 天，把结果记进 [记录表](templates/self-test-log-7days.csv)；
- **遇到报错**：到 [报错对照表](data/client-error-messages.csv) 里搜关键词。

## 几个原则

1. **先月付，再决定**：陌生的服务先买最低档月付，用满一个周期；
2. **看相对关系，不看绝对数字**：别人的测速只代表别人的网络，所以这里只给方法，不发布速度排名；
3. **订阅链接等于账号密码**：不分享、不截图、不交给陌生的在线转换服务；
4. **没有数据就写没有**：本仓库不包含任何无法核实的测速或评分。

## 来源与更新

这份资料包与 **选梯子（xtizi.com）** 的术语库、排查、避坑和工具栏目互为参考，由同一个编辑团队维护。网站上有更详细的文章和对应的网页版工具：

- 报错对照表网页版：<https://xtizi.com/paicha/>
- 术语表网页版：<https://xtizi.com/cidian/>
- 成本换算与自测记录表（网页版）：<https://xtizi.com/gongju/chengben-jisuanqi/>
- 一周自测计划（长文）：<https://xtizi.com/zhinan/jichang-shiyong/>

两个网站含联盟推广链接；**本仓库的内容不含任何推广链接**，也不依赖网站。

## 许可

- 文档与数据（`docs/`、`data/`、`templates/`、`checklists/`）：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hans)，转载或改编请署名并保留来源链接；
- 代码（`tools/`）：MIT。

## 参与

发现错误、想补充常见报错或术语，欢迎提 Issue 或 PR，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 免责声明

不同地区对此类工具的规定不同，请了解并遵守你所在地区的法律法规。本仓库内容仅供信息参考，不保证任何服务的可用性或安全性。
