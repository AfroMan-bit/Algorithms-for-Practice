function reverseStr (someString) {
    var newString = "";
    for (var i= someString.length-1; i >=0, i--){
        newString += someString[i];
    }
    console.log(newstring);
    return newString
}
 reverseStr ("hello")
