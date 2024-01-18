## utilisation

https://pod-2024.cyclic.app/getList?site=721  --> retourne un json avec les qrcodes pour la 721

https://pod-2024.cyclic.app/setStatutScanned?qrcode=ab6d9f53-0d8c-47cb-9af0-fa58af2907d9&qui=MACadress --> après avoir scanné le qr en question

https://pod-2024.cyclic.app/getList?site=721  --> voir le résultat



# Flask API Starter

This is the simplest possible python api using flask that responds with: 
```
Hello, world!
```

## Deploy to Cyclic in seconds 

[![Deploy to Cyclic](https://deploy.cyclic.app/button.svg)](https://deploy.cyclic.app/)


## Run Locally

Prerequisites:
- pyenv
- python 3.10.11

Install: `bin/install`
- creates virtual env
- installs dependencies from `requirements.txt`

Run: `bin/start`
- runs a `gunicorn` server


## Questions / Help

Join us on Discord: [https://discord.cyclic.sh](https://discord.cyclic.sh)

Enjoy!
