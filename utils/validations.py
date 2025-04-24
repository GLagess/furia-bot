import re

def validar_nome(nome: str) -> bool:
    return nome.replace(" ", "").isalpha() and len(nome) >= 2

def validar_idade(idade: str) -> bool:  
    return idade.isdigit() and int(idade) >= 10

def validar_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
