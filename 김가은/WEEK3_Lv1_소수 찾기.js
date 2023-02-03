// 최종 풀이
function solution(n) {
  const sqrt = Math.sqrt(n);

  let arr = Array.from({ length: n }, (_, i) => i + 1);

  for (let i = 2; i <= sqrt; i++) {
    for (let j = i; j <= n; j += i) {
      if (j !== i) arr[j - 1] = "";
    }
  }

  return arr.filter((a) => a).length - 1;
}
