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
<img width="857" height="792" alt="image" src="https://github.com/user-attachments/assets/007c8aae-f310-4247-8b1c-92ae65e019d8" />
<img width="807" height="726" alt="image" src="https://github.com/user-attachments/assets/e44bb2dd-167a-454a-934e-f2466e208994" />
<img width="825" height="750" alt="image" src="https://github.com/user-attachments/assets/d8d68a16-581a-4e92-9849-96765b6f071d" />

<img width="830" height="561" alt="image" src="https://github.com/user-attachments/assets/1d9cf29a-8689-484e-aa1f-aed53ef251e0" />



