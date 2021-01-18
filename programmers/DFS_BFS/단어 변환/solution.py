'''
�� ���� �ܾ� begin, target�� �ܾ��� ���� words�� �ֽ��ϴ�. �Ʒ��� ���� ��Ģ�� �̿��Ͽ� begin���� target���� ��ȯ�ϴ� ���� ª�� ��ȯ ������ ã������ �մϴ�.

1. �� ���� �� ���� ���ĺ��� �ٲ� �� �ֽ��ϴ�.
2. words�� �ִ� �ܾ�θ� ��ȯ�� �� �ֽ��ϴ�.
���� ��� begin�� hit, target�� cog, words�� [hot,dot,dog,lot,log,cog]��� hit -> hot -> dot -> dog -> cog�� ���� 4�ܰ踦 ���� ��ȯ�� �� �ֽ��ϴ�.

�� ���� �ܾ� begin, target�� �ܾ��� ���� words�� �Ű������� �־��� ��, �ּ� �� �ܰ��� ������ ���� begin�� target���� ��ȯ�� �� �ִ��� return �ϵ��� solution �Լ��� �ۼ����ּ���.

���ѻ���
�� �ܾ�� ���ĺ� �ҹ��ڷθ� �̷���� �ֽ��ϴ�.
�� �ܾ��� ���̴� 3 �̻� 10 �����̸� ��� �ܾ��� ���̴� �����ϴ�.
words���� 3�� �̻� 50�� ������ �ܾ ������ �ߺ��Ǵ� �ܾ�� �����ϴ�.
begin�� target�� ���� �ʽ��ϴ�.
��ȯ�� �� ���� ��쿡�� 0�� return �մϴ�.

����� ��
begin	target	words	return
hit	cog	[hot, dot, dog, lot, log, cog]	4
hit	cog	[hot, dot, dog, lot, log]	0

https://programmers.co.kr/learn/courses/30/lessons/43163
'''

from queue import Queue
import copy

def _word_compare(src_word, dest_word):
    diff_count = 0
    for i in range(len(src_word)):
        if src_word[i] != dest_word[i]:
            diff_count += 1
        
        if diff_count > 1:
            return False
    
    return True

def _search(begin, target, words):
    queue = Queue()
    depth = 0
    used = set()

    if target not in words:
        return 0

    queue.put((begin, 0))
    while(queue.qsize() > 0):
        cur_node = queue.get()
        src_word = cur_node[0]
        depth = cur_node[1]
        if _word_compare(src_word, target):
            return depth + 1


        for word in words:
            if _word_compare(src_word, word) and (word not in used):
                queue.put((word, depth + 1))
                used.add(word)
    return 0

def solution(begin, target, words):
    answer = _search(begin, target, words)
    return answer
