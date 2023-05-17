let numberOfBeers = Math.floor(Math.random()*(150-50)) + 50

for (let i = 1; i<=numberOfBeers; i++) {
    console.log(`${numberOfBeers} bottle${(numberOfBeers==1)? "" : "s"} of beer on the wall
${numberOfBeers} bottle${(numberOfBeers==1)? "" : "s"} of beer
Take ${i} down, pass ${(i==1)? "it" : "them"} around
${numberOfBeers-i} bottle${(numberOfBeers==1) ? "" : "s"} of beer on the wall\n`)
    numberOfBeers -= i
}

if (numberOfBeers != 0) {
    console.log(`${numberOfBeers} bottle${(numberOfBeers==1) ? "" : "s"} of beer on the wall
${numberOfBeers} bottle${(numberOfBeers==1) ? "" : "s"} of beer
Take all down, pass them around
no bottles of beer on the wall\n`)
}