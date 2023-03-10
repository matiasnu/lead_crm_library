# lead-crm-library/salesforce/leads.py

from .auth import authenticate
from .exceptions import SalesforceError
from .utils import normalize_lead_data

def add_lead(name, email, phone, car_model, suspension_type, payment_method, contact_preferred_time):
    try:
        access_token = authenticate("username", "password", "security_token")

        # Normalizar los datos del lead antes de agregarlos a Salesforce
        normalized_data = normalize_lead_data(name, email, phone, car_model, suspension_type, payment_method, contact_preferred_time)

        # Código para agregar un lead a Salesforce usando el token de acceso y los datos normalizados
        pass

    except Exception as e:
        raise SalesforceError(f"Error al agregar lead a Salesforce: {str(e)}")

