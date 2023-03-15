package onboard;

import java.util.ArrayList;
import java.util.List;

public class Problem1 {
    public static List<Integer> solution(Integer hour, Integer minute){
        List<Integer> answer = new ArrayList<>();

        if(minute < 45) {
            hour--;
            minute = 15 + minute;

            if (hour < 0) {
                hour = 23;
            }

            answer = List.of(hour, minute);
        }

        else {
            answer = List.of(hour, minute - 45);
        }
        return answer;
    }
}
