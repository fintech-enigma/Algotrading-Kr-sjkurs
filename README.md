# Algotrading-Kræsjkurs
Kræsjkurs i algoritmisk trading for gamle og nye Fintech-medlemmer

## Oppstart

### Lag og sett opp miljø

- Åpne Terminal (Ctrl + J / Cmd + J)

- Skriv følgende linje:

    ````
    python3 -m venv env
    ````

- Åpne ny Git Bash terminalvindu

- Skriv inn følgende:

    ````
    source env/Scripts/activate
    ````

### Innstaller dependecies

- Skriv inn følgende i Git Bash:

    ````
    pip3 install -r requirements.txt
    ````

## Kursplan

### 1. Installere Python

Gå til [python.org](https://www.python.org/) og installer

For Windows laste ned driver fra Google play

### 2. Teste pip

Skriv følgende i Terminal:

````
pip3 --version
````

### 3. Installere VS-Code

Gå til [code.visualstudio.com](https://code.visualstudio.com/) og installer.

### 4. Konfigurere git

1. Sørg for å ha bruker på [github.com](https://github.com/).

2. Last ned git fra [git-scm.com/downloads](https://git-scm.com/downloads).

3. Skriv følgende inn i terminalen: 

    ````
    git config --global user.name "DITT BRUKERNAVN"
    ````

     ````
    git config --global user.email "NAVN@eksempel.com"
    ````

4. Klon repoet på din PC og åpne i VS-Code

    ````
    git clone https://github.com/fintech-enigma/Algotrading-Kraesjkurs.git
    ````

    ````
    cd Algotrading-Kraesjkurs
    ````

    ````
    code .
    ````

### 5. Konfigurere Alpaca

1. Lag bruker på [alpaca.markets](https://alpaca.markets/).

2. Generer din egen API key og Secret Key.

3. Opprett en fil som heter `.env`.

3. Skriv følgende inn i filen og erstatt med dine nøkler. 

    ````
    END_POINT=https://paper-api.alpaca.markets
    API_KEY=DIN_API_KEY
    SECRET_KEY=DIN_SECRET_KEY
    ````

### 6. Første tradingprogram.

Bruker eksempelet under mappen `Basics`.

### 7. Clap 'n Trade Tesla!

Kan man klappe og trade Tesla??

Eksempel under `Tesla`

### 8. 180 dagers EMA trading

Vi lager et program som trader en aksje ut i fra 180EMA tallene. 

Eksempel i mappen `180EMA`.