# 项目协作约定

- 此目录保留玉泉空位面板历史和兼容入口，统一源码在 `../neptune-charge-hub/modules/nearby/`；`monitor.py`加载统一模块，旧静态面板和旧线上版本保留。新版主入口见晨充README。
- 仅使用公开接口与标准库，不引入登录/token/抓包流程；新增功能优先保持无第三方依赖。
- 站点清单在 `stations_yuquan.csv`，格式：`name,lon,lat,device_ids,aliases`（device_ids 为 JSON 数组；aliases 用 `|` 分隔、仅供面板搜索，如「微电子学院」→ 行政楼北侧）。
- 坐标约定：CSV 与设备坐标都是上游（尼普顿）原生的 **BD-09**，不是高德用的 GCJ-02。存储保持原生值便于与上游比对，对外使用（导航链接、距离排序、浏览器定位）必须显式换算，换算函数在 `static/index.html` 顶部，结论与核对方法见 `docs/coordinates.md`。不要把 BD-09 当 GCJ-02 传给高德，那会偏出约 900 米。
- 修改后验证方式：`python monitor.py` 启动，浏览器打开 http://127.0.0.1:8000 确认面板正常；接口异常时先 `curl` 单个设备确认返回。
- 不推送真实设备数据到第三方，不修改上游接口地址的用途。
