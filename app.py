import requests

# Replace this with your actual Teams webhook URL
TEAMS_WEBHOOK_URL = "https://netorgft1145305.webhook.office.com/webhookb2/192693be-87de-4fc8-8bd9-376836260dc8@0eadb77e-42dc-47f8-bbe3-ec2395e0712c/IncomingWebhook/23344fa27c4e40009d7495bc98030ff7/76cab651-224b-4fb2-aa60-c5fd12420ed5"

# Function to send a message to Teams using the webhook
def send_message_to_teams(message):
    payload = {
        "text": message
    }
    response = requests.post(TEAMS_WEBHOOK_URL, json=payload)
    return response.status_code, response.text

# Main function to check for specific words and send replies
def auto_reply_to_teams_channel(message):
    # Check if the message contains the word "hello"
    if "Hello"  in message or "hi" in message:
        # Send a response message
        response_code, response_text = send_message_to_teams("Hi there!")
        return response_code, response_text
    elif "How are you" in message :
        response_code, response_text = send_message_to_teams("I am Good!")
        return response_code, response_text
    else:
        return 200, "No action taken."

# Example usage
if __name__ == "__main__":
    teams_message = input("enter message = ")
    status_code, reply_text = auto_reply_to_teams_channel(teams_message)
    print("Status Code:", status_code)
    print("Reply Text:", reply_text)