# 📧 Auto Email Listener

Um script em Python leve e robusto, projetado para se conectar a servidores de e-mail (Gmail, Locaweb, Outlook, etc.) via protocolo **IMAP** e buscar novas mensagens não lidas.

Este projeto foi desenvolvido com foco em **Boas Práticas de Engenharia de Software**, abordando segurança, gerenciamento de recursos e abstração de infraestrutura.

## ✨ Funcionalidades

- **Agnóstico de Provedor**: Funciona com qualquer provedor de e-mail que suporte a especificação IMAP.
- **Segurança Nativa**: Utiliza variáveis de ambiente (`.env`) para garantir que credenciais sensíveis nunca sejam expostas no código-fonte.
- **Alta Performance**: A filtragem de e-mails (`seen=False`) ocorre diretamente no servidor, poupando largura de banda e memória (dispensa o download em massa).
- **Design Fail-Fast**: O script valida a presença das variáveis de ambiente na inicialização e aborta a execução instantaneamente caso as credenciais não estejam configuradas.
- **Gerenciamento de Contexto Seguro**: Evita vazamentos de conexão (socket leaks) ao usar a estrutura `with` para garantir o fechamento da comunicação ao término da rotina.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **[imap_tools](https://github.com/ikvk/imap_tools)**: Uma interface moderna e Pythônica para abstrair as complexidades da biblioteca nativa `imaplib`.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)**: Gerenciamento seguro de variáveis de ambiente.
- **Black Formatter**: Para aderência estrita às regras de estilo PEP-8.

## 🚀 Como Executar Localmente

### 1. Clonando o repositório
```bash
git clone https://github.com/SEU-USUARIO/auto-email-listener.git
cd auto-email-listener
```

### 2. Configurando o Ambiente Virtual
É altamente recomendado rodar o projeto em um ambiente isolado:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate
```

### 3. Instalando as Dependências
```bash
pip install imap-tools python-dotenv
```

### 4. Configurando Credenciais
Crie um arquivo chamado exato **`.env`** na raiz do projeto e preencha com as suas informações:

```env
EMAIL_USER=seu_email@dominio.com
EMAIL_PASS=sua_senha_de_aplicativo_ou_normal
IMAP_SERVER=imap.seudominio.com
```
*⚠️ Importante: O arquivo `.env` nunca deve ser "commitado". Ele já está incluído no `.gitignore`.*

### 5. Executando o "Listener"
```bash
python src/main.py
```
---
Feito com ☕ e código limpo.
