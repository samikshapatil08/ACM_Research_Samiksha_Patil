import re
from datetime import datetime

def get_day_with_suffix(day_number):
    if 11 <= day_number <= 13:
        return str(day_number) + "th"
    last_digit = day_number % 10
    if last_digit == 1:
        return str(day_number) + "st"
    elif last_digit == 2:
        return str(day_number) + "nd"
    elif last_digit == 3:
        return str(day_number) + "rd"
    else:
        return str(day_number) + "th"


def transform_text(input_text: str) :
    text = input_text
    #changing python and java to emojis
    text = text.replace("Python", "🐍")
    text = text.replace("Java","☕")

    # Changing phone number to redacted
    phone_pattern = r"\d{5}-\d{5}"
    text = re.sub(phone_pattern, "[REDACTED]", text)

    # reformating dates
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    found_dates = re.findall(date_pattern, text)
    for date_str in found_dates:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        
        day = get_day_with_suffix(date_obj.day)
        month = date_obj.strftime("%B")
        year = date_obj.strftime("%Y")
        new_date_format = f"{day} {month} {year}"
        
        text = text.replace(date_str, new_date_format)

    return text

input_example=input("enter string to transform")
transformed_output = transform_text(input_example)
print(transformed_output)

#Sample Input: “Call me at 98123-45678 on 2025-08-23.I love Python more than Java.”
#Sample Output: “Call me at [REDACTED] on 23rd August 2025.I love 🐍 more than ☕.”