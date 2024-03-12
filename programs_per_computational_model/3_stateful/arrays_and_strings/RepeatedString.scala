/*

    Repeat `string` n times

        1 to n.toList.map(_ => )

    Find occurences of `a`
        filter when letter = `a`


    result = string.split()
    occurences = result.filter(l => l == "a").length * n

    ==================================

    generate n characters
        following the base pattern


    === SOL

    I'll explain here with an example, suppose the input is:

        aba
        10

    n = 10,
    means the string s = "aba"
    is repeated over the course of 10 letters,
    i.e. abaabaabaa. Now, we break this string further down.
    First part, the exactly divisible part,
    s1 = "abaabaaba" and the second part,
    the remainder part, s2 = "a".
    To represent the count of a in s1 and s2, we have,
    int(n/len(s)) or n//len(s) and s[:n%len(s)], multiplied by count of a in s, respectively.

    ========
    aba
    10

    abaabaabaa

    s1 = abaabaaba
    s2 = a

    whole



 */
/*

generate n characters
    following the base pattern

count number of 'a's
 */

object Soluition {
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

  println(repeatedString("aba", 10))
}
