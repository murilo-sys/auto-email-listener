import time
import os
import re
from services.consultaPagina import consultaPagina

from imap_tools import MailBox, AND, MailMessageFlags
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
IMAP_SERVER = os.getenv("IMAP_SERVER")

# Regex do link
padrao_link = (
    r"https://activeonsupply\.com\.br/SITE/Coleta/AprovaDesaprova\?rastreamento=[\w-]+"
)


def verificarEnv():
    print("Iniciando aplicação")

    if not EMAIL_USER or not EMAIL_PASS or not IMAP_SERVER:
        print("Faltam variáveis no arquivo .env")
        exit(1)


def verificarEmail():
    print("-" * 40)
    print("Verificando")

    try:

        # Loga com serviço IMAP
        with MailBox(IMAP_SERVER).login(EMAIL_USER, EMAIL_PASS) as mailbox:

            # Seta na pasta INBOX geralmente principal
            mailbox.folder.set("INBOX")

            # Loop for que verifica cada mensagem que não foi vista
            for msg in mailbox.fetch(criteria=AND(seen=False), mark_seen=False):

                # Caso o DE for diferente do definido
                if msg.from_ != "matheus.martinelli@globalcargo.com.br":
                    continue

                # Roda um regex e procura apenas o link
                link = re.search(padrao_link, msg.text)

                # Caso não tenha o link, retorna
                if not link:
                    continue

                # Consulta a pagina do link
                consulta = consultaPagina(link.group())

                # Se a consulta não existir
                if not consulta:
                    print(f"Link indisponivel ou inacessivel. E-mail: {msg.subject}")
                    continue

                # Printa a coleta se ela existir
                print(consulta)
                mailbox.flag(msg.uid, MailMessageFlags.SEEN, True)

    except Exception as e:
        print(f"Erro ao verificar e-mails: {e}")


if __name__ == "__main__":

    verificarEnv()

    while True:
        verificarEmail()
        time.sleep(5)
