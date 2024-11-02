from times import compute_overlap_time, time_range
import pytest
import yaml
from pathlib import Path

# Load the YAML file
def load_test_cases():
    with open(Path(__file__).parent / "fixture.yaml", "r") as f:
        cases = yaml.safe_load(f)
    # Convert YAML data into tuples for parametrization
    test_data = []
    for case in cases:
        name, values = next(iter(case.items()))
        time_range_1 = time_range(
            values["time_range_1"]["start"], values["time_range_1"]["end"],
            values["time_range_2"].get("interval_count"), values["time_range_2"].get("interval_length"))
        time_range_2 = time_range(
            values["time_range_2"]["start"], values["time_range_2"]["end"],
            values["time_range_2"].get("interval_count"), values["time_range_2"].get("interval_length"))
        expected = [tuple(pair) for pair in values["expected"]]
        test_data.append((time_range_1, time_range_2, expected))
    return test_data

@pytest.mark.parametrize("first_range, second_range, expected", load_test_cases())
def test_compute_overlap_time(first_range, second_range, expected):
    result = compute_overlap_time(first_range, second_range)
    assert result == expected




# def test_generic_case():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
#     assert compute_overlap_time(large, short) == expected

# def test_no_overlap():
#     short = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     large = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
#     result = compute_overlap_time(large, short) 
#     expected = []
#     assert result == expected

# def test_two_intervals():
#     t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
#     t_2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

#     expected_two_intervals = [("2010-01-12 10:30:00", '2010-01-12 10:37:00'),
#                                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

#     assert compute_overlap_time(t_1, t_2) == expected_two_intervals   

# def test_directly_consecutive_times():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
#     result = compute_overlap_time(large, short) 
#     expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
#     assert result == expected

# def test_start_time_after_end_time():
#     with pytest.raises(ValueError):
#         time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


