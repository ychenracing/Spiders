# ChatGPT Project Brief

> 本文件只保存长期稳定、仓库级的信息。当前任务、临时分支、SHA、测试状态和执行进度应保存在当前 Pull Request 正文中。

## 1. Project

- 项目名称：Spiders
- GitHub 仓库：`ychenracing/Spiders`
- 默认分支：`master`
- 系统定位：多个 Python 网络爬虫示例和项目的集合，使用 requests、BeautifulSoup、Scrapy、Selenium 等工具。
- 数据边界：不同爬虫可能把结果保存到 MongoDB、MySQL、Redis 或本地磁盘。

## 2. Purpose and Non-Goals

仓库按目标站点保存独立爬虫，包括 `haofl`、`kongjie`、`qiubai`、`onesixnine`、`flhhkkSpider` 和 `ipproxy`。每个子项目拥有自己的抓取逻辑、依赖、数据模型和存储约定。

仓库文档未把这些项目定义为统一爬虫框架、托管抓取服务或稳定公共 API。不要在缺少目标站点授权、当前接口文档和运行验证的情况下宣称爬虫仍可用。

## 3. Architecture and Module Boundaries

- 每个顶层爬虫目录是相对独立的项目边界。
- `haofl/`：基于 Scrapy 的 haofl.net 爬虫。
- `kongjie/`：requests + BeautifulSoup 爬虫，使用 Redis hash 去重人员。
- `qiubai/`：Scrapy 爬虫，结果写入 MongoDB。
- `onesixnine/`：Scrapy CrawlSpider、Rule 和 LinkExtractor 驱动的全站图片抓取，图片保存本地。
- `flhhkkSpider/`：Scrapy + Selenium 的链接抓取，结果写入 MySQL。
- `ipproxy/`：代理相关爬虫项目；具体边界以目录实现为准。
- `images/`：README 展示用截图，不是生产数据源。

子项目的 item、pipeline、settings、spider 和外部存储配置不能跨目录随意混用。具体数据流必须从目标子项目文件核实。

## 4. Non-Negotiable Constraints

- 运行前确认目标网站当前服务条款、robots 约定、法律要求和访问授权。
- 控制请求频率、并发和重试，避免对目标站点造成不当负载。
- 不得提交网站账号、Cookie、数据库密码、代理秘密或本地绝对路径。
- 不得在仓库中提交抓取到的个人数据、受版权保护的大量内容或未授权数据集。
- 数据库、Redis 和文件输出必须使用任务明确授权的环境，避免覆盖未知数据。
- 站点结构、反爬机制和接口会变化；不得将旧实现状态描述为当前已验证可用。
- 修改一个子项目时优先限定到该目录及其直接依赖。
- 遵循 `AGENTS.md` 的渐进式、影响范围驱动验证策略。

## 5. Authoritative Sources

- 仓库定位和子项目概览：`README.md`
- 工程验证约定：`AGENTS.md`
- 各爬虫实现、依赖和命令：对应顶层子项目目录
- Scrapy 项目设置：对应目录中的 `scrapy.cfg`、settings、items、pipelines 和 spiders（如存在）
- requests/BeautifulSoup 脚本接口：目标脚本及直接调用者
- 数据库/Redis schema 和连接方式：对应项目实现及非秘密配置
- 目标网站规则：目标网站当前公开条款与 robots 信息
- 版本状态：Git 历史、标签和 GitHub Releases（如适用）

## 6. Standard Commands

仓库级 README 未提供统一安装、运行、测试或 lint 命令，各子项目技术栈和外部服务不同。

处理具体爬虫时，应先读取目标目录中的依赖、`scrapy.cfg`、settings、入口脚本和存储配置，再确定最小安全命令。不得凭 Scrapy 或 Python 惯例猜测并报告命令有效。

涉及真实网站或数据库的运行不是默认验收方式；优先使用离线样例、解析单元和受控 mock 验证。

## 7. Important Paths

- `README.md`：仓库和爬虫概览。
- `AGENTS.md`：渐进式验证约定。
- `haofl/`：haofl Scrapy 项目。
- `kongjie/`：requests/BeautifulSoup 与 Redis 去重项目。
- `qiubai/`：Scrapy 与 MongoDB 项目。
- `onesixnine/`：图片 CrawlSpider 项目。
- `flhhkkSpider/`：Scrapy、Selenium 与 MySQL 项目。
- `ipproxy/`：代理相关项目。
- `images/`：说明文档截图。

## 8. CI and Acceptance Entry Points

仓库没有 GitHub Actions workflow，也没有统一自动化验收入口。

- 解析改动优先使用保存的最小 HTML fixture 或 mock response。
- pipeline 改动应验证 item 到目标存储的映射，不应连接未知生产数据库。
- 调度、并发、重试和下载改动应验证请求边界与失败行为。
- 真实网站 smoke 仅在明确授权、低频且不会写入未知系统时执行。
- Definition of Done：适用验收条件满足；已执行检查及外部访问准确记录；未运行项明确标记；没有未解决的合规、数据安全或阻断审查问题。

## 9. Prohibited Actions

- 不得绕过访问控制、验证码、付费墙或网站明确限制。
- 不得进行高并发、拒绝服务式访问或未授权批量下载。
- 不得提交凭证、Cookie、个人信息、数据库转储或受限抓取结果。
- 不得把旧网站结构、旧运行截图或历史博客当作当前可用性证明。
- 不得在未知数据库、Redis 或文件路径上运行有写入副作用的爬虫。
- 不得把未执行的在线抓取或存储验证报告为通过。
- 不得擅自改写 Git 历史、force push、丢弃未知工作或覆盖无关改动。
- 不得根据旧聊天猜测当前分支、SHA、PR 或 CI 状态。

## 10. Context Loading Protocol

1. 新开发任务可以直接使用自然语言提出，不要求预先填写固定 Prompt。
2. 开始任务时先读取本文件。
3. 搜索与任务相关的开放 PR、分支和 Issue。
4. 如果存在匹配工作，从现有现场原地继续。
5. 当前动态任务状态默认维护在 Pull Request 正文。
6. 不强制普通单 PR 任务创建 Issue。
7. 优先读取目标代码、直接调用者、相关测试和直接相关配置。
8. 只有证据不足、状态冲突或影响范围扩大时才扩大读取。
9. 不默认加载完整仓库、完整聊天、完整日志或全部 GitHub Actions 历史。
10. 长对话交接使用 `conversation-continuity-guard`，但 GitHub 当前现场仍是状态权威来源。

## 11. References

- `README.md`
- `AGENTS.md`
- `haofl/`
- `kongjie/`
- `qiubai/`
- `onesixnine/`
- `flhhkkSpider/`
- `ipproxy/`
