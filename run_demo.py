import webbrowser
import threading
import time
import os
from app import app

def open_browser():
    """Wait for the server to start, then open the browser."""
    time.sleep(1.5)  # Give the server a moment to start
    webbrowser.open("http://127.0.0.1:5001")

if __name__ == "__main__":
    print("--- Secure Guessing Game Launcher ---")
    print("Designed by Siyabonga Mkhize")
    print("\nStarting web server...")
    
    # Start the browser opening thread
    threading.Thread(target=open_browser).start()
    
    # Run the Flask app
    app.run(debug=False, port=5001)
