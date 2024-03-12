object Solution {
  def repeatedString(s: String, n: Long): Long = {

    val maxIndex = s.length - 1
    var numberOfAs = 0

    if (s == "a") n
    else {
      for (i <- Range.Long(0, n, 1)) {
        // println("in loop")
        for (patternCharacterIndex <- 0 until maxIndex) {
          println(s(patternCharacterIndex))
          if (s(patternCharacterIndex) == 'a') {
            // println("increment As")
            // println(patternCharacterIndex)
            numberOfAs += 1
          }
        }

      }
    }

    numberOfAs
  }

  println(repeatedString("aba", 10))
}
