import asyncio
from kasa import SmartPlug
from dotenv import dotenv_values

config = dotenv_values(".env")

async def controls():
  plug = SmartPlug(config["SMARTPLUG"])

  await plug.update()
  alias = plug.alias
  print(f"Connected to {alias}")
  if plug.is_on:
    await plug.turn_off()
    print(f"{alias} has been turned off.")
  else:
    await plug.turn_on()
    print(f"{alias} has been turned on.")

async def main():
  try:
    await controls()
  except Exception as e:
    print("Caught exception:", e)
    return 100
  return 0

if __name__ == "__main__":
  # Work around for Windows Asyncio Error RuntimeError: Event loop is closed
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Remove this line for MacOS
  loop = asyncio.run(main())
  print(f"Exiting with status code {loop}")
  
