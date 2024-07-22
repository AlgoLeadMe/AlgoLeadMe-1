import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import static java.lang.System.out;

public class 다이어트 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long g = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<Integer>();
        int head = 2;
        int tail = 1;

        while (head >= tail && head < 987654321) {
            // 제곱 빼기 제곱 계산 결과
            int x = (head + tail) * (head - tail);

            // g 보다 크다면 tail 을 증가시킴
            if (x > g) {
                tail++;
                continue;
            }

            // g 보다 작다면 head 를 증가시킴
            if (x < g) {
                head++;
                continue;
            }

            // g 랑 같으면 리스트에 집어넣음
            list.add(head);
            tail++;
            head++;
        }

        // 없으면 -1 출력
        if (list.isEmpty()) {
            out.println(-1);
            return;
        }

        // 있으면 순서대로 출력
        list.forEach(out::println);
    }
}