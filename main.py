# main.py

import pyautogui
import os
from datetime import datetime
import keyboard  # pip install keyboard

# Criar pasta "screenshots" se não existir
os.makedirs("screenshots", exist_ok=True)

def tirar_print():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"[OK] Screenshot salva: {filename}")

def main():
    print("Pressione '/' para tirar um screenshot. Pressione ESC para sair.")
    while True:
        if keyboard.is_pressed('/'):
            tirar_print()
            # Evitar múltiplos prints enquanto a tecla estiver pressionada
            keyboard.wait('/')  

        if keyboard.is_pressed('esc'):
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
