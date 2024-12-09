def cars(manufacturer, model, **car_infos):
    """Print some information about that car you want."""
    car = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }
    for car_info, value in car_infos.items():
        car[car_info] = value
    
    return car



car1 = cars("BMW", "i330", edition="2018", option="full option")
car2 = cars("mercedes", "E200", color="gray", max_speed=240)
car3 = cars("tesla", "s", base="electric", max_speed=320, color="red")

print(car1)
print(car2)
print(car3)
