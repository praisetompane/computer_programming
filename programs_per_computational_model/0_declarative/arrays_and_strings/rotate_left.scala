import scala.annotation.tailrec
/*
    for rotations
        foreach index
            newIndex = index - 1
            if newIndex >= 0
                newArray[newIndex] = array[index]
            else
                newArray[lastIndex] = array[index]
 */
def rotateLeft(a: Array[Int], d: Int): Array[Int] = {

  // Example of calculating a future state once
  @tailrec
  def new_index(currentIndex: Int, rotationsLeft: Int): Int =
    val decrement = 1
    val newIndex = currentIndex - decrement
    if rotationsLeft <= 0 then currentIndex
    else 
      if newIndex < 0 then
        new_index(a.length - decrement, rotationsLeft - decrement)
      else new_index(newIndex, rotationsLeft - decrement)

  // def new_index(currentIndex: Int, rotations: Int) = 
  //   val newDistance = currentIndex - rotations
  //   if (newDistance < 0) newDistance.abs - 1 else newDistance

  val newArray = new Array[Int](a.length)

  a.zipWithIndex.foreach { case (value: Int, index: Int) =>
    newArray(new_index(index, d)) = value
  }

  newArray
}


@main def main(): Unit = 
  rotateLeft(Array(1, 2, 3, 4, 5), 3).foreach(print)
  assert(rotateLeft(Array(1, 2, 3, 4, 5), 3).sameElements(Array(4,5,1,2,3)))
  println("completed successfully")