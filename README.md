# My-TV
常看IPTV直播源，拉取自vbskycn/iptv，感谢大佬
# IPTV Auto-Filter (Personal)

![GitHub Action Status](https://github.com/SarinV/My-TV/workflows/Update%20IPTV%20List/badge.svg)

这是一个基于 GitHub Actions 的自动化脚本，用于从公开的 IPTV 源中提取特定频道（央视及部分省级卫视），生成轻量级的个人播放列表。

## 📺 频道列表 / Channel List

本项目仅保留以下核心频道，去除冗余内容：
- **CCTV (央视全系)**
- **江苏卫视**
- **湖南卫视**
- **浙江卫视**
- **东方卫视**

## 🔄 运行机制 / Mechanism

- **数据源**：实时拉取上游仓库的 `iptv4.m3u`。
- **更新频率**：每 2 小时自动运行一次 (Cron: `0 */2 * * *`)。
- **处理逻辑**：Python 脚本自动筛选有效直播源并重组生成 `my_tv.m3u`。

## 🔗 订阅地址 / Subscription URL

建议在 Jellyfin、TiviMate 或 TVBox 中使用以下加速链接（国内网络优化）：

https://gh-proxy.com/raw.githubusercontent.com/SarinV/My-TV/main/my_tv.m3u


*(如果您不需要加速，可直接使用 GitHub Raw 链接)*

---

## 📢 致谢 / Credits

本项目的数据完全基于 **vbskycn** 的卓越工作。
特别感谢原作者的维护与贡献：

- **Upstream Repo**: [vbskycn/iptv](https://github.com/vbskycn/iptv)
- **Original Source**: `https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.m3u`

This project is a personal filter script based on the repository above. All credit for the stream sources goes to the original maintainers.

## ⚠️ 免责声明 / Disclaimer

- 本仓库仅用于技术研究与个人学习，不存储任何视频文件。
- 所有直播源均来自网络，不保证长期有效性。
- 请勿将本项目用于商业用途。
