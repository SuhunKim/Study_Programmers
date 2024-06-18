using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) {
     int[] answer = new int[] { };
        int[,] arr = new int[n,n];    //n*n Matrix
        int x = -1, y = 0;
        int cnt = 1;
        //최상위 1 ->    n-1만큼 아래이동 -> n-1만큼 우측이동 -> n-1-1만큼 상좌이동
        //              n-3만큼 아래이동 -> n-3만큼 우측이동 -> n-3-1만큼 상좌이동
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
            if (i % 3 == 0) x++;
            else if (i % 3 == 1) y++;
            else {x--;y--;}
                arr[x, y] = cnt++;
            }
        }
        List<int> array = new List<int>();
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (arr[i, j] > 0)
                {
                    array.Add(arr[i, j]);
                }
            }
        }
        answer = array.ToArray();
        return answer;
    }
}
