/**
 * arr가 정렬된 int 배열 일때,
 * arr[i] / arr[j] (i < j) 중 K번째로 큰 수를 만들어내는 i, j를 찾는 문제
 * 1 < arr.length < 1000 이기 때문에,
 * 모든 경우의 수를 heap에다가 넣고 k번 fetching함
 * 
 * O(n * n * log n)
 * 
 */

import java.util.*;

class Node {
    double value;
    int a;
    int b;

    public Node(int a, int b) {
        this.value = (double) a/b;
        this.a = a;
        this.b = b;
    }
}

class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int left = 0;

        PriorityQueue<Node> queue = new PriorityQueue<Node>((o1, o2) -> Double.compare(o1.value, o2.value));
        for (int i = 0 ; i < arr.length ; i++) {
            for (int j = i+1 ; j < arr.length ; j++) {
                queue.offer(new Node(arr[i], arr[j]));
            }
        }
        for (int i = 0 ; i < k-1 ; i++) {
            queue.poll();
        }
        Node current = queue.poll();
        return new int[]{current.a, current.b};
    }
}