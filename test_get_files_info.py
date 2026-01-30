from functions.get_files_info import get_files_info

print("Result for current directory:")
for line in get_files_info("calculator", ".").splitlines():
    print(f"  {line}")

print("Result for 'pkg' directory:")
for line in get_files_info("calculator", "pkg").splitlines():
    print(f"  {line}")

print("Result for '/bin' directory:")
for line in get_files_info("calculator", "/bin").splitlines():
    print(f"  {line}")

print("Result for '../' directory:")
for line in get_files_info("calculator", '../').splitlines():
    print(f"  {line}")