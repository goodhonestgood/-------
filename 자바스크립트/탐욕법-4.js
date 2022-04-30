function solution1(people, limit) {
    let count = 0
    people.sort((a,b)=>b-a)
    while(people.length > 0) {
        let temp = people.shift()
        let arr = people.filter(a=>a<=limit-temp)
        if(arr[0] !== undefined) {
            people.splice(people.indexOf(arr[0]),1)
        }
        count++
    }
    
    return count
}



function solution(people, limit) {
    let count = 0
    people.sort((a,b)=>b-a)
    let i = 0
    let j = people.length-1
    while(i<j) {
        let temp = people[i]
        if(people[j] <= limit-temp) j--;
        i++
        count++
    }
    if(i==j) count++
    return count
}