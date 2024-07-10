from playsound import playsound
import time

CLEAR = '\033[2j'
CLEAR_AND_RETURN = '\033[H'

def alarm(seconds):
  time_passed = 0
  while time_passed < seconds:
    print(CLEAR)
    time.sleep(1)
    time_passed += 1
    total = seconds - time_passed
    Seconds = total % 60
    minutes = total // 60
    print(f"{CLEAR_AND_RETURN}{minutes:02d}:{Seconds:02d}")
  print("Time's up!!")

alarm(10)
playsound('Alarm_sound/cyber-alarms-synthesized-116358.mp3')