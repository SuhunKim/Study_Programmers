using System;

public class Solution {
    public long[] solution(long[] numbers) 
   {
        long[] answer = new long[numbers.Length];
        //numbers[i] 보다 크고 비트의 차이가 1,2개 나는 수 중에 가장 작은 수 numbers[i]에서 1씩추가해서 다른지점이 1,2개이면 그 수가 answer에 대입
        long lsb;
        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] % 2 == 0)    //x가 짝수일 경우 x+1이 가장 작은 수
            {
                    answer[i]=(numbers[i]+1);
            }
            else    //x가 홀수인 경우
            {
                lsb  = numbers[i]+1 & (-numbers[i]);
                answer[i] = (numbers[i] | lsb) & (~(lsb >> 1));
            }
        }
        return answer;
    }
}
