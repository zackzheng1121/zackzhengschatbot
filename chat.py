# coding:utf-8

chatbot_dict = {
    "你是什麼時候誕生的": "是2023年的8月7號",
    "請問開發者是誰": "是zackzheng_online",
    "你好": "你好！有什麼可以幫助您的嗎？",
    "今天天氣如何": "抱歉，我不具備查詢天氣的功能。",
    "你會說英文嗎": "我當然會！Hello there!",
    "告訴我一個笑話": "為什麼螞蟻不生病？因為有螞蟻生病，那就是病蟲害了！",
    "什麼是自然語言處理": "自然語言處理是一門人工智能的領域，專注於讓機器理解、解讀和生成人類語言。它涉及文本分析、語義理解、語法分析等技術。",
    "如何建立聊天機器人": "您可以參考這篇教學，使用Python建立聊天機器人：[1](https://www.pluralsight.com/guides/build-a-chatbot-with-python)",
    "如何在聊天機器人中取得回應": "您可以使用字典和條件判斷來實現聊天機器人的回應，參考這個StackOverflow討論：[2](https://stackoverflow.com/questions/71284764/get-response-from-dictionary-in-chatbot)",
    "如何用ChatterBot建立聊天機器人": "您可以參考這篇教學，使用ChatterBot建立自學聊天機器人：[3](https://realpython.com/build-a-chatbot-python-chatterbot/)",
}

help_response = "目前可用的問題有：\n" + "\n".join(chatbot_dict.keys())

print("你好，我是zack的聊天機器人，請問有需要我幫忙的地方嗎？")

while True:
    q = input()
    if q in chatbot_dict:
        print(chatbot_dict[q])
    elif q == "help":
        print(help_response)
    else:
        print("抱歉，我還沒學到，請向開發者聯繫讓我更新到最新的知識。")
