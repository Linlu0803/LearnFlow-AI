# LearnFlow-AI
AI学习小工具Demo，将中长视频转成清晰文本和结构化笔记
## 💡 技术亮点 (Technical Implementation)

- **容器化部署**：基于 Docker (Python 3.12-slim) 构建，通过多阶段构建优化镜像体积，并集成 FFmpeg 实现音频预处理。
- **高性能 ASR**：集成 `faster-whisper` 模型
- **自动化 Pipeline**：实现从 Bilibili 链接抓取到结构化笔记生成的全自动流转。


## 🛠️ 如何运行 (How to run)

1. **Local Docker:**
   docker build -t learnflow .
   docker run -p 8501:8501 learnflow
