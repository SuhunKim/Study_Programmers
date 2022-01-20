using System;
using System.Linq;

public class Solution {
    public int solution(int[] numbers) {
    //   int answer = 0;
    //   int num=0;
    //   for(int i=0;i<numbers.Length;i++)
    //   {
    //       num+=numbers[i];
    //   }
    //   answer = 45-num;
        return 45-numbers.Sum();
    }
}
