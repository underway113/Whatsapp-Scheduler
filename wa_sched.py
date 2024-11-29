import pyautogui
import time
from datetime import datetime


DELAY_TIME = 0.2
DELAY_MESSAGE_TIME = 2

def open_whatsapp():
    """Open WhatsApp Desktop from the taskbar."""
    try:
        pyautogui.hotkey('win', 'd')  # Minimize all windows (Windows only)
        time.sleep(DELAY_TIME)
        pyautogui.hotkey('win', '1')  # Adjust this to open WhatsApp Desktop (based on taskbar position)
        time.sleep(DELAY_TIME)  # Wait for WhatsApp Desktop to open
    except Exception as e:
        print(f"Error opening WhatsApp: {e}")

def search_contact(contact_name):
    """Search for a contact on WhatsApp."""
    try:
        pyautogui.hotkey('ctrl', 'f')  # Shortcut to open the search bar
        time.sleep(DELAY_TIME)
        pyautogui.hotkey('ctrl', 'a')  # Select any pre-existing text in the search field
        time.sleep(DELAY_TIME)
        pyautogui.press('delete')  # Delete the selected text
        time.sleep(DELAY_TIME)
        pyautogui.write(contact_name)  # Type the contact name
        time.sleep(DELAY_TIME)
        pyautogui.press('tab')  # Navigate to the contact
        time.sleep(DELAY_TIME)
        pyautogui.press('enter')  # Open the contact's chat
        time.sleep(DELAY_TIME)
    except Exception as e:
        print(f"Error searching contact: {e}")

def send_text_message(message):
    """Send the message in the chat."""
    try:
        current_time = datetime.now().strftime("%d %b %Y %H:%M:%S")
        pyautogui.write(message + " " + current_time)  # Type the message with timestamp
        time.sleep(DELAY_MESSAGE_TIME)
        pyautogui.press('enter')  # Send the message
        time.sleep(DELAY_TIME)
    except Exception as e:
        print(f"Error sending message: {e}")

def close_whatsapp():
    """Close the WhatsApp chat and return to the main window."""
    try:
        pyautogui.press('esc')  # Close the chat
        pyautogui.press('esc')
        pyautogui.press('esc')  # Close any remaining overlays
    except Exception as e:
        print(f"Error closing WhatsApp: {e}")

def send_message(contact_name, message):
    """Main function to send a message to a contact."""
    try:
        open_whatsapp() 
        search_contact(contact_name)
        send_text_message(message) 
        close_whatsapp()

        # Log the sent message with the timestamp
        current_time = datetime.now().strftime("%d %b %Y %H:%M:%S")
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