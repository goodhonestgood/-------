function solution(prices) {
    let answer = []
    while (prices.length > 0) {
        p = prices.shift()
        for(let i = 0; i < prices.length; i++) {
            if(prices[i] < p) break;
        }
        answer.push(i+1)
    }
    return answer
}