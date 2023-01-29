import os
import openai
def GPT_Completion(query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    #openai.api_key = "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"
    response = openai.Completion.create(
    model = "curie:ft-personal-2023-01-29-16-21-59",
    prompt = query,
    temperature = 0.7,
    top_p = 1,
    max_tokens = 50,
    frequency_penalty = 0,
    presence_penalty = 0
    )
    return print(response.choices[0].text)

query = "Is 67 an even natural number? You say ->"
result = GPT_Completion(query)
print(result)