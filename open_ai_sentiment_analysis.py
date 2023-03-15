from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("API_KEY")

# prompt = "Determine whether the sentiment in each of these responses is positive, negative, or neutral:\n\n"
prompt = "Determine what the sentiment of each of these responses is on a scale of 1 - 5, where 1 is the most negative, 3 is neutral, and 5 is positive:\n"

# List of models: https://platform.openai.com/docs/models/gpt-3
responses = [
    "Could do better work next time, currently still progress that needs to be made",
    "Did a good job in the classroom, students listened to them",
    "Amazing work, keep it up!",
    "Not good, not bad",
    "While this was enjoyable enough, it wasn't really great...in fact, I'd go so far as to say it wasn't great at all",
]

for i in range(len(responses)):
    prompt += f"{i + 1}. {responses[i]}\n"

print(prompt)


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

data = response.choices[0].text
sentiments = data.split("\n")

print(sentiments)
print()
print(response)