from ollama import Client

client = Client(host='http://127.0.0.1:11434')

def get_interview_questions(resume_text):
    response = client.chat(
        model='llama3',
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert HR interviewer. "
                    "You MUST output exactly 5 technical interview questions with detailed answers. "
                    "Output MUST be exactly like:\n"
                    "Q1: question\nA1: answer\n"
                    "Q2: question\nA2: answer\n"
                    "Q3: question\nA3: answer\n"
                    "Q4: question\nA4: answer\n"
                    "Q5: question\nA5: answer\n"
                    "DO NOT say anything else. No disclaimers."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Generate the questions and answers based on this resume:\n{resume_text}"
                )
            }
        ]
    )
    return response['message']['content']
