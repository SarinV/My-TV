import requests
import re

# 源地址
SOURCE_URL = "https://raw.githubusercontent.com/vbskycn/iptv/refs/heads/master/tv/iptv4.m3u"
# 输出文件名
OUTPUT_FILE = "my_tv.m3u"

# 筛选关键词（支持正则，已为您配置好）
# 注意：东方卫视通常标识为"东方卫视"，央视通常为"CCTV"
KEYWORDS = [
    "CCTV",       # 央视
    "江苏卫视",    # 江苏
    "湖南卫视",    # 湖南
    "浙江卫视",    # 浙江
    "东方卫视",    # 上海东方
]

def update_m3u():
    try:
        print(f"正在拉取: {SOURCE_URL}")
        response = requests.get(SOURCE_URL, timeout=30)
        response.encoding = 'utf-8' # 强制UTF-8防止乱码
        lines = response.text.split('\n')
        
        filtered_lines = ["#EXTM3U"] # 头部必须保留
        
        # 遍历每一行寻找匹配项
        # 逻辑：M3U格式通常是两行一组：
        # Line 1: #EXTINF:-1 group-title="...", 频道名
        # Line 2: http://...
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("#EXTINF"):
                # 检查频道名是否包含关键词
                if any(keyword in line for keyword in KEYWORDS):
                    # 如果匹配，保留这一行（频道信息）
                    filtered_lines.append(line)
                    # 并且保留下一行（播放链接）
                    if i + 1 < len(lines):
                        url_line = lines[i+1].strip()
                        filtered_lines.append(url_line)
        
        # 写入文件
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write('\n'.join(filtered_lines))
            
        print(f"更新成功！共筛选出 {len(filtered_lines)//2} 个频道。")

    except Exception as e:
        print(f"更新失败: {e}")
        exit(1) # 报错退出，通知Action失败

if __name__ == "__main__":
    update_m3u()
