import java.io._
import java.math._
import java.security._
import java.text._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {

  /*
        Analysis

        Mountain = consecutive steps above sea level
                starting with a step up from sea level and ending with a step down to sea level.

        Valley = sequence
                    consecutive steps
                        below sea level
                    starting
                        step down from sea level
                    ending
                        with a step up to sea level.

        Given Gary's sequence of up and down steps during his last hike
            Find number of valleys
                he walked through

        Key
            U = uphill step
            D = downhill step

        Start of hike = sea level
        End of hike = sea level


        =============================

        stepsBelowLevel: Int

        Representation?
            Stack: LIFO = No
            Queue: FIFO

            UDDDUDUU

            U
                stepsBelowLevel = -1
            D
                stepsBelowLevel = 0
            D
                stepsBelowLevel = 1
            D
                stepsBelowLevel = 2
            ==========================> Valley
            U
                stepsBelowLevel = 1
            D
                stepsBelowLevel = 2
            U
                stepsBelowLevel = 1
            U
                stepsBelowLevel = 0


        Count valleys
        For whole queue
            Extract step
                if step == U, stepsBelowLevel -=1
                if step == D && stepsBelowLevel == 0, stepsBelowLevel +=1
                if step == D, stepsBelowLevel +=1


   */
  // Complete the countingValleys function below.
  def countingValleys(n: Int, s: String): Int = {
    val stepsQueue = s.split("").toList
    count(0, 0, stepsQueue, "")
  }

  private def count(
      valleys: Int,
      stepsBelowSeaLevel: Int,
      steps: List[String],
      previousMove: String
  ): Int = steps match {
    case head :: tail
        if head == "U" && previousMove == "U" && stepsBelowSeaLevel == 0 =>
      count(valleys + 1, stepsBelowSeaLevel - 1, tail, head)

    case head :: tail
        if head == "D" && previousMove == "U" && stepsBelowSeaLevel == 0 =>
      count(valleys + 1, stepsBelowSeaLevel + 1, tail, head)

    case head :: tail if head == "U" =>
      count(valleys, stepsBelowSeaLevel - 1, tail, head)

    case head :: tail if head == "D" =>
      count(valleys, stepsBelowSeaLevel + 1, tail, head)

    case Nil if previousMove == "U" && stepsBelowSeaLevel == 0 => valleys + 1

    case Nil => valleys
  }

  def main(args: Array[String]) {
    val stdin = scala.io.StdIn

    // val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

    val n = stdin.readLine.trim.toInt

    val s = stdin.readLine

    val result = countingValleys(n, s)

    println(result)

  }
}
