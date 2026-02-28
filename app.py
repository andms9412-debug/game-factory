import streamlit as st
from pathlib import Path

st.set_page_config(page_title="🎮 Game Factory", layout="wide")

games_dir = Path(__file__).parent / "games"
games = sorted([d.name for d in games_dir.iterdir() if d.is_dir() and (d / "index.html").exists()])

if not games:
    st.error("沒有找到任何遊戲")
    st.stop()

st.sidebar.title("🎮 Game Factory")
selected = st.sidebar.radio("選擇遊戲", games, format_func=lambda x: x.replace("-", " ").title())

html = (games_dir / selected / "index.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=800, scrolling=True)
