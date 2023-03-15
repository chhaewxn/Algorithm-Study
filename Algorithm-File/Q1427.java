package onboard;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Problem4 {
    public static Integer solution(Integer number){
        List<Integer> bits = new ArrayList<>();
        while(number > 0){
            bits.add(number % 10);
            number = number / 10;
        }
        Collections.sort(bits, Collections.reverseOrder());
        Integer answer = 0;
        for(Integer num : bits){
            answer = answer * 10 + num;
        }
        return answer;
    }
}
