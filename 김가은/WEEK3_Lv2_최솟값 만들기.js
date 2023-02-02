// 최종 풀이
function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  return A.map((a, i) => a * B[i]).reduce((p, c) => p + c);
}
