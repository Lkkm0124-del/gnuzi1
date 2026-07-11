import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="My Introduction",
    page_icon="👋",
    layout="centered"
)

# 제목
st.title("👋 Hello, GitHub!")
st.subheader("자기소개")

# 기본 정보
name = "홍홍홍길동"
major = "홍홍홍진호"
grade = "안녕하세요"
interest = ["Python", "AI", "Data Analysis"]

st.write(f"**이름:** {name}")
st.write(f"**전공:** {major}")
st.write(f"**학년:** {grade}")

st.write("### 💡 관심 분야")
for item in interest:
    st.write(f"- {item}")

st.write("### ✨ 한마디")
st.success("안녕하세요! Python과 AI를 공부하고 있는 학생입니다. 앞으로 다양한 프로젝트를 GitHub에 업로드할 예정입니다. 😊")
