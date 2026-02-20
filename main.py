import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found")
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )
    usage_metadata=response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("failed API request")
    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")
    if response.function_calls:
        function_responses = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, args.verbose)
            if not function_call_result.parts:
                raise Exception("Nothing in the list!")
            first_item = function_call_result.parts[0]
            if first_item.function_response is None:
                raise Exception("Nested data is missing!")
            if first_item.function_response.response is None:
                raise Exception("Empty!")
            function_responses.append(first_item)
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
