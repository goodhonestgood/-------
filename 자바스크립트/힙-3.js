function solution (operations) {

    let queue = []
    for(let op of operations) {
        op = op.split(" ")
        if (op[0] === "I") {
            queue.push(op[1])
        } else if (op[0] === "D") {
            queue.sort((a,b)=>a-b)
            if (op[1] === "1") {
                queue.pop()
            } else {
                queue.shift()
            }
        }
    }
    return queue.length>0? [Math.max(...queue), Math.min(...queue)] : [0,0]
}