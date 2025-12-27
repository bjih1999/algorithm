/**
 * 
 * 모든 경우의 수를 넣게 되면 O(n * n * logn) 이니까,
 * k만큼만 넣는 방법
 * 각 원소들을 분자로 했을 때 가장 작은 수들만 힙에 넣어두고 그 수들이 poll 될 때마다 그 다음 큰 수를 넣어줌.
 * 위 행위를 k번 수행함
 * 
 *  O((n+k) log (n+k))
 */

import java.util.*;

class Node {
    double value;
    int a;
    int b;

    public Node(int[] arr, int a, int b) {
        this.value = (double) arr[a]/arr[b];
        this.a = a;
        this.b = b;
    }
}

class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        
        PriorityQueue<Node> queue = new PriorityQueue<Node>((o1, o2) -> Double.compare(o1.value, o2.value));
        for (int i = 0 ; i < arr.length ; i++) {
            queue.offer(new Node(arr, i, arr.length-1));
        }

        for (int i = 0 ; i < k-1 ; i++) {

            Node node = queue.poll();

            if (node.a < node.b) {
                queue.offer(new Node(arr, node.a, node.b-1));
            }
        }


        Node current = queue.poll();
        return new int[]{arr[current.a], arr[current.b]};
    }
}