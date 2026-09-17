# 项目协作约定

- 本项目是尼普顿充电桩监控面板（玉泉校区），`monitor.py` 是正式源码，`static/index.html` 是面板，二者共同构成运行体；`README.md` 面向使用者。
- 仅使用公开接口与标准库，不引入登录/token/抓包流程；新增功能优先保持无第三方依赖。
- 站点清单在 `stations_yuquan.csv`，格式：`name,lon,lat,device_ids`（device_ids 为 JSON 数组）。
- 修改后验证方式：`python monitor.py` 启动，浏览器打开 http://127.0.0.1:8000 确认面板正常；接口异常时先 `curl` 单个设备确认返回。
- 不推送真实设备数据到第三方，不修改上游接口地址的用途。
