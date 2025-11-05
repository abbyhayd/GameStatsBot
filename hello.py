from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

prompt = "Who won the 2025 World Series?"
prompt += "And also provide the final score of game 7 of the 2025 World Series."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

if response != None:
    print(response.text)
else:
    print("broke")