package onboard;

import java.util.Arrays;

public class Problem5 {
    public static Integer solution(Integer N, Integer K, Integer[] values){
        Integer answer = 0;

        Integer[] coin = new Integer[K+1];
        Arrays.fill(coin, 100001);
        coin[0] = 0;

        for(int i=1; i<=K; i++) {
            for(int j=0; j<N; j++) {
                if(i - values[j] >= 0) {
                    coin[i] = Math.min(coin[i], coin[i-values[j]]+1);
                }
            }
        }

        answer = coin[K] == 100001 ? -1 : coin[K];
        return answer;
    }
}
