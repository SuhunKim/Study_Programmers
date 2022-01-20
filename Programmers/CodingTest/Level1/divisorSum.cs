using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int left, int right)
    {
    	int answer = 0;
        int cnt = 0;
        List<int> divEven = new List<int> { };
        List<int> divOdd = new List<int> { };
        for (int i = left; i <= right; i++)
        {
    	    cnt = 0;
            for (int j = 1; j < i; j++)
            {
                if (i%j==0)
                {
    			    cnt++;
                }
            }
    	    cnt++; //i 자신을 포함한 약수개수
    	    if (cnt % 2 == 0) divEven.Add(i);
    	    else divOdd.Add(i);
        }
        answer += divEven.Sum(); 
        answer -= divOdd.Sum();
        return answer;
    }
}
