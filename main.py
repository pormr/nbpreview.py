# -*- coding: utf-8 -*-

import webbrowser
import base64
import sys
import os

if __name__ == '__main__':
    path = sys.argv[-1]
    os.chdir(os.path.dirname(sys.argv[0]))
    if path == sys.argv[0]:
        webbrowser.open("index2.html", new=1)
    else:
        basename = os.path.basename(path)
        with open("template.html", encoding="utf-8") as template,\
             open(path, "rb") as ipynb,\
             open("index.html", mode = "w") as output:
            data = base64.b64encode(ipynb.read()).decode("utf-8")
            output.write("".join(template.readlines()) % (basename, data))
            webbrowser.open(output.name, new=1)
            
