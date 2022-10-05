## Quick moss definitions
Made for people interested while grove is a WIP. will be deleted soon

no nlp, does not include synonyms or extended dictionary

- Install lilypond development version from the [official site](https://lilypond.org/development.html) or use lilypond-devel package in AUR
- cd to directory
- make venv: `python3 -m pip venv venv`
- activate venv (run every time you use): `source ./venv/bin/activate`
- install pip deps: `pip3 install --require-virtualenv -U -r requirements.txt`
- `python3 main.py`

you can set a custom key signature (defs are written in c major, script transposes to b major as an example)