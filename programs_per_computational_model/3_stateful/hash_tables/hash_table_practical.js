//start non hash table solution
votes = []

function addVote(candidate) {
    votes.push(candidate)
}

function countVotes() {
    tally = {}
    for (i = 0; i < votes.length; i++) {
        candidate = votes[i];
        if (tally[candidate]) {
            tally[candidate]++;
        } else {
            tally[candidate] = 1
        }
    }
    return tally
}

addVote("Papudi")
addVote("Papudi")
addVote("Mosotho")
addVote("Thato")
console.log('Count votes linear ', countVotes(votes))

/*
    O(1) insetion
    𝑂(𝑁) counting/read
*/
//end non hash table solution
votesH = {}

function addVoteH(candidate, votes) {
    if (votes[candidate]) {
        votes[candidate]++
    } else {
        votes[candidate] = 1
    }
    return votes;
}

addVoteH("Papudi", votesH)
addVoteH("Papudi", votesH)
addVoteH("Mosotho", votesH)
addVoteH("Thato", votesH)
/*
    O(1) insert
    O(1) read   
*/
console.log('Count votes hash ', votesH)