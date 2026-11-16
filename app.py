import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 메뉴 추천", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라줍니다!")

# 추천할 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정해 보세요)
menu_list = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "비빔밥",
    "칼국수",
    "햄버거",
    "파스타",
    "마라탕",
    "순대국밥",
    "샌드위치",
    "떡볶이",
]

# 추천 버튼 생성
if st.button("🎲 점심 메뉴 뽑기!", use_container_width=True):
    # random.choice()를 사용해 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(menu_list)

    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}** 입니다! 맛있게 드세요! 😋")
