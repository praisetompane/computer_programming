(define (average guess xquotient) (/ (+ guess xquotient) 2))

(define (improve guess x ) (average guess (/ x guess)))

(define (square x) (* x x))

(define (isGoodEnough? guess x)
  (< (abs(- (square guess) x)) .001))

(define (try guess x)
  (IF(isGoodEnough? guess x)
    guess
    (try (improve guess x) x)))

(define (square_root x) (try 1 x))

(square_root 2)