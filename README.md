# 尼普顿充电桩监控面板（玉泉校区）

面向个人使用的尼普顿（浙江尼普顿科技）电动自行车充电桩实时状态监控面板，当前仅覆盖**浙江大学玉泉校区**。

- 仅使用公开设备接口，**无需登录、无需 token、无需抓包**
- 仅依赖 Python 标准库，**无需安装第三方依赖**
- 后台定时轮询，内置 Web 面板实时展示各站点插座状态

## 快速开始

需要 Python 3.8+（仅标准库）。

```powershell
cd D:\Workspace\projects\neptune-charger-monitor
python monitor.py
```

启动后浏览器访问 <http://127.0.0.1:8000>。首次抓取约需数秒，之后每 20 秒自动刷新，面板每 15 秒拉取一次。

## 展示内容

- 顶部汇总：空闲 / 使用中 / 故障 / 总插座数
- 站点卡片：每个站点的插座状态以**逐孔圆点**展示（绿=空闲、橙=使用中、红=故障、灰=其他）
- 自动刷新、在线状态指示、异常提示

## 数据来源与说明

| 项 | 说明 |
| --- | --- |
| 接口 | `POST http://www.szlzxn.cn/wxn/getDeviceInfo`（`devaddress` 定位设备） |
| 状态字段 | 返回 `obj.portstatur` 字符串，每个字符表示一个插座：`0`=空闲、`1`=使用中、`3`=故障 |
| 站点清单 | `stations_yuquan.csv`，来自开源项目 [ZJU-Charger](https://github.com/ZJU-Charger/ZJU-Charger) 的站点数据 |

> 免责声明：本工具仅用于个人学习与状态查看。数据来自第三方公开接口，可能随时失效或变更；请勿高频请求或用于商业用途。接口若失效，仅需更新 `monitor.py` 中的接口地址或 `stations_yuquan.csv` 站点清单。

## 目录结构

```text
monitor.py           # 主程序：轮询 + 内置 HTTP 服务（标准库）
stations_yuquan.csv  # 玉泉校区站点与设备号清单
static/index.html    # Web 面板（原生 HTML/CSS/JS，无外部依赖）
```

## 已知边界

- 仅能获取公开的**插座占用/故障状态**，不含他人订单的剩余充电时间（会话级数据，需本人登录 token）。
- 站点清单为静态维护；新增/迁移站点需手动更新 `stations_yuquan.csv`。
- `areaId` 参数经实测不影响返回结果，`devaddress` 决定具体设备。

## Vercel 部署

项目已包含 `api/status.py` 和 `vercel.json`，可直接部署为 Vercel Serverless Function：静态面板通过 `/api/status` 实时请求公开设备接口。

```powershell
vercel --prod
```

> Vercel Serverless Function 不保持本地轮询进程；每次面板刷新会触发一次数据聚合请求。为减少上游请求，面板默认每 15 秒刷新一次。
