import uuid

def text_in_file(text):
    fname = f'logs/ai_ans/{str(uuid.uuid4())}.txt'
    with open(fname, 'w', encoding="UTF-8") as f:
        f.writelines(text)
        return fname

def save_ai_log(prompt, user, ffname):
    fname = 'logs/log_ai.txt'
    text = f'промпт от @{user}: {prompt} | ответ сохранен или нет в файле: {ffname}\n'
    with open(fname, 'a', encoding="UTF-8") as f:
        f.writelines(text)