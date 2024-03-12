import scala.collection.immutable.Stack

object Solution {
  def isCorrectClosingBracket(
      sourceCharacters: List[Char],
      stackedCharacters: List[Char],
      expectedOpeningBrace: Char
  ) = stackedCharacters match {
    case stackedHead :: stackedTail if stackedHead == expectedOpeningBrace =>
      isBalanced(sourceCharacters, stackedTail)
    case stackedHead :: stackedTail => false
    case Nil                        => false
  }

  def isBalanced(
      sourceCharacters: List[Char],
      stackedCharacters: List[Char]
  ): Boolean = sourceCharacters match {
    case Nil if stackedCharacters.isEmpty  => true
    case Nil if !stackedCharacters.isEmpty => false
    case sourceHead :: sourceTail =>
      if (sourceHead == '(' || sourceHead == '[' || sourceHead == '{')
        isBalanced(sourceTail, sourceHead :: stackedCharacters)
      else if (sourceHead == ')')
        isCorrectClosingBracket(sourceTail, stackedCharacters, '(')
      else if (sourceHead == ']')
        isCorrectClosingBracket(sourceTail, stackedCharacters, '[')
      else isCorrectClosingBracket(sourceTail, stackedCharacters, '{')
  }

  println(isBalanced(List('{', '[', '(', ']', ')', '}'), List()))
}
