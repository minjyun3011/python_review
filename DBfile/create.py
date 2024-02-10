from DBfile.db_config import Message

# インスタンスを作成してから保存
message = Message(user="Bob", content="Hello Tom!")
message.save()
# インスタンスを生成しないでcreate
Message.create(user="Tom", content="Hello Bob!")
