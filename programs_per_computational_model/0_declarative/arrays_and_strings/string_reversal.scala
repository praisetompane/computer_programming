import io.Source.stdin
import scala.annotation.tailrec

/*
    Constraints:
        0 <= T <= 10
        0 <= n <= 10^2
    Performance:
        Time:
            T = number of test cases
            n = length of each string
            O(T * n)

 */
object Solution {
  def main(args: Array[String]): Unit = {
    @tailrec
    def rotate(rotations: Int, rotated: String, output: String): String = {
      if (rotations <= 0) output
      else {
        val _rotated = rotated.appended(rotated(0)).drop(1)
        rotate(rotations - 1, _rotated, output ++ _rotated ++ " ")
      }
    }

    val incomingStrings = stdin.getLines().takeWhile(_.nonEmpty).toList
    incomingStrings.drop(1).foreach { input =>
      println(rotate(input.length(), input, ""))
    }
  }
}
