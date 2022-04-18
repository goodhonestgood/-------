function solution(brown, yellow) {
    brown -= 4
    let i = 3
   
    while (true) {
        if (brown <= 4*(i-2) && (i-2)*(brown-(2*(i-2))) == yellow*2) {
            return [i, (brown-(2*(i-2)))/2+2]
        }
        i++
    }
}