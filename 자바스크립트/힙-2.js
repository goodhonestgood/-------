// 디스크 컨트롤러
// 우선순위 큐 : 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나온다
// 힙 : 완전 이진 트리, 부모와 자식간 비교만 하므로 시간복잡도가 낮다
// 다시해보기
function solution(jobs) {
    jobs.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
    let [answer,time,waitQueue] = [0,0,[]];

    for(let i = 0; i<jobs.length; ++i){
        const [reqTime, workTime] = jobs[i];
        if(i===0){
            time = (workTime + reqTime);
            answer += (time - reqTime);
        } else {
            if(reqTime <= time){
                waitQueue.push(jobs[i]);
            } else {
                if(waitQueue.length){
                    const [rt, wt] = waitQueue.shift();
                    time += wt;
                    answer += (time - rt);
                    --i;
                }
                else{
                    time = (workTime + reqTime);
                    answer += (time - reqTime);
                }
            }
        }
        waitQueue.sort((a,b) => a[1]-b[1])
    }
    if (waitQueue.length) {
        for(const job of waitQueue){
            const [reqTime, workTime] = job;
            time += workTime;
            answer += (time - reqTime);
        }
    }
    return parseInt(answer/jobs.length)
}