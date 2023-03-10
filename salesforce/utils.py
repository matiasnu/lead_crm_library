# lead-crm-library/salesforce/utils.py

def normalize_lead_data(name, email, phone, car_model, suspension_type, payment_method, contact_preferred_time):
    # Código para normalizar los datos del lead antes de agregarlo a Salesforce
    normalized_data = {
        "FirstName": name.split()[0],  # Tomar el primer nombre del lead
        "LastName": name.split()[-1],  # Tomar el apellido del lead
        "Email": email,
        "Phone": phone,
        "Car_Model__c": car_model,  # Campo personalizado para el modelo del auto
        "Suspension_Type__c": suspension_type,  # Campo personalizado para el tipo de suspensión
        "Payment_Method__c": payment_method,  # Campo personalizado para el método de pago
        "Contact_Preferred_Time__c": contact_preferred_time  # Campo personalizado para el horario preferido de contacto
    }
    return normalized_data

