import firebase_admin
from firebase_admin import credentials, firestore

# Verifica se o Firebase já foi inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")  # Caminho para o arquivo de credenciais JSON
    firebase_admin.initialize_app(cred)
else:
    print("Firebase já foi inicializado.")

# Cria o cliente do Firestore
db = firestore.client()

def salvar_usuario(user_id: int, dados: dict):
    try:
        # Salva o documento do usuário no Firestore
        db.collection("usuarios").document(str(user_id)).set(dados)
        print("Usuário salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar usuário: {e}")

def usuario_existe(user_id: int) -> bool:
    try:
        # Verifica se o documento do usuário existe
        doc = db.collection("usuarios").document(str(user_id)).get()
        return doc.exists
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False
