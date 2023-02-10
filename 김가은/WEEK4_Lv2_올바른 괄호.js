<<<<<<< HEAD
// 최종 풀이
=======
// 최종풀이
>>>>>>> kimGaeun
function solution(s) {
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack.at(-1) + s[i] === "()") stack.pop();
    else stack.push(s[i]);
  }

  return stack[0] ? false : true;
}

// 시간초과 난 풀이
function solution(s) {
  while (true) {
    let newS = s.split("()").join("");
    if (s === newS) break;
    s = newS;
  }

  return s ? false : true;
}
