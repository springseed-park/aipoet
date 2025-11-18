# 🎨 AI 시인 (AI Poet)

OpenAI GPT-4o-mini를 활용한 인공지능 시 생성 웹 애플리케이션

## 📖 프로젝트 소개

사용자가 입력한 주제에 대해 AI가 자동으로 시를 작성해주는 웹 애플리케이션입니다. Streamlit과 LangChain을 활용하여 간단하면서도 직관적인 인터페이스를 제공합니다.

## ✨ 주요 기능

- 🔐 OpenAI API 키 입력 지원
- 📝 시 주제 입력 기능
- 🤖 GPT-4o-mini 모델을 통한 시 생성
- 🎯 실시간 시 작성 및 표시

## 🛠️ 기술 스택

- **Python 3.x**
- **Streamlit** - 웹 인터페이스
- **LangChain** - LLM 통합 프레임워크
- **OpenAI GPT-4o-mini** - AI 모델

## 📋 사전 요구사항

1. Python 3.8 이상
2. OpenAI API 키 ([발급 방법](https://platform.openai.com/api-keys))
3. pip 패키지 관리자

## 🚀 설치 방법

### 1. 저장소 클론 또는 파일 다운로드
```bash
# 프로젝트 폴더로 이동
cd your-project-folder
```

### 2. 가상환경 생성 및 활성화 (선택사항, 권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. Streamlit 추가 설치
```bash
pip install streamlit
```

## 💻 실행 방법

### 1. 애플리케이션 실행
```bash
streamlit run app.py
```

### 2. 웹 브라우저에서 자동으로 열림
- 기본 주소: `http://localhost:8501`
- 자동으로 열리지 않으면 위 주소를 브라우저에 직접 입력

### 3. 사용 방법
1. 왼쪽 사이드바에 OpenAI API 키 입력
2. 메인 화면에서 시의 주제 입력 (예: "봄", "사랑", "희망")
3. "시 작성하기" 버튼 클릭
4. AI가 생성한 시 확인

## 📁 프로젝트 구조

```
ai-poet/
│
├── app.py              # 메인 애플리케이션 파일
├── requirements.txt    # 필요한 패키지 목록
├── .env               # 환경 변수 파일 (선택사항)
└── README.md          # 프로젝트 설명 문서
```

## 📝 코드 설명

### app.py 주요 구성요소

1. **라이브러리 임포트**
   - LangChain 관련 모듈
   - Streamlit (웹 인터페이스)
   - dotenv (환경변수 관리)

2. **UI 구성**
   - 제목 설정
   - 사이드바 (API 키 입력)
   - 메인 영역 (주제 입력 및 시 출력)

3. **LLM 체인 구성**
   - ChatPromptTemplate: 프롬프트 구조 정의
   - init_chat_model: GPT-4o-mini 모델 초기화
   - StrOutputParser: 출력 형식 처리

4. **시 생성 로직**
   - 사용자 입력 받기
   - AI에게 시 작성 요청
   - 결과 화면에 표시

## 🔧 환경 변수 설정 (선택사항)

`.env` 파일을 생성하여 API 키를 저장할 수 있습니다:

```env
OPENAI_API_KEY=your-api-key-here
```

## ⚠️ 주의사항

- OpenAI API 사용은 유료입니다 (사용량에 따라 과금)
- API 키는 절대 공개 저장소에 업로드하지 마세요
- 인터넷 연결이 필요합니다

## 🐛 문제 해결

### 일반적인 오류와 해결방법

1. **"ModuleNotFoundError"**
   - 해결: `pip install -r requirements.txt` 재실행

2. **"Invalid API Key"**
   - 해결: OpenAI API 키 확인 및 재입력

3. **"Connection Error"**
   - 해결: 인터넷 연결 확인

## 🔄 향후 개선 아이디어

- [ ] 다양한 시 형식 선택 기능 (자유시, 정형시 등)
- [ ] 시 저장 기능
- [ ] 시 스타일 선택 (낭만적, 서정적, 철학적 등)
- [ ] 다국어 지원
- [ ] 시 이미지와 함께 생성

## 📚 참고 자료

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [LangChain 공식 문서](https://python.langchain.com/)
- [OpenAI API 문서](https://platform.openai.com/docs)

## 📄 라이선스

이 프로젝트는 개인 학습 및 연구 목적으로 자유롭게 사용 가능합니다.

## 👨‍💻 개발자

AI 시인 프로젝트 - LangChain과 Streamlit을 활용한 첫 번째 AI 애플리케이션

---

*마지막 업데이트: 2025년 11월*