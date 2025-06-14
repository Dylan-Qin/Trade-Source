---
layout: post
categories: paper
title: "IPv6 Large Scale Network Address Translation (NAT)"
author: "BITAG Technical Working Group"
date: 2016-01-14
tags: ['NAT', ' IPv6', ' LSN', ' Network address translation', ' open internet', ' net neutrality', ' BITAG', ' multistakeholder']
---

Executive Summary: The Internet is running out of addresses in the format in which they were originally standardized, known as IPv4, due to aspects of that format which constrain the address space to a relatively “small” number of unique addresses as compared to the burgeoning number of devices requiring those same addresses to function on the Internet. A successor address format, IPv6, has been developed to support as many devices as can conceivably be connected to the Internet for the foreseeable future. While the global transition to IPv6 is in progress, it is going to take a number of years to upgrade all Internet applications and services, consumer electronics devices, and networks to support IPv6. The transition period is also likely to be lengthy given that, among other things, IPv4-only equipment is still being manufactured and sold to consumers. As network operators deploy IPv6 technology into their existing IPv4 networks, IPv4 and IPv6 will thus need to co-exist until the demand for IPv4 services diminishes. Given the amount of time it may take to migrate out of a pure IPv4, or mixed IPv4 and IPv6 network environment, to pure IPv6 service, network operators are employing a variety of techniques to extend the life of IPv4 addressing. One such technique is the use of Large Scale Network Address Translation (also known as Large Scale NAT or LSN). LSN equipment allows a large number of IPv4-enabled end devices to share a single public IPv4 address. Network Address Translation (NAT) functionality has long existed in local/private networks to help network operators manage their network addresses using private address space. NAT functionality is known to adversely impact some Internet applications; wider use of NAT as part of LSN therefore deserves careful examination. The BITAG is interested in LSN given that IP address sharing is a key tool for extending the life of IPv4 during the transition to IPv6.  LSN is likely to affect many players in the Internet ecosystem: ISPs, end users, application providers, equipment vendors, content delivery networks, and third parties such as law enforcement agencies. A broad understanding of problems that may arise has the following benefits: (1) it will help stakeholders to prepare for actions that minimize the impact on end users and applications; (2) it will inform policymakers and regulators of the motivations and trade-offs for the deployment of this technology; (3) it will accelerate the transition to IPv6; and (4) it will more generally help to reduce or preclude friction and/or conflict surrounding use of this technique among stakeholders, as some have argued that Large Scale NAT could be abused by parties for anti-competitive, discriminatory, or other non-technical purposes. LSN Deployments and Impacts: LSN will be deployed in different ways depending on which IPv6 transition technologies are in use. These alternatives are discussed in the body of this paper. For all of these alternatives, there are a variety of technical implications of LSN for end users, ISPs, and application providers to consider. The address sharing enabled by LSN use impacts end users in three primary ways: (1) the number of connections available per user is affected, (2) the ability to uniquely identify an end user device solely via the source IP address is lost, and (3) it becomes much more difficult to reach and maintain connectivity to end user devices.  All of these impacts are present in local/private network implementation of NATs.  Introduction of LSN increases the probability that users will be affected due to sharing of the port number space. The number of users affected by the limitation in port availability may also increase for the same reason.  However, note that a user checking email or performing simple web browsing functions will not be affected by the LSN. Internet Service Providers (ISPs) electing to use LSNs must balance the impacts of new network infrastructure (operational and capital costs) and of engineering this new infrastructure for scalability, resiliency, security, and capacity, as well as meeting mandates to be able to log individual customer IP address assignments, with maintaining an appropriate level of customer service.  In the mobile environment, where every device must be assigned at least one IP address and where simple devices may have limited access to Internet applications, mobile operators have already implemented LSN and faced some of these challenges. However, the continued swift growth in the number of mobile customers and their likely evolution toward expecting wireless Internet service to behave in a manner comparable to wireline service presents new challenges. LSN can have a wide variety of impacts on applications. These may relate to capacity constraints if the LSN is undersized, the handling of multiple connections to the same application server, the loss of IP-based geolocation capability, new logging requirements, and a variety of other factors. Recommendations: BITAG has compiled recommendations regarding steps that can be taken to help ensure optimal user experience, balanced with efficient LSN deployments and operations. Please see the recommendations in the report.

