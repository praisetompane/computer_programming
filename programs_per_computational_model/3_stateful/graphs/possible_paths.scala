/*
    0 0 1 0 0 1 0

    7
    starts with consecutively numbered clouds.

        clouds are thunderheads and others are cumulus

        Can:
            jump on any cumulus cloud 
            having a number that is 
            equal to the number of the c
            
            Can jump to current cloud plus 1 or 2 where destination is cumulus(safe)

    clouds
        0 = safe
        1 = avoid

    Start index = 0

    Output = minimum number of jumps required 
            from start index to last index


    ==================================================================

    paths = Find all possible paths
        path = index progression

        how do we know we've found them all?

    return shortest path 
        shortestPath = smallest number of steps

    ==================================================================


    ==== Data explore ====
    i = )
    o = 3

    currentPosition = 0

    if currentPosition + 2 != 1
        currentPosition += 2
    else
        currentPosition += 1 //since I can always WIN as per spec


    inject baseIncrement

        if currentPosition + baseIncrement >= ar.length
            if currentPosition + alternativeIncrement => ar.length
                return
        if currentPosition + baseIncrement != 1 
            currentPosition + baseIncrement
        else 
            currentPosition + alternativeIncrement


    Out of bounds??

    ====

    0 2 4 6

    0 2 3 4 6



    ===================================
    WINNER!!!
    jumps = 0
    currentPosition = 0

    if currentPosition >= ar.length, return steps
    if value at currentPosition + 2 != 1
        currentPosition += 2
        jumps += 1
    else    
        currentPosition += 1
        jumps += 1


    =====================================

    (0, 1, 0, 0, 0, 1, 0)

    filter out entries == 1

    get length of remaing safes spots
    if length%2 == 0, then return length/2
    else return length/2 + length%2

*/
//know all possible combinations

    private def count(jumps: Int, currentPosition, clouds: Array[Int]) {
        if(currentPosition >= clouds.length) jumps
        else if clouds(currentPosition + 2 != 1) count(jumps + 1, currentPosition + 2, clouds)
        else count(jumps + 1, currentPosition + 1, clouds)
    }