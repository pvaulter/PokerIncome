"""Wrap src/app.html into a standalone docs/index.html for GitHub Pages.

python3 tools/build.py --site DIR  also writes a copy for pokeroddspro.com into DIR
(PokerTrainer2/public/poker-income), which uses the site's /sign-in page instead of its own.
"""
import pathlib, shutil, sys
root = pathlib.Path(__file__).resolve().parent.parent
body = (root / 'src/app.html').read_text()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1d5c45">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>
'''
# Move <title>/<meta>/<link>/<style> (everything before #app) into <head>.
split = body.index('<div id="app">')
out = head + body[:split] + '</head>\n<body>\n' + body[split:] + '\n</body>\n</html>\n'
(root / 'docs/index.html').write_text(out)
print('wrote docs/index.html', len(out))

if '--site' in sys.argv:
    dest = pathlib.Path(sys.argv[sys.argv.index('--site') + 1])
    dest.mkdir(parents=True, exist_ok=True)
    for f in (root / 'docs').iterdir():
        if f.name != 'index.html': shutil.copy(f, dest / f.name)
    site = out.replace('<link rel="manifest"', '<meta name="site-signin" content="/sign-in">\n<link rel="manifest"', 1)
    (dest / 'index.html').write_text(site)
    print('wrote', dest / 'index.html')
