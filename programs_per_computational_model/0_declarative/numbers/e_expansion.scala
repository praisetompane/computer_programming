import scala.annotation.tailrec
def e_series_expansion(x: Double): Double = {
  def factorial(number: Int): Int = {
    @tailrec
    def _factorial(total: Int = 1, number: Int): Int = number match {
      case 0 => total
      case _ => _factorial(total * number, number - 1)
    }
    _factorial(1, number)
  }

  def sum(total: Double, iteration: Int): Double = {
    if (iteration > 9) total
    else {
      sum(total + Math.pow(x, iteration) / factorial(iteration), iteration + 1)
    }
  }
  sum(1 + x, 2)
}

@main def main(): Unit = {
  println(e_series_expansion(1.0000))
}
