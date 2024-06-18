using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int exp = 0;
        int quo=0, rem=n;   //몫  quo, 나머지 rem
        int cnt=0;
        int[] num= new int[1000];
        
        while (rem > 0)       // 3진수를 구한다. 
            {
                quo = rem / 3;
                rem = rem % 3;
                num[cnt++] = rem;
                rem = quo;
            }


            exp = cnt;      //지수를 대입한다.
      
        for (int i = 0; i < cnt; i++)
            {
                if (num[i] >= 0 && num[i] < 3)
                {
                answer += (Convert.ToInt32( Math.Pow(3,--exp)) * num[i]);   // (num[N]*3^exp) + ... +  계산 수행
                }
            }
        return answer;
    }
}
