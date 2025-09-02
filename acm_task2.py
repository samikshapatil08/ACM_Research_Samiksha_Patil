import re

email_text = """
Hey Alex,  

Hope you're doing well! Just a reminder—our team meeting is set for next Thursday (Sept 7, 2023) at 3:30 pm in Conference Room B.  
Could you also send me the final draft of the marketing report by Tuesday evening?  
I’ll be out of office on Friday, so earlier is better.  

Also, FYI: Sarah (sarah.jones@example.com) will join us remotely, and we should loop in Michael too.  

Thanks,  
John  
Sent from my iPhone  
"""

structured_info = {}

receiver_match = re.search(r"Hey\s+(\w+)", email_text)
structured_info["Receiver"] = receiver_match.group(1) if receiver_match else None

sender_match = re.search(r"Thanks,\s*\n(\w+)", email_text)
structured_info["Sender"] = sender_match.group(1) if sender_match else None

meeting_match = re.search(r"\((.*?)\)\s+at\s+([\d:]+\s*[ap]m)", email_text)
if meeting_match:
    structured_info["Meeting Date"] = meeting_match.group(1)
    structured_info["Meeting Time"] = meeting_match.group(2)

location_match = re.search(r"in\s+(Conference Room \w+)", email_text)
structured_info["Location"] = location_match.group(1) if location_match else None

deadline_match = re.search(r"final draft.*?by (.*?)\?", email_text, re.IGNORECASE)
structured_info["Task Deadline"] = deadline_match.group(1) if deadline_match else None

participants = re.findall(r"([A-Z][a-z]+).*?\(([\w\.-]+@[\w\.-]+)\)", email_text)
structured_info["Participants"] = participants if participants else ["Michael"]

ooo_match = re.search(r"out of office on (\w+)", email_text)
structured_info["OOO Day"] = ooo_match.group(1) if ooo_match else None

print("Extracted Information:\n")
for key, value in structured_info.items():
    print(f"{key}: {value}")
