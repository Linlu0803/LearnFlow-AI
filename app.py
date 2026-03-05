# app.py

import streamlit as st
import os
from pipeline.downloader import download_audio
from pipeline.audio import normalize_audio
from pipeline.asr_v2 import transcribe_audio  
from pipeline.asr_io import save_asr_result
from pipeline.summarizer import generate_summary 

# 终端要先运行虚拟环境.venv: source .venv/bin/activate

# 终端运行命令：streamlit run app.py



# ==============================
# 1. 页面基础配置
# ==============================
st.set_page_config(
    page_title="LearnFlow AI (MVP)",
    layout="centered",
    page_icon="🎧"
)

# ==============================
# 2. 初始化 Session State (核心：防止刷新丢失)
# ==============================
# 我们把需要持久化的数据存入 st.session_state
if "asr_result" not in st.session_state:
    st.session_state.asr_result = None
if "final_note" not in st.session_state:
    st.session_state.final_note = None
if "processed_url" not in st.session_state:
    st.session_state.processed_url = ""

# ==============================
# 3. UI 标题区
# ==============================
st.title("🎧 LearnFlow AI")
st.write("把视频转成**可学习的文字笔记**")

# ==============================
# 4. 输入区
# ==============================
url = st.text_input(
    "请输入 B 站视频链接",
    placeholder="https://www.bilibili.com/video/..."
)

# 如果用户输入了新 URL，清空之前的状态，防止看错
if url != st.session_state.processed_url:
    st.session_state.asr_result = None
    st.session_state.final_note = None

# ==============================
# 5. 执行按钮逻辑
# ==============================
if st.button("🚀 开始榨取知识", type="primary"):
    if not url:
        st.warning("请先输入视频链接")
    else:
        try:
            with st.status("🚀 正在全力处理中...", expanded=True) as status:
                # 1️⃣ 下载音频
                status.write("⬇️ 下载音频...")
                audio_files = download_audio(url)
                raw_audio = audio_files[0]

                # 2️⃣ 标准化音频
                status.write("🎼 标准化音频...")
                # 建议：文件名可以带上 URL 哈希，防止多人冲突，这里先沿用你的 temp/audio.wav
                wav_audio = normalize_audio(raw_audio, "temp/audio.wav")

                # 3️⃣ ASR (这里调用的是带缓存的版本)
                status.write("🧠 语音转文字（ASR 高速版）...")
                asr_result = transcribe_audio(wav_audio)

                # 4️⃣ 保存结果 (保存到本地作为备份)
                status.write("💾 保存转录文本...")
                save_asr_result(
                    asr_result,
                    output_path="temp/asr.json",
                    source_url=url,
                )

                # 5️⃣ AI 总结
                status.write("✨ 正在提取知识精华 (GPT-4o-mini)...")
                final_note = generate_summary(
                    "temp/asr.json",
                    "prompts/summary_cn.txt"
                )

                # 【关键：存入 State】
                st.session_state.asr_result = asr_result
                st.session_state.final_note = final_note
                st.session_state.processed_url = url

                status.update(label="✅ 知识榨取完成！", state="complete", expanded=False)

        except Exception as e:
            st.error(f"处理失败，错误信息: {e}")

# ==============================
# 6. 展示结果区 (放在按钮逻辑外)
# ==============================
# 只要 session_state 里有数据，无论怎么刷新页面，这里都会显示
if st.session_state.final_note and st.session_state.asr_result:
    st.divider() # 视觉分割线
    
    tab1, tab2 = st.tabs(["📝 深度学习笔记", "📄 转录原文"])
    
    with tab1:
        st.markdown(st.session_state.final_note)
        
        # 下载按钮：现在点击它，页面刷新后内容依然在！
        st.download_button(
            label="💾 保存笔记为 Markdown",
            data=st.session_state.final_note,
            file_name="learning_note.md",
            mime="text/markdown",
            key="download_btn" # 给个固定 key 也是好习惯
        )

    with tab2:
        st.text_area(
            "全文文本",
            st.session_state.asr_result["text"],
            height=400
        )
        st.info("提示：如果需要更精细的时间戳，可以查看 temp/asr.json")