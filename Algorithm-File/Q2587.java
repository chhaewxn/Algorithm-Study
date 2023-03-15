package onboard;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Problem3 {
    public static List<Integer> solution(List<Integer> numbers){
        List<Integer> answer = new ArrayList<>();
        int sum = 0;

        Collections.sort(numbers);

        for(int i=0; i<5; i++){
            sum += numbers.get(i);
        }
        int average = sum / 5;

        int mid;
        mid = numbers.get(numbers.size() / 2);

        answer.add(average);
        answer.add(mid);

        return answer;
    }
}
