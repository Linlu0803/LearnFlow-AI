# LearnFlow-AI
AI学习小工具Demo，将中长视频转成清晰文本和结构化笔记
## 💡 技术亮点 (Technical Implementation)

- **容器化部署**：基于 Docker (Python 3.12-slim) 构建，通过多阶段构建优化镜像体积，并集成 FFmpeg 实现音频预处理。
- **高性能 ASR**：集成 `faster-whisper` 模型
- **自动化 Pipeline**：实现从 Bilibili 链接抓取到结构化笔记生成的全自动流转。


## 🛠️ 如何运行 (How to run)

 **Local Docker:**
   - docker build -t learnflow .
   - docker run -p 8501:8501 learnflow

## 🧭 使用步骤 (User Guide)
1. 左侧选择直接输入视频链接🔗 或者 上传本地文件：mp3,mp4,m4a
2. 点击“开始榨取知识”，等待程序解析整理
3. 最终可以得到：
   - 深度学习笔记：AI根据后端制定的prompt生成的总结笔记（带有时间戳），下方可以下载markdown格式
   - 转录原文： 作为辅助，会显示识别的全部文本，方便用户获取源信息。

<img width="1456" height="823" alt="image" src="https://github.com/user-attachments/assets/2ffe98d5-ebe8-499b-b85d-e1904e02a08f" />
<img width="1454" height="703" alt="image" src="https://github.com/user-attachments/assets/9e5e8510-2204-4123-9f9b-1429f0da5bb8" />
<img width="1458" height="389" alt="image" src="https://github.com/user-attachments/assets/53deb3af-b084-4a2d-bdbf-3e7a03b701b8" />
<img width="1466" height="519" alt="image" src="https://github.com/user-attachments/assets/721f5ca7-fa43-4358-b22b-8bb3ff9e8e90" />
<img width="1462" height="836" alt="image" src="https://github.com/user-attachments/assets/d41fd72d-96bf-4bdd-802a-5c18d06a5b43" />
<img width="1462" height="834" alt="image" src="https://github.com/user-attachments/assets/0ed13a23-5f93-4f73-a66d-d4ed3be52aaf" />
<img width="1465" height="820" alt="image" src="https://github.com/user-attachments/assets/8549cbdf-53b6-4a7a-881f-b342431503ca" />
