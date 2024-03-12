object Solution {
  def repeatedString(s: String, n: Long): Long = {

    val maxIndex = s.length - 1

    def countA(letter: Char, numberOfAs: Int) =
      if (letter == 'a') numberOfAs + 1 else numberOfAs

    def count(
        patternCharacterIndex: Int,
        numberOfCharacterChecked: Int,
        numberOfAs: Int
    ): Int =
      if (numberOfCharacterChecked == n) numberOfAs
      else if (patternCharacterIndex == maxIndex)
        count(
          0,
          numberOfCharacterChecked + 1,
          countA(s(patternCharacterIndex), numberOfAs)
        )
      else
        count(
          patternCharacterIndex + 1,
          numberOfCharacterChecked + 1,
          countA(s(patternCharacterIndex), numberOfAs)
        )

    if (s == "a") n
    else count(0, 0, 0)
  }
}
