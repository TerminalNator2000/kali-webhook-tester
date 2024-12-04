Create a new Python script for your webhook listener:

bash
```
nano webhook_server.py
```
Insert server.py: In kali-linux (Save and exit [CTRL + O, Enter, then CTRL + X]

Run the server:
bash
```
python3 webhook_server.py
```
The server will listen on port 8000 for incoming POST requests.

If you're testing on a local machine and need to expose it to the internet, you can use a tunneling tool like ngrok:

Install ngrok (if not already installed):
bash
```
sudo apt install ngrok
```
Start an ngrok tunnel:
bash
```
ngrok http 8000
```
Ngrok will provide a public URL (e.g., https://abcd1234.ngrok.io) that forwards to your local server. Use this URL as your webhook target.

Test Your Webhook Server
Use a tool like curl to send a test POST request:
bash
```
curl -X POST -H "Content-Type: application/json" \
-d '{"url": "http://example.com", "user": "admin"}' \
http://localhost:8000
```

Check the terminal running the server for the printed payload:
css
```
Webhook received:
{"url": "http://example.com", "user": "admin"}
```

