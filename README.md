# Poker Income

Track poker sessions: buy-in, cash out, hours, mileage at the IRS rate, net profit and hourly rate, with charts by venue, year and session length.

Each person signs up with a username and password on their own device. Sessions are encrypted with that password (PBKDF2 + AES-GCM) and saved only in the browser. Nothing is sent to a server, so there is no password reset; use **Account → Export backup** to keep a copy or move to another device.

- `src/app.html`: the app (HTML, CSS and JS in one file)
- `tools/build.py`: wraps it into `docs/index.html` for GitHub Pages
- `docs/`: the site (with manifest and service worker for offline use and "Add to Home Screen")

Build: `python3 tools/build.py`. Host: GitHub Pages from the `docs/` folder.

## pokeroddspro.com

The live app is served at https://pokeroddspro.com/poker-income/ from the PokerTrainer2 repo. After changing the app here, run `python3 tools/build.py` and copy `docs/*` into `PokerTrainer2/public/poker-income/`.
