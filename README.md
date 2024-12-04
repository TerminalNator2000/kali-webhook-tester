# kali-webhook-tester
Python server instance inside kali-linux for testing web-hooks
Setting up a test server to receive webhooks is straightforward. Here’s a step-by-step guide:

---

### **Step 1: Choose a Test Server Tool**
For simplicity, use Python's built-in HTTP server. It’s lightweight and sufficient for testing webhooks.

#### Option 1: Python Script for Webhooks
1. Open your Kali Linux terminal.
2. Create a new Python script for your webhook listener:
   ```bash
   nano webhook_server.py
   ```
3. Paste the following script:
   ```
   from http.server import BaseHTTPRequestHandler, HTTPServer
   import json

   class WebhookHandler(BaseHTTPRequestHandler):
       def do_POST(self):
           content_length = int(self.headers['Content-Length'])  # Get the payload size
           post_data = self.rfile.read(content_length)          # Read the payload
           print("Webhook received:")
           print(post_data.decode('utf-8'))                     # Print the payload to the terminal

           # Respond to the webhook
           self.send_response(200)
           self.send_header('Content-type', 'text/plain')
           self.end_headers()
           self.wfile.write(b"Webhook received successfully!")

   if __name__ == "__main__":
       server_address = ('', 8000)  # Listen on port 8000
       httpd = HTTPServer(server_address, WebhookHandler)
       print("Starting webhook server on port 8000...")
       httpd.serve_forever()
   ```

4. Save and exit (`CTRL + O`, `Enter`, then `CTRL + X`).

---

### **Step 2: Start the Webhook Server**
1. Run the server:
   ```bash
   python3 webhook_server.py
   ```
2. The server will listen on port `8000` for incoming POST requests.

---

### **Step 3: Obtain Your Server's Public URL**
If you're testing on a local machine and need to expose it to the internet, you can use a tunneling tool like **ngrok**:
1. Install ngrok (if not already installed):
   ```bash
   sudo apt install ngrok
   ```
2. Start an ngrok tunnel:
   ```bash
   ngrok http 8000
   ```
3. Ngrok will provide a public URL (e.g., `https://abcd1234.ngrok.io`) that forwards to your local server. Use this URL as your webhook target.

---

### **Step 4: Test Your Webhook Server**
1. Use a tool like `curl` to send a test POST request:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
   -d '{"url": "http://example.com", "user": "admin"}' \
   http://localhost:8000
   ```
2. Check the terminal running the server for the printed payload:
   ```
   Webhook received:
   {"url": "http://example.com", "user": "admin"}
   ```

---



