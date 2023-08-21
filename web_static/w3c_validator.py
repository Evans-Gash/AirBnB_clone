import requests

def validate_html(html_code):
    validation_url = "https://validator.w3.org/nu/?out=json"
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "Custom_HTML_Validator/1.0"
    }
    encoded_data = html_code.encode("utf-8")

    response = requests.post(validation_url, headers=headers, data=encoded_data)
    validation_result = response.json()

    if response.status_code == 200:
        if validation_result["messages"]:
            for message in validation_result["messages"]:
                print(f"{message['type'].capitalize()}: {message['message']} at line {message['lastLine']}")
        else:
            print("No validation errors detected.")
    else:
        print("An error occurred while connecting to the validator.")

# Example usage
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Custom HTML Validator Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>alx</p>
</body>
</html>
"""

validate_html(html_content)
