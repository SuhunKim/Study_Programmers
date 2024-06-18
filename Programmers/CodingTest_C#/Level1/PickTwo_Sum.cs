using System;
using System.Collections;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[] { };
			List<int> array = new List<int>();
			

			int cnt = 0;
			for (int i = 0; i < numbers.Length - 1; i++)
			{
				for (int j = i+1; j < numbers.Length; j++)
				{
					if (!array.Contains(numbers[i] + numbers[j]))
					{
					 array.Add(numbers[i] + numbers[j]);
					 cnt++;
					}
				}
			}

			array.Sort();
			answer = array.ToArray();
			return answer;        //더 간결한 알고리즘 필요.
    }
}
