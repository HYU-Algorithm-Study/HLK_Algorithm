function solution(survey, choices) {
  const obj = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };

  const max = (a, b) => {
    if (obj[a] === obj[b]) return [a, b].sort()[0];
    return obj[a] > obj[b] ? a : b;
  };

  survey.forEach((a, i) => {
    if (choices[i] < 4) obj[a[0]] += 4 - choices[i];
    else if (choices[i] > 4) obj[a[1]] += choices[i] - 4;
  });

  return max("R", "T") + max("C", "F") + max("J", "M") + max("A", "N");
}
