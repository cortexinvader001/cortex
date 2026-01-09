from flask import request

def challenge(verify_token: str):
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == verify_token:
        return challenge, 200
    return "Verification failed", 403
    
def event(handler = None):
    data = request.json
    for entry in data.get("entry", []):
        for messaging_event in entry.get("messaging", []):
            sender_id = messaging_event["sender"]["id"]
            message = messaging_event.get("messages",{})
            if "text" in message:
                if handler:
                    handler(sender_id, "text", message["text"])
            elif "attachments" in message:
                for att in message["attachments"]:
                    att_type = att.get("type")
                    att_url = att.get("payload", {}).get("url")
                    if handler:
                        handler(sender_id, att_type, att_url)

    return "EVENT_RECEIVED", 200

  