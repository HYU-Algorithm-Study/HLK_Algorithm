function solution(s, skip, index) {
  const char = "abcdefghijklmnopqrstuvwxyz"
    .split("")
    .filter((a) => !skip.includes(a));

  let answer = "";

  for (let x of s) {
    let i = (char.indexOf(x) + index) % char.length;
    answer += char[i];
  }

  return answer;
}
