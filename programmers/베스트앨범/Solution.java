package º£½ºÆ®¾Ù¹ü;

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

		for(int  i = 0 ; i < genres.length ; i++){
			if(!genreMap.containsKey(genres[i])){
				genreMap.put(genres[i], plays[i]);
			}
			else{
				genreMap.put(genres[i], genreMap.get(genres[i]).intValue() + plays[i]);
			}
			songs.add(new Song(i, genres[i], plays[i]));
			System.out.println(i);
			System.out.println(genres[i]);
			System.out.println(plays[i]);
		}
		answer = new int[genreMap.keySet().size()*2];

		List<Map.Entry<String, Integer>> entries = new LinkedList<>(genreMap.entrySet());
		Collections.sort(entries, (o1, o2) -> o1.getValue().compareTo(o2.getValue()));
		Collections.sort(songs, (o1, o2) -> ((Integer)o1.play).compareTo(o2.play));

		int count = 0;
		for(Map.Entry<String, Integer> entry : entries ){
			for(Song song : songs){
				if(song.genre == entry.getKey()){
					answer[count] = song.id;
					count++;
				}
				if(count % 2 == 1){
					break;
				}
			}
		}
        return answer;
	}
	
	static void main(String[] agrs){
		Solution solution = new Solution();
		String[] genres = {"classic", "pop", "classic", "classic", "pop"};
		int[] plays = {500, 600, 150, 800, 2500};
		solution.solution(genres, plays);
	}
}