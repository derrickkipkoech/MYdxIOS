"""Builds www/ for the Android app from the SAME panel and bridge the Windows app uses (one source of truth).
Run from anywhere:  python android-app/make_android.py      (the GitHub workflow runs it before every build)"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WWW = os.path.join(HERE, "www")
HEAD = ('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">'
        '<meta name="mobile-web-app-capable" content="yes"><meta name="theme-color" content="#000000">'
        '<style>*{touch-action:manipulation;-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none}'
        'html,body{overscroll-behavior:none}</style>')

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    panel = os.path.join(ROOT, "dxarrangernew1.html")
    bridge = os.path.join(ROOT, "bridge.js")
    for p in (panel, bridge, os.path.join(WWW, "engine.js")):
        if not os.path.isfile(p):
            sys.exit(f"missing {p}")
    html = read(panel)
    j = html.find("</head>")
    html = html[:j] + HEAD + html[j:] if j >= 0 else HEAD + html
    tags = '<script src="engine.js"></script><script src="bridge.js"></script>'   # engine first: it answers the panel's /api calls
    i = html.rfind("</body>")
    html = html[:i] + tags + html[i:] if i >= 0 else html + tags
    with open(os.path.join(WWW, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    shutil.copyfile(bridge, os.path.join(WWW, "bridge.js"))
    print("www/ ready:", sorted(os.listdir(WWW)))

if __name__ == "__main__":
    main()
