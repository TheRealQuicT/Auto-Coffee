#!/usr/bin/python3

import asyncio
import subprocess
import time
from kasa import SmartPlug

# <-- Enter your SmartPlug IP address -->
config = '255.255.255.255'


def schedule_wake_event(hour: int, minute: int) -> None:
  """
  Sets the start/end wake time using pmset.

  Args:
      hour: int
      minute: int
  """

  command = f"sudo pmset repeat wake MTWRFSU {hour}:{minute}:00"
  subprocess.run(command, shell=True)


async def controls() -> None:
  """
  Controls the on/off functionality of the SmartPlug.
  """

  plug = SmartPlug(config)

  await plug.update()
  alias = plug.alias
  print(f"Connected to {alias}")

  if plug.is_on:
    await plug.turn_off()
    # Do not put leading 0's 
    # example (08,50)
    schedule_wake_event(8,50) # <-- Adjust Start time here
    print(f"{alias} has been turned off.")
  else:
    await plug.turn_on()
    # Do not put leading 0's 
    # example (09,30)
    schedule_wake_event(9,30) # <-- Adjust End time here
    print(f"{alias} has been turned on.")


async def main() -> int:
  """
  Main Function Logic

  Returns:
      int: Exit code
  """

  try:
    await controls()
  except Exception as e:
    print("Caught exception:", e)
    return 100
  return 0

if __name__ == "__main__":
  loop = asyncio.run(main())
  print(f"Exiting with status code {loop}")
  print('Timestamp:', " ".join(time.ctime().split()))
  print("-----------------------------------")
