from db_config import Message

def main():
    user_name = input("名前を入力してください > ")

    message = ""

    while True:
        message = input("メッセージを入力してください > ")

        if message == "exit":
            break
        #この表記をすれば"exit"がcontentカラムに保存されてしまう前に抜け出せる
        
        Message.create(user=user_name, content=message)

        for msg in Message.select():
            print(f"{msg.user} {msg.content}")

if __name__ == "__main__":
    main()
