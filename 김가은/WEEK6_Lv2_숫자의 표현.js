// 최종 풀이
function solution(n) {
  let answer = 0;

  for (let i = 1; i <= n; i++) {
    if (n % i === 0 && (n % 2 || (n / i) % 2)) answer++;
  }

  return answer;
}
