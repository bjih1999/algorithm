'''
��Ʈ���� ����Ʈ���� �帣 ���� ���� ���� ����� �뷡�� �� ���� ��� ����Ʈ �ٹ��� ����Ϸ� �մϴ�. �뷡�� ���� ��ȣ�� �����ϸ�, �뷡�� �����ϴ� ������ ������ �����ϴ�.

���� �뷡�� ���� ����� �帣�� ���� �����մϴ�.
�帣 ������ ���� ����� �뷡�� ���� �����մϴ�.
�帣 ������ ��� Ƚ���� ���� �뷡 �߿����� ���� ��ȣ�� ���� �뷡�� ���� �����մϴ�.
�뷡�� �帣�� ��Ÿ���� ���ڿ� �迭 genres�� �뷡�� ��� Ƚ���� ��Ÿ���� ���� �迭 plays�� �־��� ��, ����Ʈ �ٹ��� �� �뷡�� ���� ��ȣ�� ������� return �ϵ��� solution �Լ��� �ϼ��ϼ���.

https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
'''
def solution(genres, plays):
    answer = []
    genre_dic = {}
    genre_play = []
	
    for index, genre in enumerate(genres) :
        if genre not in genre_dic:
            genre_dic[genre] = plays[index]
        else:
            genre_dic[genre] += plays[index]

        genre_play.append((index, genre, plays[index]))

    sorted_genre = list(reversed(sorted(genre_dic.items(), key = lambda x : x[1])))
    sorted_song = list(reversed(sorted(genre_play, key = lambda x : (x[2], -x[0]))))

    for genre in sorted_genre:
        count = 0
        for song in sorted_song:
            if genre[0] == song[1]:
                count += 1
                answer.append(song[0])
            if count > 1:
                break
    return answer