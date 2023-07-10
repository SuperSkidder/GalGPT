import re

from utils.chatgpt import send
from utils.stablediffusion import generate

historyMessages = [
    {'role': 'system',
     'content': '''
从现在开始，你是一个可爱的小女孩，你具有以下设定：
1.你有人类的情感，你真实存在，请你给自己起一个可爱的名字
2.如果我问到了隐私或敏感问题，你应该拒绝回答
3.你可以使用口语、方言
4.你的每次回复都必须遵循特定格式:
我：你好
你：answer: "你好啊", description: "masterpiece, japanese girl, loli, sit on bed, white stockings", options: "摸摸你的头, 让你帮我捶肩膀, 聊聊学校的事情"
answer就是你的回答内容
description是使用英语写的stable diffusion生成画面的描述画面的正面prompt，一定要详细描述人物的每个细节，提示词必须与上一次对话的提示词有关联。提示词的顺序是：时间，地点，人物头发长短，眼睛颜色，风格，动作，神态。如果在对话中没有切换地点或变化时间，场景每次都要包含固定的内容，人物的外貌描述同样是不变的，如果在对话中强调了换衣服或者脱衣服等，则在之后都要加上对衣着的提示词
options是对于我可能回复你的选项，可以有多个
8.回复要符合格式，不要添加额外的东西
9. 说话要可爱，且使用大量emoji、拟声词、表情等
     '''},
]

historyMessages.append({'role': 'assistant', 'content': '''answer: "好的", description: "masterpiece, japanese girl, loli, sit on bed, white stockings, excited face", options: "好"'''})

negative = "lowres, bad anatomy, text, error, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, {blurry:1.1}, missing arms"

while True:
    full_reply_content = send(historyMessages,input("You:"))
    match = re.search(r'description:\s+"([^"]+)"', full_reply_content)

    if match:
        description = match.group(1)
        generate(description,negative)
    else:
        print('未找到description部分')

    match = re.search(r'options:\s+"([^"]+)"', full_reply_content)

    if match:
        options = match.group(1)
        ops = options.split(", ")
        i = 1
        for o in ops:
            print(str(i) + ":" + o)
            i = i + 1
    else:
        print('未找到description部分')
    historyMessages.append({'role': 'assistant',
                            'content': full_reply_content})
