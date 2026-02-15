from functions.get_file_content import get_file_content
from config import MAX_CHARS

result = get_file_content("calculator", "lorem.txt")
print(f"Length of result: {len(result)}")
print(result.endswith(f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'))
print(result)

result = get_file_content("calculator", "main.py")
print(f"Length of result: {len(result)}")
print(result.endswith(f'[...File "main.py" truncated at {MAX_CHARS} characters]'))
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print(f"Length of result: {len(result)}")
print(result.endswith(f'[...File "pkg/calculator.py" truncated at {MAX_CHARS} characters]'))
print(result)

result = get_file_content("calculator", "/bin/cat")
print(f"Length of result: {len(result)}")
print(result.endswith(f'[...File "/bin/cat" truncated at {MAX_CHARS} characters]'))
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"Length of result: {len(result)}")
print(result.endswith(f'[...File "pkg/does_not_exist.py" truncated at {MAX_CHARS} characters]'))
print(result)