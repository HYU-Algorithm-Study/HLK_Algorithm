function solution(brown, yellow) {
  const sum = brown + yellow;

  for (let i = 1; i <= Math.sqrt(sum); i++) {
    const j = sum / i;
    if (sum % i) continue;
    if (yellow === (i - 2) * (j - 2)) return [j, i];
  }
}
