# Auto-Coffee

This Repository is used as an Auto brew Script for my morning coffee. Using python-kasa I am controlling my Kasa TP-Link plug to turn on at a set time, brewing myself a fresh pot of coffee ready for me every morning before I wake up.

> [!IMPORTANT]
> **You will need to be using a Kasa SmartPlug**<br>**These instructions are currently only for MacOS. The device I am using for this is running MacOS Sonoma 14.4.1**

# **Python Version and dependencies**

To get started, make sure that you have a version of Python 3.10 or higher. To check this, in your terminal type<br> `python --version` or `python3 --version`

After, ensure that you have the required python-kasa package installed. If you do not, you can install it using<br> `pip install -r path/to/requirements.txt` or `pip3 install -r path/to/requirements.txt`

> [!WARNING]
> **If you haven't set up your Kasa SmartPlug yet, please do so before following this next step.**

Lastly, you will need your device's local IP. To get this, in your terminal type the command `kasa discover`<br> This will return all of your device info, what you are looking for is `Host:` followed by an IP, Which is your device's local IP.

# **Setting up main.py**

To set up your main.py, you will need to change 3 things.
1. You will need to replace `config` with your local IP.
2. Adjust the start time.
3. Adjust the end time.

> [!WARNING]
> **When adjusting `schedule_wake_event()` do not put leading 0's. Since it is looking for a value of int, you will get an error.<br> For example, if you want to set it for 8:00AM. You would use `schedule_wake_event(8,0)`**<br> **DO NOT USE `schedule_wake_event(08,00)`**

# **Setting up .plist file**

When setting up your `.plist` file you will want to change a few things, the first is the name of the file. For testing purposes, I use `com.user.coffee.plist` so that I can find my file later on but, you can name it as you wish so long that it has `.plist` at the end.

After you have named your file, you are gonna want to edit the contents. The first thing to change is `<string>com.user.example</string>` replace `com.user.example` with the name of your file. **Do not put .plist at the end of this.**

Then, you are gonna want to put the path to your `python3` in  `<string>/your/path/to/python3</string>` and the path to your `python script` in `<string>/your/path/to/script</string>`. To find your `python3 path` you can use this command in your terminal<br> `which python` or `which python3`

> [!NOTE]
> **If you don't know how to find the path to your script, drag and drop the file in your terminal and it will give you the full path.**

Next, you will need to change the `Start` and `End` times. Make sure that you are using the same times as the ones you put in your `main.py` from earlier. Currently, the start time is set to `8:50AM` and the end time `9:30AM`. To change the start time, find the section marked `Start time` and replace the number in the `<integer></integer>` tag under `<key>Hour</key>` and `<key>Minute</key>`. Use the `24 hour format` for the `<key>Hour</key>`. To change the end time, repeat those steps for the tags under the section marked `End time`

> [!WARNING]
> **Make sure to use leading 0's for this section.<br> For Example, if you want to set it for 8:00AM. You would use<br> `<key>Hour</key>` <br>`<integer>08</integer>` <br>`<key>Minute</key>` <br>`<integer>00</integer>`**

Finally, you will need to replace `<string>/your/path/to/stderr</string>` and `<string>/your/path/to/stdout</string>` with their respective paths. I suggest putting it in the same folder as your main.py to stay organized.

> [!IMPORTANT]
> **You do not need to create the `stderr` and `stdout` files before selecting their path, when the code executes it will create the files for you.**

# **Bringing it all together**

Now that we have all our files set up, it's time to put everything together. The first thing you are gonna want to do is move your `.plist` file to the `LaunchDaemons` Folder. This folder is usually located in the `/Library` directory. To move your `.plist` file to this directory from the terminal you can do `mv path/to/your/.plist /Library/LaunchDaemons`<br> If you want to move the file using Finder, you will need to go to `Macintosh HD -> Library -> LaunchDaemons`.

> [!NOTE]
> **Macintosh HD might be under a different name depending on how you set up your Mac.**

Next, in your terminal, you are gonna want to set up a `pmset`. This is what we will use to wake up your Mac so that it can run your `.plist` file. To do this you are gonna want to type this command `sudo pmset repeat wake MTWRFSU 'your start time'`. For our example, my start time is `8:50AM` so I would put `sudo pmset repeat wake MTWRFSU 08:50:00`

To check if you have done this properly you can type `pmset -g sched` it should say<br> `Repeating power events: wake at 'your start time' every day`

> [!NOTE]
> **If you want to remove your `pmset` type this command in the terminal `pmset repeat cancel`**

Finally, we need to load the `.plist` file. For this part, I suggest using [LaunchControl](https://www.macupdate.com/app/mac/46921/launchcontrol) you can download it at the link or through the Appstore. If you are using LaunchControl all you need to do is select the `Global Daemon` checkbox, find your `.plist` file and click on it, then click on this button<picture><img alt="circle with an arrow in it pointing up." src="https://github.com/TheRealQuicT/TheRealQuicT/blob/main/Pictures/circle-arrow.png"></picture> located at the top center of the window and your done.

If you want to do it using the terminal you are gonna need to get to your `root user`, to do this type `sudo zsh` then input your password. From there you are gonna type `launchctl load /path/to/your/.plist` replace `/path/to/your/.plist` with your path. To see if you have successfully loaded your `.plist` type in the terminal `launchctl list` and scroll through until you find the name of your `.plist` file.

> [!NOTE]
> **If you want to unload your `.plist` file all you need to do is click the same button if you are using LaunchControl or type `launchctl unload /path/to/your/.plist`**

> [!WARNING]
> **As long as you do not shut down your Mac then everything will execute properly even while it is in sleep mode and/or the lid is closed.**
