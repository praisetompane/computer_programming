object Solution {
  val a = "bacdc"
  val b = "dcfezq"

  def makeAnagrams(a: String, b: String, deletions: Int): Int = {

    def checkLetter(letter: Char, subject: String, comp: String) = {
      val subjectOccurrance = subject.count(_ == letter)
      val compOccurrance = comp.count(_ == letter)
      val deletions = math.abs(subjectOccurrance - compOccurrance)

      if (subjectOccurrance > compOccurrance) {
        (subject.diff(letter.toString * deletions), comp, deletions)
      } else if (subjectOccurrance < compOccurrance) {
        (subject, comp.diff(letter.toString * deletions), deletions)
      } else (subject, comp, deletions)
    }

    def areAnagrams(a: String, b: String) = a.sorted == b.sorted

    if (areAnagrams(a, b)) deletions
    else {
      val stringAChanges = a.map { letter =>
        {
          val changed = checkLetter(letter, a, b)
          if (areAnagrams(changed._1, changed._2)) changed._3
          else changed._3
        }
      }
      val stringBChanges = b.map { letter =>
        {
          val changed = checkLetter(letter, b, a)
          if (areAnagrams(changed._1, changed._2)) changed._3
          else changed._3
        }
      }
      stringAChanges.sum + stringBChanges.sum
    }
  }

  println(makeAnagrams(a, b, 0))
}
