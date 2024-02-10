import os
print(os.environ.get("PWD"))
print(os.environ.get("SECRET"))

from dotenv import load_dotenv
load_dotenv()
print(os.environ["SECRET"])  # 存在しなかった場合はKeyError
print(os.environ.get("SECRET"))  # 存在しなかった場合はNone
print(os.environ.get("SECRET", "PUBLIC"))  # 存在しなかった場合は"PUBLIC"

