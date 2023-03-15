package onboard;

import java.util.ArrayList;
import java.util.List;

public class Problem2 {
    public static Integer[] solution(Integer[][] flipCards){
        Integer[] answer = new Integer[]{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};

        for(int i=0; i < 10; i++){
            int start = flipCards[i][0] - 1;
            int end = flipCards[i][1] - 1;
            int middle = (start + end) / 2;
            int temp = 0;

            for(int s=start, e=end; s<=middle; s++, e--){
                temp = answer[s];
                answer[s] = answer[e];
                answer[e] = temp;
            }
        }
        return answer;
    }
}