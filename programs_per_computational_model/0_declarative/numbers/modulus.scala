import scala.annotation.tailrec

/*
  Performance:
    O(largest%smallest)
      similar to O(log₂N) where the problem size halves
      what does % do to a problem space?
        see "modulus.py" for graph

        NB: both log₂N and % divide the problem space with each iteration
              significantly it
              - log₂N: halve the problem space N per iteration
              - %: reduce the problem space to the quotient of x/y
 */
def mod(x: Int, y: Int): List[Int] = {
  @tailrec
  def _mod(largest: Int, smallest: Int, remainders: List[Int]): List[Int] = {
    val remainder = largest % smallest
    if (remainder == 0) remainders :+ remainder
    else _mod(smallest, remainder, remainders :+ remainder)
  }

  if (x >= y) _mod(x, y, List(x))
  else _mod(y, x, List(x))
}

@main def main() = {
  println(mod(1000000, 11))
  println(mod(1000000, 12345))
  println(mod(1000000, 999999))
}
