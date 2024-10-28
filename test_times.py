from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = []
    assert result == expected

def test_two_intervals():
    t_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    t_2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    expected_two_intervals = [("2010-01-12 10:30:00", '2010-01-12 10:37:00'),
                               ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert compute_overlap_time(t_1, t_2) == expected_two_intervals   

def test_directly_consecutive_times():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    assert result == expected