// 최종 풀이 1
function solution(s) {
  return s.toLowerCase().replace(/\b[a-z]/g, (a) => a.toUpperCase());
}

// 최종 풀이 2
function solution(s) {
  return s
    .toLowerCase()
    .split(" ")
    .map((a) => a.replace(a[0], a[0]?.toUpperCase()))
    .join(" ");
}
