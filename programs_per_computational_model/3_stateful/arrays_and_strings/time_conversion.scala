def timeConversion(s: String): String = {
  if (!s.isEmpty && s.length == 10) {
    val dayTimeIndicator = s.substring(8, 10)
    val hour = s.substring(0, 2)
    val minutes = s.substring(3, 5)
    val seconds = s.substring(6, 8)
    val hourConversionTable = Map(
      "00PM" -> "24",
      "11PM" -> "23",
      "10PM" -> "22",
      "09PM" -> "21",
      "08PM" -> "20",
      "07PM" -> "19",
      "06PM" -> "18",
      "05PM" -> "17",
      "04PM" -> "16",
      "03PM" -> "15",
      "02PM" -> "14",
      "01PM" -> "13",
      "11AM" -> "11",
      "10AM" -> "10",
      "09AM" -> "09",
      "08AM" -> "08",
      "07AM" -> "07",
      "06AM" -> "06",
      "05AM" -> "05",
      "04AM" -> "04",
      "03AM" -> "03",
      "02AM" -> "02",
      "01AM" -> "01"
    )
    val convertedHour = hourConversionTable(s"$hour$dayTimeIndicator")
    s"$convertedHour:$minutes:$seconds"
  } else ""
}

assert(timeConversion("07:05:45PM") == "19:05:45")
assert(timeConversion("") == "")
assert(timeConversion("07:05") == "")
assert(timeConversion("00:00:00PM") == "24:00:00")
assert(timeConversion("11:00:00PM") == "23:00:00")
assert(timeConversion("10:00:00PM") == "22:00:00")
assert(timeConversion("09:00:00PM") == "21:00:00")
assert(timeConversion("08:00:00PM") == "20:00:00")
assert(timeConversion("07:00:00PM") == "19:00:00")
assert(timeConversion("06:00:00PM") == "18:00:00")
assert(timeConversion("05:00:00PM") == "17:00:00")
assert(timeConversion("04:00:00PM") == "16:00:00")
assert(timeConversion("03:00:00PM") == "15:00:00")
assert(timeConversion("02:00:00PM") == "14:00:00")
assert(timeConversion("01:00:00PM") == "13:00:00")

assert(timeConversion("01:00:00AM") == "24:00:00")
assert(timeConversion("02:00:00AM") == "24:00:00")
assert(timeConversion("03:00:00AM") == "24:00:00")
assert(timeConversion("04:00:00AM") == "24:00:00")
assert(timeConversion("05:00:00AM") == "24:00:00")
assert(timeConversion("06:00:00AM") == "24:00:00")
assert(timeConversion("07:00:00AM") == "24:00:00")
assert(timeConversion("08:00:00AM") == "24:00:00")
assert(timeConversion("09:00:00AM") == "24:00:00")
assert(timeConversion("10:00:00AM") == "24:00:00")
assert(timeConversion("11:00:00AM") == "24:00:00")
assert(timeConversion("12:00:00AM") == "24:00:00")
