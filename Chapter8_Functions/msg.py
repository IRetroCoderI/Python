
messages = ['ily','lol','rofl',"I'm pregnant", 'heyyy ;)']

def showMessages(msgs):
    for msg in msgs:
        print(f"{msg}")

def sendMessages(msgs):
    sentMsgs = []
    
    while msgs: 
        sent = msgs.pop()
        print(f"Sent message: {sent}")
        sentMsgs.append(sent)
    return sentMsgs

sent = sendMessages(messages[:])
print(f"messages : {messages}")
print(f"sent messages : {sent}")