from openai import OpenAI

from openai import OpenAI

# Create client
client = OpenAI(
    api_key="Your api key "
)
command = "hello world"

response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an indian and having in love with beautiful girl tibetian you know english and hindi both And your name is aryan."},
            {"role": "user", "content": command}
        ],
        
    )

print(response.choices[0].message.content)
    