function solution(n) {
  let answer = n;
  const removeZero = (num) => num.toString(2).replace(/0/g, "").length;

  while (true) {
    answer++;
    if (removeZero(n) === removeZero(answer)) return answer;
  }
}
