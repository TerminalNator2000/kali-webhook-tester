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

    def do_GET(self):
        # Handle GET requests (like /favicon.ico)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Server is running.")

if __name__ == "__main__":
    server_address = ('', 8000)  # Listen on port 8000
    httpd = HTTPServer(server_address, WebhookHandler)
    print("Starting webhook server on port 8000...")
    httpd.serve_forever()
