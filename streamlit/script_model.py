
import streamlit as st
# OpenAI 대신 로컬 LLM 모델을 사용하기 위한 함수 임포트
from rag import get_chain_result

# 페이지 설정
st.set_page_config(
    page_title="Enco Library Chatbot",
    page_icon="📑",
    layout="wide",
)

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 메시지 전송 함수
def send_message():
    user_message = st.session_state["user_input"]
    if user_message:
        st.session_state["messages"].append({"role": "user", "content": user_message})

        # 로컬 LLM 모델을 사용하여 응답 생성
        with st.spinner("잠시만 기다려 주세용♥"):
            try:
                assistant_message = get_chain_result(user_message)
                st.session_state["messages"].append({"role": "assistant", "content": assistant_message})
            except Exception as e:
                st.error(f"오류 발생!!: {e}")

        # 입력 필드 초기화
        st.session_state["user_input"] = ""

# 메시지 표시 함수
def display_messages():
    for idx, message in enumerate(st.session_state["messages"]):
        message_id = f"message_{idx}"
        if message["role"] == "user":
            message_html = f"""
            <div id="{message_id}" style='background-color:#1478CD; padding:10px 20px; border-radius:10px; margin:5px; text-align:right; width: 450px; float: right;'>
                {message['content']}
            </div>
            """
            st.markdown(message_html, unsafe_allow_html=True)
        else:
            message_html = f"""
            <div id="{message_id}" style='background-color:#495057; padding:10px 20px; border-radius:10px; margin:5px; text-align:left; width: 450px;'>
                {message['content']}
            </div>
            """
            st.markdown(message_html, unsafe_allow_html=True)

# 사이드바에 대화 기록 표시
st.sidebar.title("📑 대화 기록")
role = "😍"
for idx, message in enumerate(st.session_state["messages"]):
    if message["role"] == "user":
        message_preview = message["content"][:20]  # 메시지의 처음 20자만 표시
        message_id = f"message_{idx}"
        st.sidebar.markdown(f"- [{role} {message_preview}](#{message_id})")

# 메인 레이아웃 구성
st.title(" 📖 Enco Library Chatbot")

# 메시지 표시
display_messages()

# 자동 스크롤 스크립트 추가
scroll_script = """
<script>
window.onload = function() {
    var hash = window.location.hash;
    if (hash) {
        var element = document.querySelector(hash);
        if (element) {
            element.scrollIntoView({behavior: "smooth", block: "start"});
        }
    }
}
</script>
"""
st.components.v1.html(scroll_script)

# 입력 창
st.markdown(
    """
    <style>
    .stTextInput {
        padding: 20px 0 0 0;
        position: fixed;
        bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.text_input("메시지를 입력하세요", 
              key="user_input", 
              on_change=send_message,       
              help='''
              질문양식\n
                제목이 {제목}인 책에 대해서 알려줘\n
                {작가이름} 작가의 책을 알려줘\n
                {분야} 책을 알려줘
              ''')