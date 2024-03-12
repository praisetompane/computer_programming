/*
    Objective:
        Return minimum bribes
            to generate current queue state
        Or "Too chaotic" if it's not possible

    Constraints:
        MaxBribes = 2
        People at the back bribe ones infront
            No backwards bribing
        Initial array was 1,2,3,4,5,6,7,8


        target = 1 2 5 3 7 8 6 4


        1,2,3,4,5,6,7,8

        1,2,5,3,4,6,7,8

        1,2,5,3,7,4,6,8

        1,2,5,3,7,8,4,6

        1,2,5,3,7,8,6,4


        2 2 2

    Input:
        final state of the array

    Algo:
        bribes = 0
        for each value
            bribesUsed = abs(value - currentIndex)
            if(bribesUsed > MaxBribes) println("too chaotic")
            else bribes += bribesUsed
 */

/*
    Ascending bubble sort

    if(index == arr.length) finish
    if(value > nextValue)
        swap(value, nextValue)
        increment bribes


    Any person in the queue can bribe the person directly in front of them to swap positions.
    One person can bribe at most two others
 */

def minimumBribes(finalQueue: Array[Int]): Unit = {
  val MaxBribes = 2
  val finalIndex = finalQueue.length - 1
  var bribes = 0
  var swapped = true
  val zeroIndexOffset = 1

  def swap(indexA: Int, indexB: Int) = {
    val tempB = finalQueue(indexB)
    finalQueue(indexB) = finalQueue(indexA)
    finalQueue(indexA) = tempB
  }

  while (swapped) {
    swapped = false
    finalQueue.zipWithIndex.foreach { case (value: Int, index: Int) =>
      val nextIndex = index + 1
      val distanceFromOriginalPosition =
        math.abs(value - (index + zeroIndexOffset))

      if (value > index && distanceFromOriginalPosition > MaxBribes) {
        println("Too chaotic")
        return
      }

      if (index != finalIndex && value > finalQueue(nextIndex)) {
        swapped = true
        bribes += 1
        swap(index, nextIndex)
      }
    }
  }

  println(bribes)
}

minimumBribes(Array(1, 2, 5, 3, 7, 8, 6, 4))
