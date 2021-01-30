import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("""
\x1b[1;00m        ▓██      ▒█████    ▄████  ██▓ ███▄    █▓
        ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █▓
        ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
        ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
        ░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
        ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒
        ░ ░\x1b[00m\033[041m S A T P A M  P O S  R O N D A  \033[00m\x1b[1;00m░░
          ░ ░   ░   ░    ░ ░   ░    ░   ░   ░\x1b[00m
""")
m('\x1b[00m\033[041m Install bahan automatis  \033[00m')
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install nano")
os.system("pkg install python -y")
os.system("pkg install python2 -y")
m("DONE")
os.system("clear")
