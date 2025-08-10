import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    flags = []
    prompt_parts = []

    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            prompt_parts.append(arg)

    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            flags.append(arg)

    full_prompt = " ".join(prompt_parts)

    if len(prompt_parts) < 2:
        print("AI Code Assistant:")
        print("Missing user prompt.")
        print("Usage: python main.py '<your prompt>' args...")
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=full_prompt)]),
    ]

    response = client.models.generate_content(model = model, contents= messages)

    print(response.text)
    if "--verbose" in flags:
        print(f"User prompt: {full_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
