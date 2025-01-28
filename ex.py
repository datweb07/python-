import pyfiglet
import time
text = pyfiglet.figlet_format('Happy New Year', width = 200)
for i in text.splitlines():
    print(i)
    time.sleep(0.5)