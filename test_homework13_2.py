from homework13 import humanize_car_trip_info
import pytest


def test_positive_values():
    result = humanize_car_trip_info(seconds=10, speed_meters_per_seconds=3, car_weight=1000)
    expected_result = "A vehicle weighing 1000 kg moved for 10 seconds at a speed of 3m/sec, and covered a distance of 30.0 meters"
    assert expected_result


@pytest.mark.parametrize("seconds, speed, weight", [
    (-10, 3, 1000),
    (10, -3, 1000),
    (10, 3, -1000),
])
def test_invalid_values(seconds, speed, weight):
    with pytest.raises(ValueError):
        humanize_car_trip_info(seconds=seconds, speed_meters_per_seconds=speed, car_weight=weight)
