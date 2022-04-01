function solution(bridge_length, weight, truck_weights) {
    let time = 0
    let stack = []
    while(truck_weights.length > 0) {
        if (stack.length == bridge_length) weight += stack.shift();
        if (weight - truck_weights[0] >= 0) {
            let ts = truck_weights.shift()
            stack.push(ts)
            weight -= ts
        }
        else stack.push(0);
        time++
    }

    return stack.length > 0 ? time+bridge_length : time
}