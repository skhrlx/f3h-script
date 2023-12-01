import pyautogui
import keyboard

def main():
    while True:
        try:
            keyboard.wait("O")  # Wait for the "O" key to be pressed
            pyautogui.hotkey("F3", "h")  # Simulate pressing "F3 + h"
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()