import gspread
from google.oauth2.service_account import Credentials

# Escopos e caminho da chave
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Autenticação
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
client = gspread.authorize(creds)

# Planilha e aba
SPREADSHEET_ID = '1af49_XtK429ufofkMbF6TIqxjGnKcN9egbU0lc0hCOo'  # <-- Use seu ID aqui
SHEET_NAME = 'Página1'

sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Salva telefone, mensagem e quantidade de senhas
def salvar_mensagem(telefone, mensagem, quantidade_senhas):
    try:
        sheet.append_row([telefone, mensagem, quantidade_senhas])
        print(f"[✅] Dados salvos no Google Sheets")
    except Exception as e:
        print(f"[❌] Erro ao salvar no Google Sheets: {e}")
