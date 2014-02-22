#!/usr/bin/env python
import os, sys, re

def read_env():
    try:
        with open('.env') as f:
            content = f.read()
    except IOError:
        content = ''
 
    for line in content.splitlines():
        trimmed_line = line.replace(" ","")
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', trimmed_line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            os.environ.setdefault(key, val)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fightclub.settings")
    from django.core.management import execute_from_command_line
    read_env()
    import fightclub.startup as startup
    startup.run()
    execute_from_command_line(sys.argv)

