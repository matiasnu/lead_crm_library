# lead-crm-library/salesforce/auth.py
from simple_salesforce import Salesforce

def authenticate(username, password, security_token):
    # Código para autenticarse con Salesforce usando credenciales de usuario y un token de seguridad
    f = Salesforce(username=username, password=password, security_token=security_token)
    return f
