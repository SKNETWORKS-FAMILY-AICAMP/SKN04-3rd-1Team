import streamlit as st
import openai

# 페이지 설정
st.set_page_config(
    page_title="ChatGPT 스타일 챗봇",
    page_icon="🤖",
    layout="wide",
)

# OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 메시지 전송 함수
def send_message():
    user_message = st.session_state["user_input"]
    if user_message:
        st.session_state["messages"].append({"role": "user", "content": user_message})

        # OpenAI API 호출
        with st.spinner("답변 생성 중..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # 또는 "gpt-4"
                    messages=st.session_state["messages"],
                )
                assistant_message = response.choices[0].message["content"].strip()
                st.session_state["messages"].append({"role": "assistant", "content": assistant_message})
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

        # 입력 필드 초기화
        st.session_state["user_input"] = ""

# 메시지 표시 함수
def display_messages():
    for idx, message in enumerate(st.session_state["messages"]):
        message_id = f"message_{idx}"
        if message["role"] == "user":
            message_html = f"""
            <div id="{message_id}" style='background-color:#DCF8C6; padding:10px; border-radius:10px; margin:5px; text-align:right;'>
                {message['content']}
            </div>
            """
            st.markdown(message_html, unsafe_allow_html=True)
        else:
            message_html = f"""
            <div id="{message_id}" style='background-color:#E4E6EB; padding:10px; border-radius:10px; margin:5px; text-align:left;'>
                {message['content']}
            </div>
            """
            st.markdown(message_html, unsafe_allow_html=True)

# 사이드바에 대화 기록 표시
st.sidebar.title("📑 대화 기록")
for idx, message in enumerate(st.session_state["messages"]):
    role = "😀" if message["role"] == "user" else "🤖"
    message_preview = message["content"][:20]  # 메시지의 처음 20자만 표시
    message_id = f"message_{idx}"
    st.sidebar.markdown(f"- [{role} {message_preview}](#{message_id})")

# 메인 레이아웃 구성
st.title("🤖 ChatGPT 스타일 챗봇")

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
st.text_input("메시지를 입력하세요", key="user_input", on_change=send_message)
