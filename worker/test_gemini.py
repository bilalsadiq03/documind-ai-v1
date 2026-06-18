from gemini_client import generate_readme

response = generate_readme(
    "Say hello in one sentence."
)

print(response)