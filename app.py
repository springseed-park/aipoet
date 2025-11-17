from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.title("인공지능 시인")

# 사이드바에서 API 키 입력받기
with st.sidebar:
    st.header("설정")
    api_key = st.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었을 때만 실행
if api_key:
    # OpenAI API 키 설정
    os.environ["OPENAI_API_KEY"] = api_key
    
    # chatopenai 초기화
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")

    # 프롬프트 템플릿 생성
    prompt = ChatPromptTemplate.from_messages([
        ("system","You are a helpful assistant."),
        ("user","{input}")
    ])

    # 문자열 출력 파서
    output_parser = StrOutputParser()

    # LLM 체인 생성
    chain = prompt | llm | output_parser

    # 시 주제 입력 필드
    content = st.text_input("시의 주제를 입력하세요")

    # 시 작성 요청하기
    if st.button("시 작성하기"):
        if content:
            with st.spinner("시를 작성하는 중입니다..."):
                result = chain.invoke({"input":f"{content}에 대한 시를 써줘."})
                st.write(result)
        else:
            st.warning("시의 주제를 입력해주세요!")
else:
    st.warning("⚠️ OpenAI API 키를 입력해주세요!")