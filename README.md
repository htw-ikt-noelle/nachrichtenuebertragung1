# Nachrichtenuebertragung 1

Die [Jupyter](https://de.wikipedia.org/wiki/Project_Jupyter) Notebooks in diesem Repository dienen als interaktives Skript zu der Vorlesung "Nachrichtenübertragung 1" im Studiengang [Informations- und Kommunikationstechnik](https://ikt-bachelor.htw-berlin.de/) der [Hochschule für Technik und Wirtschaft (HTW)](https://www.htw-berlin.de/) Berlin. Sie wurden von [Markus Nölle](https://www.htw-berlin.de/hochschule/personen/person/?eid=9586) entworfen und weiter gepflegt. Sollten Sie Feher finden und / oder Fragen und Anmerkungen dazu haben melden Sie sich gerne bei mir.

Diese Jupyter Notebooks können prinzipiell entweder
* lokal auf Ihrem Rechner (benötigt eine [Jupyter](https://de.wikipedia.org/wiki/Project_Jupyter) Installation) oder
* im Brower in der Cloud über folgenden Link [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/htw-ikt-noelle/nachrichtenuebertragung1.git/HEAD?urlpath=lab) mittels [Binder](https://mybinder.org/) (benötigt nur eine Internetverbindung) 

ausgeführt werden.

Sie behandeln einzelne Themengebiete der Vorlesung und kombinieren statischen Lehrbuchinhalte mit interaktiven Programmierbeispielen, die Sie nach Belieben "ausprobieren" und verändern können. Diese [Python](https://de.wikipedia.org/wiki/Python_(Programmiersprache)) Programmierbeispiele benutzen zum Teil ein frei verfügbares Pythonmodul ([scikit-comm](https://gitlab.rz.htw-berlin.de/noelle/comm)), welches als [Submodul](https://git-scm.com/book/de/v2/Git-Tools-Submodule) in dieses Repository eingebunden ist. Auch dieses Submodul wird in der Veranstaltung (vor allem in den zugehörigen Laboren) intensiv benutzt.

## Anleitung zur Installation von [Jupyterlab](https://de.wikipedia.org/wiki/Project_Jupyter#JupyterLab) in einer [virtuellen Pythonumgebung](https://docs.python.org/3/library/venv.html)

Diese Anleitung gilt nur für [Windows Systeme](https://de.wikipedia.org/wiki/Microsoft_Windows). Für andere Betriebssysteme finden Sie im Internet weiterführende Installationsbeispiele.

* Laden Sie dieses Ropository herunter und speichern Sie es unter `<Repositoryspeicherort>`.
* Laden Sie eine aktuelle [Pythonversion](https://www.python.org/downloads/) für Ihr System herunter und installieren Sie diese. Bitte merken Sie sich den `<Python-Installationspfad>` (Standard bei Windows `C:\Users\<user>\AppData\Local\Programs\Python\PythonXXX`).
* Öffnen Sie eine Konsole (Windows: cmd.exe).
* Erzeugen Sie eine neue virtuelle Pythonumgebung in der Sie dann alle weiteren Pakete installieren. Sie können für diese virtuelle Pythonumgebung einen beliebigen Speicherort (`<Umgebungsspeicherort>`) angeben. Bitte beachten Sie aber, dass Sie Schreibrechte in diesem Ordner brauchen. Der Name des Ordners ist dann gleichzeitig der Name der virtuellen Pythonumgebung.
  
  `<Python-Installationspfad>\python.exe -m venv <Umgebungsspeicherort>`
  
* Aktivieren Sie die gerade erzeugte Pythonumgebung

    `<Umgebungsspeicherort>\Scripts\activate.bat`

* Installieren Sie alle benötigten Pythonmodule und -pakete mittels [pip](https://de.wikipedia.org/wiki/Pip_(Python)). Benutzen Sie dazu die Textdatei requirements.txt, in der alle benötigten Pakete aufgeführt sind.

    `pip install -r <Repositoryspeicherort>\binder\requirement.txt`

* Starten Sie Jupyterlab (in der aktivierten virtuellen Pythonumgebung)
  
    `jupyterlab`

## Lizenz???
