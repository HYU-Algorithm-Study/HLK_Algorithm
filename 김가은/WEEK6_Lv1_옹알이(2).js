// 최종 풀이
function solution(babbling) {
  let answer = 0;

  for (let x of babbling) {
    if (/ayaaya|yeye|woowoo|mama/g.test(x)) continue;
    if (!x.replace(/aya|ye|woo|ma/g, "").length) answer++;
  }

  return answer;
}
