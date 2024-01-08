import mysql.connector
import time 
from dotenv import load_dotenv
import os 

load_dotenv()

db_config = {
    'host': f"{os.getenv('DB_HOST')}",  # Ersetzen Sie 'IhrHost' mit der Adresse Ihres Datenbankservers
    'user': f"{os.getenv('DB_USER')}",  # Ersetzen Sie 'IhrBenutzername' mit Ihrem Datenbankbenutzernamen
    'password': f"{os.getenv('DB_PASSWORD')}",  # Ersetzen Sie 'IhrPasswort' mit Ihrem Datenbankpasswort
    'database': f"{os.getenv('DB_DATABASE')}" # Ersetzen Sie 'IhrDatenbankname' mit dem Namen Ihrer Datenbank
}

def verbinde_zur_datenbank():
    while True:
        try:
            conn = mysql.connector.connect(**db_config)
            print("Datenbankverbindung erfolgreich.")
            return conn
        except mysql.connector.Error as e:
            print(f"Fehler bei der Datenbankverbindung: {e}")
            print("Versuche, die Verbindung in 5 Sekunden erneut herzustellen...")
            time.sleep(5)


def aktualisiere_product_content(conn, id, neuer_content):
    cursor = conn.cursor()
    try:
        update_query = "UPDATE cwnFp_posts SET post_content = %s WHERE post_title LIKE %s AND post_status = 'publish'"
        cursor.execute(update_query, (neuer_content, '%' + id + '%'))
        conn.commit()
        print(f"Content aktualisiert für Post-ID: {id}")
    except mysql.connector.Error as e:
        print(f"Fehler beim Aktualisieren des Posts: {e}")
    finally:
        cursor.close()


def hole_alle_produkte(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        produkt_query = "SELECT * FROM `kxb76_posts` WHERE `post_type` LIKE 'product'"
        cursor.execute(produkt_query)
        produkte = cursor.fetchall()

        meta_query = """
        SELECT * FROM `kxb76_postmeta` 
        WHERE `post_id` IN (
            SELECT ID FROM `kxb76_posts` WHERE `post_type` = 'product'
        )
        """
        cursor.execute(meta_query)
        metadaten = cursor.fetchall()

        return produkte, metadaten
    except mysql.connector.Error as e:
        print(f"Fehler beim Abrufen der Produkte: {e}")
        return None, None
    finally:
        cursor.close()


# Verwendung der Funktionen
conn = verbinde_zur_datenbank()
if conn:
    produkte, metadaten = hole_alle_produkte(conn)
    if produkte and metadaten:
        print("Produkte:", produkte)
        print("Metadaten:", metadaten)
    conn.close()

#SELECT * FROM `kxb76_postmeta` WHERE `post_id` IN (SELECT ID FROM `kxb76_posts` WHERE `post_type` = 'product')

#SELECT * FROM `kxb76_posts` WHERE `post_type` LIKE 'product'