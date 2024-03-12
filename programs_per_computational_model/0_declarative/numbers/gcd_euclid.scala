import scala.annotation.tailrec

/*
  Given:
      Intergers, x, y
      if x > y
        largest = x
        smallest = y
        _gcd(largest, smallest)

      _gcd(largest, smallest)
        remainder = largest % smallest
        quotient = largest / smallest

        if remainder == 0, then quotient
        else _gcd(smallest, remainder)

  Performance:
    O(largest%smallest)
      similar to O(log₂N) where the problem size halves
      what does % do to problem space
 */
def gcd(x: Int, y: Int): Int = 
  @tailrec
  def _gcd(largest: Int, smallest: Int): Int =
    val remainder = largest % smallest
    if (remainder == 0) smallest
    else _gcd(smallest, remainder)
  
  if (x == y) x
  else if (x > y) _gcd(x, y)
  else _gcd(y, x)

@main def main() = 
  assert(gcd(10000, 12345) == 5)