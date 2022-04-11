function solution(numbers) {
    numbers.sort((a, b) => (b.toString() + a.toString()) - (a.toString() + b.toString()));
    return numbers[0] == 0 ? "0" : numbers.join('')
}