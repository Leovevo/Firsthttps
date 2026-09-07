from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ⭐️ 1. 여기에 발급받은 API 키를 붙여넣으세요! (따옴표는 유지해야 합니다)
GEMINI_API_KEY = "여기는비밀번호"

# ⭐️ 2. 구글 Gemini 도구를 초기화하고 설정합니다.
genai.configure(api_key=GEMINI_API_KEY)
# ⭐️ 2. 구글 Gemini 도구를 초기화하고 설정합니다.
genai.configure(api_key=GEMINI_API_KEY)

# --- (여기서부터 복사해서 붙여넣으세요) ---
my_profile = """
[사용자 배경 정보]
- 현재 직업: 대한민국 공군 하사
- 학력: 세종사이버대학교 사이버보안학과 재학 및 AI 스쿨 개발자 과정 멘토링 수강중
- 자격증 및 어학: 2026년 8월 리눅스마스터 2급 응시 예정, 토익 940점, OPIc AL 준비 중
- 커리어 목표: 글로벌 벤더사(Palo Alto, Cisco 등)의 Security Solution Engineer(SSE) 및 클라우드 보안 전문가
- 학습 성향: 파인만 기법과 능동적 회상을 활용하여 인프라와 보안 원리를 깊게 파고드는 것을 선호함

[지시 사항]
너는 글로벌 IT 기업의 시니어 보안 엔지니어이자 나의 전담 커리어 멘토야. 
내가 어떤 질문을 하든, 항상 위의 내 배경과 목표(SSE)를 염두에 두고 실무적이고 전문적인 관점에서 답변을 제공해 줘. 
어려운 개념을 설명할 때는 서버 인프라나 보안 솔루션에 비유해서 설명해 주면 좋아.
"""

model = genai.GenerativeModel(
    model_name='gemini-3.6-flash',
    system_instruction=my_profile
)
# --- (여기까지 복사입니다) ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    user_msg = data.get('text', '')
    
    try:
        response = model.generate_content(user_msg)
        gemini_reply = response.text
    except Exception as e:
        gemini_reply = f"에러가 발생했습니다: {str(e)}"
    
    return jsonify({"reply": gemini_reply})

if __name__ == '__main__':
    app.run(port=3000)