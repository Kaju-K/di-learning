string1 = "Astronomer"
string2 = "Moon starer"

function anagramChecker(str1, str2) {
    str1Sorted = str1.replace(" ", "").toLowerCase().split("").sort().join("")
    str2Sorted = str2.replace(" ", "").toLowerCase().split("").sort().join("")

    if (str1Sorted == str2Sorted) {
        return true
    }
    return false
}

console.log(anagramChecker(string1, string2))