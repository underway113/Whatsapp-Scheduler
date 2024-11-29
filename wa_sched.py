import pyautogui
import time
from datetime import datetime  # Import the datetime module

def send_message(contact_name, message):
    try:
        # Open WhatsApp Desktop (ensure it's in the taskbar)
        pyautogui.hotkey('win', 'd')  # Minimize all windows (Windows only)
        time.sleep(0.2)
        pyautogui.hotkey('win', '1')  # Adjust this to open WhatsApp Desktop (based on taskbar position)
        time.sleep(0.2)  # Wait for WhatsApp Desktop to open

        # Search for the contact
        pyautogui.hotkey('ctrl', 'f')  # Shortcut to open the search bar
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'a') 
        time.sleep(0.2)
        pyautogui.press('delete')
        time.sleep(0.2)
        pyautogui.write(contact_name)  # Type the contact name
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)

        
        current_time = datetime.now().strftime("%d %b %Y %H:%M:%S")
        # Send the message
        pyautogui.write(message + " " + current_time)  # Type the message
        time.sleep(1.9)
        pyautogui.press('enter')  # Send the message
        time.sleep(0.2)
        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')


        print(f"{current_time} | {contact_name} | {message}")
    except Exception as e:
        print(f"An error occurred: {e}")



# Schedule message sending every minute
def schedule_messages():
    contact_name = "Notes Private"  # Replace with your contact's name
    message = "Hello! This is an automated message sent via WhatsApp Desktop."
    
    while True:
        send_message(contact_name, message)
        time.sleep(10)  # Wait for 1 minute before sending the next message

# Start sending messages
if __name__ == "__main__":
    schedule_messages()