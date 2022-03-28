// 프린터

function solution(priorities, location) 
    let sequence = 0

    while (true) {
        let priority = priorities.shift()
        let maxValue = Math.max(...priorities)
        if (priority >= maxValue) {
            sequence++
            if (0 == location) break;
        }
        else {
            priorities.push(priority)
        }
        location = location-1 == -1 ? priorities.length-1 : location-1
    }

    return sequence
}