/*
    Stacks are useful for:
        - processing data in reverse order
        - undo operation
        - executing function calls in a networked application
            - the last one that came thrught must be ran 
                - it's output substituted in the second last function and so on...
*/
circleOpeningBracket = '('
circleClosingBracket = ')'
curlyOpeningBracket = '{'
curlyClosingBracket = '}'
squareOpeningBracket = '['
squareClosingBracket = ']'

const bracketsMatch = (code) => {
    characters = code.split('')
    //stack in name for learning
    //keeps track of opening brackets that still need to be closed
    openingBracketStack = []
    for (i = 0; i < characters.length; i++) {
        character = characters[i]
        if (isOpeningBrace(character)) {
            openingBracketStack.push(character)
        } else if (isClosingBrace(character)) {
            if (!isClosingBracketOfRecentOpeningBracket(character, openingBracketStack)) {
                return `Incorrect closing bracket "${character}" at index ${i}`
            }
        }
    }
    if (openingBracketStack.length == 0) {
        return true
    }
    else {
        return `${openingBracketStack.pop()} does not have a closing brace`
    }
}

const isClosingBracketOfRecentOpeningBracket = (character, openingBracketStack) => {
    const openingBracket = {
        [circleClosingBracket]: circleOpeningBracket,
        [curlyClosingBracket]: curlyOpeningBracket,
        [squareClosingBracket]: squareOpeningBracket
    }
    return openingBracket[character] == openingBracketStack.pop()
}

const isOpeningBrace = (character) => [circleOpeningBracket, curlyOpeningBracket, squareOpeningBracket].includes(character)

const isClosingBrace = (character) => [circleClosingBracket, curlyClosingBracket, squareClosingBracket].includes(character)

console.log('Should be invalid: is valid', bracketsMatch('[(,()}])'))
console.log('Should be valid: is valid', bracketsMatch('[[({})t]]'))
console.log('Should be invalid: is valid', bracketsMatch('[}])'))
console.log('Should be invalid: is valid', bracketsMatch('[[[({})t]])'))
console.log('Should be invalid: is valid', bracketsMatch('[[[({})t]]'))