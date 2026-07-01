import time
import os

from imap_tools import MailBox, AND
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
IMAP_SERVER = os.getenv("IMAP_SERVER")


def verificarEnv():
    print("Iniciando aplicação")

    if not EMAIL_USER or not EMAIL_PASS or not IMAP_SERVER:
        print("Faltam variáveis no arquivo .env")
        exit(1)


def verificarEmail():
    print("Buscando e-mails")

    try:
        with MailBox(IMAP_SERVER).login(EMAIL_USER, EMAIL_PASS) as mailbox:

            mailbox.folder.set("INBOX")

            for msg in mailbox.fetch(criteria=AND(seen=False), mark_seen=False):
                print("-" * 40)
                print(f"Novo E-mail de: {msg.from_}")
                print(f"Assunto: {msg.subject}")

            print("Todos e-mails lidos")

    except Exception as e:
        print(f"Erro ao verificar e-mails: {e}")


if __name__ == "__main__":
    verificarEnv()
    verificarEmail()
