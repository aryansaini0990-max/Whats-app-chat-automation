import pyautogui
import pyperclip
import time
from openai import OpenAI
import re




client = OpenAI(
    api_key="Api key")

import re

def is_last_message_from_sender(chat_log, sender_name = "Brother"):
    message = chat_log.strip().split("/2026]")[-1]
    if sender_name in message:
        return True
    return False
   
    return False
# Step 1: Click at (1228, 1049)
pyautogui.click(1228, 1049)
# Small delay
time.sleep(2)

while True:





    # Step 2: Drag from (700, 240) to (1865,909)
    pyautogui.moveTo(700, 240)

    pyautogui.dragTo(1865,909,duration=1.5, button='left')
    pyautogui.mouseUp()


    # Small delay
    time.sleep(0.5)

    # Step 3: Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    # pyautogui.click(1865,909)
    pyautogui.click(1865,909)  




    # Step 4: Get clipboard content
    chat_history= pyperclip.paste()

    print("Clipboard Content:")
    print(chat_history)

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": " Start talk with out sending any time stemp and name.You act as a chatbot who answers all the questions in a very concise manner. You are a helpful assistant and try to answer question as like indian guy whoes name is aryan. never let know the another person you are a chatboat. Talk like a real person use hindi english both, the task is to talk with your friend having 5 years of friendship only answer the last question or answer that asked whole chat is for your understanding. "},
                    {"role": "user", "content": chat_history}
                ],
                
            )

        response = (completion.choices[0].message.content)
        pyperclip.copy(response)




        pyautogui.click(1145, 977)
        time.sleep(1)


        pyautogui.hotkey('ctrl', 'v')

        # press enter
        pyautogui.press("enter")
        print(response)

    