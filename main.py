import requests
import time
from playsound import playsound

def check_webpage(url, previous_content):
    """
    Check if the webpage content has been modified.

    Args:
        url (str): The URL of the webpage to monitor.
        previous_content (str): The previous content of the webpage.

    Returns:
        tuple: A tuple containing a boolean indicating whether the webpage was modified
               and the updated content of the webpage.
    """
    try:
        response = requests.get(url)
        current_content = response.text

        if previous_content != current_content:
            return True, current_content
        else:
            return False, current_content

    except Exception as e:
        print(f"Error checking webpage: {e}")
        return False, previous_content

def play_notification_sound():
    """
    Play a notification sound.
    """
    try:
        playsound("notification_sound.mp3")  # Change the filename to your notification sound file
    except Exception as e:
        print(f"Error playing notification sound: {e}")

def main():
    # Prompt the user to input the URL of the webpage to monitor
    url = input("Enter the URL of the webpage to monitor: ")

    # Initialize previous_content to None
    previous_content = None

    while True:
        modified, previous_content = check_webpage(url, previous_content)
        
        if modified:
            print("Webpage modified! Playing notification sound...")
            play_notification_sound()

        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
