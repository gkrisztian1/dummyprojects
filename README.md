# dummyprojects

## Hogyan töltsd le

```git clone git@github.com:gkrisztian1/dummyprojects.git```

## Virtualenv

A python projektekhez érdemes külön virtuális környezetet használni, hogy ne
akadjanak össze a package-k verziói a különböző projektekben.

Ha Pycharm-ot használsz akkor a következő lépések kb. automatikusan menni
fognak.

### Virtualenv létrehozása

```python3 -m virtualenv venv```

Ha windowson vagy akkor ```python``` és nem ```python3```.

### Virtualenv aktiválása

```source venv/bin/activate ```

Windows alatt valami ilyesmi: ```.\venv\Scripts\activate```. Ott is egy valami
activate nevű bash file-t kell keresni. Ha minden ok akkor a cmd prompt előtt
lez egy ```(venv) ``` rész. Ha ez megvan akkor minden python hívás a virtualenv
pythonhoz fog nyúlni és az oda telepített package-eket fogja használni.

### Függőségek telepítése

A csomagok pontos verziókkal a ```requirements.txt```-ben vannak. Ezeket ezzel
tudod telepíteni:

```pip install -r requirements.txt```

### Függőségek frissítése

Ha közben telepítettél olyan csomagokat amik kellenek majd a projekthez akkor
ezeket hozzá tudod adni a ```requirements.txt```-hez:

```pip freeze > requirements.txt```

### Virtualenv kikapcsolása

Ha kész vagy akkor csak ``` deactivate ``` a cmd-be, vagy ha Pycharm-ozol akkor
csak kilépsz és ok.


## Gitignore

Ha vannak olyan fájlok vagy mappák amiket nem akarod, hogy a git kövessen és
felkerüljön a remote repoba akkor add őket hozzá a ```.gitignore``` fájlhoz.
