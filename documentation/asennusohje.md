# Asennusohje

Tämä ohje on tarkoitettu projektin asentamiseen lokaalisti koneellesi.
1. Kloonaa repositorio haluamaasi hakemistoon
2. Luo uusi Python-virtuaaliympäristö riippuvuuksien ym. asentamista varten (suositeltavaa). 
```
python3 -m venv /path/to/new/virtual/environment
```
3. Aktivoi virtuaaliympäristö ja asenna riippuvuudet komennolla
```
pip install -r requirements.txt
```
4. Sovellus käynnistyy nyt oletusporttiin komennolla 
```
python3 run.py
```
