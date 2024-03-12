def checkMagazine(magazine: Array[String], note: Array[String]) {

  // val dictionary = Map[String, Array[String]]()

  def buildChainedHashTable(
      words: List[String],
      table: Map[String, List[String]]
  ): Map[String, List[String]] = words match {
    case head :: tail if (table contains head) => {
      val chain = (head -> { head :: table(head) })
      buildChainedHashTable(tail, table + chain)
    }
    case head :: tail =>
      buildChainedHashTable(tail, table + (head -> List(head)))
    case Nil => table
  }

  val dictionary =
    buildChainedHashTable(magazine.toList, Map[String, List[String]]())

  def findWord(
      note: List[String],
      dictionary: Map[String, List[String]]
  ): Unit = note match {
    case head :: tail if dictionary.contains(head) => {
      val chain = dictionary(head)
      if (chain.isEmpty) println("No")
      else findWord(tail, dictionary + (head -> chain.tail))
    }

    case Nil => println("Yes")
    case _   => println("No")
  }

  findWord(note.toList, dictionary)
}

val magazine = Array("give", "me", "night", "one", "grand", "today", "night")
val note = Array("give", "one", "grand", "today")

checkMagazine(magazine, note)
