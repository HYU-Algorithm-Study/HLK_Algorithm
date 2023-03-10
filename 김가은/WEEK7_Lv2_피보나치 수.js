function solution(n) {
  let prev = 1;
  let prevprev = 1;

  for (let i = 3; i <= n; i++) {
    const newPrev = prev;
    prev = (prev + prevprev) % 1234567;
    prevprev = newPrev % 1234567;
  }

  return prev;
}