执行摘要：由于IPv4地址格式的限制，其地址空间相对于日益增长的上网设备数量显得相对"狭小"，互联网正面临原始标准化格式IPv4地址枯竭的问题。为此，开发了新一代IPv6地址格式，可为可预见的未来所有可能接入互联网的设备提供支持。尽管全球向IPv6过渡的进程已启动，但升级所有互联网应用服务、消费电子设备和网络以支持IPv6仍需数年时间。考虑到IPv4专用设备仍在生产和销售等因素，过渡期可能相当漫长。在网络运营商将IPv6技术部署到现有IPv4网络的过程中，两种协议必须共存直至IPv4服务需求消退。鉴于从纯IPv4或混合网络环境完全迁移至纯IPv6服务耗时较长，运营商正采用多种技术延长IPv4地址的使用寿命，大规模网络地址转换（LSN）即为其中一种。LSN设备允许多个IPv4终端设备共享单个公共IPv4地址。虽然NAT技术长期存在于局域/私有网络中帮助运营商管理私有地址空间，但已知其会对部分互联网应用产生不利影响，因此LSN中广泛使用NAT需审慎评估。BITAG关注LSN技术，因其作为IPv4向IPv6过渡期间延长地址寿命的关键工具，可能影响互联网生态中的多方主体：包括ISP、终端用户、应用提供商、设备厂商、内容分发网络及执法机构等第三方。全面认识潜在问题具有多重价值：(1) 帮助利益相关方制定预案以最小化对终端用户和应用的影响；(2) 为政策制定者提供技术部署动机与权衡的决策依据；(3) 加速IPv6转型进程；(4) 总体减少因该技术应用引发的利益冲突——有观点认为LSN可能被用于反竞争、歧视等非技术目的。. . LSN部署与影响：根据采用的IPv6过渡技术差异，LSN存在多种部署方案（本报告正文详述）。无论采用何种方案，LSN对终端用户、ISP和应用提供商均会产生多重技术影响。地址共享主要通过三种方式影响终端用户：(1) 限制单用户可用连接数；(2) 无法仅通过源IP唯一识别终端设备；(3) 终端设备可达性与连接稳定性显著降低。这些影响在局域网的NAT实施中同样存在，但LSN因端口号空间共享会提高用户受影响概率，端口可用性限制波及的用户规模也可能扩大。需说明的是，普通网页浏览或邮件收发等基础功能不受LSN影响。采用LSN的ISP需权衡新网络基础设施（运营与资金成本）的投入规模，在确保可扩展性、弹性、安全性和容量的工程化设计，满足客户IP地址分配记录留存要求，与维持适当服务水平之间取得平衡。在移动网络环境中，由于每台设备至少需分配一个IP地址且简易设备对互联网应用的访问能力有限，运营商已先行部署LSN并应对部分挑战。然而移动用户持续激增及其对无线互联网服务体验向有线服务看齐的预期演进，带来了新的挑战。LSN对应用的影响多元：包括设备容量不足导致的性能约束、同一应用服务器的多连接处理、基于IP的地理定位功能失效、新增日志记录要求等诸多因素。. . 建议：BITAG已汇编相关建议以帮助实现最佳用户体验与高效LSN部署运营的平衡。具体建议详见报告内容。

### 研究目的  
该论文旨在探讨IPv6过渡期间大规模网络地址转换（LSN）技术的部署动机、技术影响及潜在问题，为利益相关方（ISP、终端用户、应用提供商等）提供决策依据，推动IPv6转型并减少技术冲突。

### 研究方法  
1. **技术分析**：对比IPv4与IPv6的地址空间差异，阐述LSN作为过渡方案的必要性。  
2. **案例研究**：分析不同LSN部署方案（如移动网络先行应用）的实际效果与挑战。  
3. **影响评估**：从技术、运营、法律等多维度评估LSN对终端用户、ISP和应用提供商的影响。  

### 核心观点  
1. **过渡必要性**：IPv4地址枯竭与IPv6普及缓慢的矛盾需LSN等过渡技术缓解。  
2. **技术影响**：  
   - **终端用户**：连接数受限、设备识别困难、可达性降低（非基础功能场景）。  
   - **ISP**：需平衡成本、扩展性、合规性（如IP记录留存）与服务体验。  
   - **应用提供商**：面临性能约束、地理定位失效、日志记录复杂化等问题。  
3. **移动网络特殊性**：LSN已部分解决设备激增问题，但用户对有线服务体验的期望带来新挑战。  

### 创新点  
1. **系统性分类**：明确LSN影响的三大主体（用户、ISP、应用方）及具体技术表现。  
2. **动态视角**：结合IPv6过渡期的长期性，提出LSN部署需随用户需求和技术演进调整。  
3. **政策关联性**：指出LSN可能被滥用于非技术目的（如反竞争），需政策干预。  

### 潜在影响  
1. **技术层面**：加速IPv6部署，但可能因LSN的副作用延缓部分应用升级。  
2. **商业层面**：ISP需优化LSN架构以降低运营成本，应用提供商需适配技术限制（如开发替代定位方案）。  
3. **政策层面**：为监管机构提供技术参考，防范LSN滥用，推动公平竞争。  

### 总结  
论文通过剖析LSN的技术逻辑与多主体影响，为IPv4/IPv6过渡期的关键问题提供了结构化解决方案框架，兼具技术指导与政策制定价值。

资源链接: [IPv6 Large Scale Network Address Translation (NAT)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2701488)
