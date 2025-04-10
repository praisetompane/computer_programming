from arrays_and_strings.time_conversion import twelve_hour_time_to_twenty_four


def test_twelve_hour_time_to_twenty_four():
    assert twelve_hour_time_to_twenty_four("01:01PM") == "13:01"
    assert twelve_hour_time_to_twenty_four("11:10AM") == "11:10"
    assert twelve_hour_time_to_twenty_four("11:50PM") == "23:50"
    assert twelve_hour_time_to_twenty_four("12:40AM") == "00:40"
    assert twelve_hour_time_to_twenty_four("12:35PM") == "12:35"
