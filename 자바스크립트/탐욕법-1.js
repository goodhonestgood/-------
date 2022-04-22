function solution1(n, lost, reserve) {
    const arr = lost.filter(st =>!(reserve.includes(st)));
    const arr2 = reserve.filter(st =>!(lost.includes(st)));
    arr.sort((a,b)=>a-b);
    arr2.sort((a,b)=>a-b);
    // 바로앞번호나 뒷번호
    var counts = n - arr.length;
    loop1: for (let i = 0; i < arr.length; i++) {
        loop2: for (let j = 0; j < arr2.length; j++) {
            if(arr[i]-1 == arr2[j]) {
                arr2[j] = -1;
                counts++;
                break loop2;
            } else if (arr[i]+1 == arr2[j]) {
                arr2[j] = -1;
                counts++;
                break loop2;
            } else continue loop2;
        }
        if (arr2.every((a=>a==-1))) {
            break loop1;
        }
    }
    return counts;
}

function solution(n, lost, reserve) {
    let count = n
    let i = 1
    let arr1 = lost.filter(st =>!(reserve.includes(st)));
    let arr2 = reserve.filter(st =>!(lost.includes(st)));
    arr1.sort((a,b)=>a-b);
    arr2.sort((a,b)=>a-b);
    
    while(i<=n){
        if (arr1.indexOf(i)>=0) {
            let lostShift = arr1.shift()
            let left = arr2.indexOf(lostShift-1)
            if(left >= 0) {
                console.log(arr2.splice(left,1))
            } else {
                let right = arr2.indexOf(lostShift+1)
                if(right >=0) {
                    console.log(arr2.splice(right,1))
                } else {
                    count--
                }
            }
        } else {
            i++
        }
    }
    return count
}