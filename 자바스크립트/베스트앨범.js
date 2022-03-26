function solution(genres, plays) {
    hashmap = {}
    for (let i = 0; i < genres.length; i++) {
        if (genres[i] in hashmap) hashmap[genres[i]].push(plays[i]);
        else hashmap[genres[i]] = [plays[i]];
    }
    for (const h in hashmap) {
        hashmap[h].push(hashmap[h].reduce((a,b)=>a+b))
        hashmap[h].sort((a,b)=>b-a)
        hashmap[h] = hashmap[h].slice(0,3)
    }

    hasharr = []
    for (let i = 0; i < genres.length; i++) {
        if (hashmap[genres[i]][1]==plays[i] || hashmap[genres[i]][2]==plays[i]) {
            hasharr.push([hashmap[genres[i]][0],plays[i],i])
        }
    }
    hasharr.sort((a,b) => {
        return b[0]-a[0] == 0 ? b[1]-a[1] : b[0]-a[0]
    })
    
    return hasharr.map(a=>a[2])
}