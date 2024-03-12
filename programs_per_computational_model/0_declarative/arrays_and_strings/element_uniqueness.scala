import io.StdIn

/*
    Given:
        string of length N

    Objective: 
        remove characters that have already appeared
        i.e. remove duplicate characters    

    Constraints
        1 <= N <= 30000
*/
def remove_duplicates(items: List[String]): List[String] = items.distinct

@main def main(): Unit = 
    val str_a = List("aa", "aa")
    assert(str_a.distinct == List("aa")) 

    val numbers = List(1, 1, 5, 6, 6, 1, 9, 6, 10)
    assert(remove_duplicates(numbers) == List(1,5,6,9))
    println("completed successfully")