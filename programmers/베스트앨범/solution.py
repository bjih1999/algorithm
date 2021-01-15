'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

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