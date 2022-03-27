// 기능개발
function solution(progresses, speeds) {
    let answer = []
    let n = 0
    let stack = []
    while (progresses.length > 0) {
        for(let i = 0; i < progresses.length; i++) {
            progresses[i] += speeds[i]
        }
        
        while (true) {
            if (progresses[0] >= 100) {
                stack.push(progresses.shift())
                speeds.shift()
            }
            else {
                if (stack.length > 0) {
                    answer.push(stack.length)
                    stack = []
                }
                n++
                break
            }
        }
    }
    return answer
}