
https://itchat.readthedocs.io/zh/latest/

pip install itchat


1. send msg to 文件管理助手:

import itchat

itchat.auto_login()
itchat.send('Hello, filehelper', toUserName='filehelper')



2. 如果你想要回复发给自己的文本消息，只需要这样：

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()

