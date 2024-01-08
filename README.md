# README für Python-Skript zur Verbindung mit einer MySQL-Datenbank

## Überblick
Dieses Python-Skript ermöglicht die Verbindung zu einer MySQL-Datenbank, das Ausführen von Abfragen und das Aktualisieren von Inhalten in der Datenbank. Das Skript verwendet die `mysql.connector` Bibliothek, um eine Verbindung zur Datenbank herzustellen, und führt verschiedene Funktionen aus, um Daten zu manipulieren und abzurufen.

## Voraussetzungen
- Python 3.x
- MySQL-Datenbankserver
- `mysql.connector` Python-Bibliothek
- `.env` Datei mit Datenbankkonfigurationsinformationen

## Installation
1. Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
2. Installieren Sie die erforderlichen Pakete:
   ```
   pip install mysql-connector-python python-dotenv
   ```
3. Erstellen Sie eine `.env`-Datei im gleichen Verzeichnis wie Ihr Skript mit folgendem Inhalt:
   ```
   DB_HOST=IhrHost
   DB_USER=IhrBenutzername
   DB_PASSWORD=IhrPasswort
   DB_DATABASE=IhrDatenbankname
   ```
   Ersetzen Sie die Platzhalter mit Ihren eigenen Datenbankinformationen.

## Skriptstruktur
- `load_dotenv()`: Lädt die Konfigurationsdaten aus der `.env` Datei.
- `db_config`: Ein Dictionary mit den Datenbankkonfigurationsdaten.
- `verbinde_zur_datenbank()`: Versucht, eine Verbindung zur Datenbank herzustellen. Bei Fehlschlagen wird nach 5 Sekunden ein erneuter Versuch unternommen.
- `aktualisiere_product_content(conn, id, neuer_content)`: Aktualisiert den Inhalt eines Posts in der Datenbank basierend auf der Post-ID.
- `hole_alle_produkte(conn)`: Holt alle Produkte und deren Metadaten aus der Datenbank.

## Verwendung
1. Starten Sie das Skript. Das Skript versucht, sich automatisch mit der Datenbank zu verbinden.
2. Nach erfolgreicher Verbindung werden die Produkte und Metadaten abgerufen und angezeigt.
3. Um den Inhalt eines Posts zu aktualisieren, verwenden Sie die Funktion `aktualisiere_product_content` mit der entsprechenden Post-ID und dem neuen Inhalt.

## Hinweis
- Stellen Sie sicher, dass Ihre Datenbankzugangsdaten korrekt und sicher aufbewahrt sind.
- Ändern Sie die Tabellen- und Spaltennamen im Skript entsprechend Ihrer Datenbankstruktur.

## Lizenz
Dieses Skript wird unter der MIT-Lizenz veröffentlicht. Beachten Sie die Lizenzbedingungen für die Verwendung und Verteilung.
