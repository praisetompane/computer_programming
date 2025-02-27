# Imprecise but fun way to think about computation models

# We have things we need to do.
#### What is your solution?
- We can do things => Declarative

# There is a lot of things to do.
#### What is your solution?
- We can do these things at the same time => Concurrent Declarative
    - value proposition: define mathematical functions
       easier to reason about and test.

# There is too much going on from doing things at the same time, to finish all the things we need to do, thus we are running out of resources.
#### What is your solution?
- We want to do these things at the same time ONLY when we need to => Lazy Declarative.
    - value proposition: adds data-flow concurrency
       retains declarative properties
       allows/adds flexible and incremental execution

# We are doing lots of things at the same time, but we forget after we are done, thus have to redo them when we need them, We are running out of resources.
#### What is your solution?
- We want to do these things at the same time ONLY when we need to and save the result of our work => Stateful 
    - value proposition: explicit state
       allows programs whose behavior can change over time
       IF correctly done(i.e. using encapsulation),
            can reason easily and test like declarative ones.

# We are doing lots of things at the same time and saving our results everywhere and stepping over each other and it is a mess!
#### What is your solution?
- We want to do these things at the same time ONLY when we need to and save the result of our work in an organised way separate from each other => Object Orientated
    - value proposition:  gives us object orientated programming(OOP)
        OOP := programming style, for stateful programming with data abstractions.
        allows ease of use of powerful techniques
            - polymorphism
            - inheritance
            ...

# We are doing lots of things at the same time and saving our results in an organised way separate from each other, but there is some resource we HAVE to share[read and write to].
#### What is your solution?
- Shared State Concurrent
    - value proposition:  combines stateful and concurrent
        IF correctly done    
            with techniques for mastering interleaving
                techniques := {monitoring, transactions}
        benefits of Stateful and Concurrent
