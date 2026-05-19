import numpy as np

def bus_factor(filename, threshold=0.5):
    commit_counts = []
    try:
        # 1. 读取并解析数据
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    try:
                        commit_counts.append(int(parts[0]))
                    except ValueError:
                        continue        
        if not commit_counts:
            print("错误：未找到有效数据。")
            return
        # 2. 从大到小排序
        commit_counts.sort(reverse=True)        
        # 3. 计算累计贡献
        total_commits = sum(commit_counts)
        cumulative_commits = 0
        bus_factor = 0        
        for count in commit_counts:
            cumulative_commits += count
            bus_factor += 1
            # 一旦达到或超过阈值（如 50%），停止计数
            if cumulative_commits >= total_commits * threshold:
                break        
        # 4. 输出结果
        print(f"--- OpenSSL 公交车指数分析 ---")
        print(f"总提交次数: {total_commits}")
        print(f"总开发者数: {len(commit_counts)}")
        print(f"设定的覆盖阈值: {threshold * 100}%")
        print(f"【公交车指数 (Bus Factor)】: {bus_factor}")
        print("-" * 30)        
        # 辅助分析：前几名开发者的具体占比
        for i in range(min(5, len(commit_counts))):
            percentage = (commit_counts[i] / total_commits) * 100
            print(f"第 {i+1} 名开发者贡献占比: {percentage:.2f}%")
    except FileNotFoundError:
        print(f"错误：找不到文件 '{filename}'")
