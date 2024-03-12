def guess(x: Array[Array[Int]], cost: Int): Int = {
            if(isMagicSquare(x)) cost
            else {
                val improved = improve(x)
                guess(improved._1, cost + improved._2)
            }
        }
        
        def improve(y: Array[Array[Int]]) = {
            val availableNumbers = Array(1,2,3,4,5,6,7,8,9)

            for {
                r <- 0 to 2
                c <- 0 to 2
                val rowSum = y(r)(c) + y(r)(c + 1) + y(r)(c + 2)
                if(rowSum != magicConstant) {
                    val differenceFromMagicConstant = rowSum - magicConstant
                    val targetNumber1 = availableNumbers.filter(x => x - y(r)(c) == differenceFromMagicConstant &&
                                                              x + y(r)(c + 1)+ y(r)(c + 2) == magicConstant) 

                    val targetNumber2 = availableNumbers.filter(x => x - y(r)(c + 1) == differenceFromMagicConstant &&
                                                              x + y(r)(c)+ y(r)(c + 2) == magicConstant) 

                    val targetNumber3 = availableNumbers.filter(x => x - y(r)(c + 2) == differenceFromMagicConstant &&
                                                              x + y(r)(c + 1)+ y(r)(c) == magicConstant)
                    if(!targetNumber1.isEmpty) y(r)(c) = targetNumber1
                    else if(!targetNumber2.isEmpty) y(r)(c + 1) = targetNumber2
                    else if(!targetNumber3.isEmpty) y(r)(c + 2) = targetNumber3

                    y
              } 
            }   yield (y, cost!!!)              
        }
      
        def isMagicSquare(x: Array[Array[Int]]) = {
            val MagicSquareSum = 45
            
            if(s(0)(0) + s(0)(1) + s(0)(2) != magicConstant) false
            else if(s(1)(0) + s(1)(1) + s(1)(2) != magicConstant) false
            else if(s(2)(0) + s(2)(1) + s(2)(2) != magicConstant) false
            else if(s(0)(0) + s(1)(0) + s(2)(0) != magicConstant) false
            else if(s(0)(1) + s(1)(1) + s(2)(1) != magicConstant) false
            else if(s(0)(2) + s(1)(2) + s(2)(2) != magicConstant) false
            else s.map(_.sum).head == 45 //can be better!!
        }
        
        guess(s, 0)


        4   9   2
        3   5   7
        8   1   5
        
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2



        4 8 2
        4 5 7
        6 1 6

        4 9 2
        3 5 7
        8 1 6

        output  = 4

