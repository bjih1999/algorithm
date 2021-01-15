/**
 * 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
 *
 * 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
 * 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
 * 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
 * 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
 *
 * https://programmers.co.kr/learn/courses/30/lessons/42579
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class Song{
    int id;
    String genre;
    int play;

    public Song(int id, String genre, int play){
        this.id = id;
        this.genre = genre;
        this.play = play;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        LinkedHashMap<String, Integer> genreMap = new LinkedHashMap<>();
        List<Song> songs = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            if (!genreMap.containsKey(genres[i])) {
                genreMap.put(genres[i], plays[i]);
            } else {
                genreMap.put(genres[i], genreMap.get(genres[i]).intValue() + plays[i]);
            }
            songs.add(new Song(i, genres[i], plays[i]));
//            System.out.println(i);
//            System.out.println(genres[i]);
//            System.out.println(plays[i]);
        }
        answer = new int[genreMap.keySet().size() * 2];

        List<Map.Entry<String, Integer>> entries = new LinkedList<>(genreMap.entrySet());
        Collections.sort(entries, (o1, o2) -> o1.getValue().compareTo(o2.getValue()));
        Collections.sort(songs, (o1, o2) -> ((Integer) o1.play).compareTo(o2.play));

        int count = 0;
        for (Map.Entry<String, Integer> entry : entries) {
            for (Song song : songs) {
                if (song.genre == entry.getKey()) {
                    answer[count] = song.id;
                    count++;
                }
                if (count % 2 == 1) {
                    break;
                }
            }
        }
        return answer;
    }
}