import os
import subprocess
import time

import pyautogui
import speech_recognition as sr

recording_duration = 4.5


def smooth_volume(original_volume, target_volume, duration=2):
    current_volume = original_volume
    start_time = time.time()

    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / duration

        # Apply an easing function to smoothly interpolate the volume
        # For example, you can use a cubic easing function (t^3) for smoother results
        eased_progress = progress**3

        # Calculate the current volume level based on the easing progress
        current_volume = original_volume + (target_volume - original_volume) * eased_progress

        # Set the volume using osascript
        subprocess.run(["osascript", "-e", f"set volume output volume {int(current_volume)}"])

        # Sleep for a short period to smooth the interpolation
        time.sleep(0.05)

    # Ensure the final volume is set to the target volume
    subprocess.run(["osascript", "-e", f"set volume output volume {target_volume}"])

def tell(name):
    recognizer = sr.Recognizer()
    os.system(f'say What Do you want to say to {name}?')
    # Use the default microphone as the audio source
    with sr.Microphone(device_index=2) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
        command = recognizer.recognize_google(audio)
        print("message:", command)

        command = [
            'osascript',
            '-e',
            f'''tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/in.touch\' \'+1{name}\' \'+2{command}\' \'+3https://web.snapchat.com/ \'"'''
        ]

        subprocess.run(command)

def message(name):
    recognizer = sr.Recognizer()
    os.system(f'say What Do you want to say to {name}?')
    # Use the default microphone as the audio source
    with sr.Microphone(device_index=2) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
        command = recognizer.recognize_google(audio)
        print("message:", command)

        command = [
            'osascript',
            '-e',
            f'''tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/inmessage.touch\' \'+1{name}\' \'+2{command}\'"'''
        ]

        subprocess.run(command)

def close_other_terminal_windows():
    # AppleScript to close other Terminal windows except the frontmost one
    applescript = '''
        tell application "Terminal"
            set front_window to front window
            set all_windows to every window
            repeat with a_window in all_windows
                if a_window is not front_window then
                    close a_window
                end if
            end repeat
        end tell
    '''

    # Execute the AppleScript
    subprocess.run(['osascript', '-e', applescript])

def watch(show_name):
    # Function to simulate playing the song (you can implement the actual song playing here)
    import os

    command = [
        'osascript',
        '-e',
        f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/netflixong.touch\' \'+1{show_name}\'"'
    ]

    subprocess.run(command)

def cshow(show_name):
    # Function to simulate playing the song (you can implement the actual song playing here)
    import os

    command = [
        'osascript',
        '-e',
        f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/cshow.touch\' \'+1{show_name} \'"'
    ]

    subprocess.run(command)

def play_song(song_name):
    # Function to simulate playing the song (you can implement the actual song playing here)
    import os

    command = [
        'osascript',
        '-e',
        f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/playsong.touch\' \'+1{song_name}\'"'
    ]

    subprocess.run(command)

import platform
import time

def lower_volume():
    # Platform-specific volume adjustment
    if platform.system() == "Darwin":
        # macOS platform using osascript
        import subprocess

        # Get the current volume
        current_volume = int(subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"]))
        subprocess.run(["osascript", "-e", f"set volume output volume {(current_volume * 0.20)}"])
    else:
        # Unsupported platform
        print("Volume adjustment not supported on this platform.")


def get_song_name():
    recognizer = sr.Recognizer()
    song_to_play = None

    # Use the default microphone as the audio source
    with sr.Microphone(device_index=0) as source:
        print("Say 'jake' to lower the volume and listen to your command...")

        # Adjust for ambient noise for better recognition
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:

                audio = recognizer.listen(source, timeout=2.5, phrase_time_limit=2.5)
                # Use Google Web Speech API to recognize the audio

                command = recognizer.recognize_google(audio)
                print("You said:", command)

                if 'Jake' in command:
                    global current_volume
                    current_volume = int(
                    subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"]))
                    subprocess.Popen(["python3", "-c", "from mru import lower_volume; lower_volume()"])
                    os.system('say I am listening')
                    audio = recognizer.listen(source, timeout=recording_duration, phrase_time_limit=recording_duration)
                    smooth_volume(original_volume=int(
                        subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                        target_volume=int(subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])))

                    print("Volume restored and desktop cleaned.")
                    command = recognizer.recognize_google(audio)

                    print("You said:", command)

                    if 'play' in command.lower():
                        song_name = command.lower().replace("play", "").strip()
                        os.system(f'say playing {song_name}')
                        subprocess.Popen(["python3", "-c", f"from mru import play_song; play_song(song_name='{song_name}')"])
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                                      target_volume=current_volume)

                        time.sleep(4)
                        close_other_terminal_windows()

                    elif 'watch' in command.lower():
                        show_name = command.lower().replace("watch", "").strip()
                        print("watching show:", show_name)
                        os.system('say show starting')
                        watch(show_name)
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                                      target_volume=current_volume)

                        time.sleep(10)
                        close_other_terminal_windows()

                    elif 'show' in command.lower():
                        show_name = command.lower().replace("change show", "").strip()
                        print("changing show:", show_name)
                        os.system("say show's been changed")
                        cshow(show_name)
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                                      target_volume=current_volume)

                        time.sleep(10)
                        close_other_terminal_windows()

                    elif 'tell' in command.lower():
                        name = command.lower().replace("tell", "").strip()
                        print("sending message to:", name)
                        os.system(f'say sending a snap to {name}')
                        tell(name)
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                            target_volume=current_volume)

                        time.sleep(10)
                        close_other_terminal_windows()

                    elif 'message' in command.lower():
                        name = command.lower().replace("message", "").strip()
                        print("sending sms message to:", name)
                        os.system(f'say Sending sms to {name}')
                        message(name)
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                            target_volume=current_volume)

                        time.sleep(10)
                        close_other_terminal_windows()
                    elif 'next song' in command.lower():
                        command = [
                            'osascript',
                            '-e',
                            f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/nect.touch\' "'
                        ]
                        subprocess.run(command)
                    elif 'previous song' in command.lower():
                        command = [
                            'osascript',
                            '-e',
                            f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/prev.touch\' "'
                        ]
                        subprocess.run(command)
                    elif 'pause' in command.lower():
                        command = [
                            'osascript',
                            '-e',
                            f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/pause.touch\' "'
                        ]
                        subprocess.run(command)
                    elif 'loop song' in command.lower():
                        command = [
                            'osascript',
                            '-e',
                            f'tell application "Terminal" to do script "python3 \'/Users/maliq/PycharmProjects/touch/touch/Touch.py\' \'/Users/maliq/PycharmProjects/touch/jamal/repe.touch\' "'
                        ]
                        subprocess.run(command)
                    else:
                        smooth_volume(original_volume=int(
                            subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])),
                            target_volume=current_volume)
                        print("Volume restored and desktop cleaned.")





            except sr.UnknownValueError:
                # Unable to understand audio
                pass
            except sr.RequestError:
                print("Error accessing the Google Web Speech API. Check your internet connection.")
                break
            except sr.WaitTimeoutError:
                # Raised when the audio source is silent (no speech) for the timeout period
                pass

if __name__ == "__main__":
    get_song_name()

