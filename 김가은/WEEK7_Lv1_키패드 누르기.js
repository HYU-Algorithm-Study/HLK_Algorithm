// 최종 풀이
const func = (num1, num2) => {
  num1 = num1 ? num1 : 11;
  num2 = num2 ? num2 : 11;

  const subtract = Math.abs(num1 - num2);
  return Math.floor(subtract / 3) + (subtract % 3);
};

function solution(numbers, hand) {
  let left = 10;
  let right = 12;

  return numbers
    .map((a) => {
      const rightFunc = () => {
        right = a;
        return "R";
      };

      const leftFunc = () => {
        left = a;
        return "L";
      };

      if ([1, 4, 7].includes(a)) return leftFunc();
      else if ([3, 6, 9].includes(a)) return rightFunc();
      else {
        if (func(left, a) > func(right, a)) return rightFunc();
        else if (func(left, a) < func(right, a)) return leftFunc();
        else if (hand === "right") return rightFunc();
        else return leftFunc();
      }
    })
    .join("");
}
