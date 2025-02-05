from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"make_id": 1, "name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"make_id": 2, "name": "Mercedes", "description": "Great cars. German technology"},
        {"make_id": 3, "name": "Audi", "description": "Great cars. German technology"},
        {"make_id": 4, "name": "Kia", "description": "Great cars. Korean technology"},
        {"make_id": 5, "name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    # Create CarMake instances with explicit make_id
    car_make_instances = {}
    for data in car_make_data:
        car_make = CarMake.objects.create(make_id=data['make_id'], name=data['name'], description=data['description'])
        car_make_instances[data['make_id']] = car_make  # Store by make_id

    # Create CarModel instances with correct ForeignKey references
    car_model_data = [
    {"model_id": 1, "name": "Pathfinder", "car_type": "SUV", "year": 2023, "car_make": 1, "dealer_id": 42},
    {"model_id": 2, "name": "Qashqai", "car_type": "SUV", "year": 2023, "car_make": 1, "dealer_id": 13},
    {"model_id": 3, "name": "XTRAIL", "car_type": "SUV", "year": 2023, "car_make": 2, "dealer_id": 87},
    {"model_id": 5, "name": "C-Class", "car_type": "SUV", "year": 2023, "car_make": 2, "dealer_id": 56},
    {"model_id": 6, "name": "E-Class", "car_type": "SUV", "year": 2023, "car_make": 2, "dealer_id": 31},
    {"model_id": 7, "name": "A4", "car_type": "SUV", "year": 2023, "car_make": 3, "dealer_id": 14},
    {"model_id": 8, "name": "A5", "car_type": "SUV", "year": 2023, "car_make": 3, "dealer_id": 39},
    {"model_id": 9, "name": "A6", "car_type": "SUV", "year": 2023, "car_make": 3, "dealer_id": 21},
    {"model_id": 10, "name": "Sorrento", "car_type": "SUV", "year": 2023, "car_make": 4, "dealer_id": 63},
    {"model_id": 11, "name": "Carnival", "car_type": "SUV", "year": 2023, "car_make": 4, "dealer_id": 29},
    {"model_id": 12, "name": "Cerato", "car_type": "Sedan", "year": 2023, "car_make": 4, "dealer_id": 77},
    {"model_id": 13, "name": "Corolla", "car_type": "Sedan", "year": 2023, "car_make": 5, "dealer_id": 91},
    {"model_id": 14, "name": "Camry", "car_type": "Sedan", "year": 2023, "car_make": 5, "dealer_id": 65},
    {"model_id": 15, "name": "Kluger", "car_type": "SUV", "year": 2023, "car_make": 5, "dealer_id": 12},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            model_id=data['model_id'],
            name=data['name'],
            car_make=car_make_instances[data['car_make']],  # Correctly referencing CarMake
            car_type=data['car_type'],
            year=data['year'],
            Dealer_Id=data['dealer_id']
        )
