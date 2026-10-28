# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(current_mileage, last_service_mileage, service_interval):
    miles_since_service = float(current_mileage) - float(last_service_mileage)
    maintenance_alert_status = 1 if miles_since_service >= float(service_interval) else 0
    return miles_since_service, maintenance_alert_status
