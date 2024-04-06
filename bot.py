import subprocess
import time
import pyautogui
import datetime

def print_with_timestamp(*args, **kwargs):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime('%H:%M:%S %m/%d/%y')
    message = f"{timestamp} - {' '.join(map(str, args))}\n"
    print(message, end='')
    with open('log.txt', 'a') as log_file:
        log_file.write(message)

def quit_game(process_name):
    try:
        subprocess.run(['taskkill', '/im', process_name, '/f'], check=True)
    except subprocess.CalledProcessError as e:
        print_with_timestamp(f"Failed to terminate {process_name}. Error: {e}")

def launch_steam_game(game_id):
    command = f"steam://run/{game_id}"

    try:
        subprocess.run(["cmd", "/c", "start", command], check=True)
        print_with_timestamp("Game is launching...")

        time.sleep(5)

        click_button("departbutton.png")
    except subprocess.CalledProcessError as e:
        print_with_timestamp(f"Failed to launch the game. Error: {e}")

def click_button(image_path):
    try:
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)

        if button_location is not None:
            pyautogui.click(button_location)
            print_with_timestamp("Departed ships successfully.")
            time.sleep(3)
            quit_game("sm_sdl_steam.exe")
            print_with_timestamp("Quitting game.")
        else:
            print_with_timestamp("Your ships are not ready to be departed.")
            time.sleep(5)
            quit_game("sm_sdl_steam.exe")
            print_with_timestamp("Quitting game.")

    except pyautogui.ImageNotFoundException:
        print_with_timestamp("Could not locate the depart button on screen.")
        quit_game("sm_sdl_steam.exe")
        print_with_timestamp("Quitting game.")

game_id = "2445660"
delay = int(input("What delay would you like between departure attempts? (Minutes): "))
delay *= 60

while True:
    is_game_running = launch_steam_game(game_id)
    time.sleep(delay)
