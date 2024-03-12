/*
    Objective:
        Return minimum swaps required

    You are allowex to swap any elements

    Assumptions
        Number always start from 1
 */

/*
    Foreach value, currentIndex pair
        expectedIndexValue = index + 1
        if expectedIndexValue == value, continue
        else
            currentValueCorrectIndex = value - 1
            swap(currentIndex, currentValueCorrectIndex)
 */

def minimumSwaps(list: Array[Int]): Unit = {
  var swaps = 0
  var swapped = true
  val zeroIndexOffset = 1

  def swap(indexA: Int, indexB: Int) = {
    val tempB = list(indexB)
    list(indexB) = list(indexA)
    list(indexA) = tempB
  }
  var i = 1
  while (i > 0) {
    swapped = false
    list.zipWithIndex.foreach { case (value: Int, index: Int) =>
      val expectedIndexValue = index + zeroIndexOffset
      list.foreach(print)
      if (expectedIndexValue != value) {
        swapped = true
        swaps += 1
        val currentValueCorrectIndex = value - zeroIndexOffset
        swap(index, currentValueCorrectIndex)
        println
      }
    }
    i -= 1
    println("out")
  }

  println(s"swaps $swaps")
}

minimumSwaps(Array(4, 3, 1, 2))
