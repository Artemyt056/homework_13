def humanize_car_trip_info(*, seconds: int, speed_meters_per_seconds: int | float, car_weight: int) -> str:
    MIN_ALLOWED_VALUE = 0
    if seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if speed_meters_per_seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'speed_meters_per_seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if car_weight < MIN_ALLOWED_VALUE:
        raise ValueError(f'car_weight value cannot be less than {MIN_ALLOWED_VALUE}')

    result = f"A vehicle weighing {car_weight} kg moved for {seconds} seconds at a speed of 3m/sec, " \
             f"and covered a distance of {seconds * speed_meters_per_seconds} meters"
    return result
