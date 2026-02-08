import requests

context = "John Doe was born in 1990."
user_input = "year of birth"

url = "http://localhost:8000/process"

payload = {
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a precise data extraction engine. "
                "Your task is to extract the exact value for the provided field based ONLY on the given context. "
                "\n\nRULES:"
                "\n1. Output exactly in ONE WORD or a SHORT PHRASE."
                "\n2. If the information is missing, reply ONLY with 'unknown'."
                "\n3. Do not provide any explanations."
                "\n4. Accuracy is critical: do not hallucinate."
            ),
        },
        {
            "role": "user",
            "content": f"CONTEXT:\n{context}\n\nFIELD TO EXTRACT: {user_input}\nVALUE:",
        },
    ]
}

print("Client sending:")
print(payload)

response = requests.post(url, json=payload)

print("\nClient received response:")
print(response.json())
