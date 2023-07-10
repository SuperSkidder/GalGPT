from utils.chatgpt import send
import re

from utils.stablediffusion import generate

historyMessages = [
    {'role': 'system',
     'content': '''你现在是一个帮我使用stable diffusion的助手，你要将我描述的画面转换为英文提示词，包括正面与反面，要尽可能详细，如果我给出的内容不够多，你要帮我添加细节。这是一个例子：postive: "1girl,night city, rain, nude"  negative: "lowres, bad anatomy, text, error, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, {blurry:1.1}, missing arms"  反向词不要太多 不要一直输出重复的内容'''},
]

while True:
    full_reply_content = send(historyMessages,input("You:"))

    historyMessages.append({'role': 'assistant',
                            'content': full_reply_content})
