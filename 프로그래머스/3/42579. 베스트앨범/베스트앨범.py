from collections import defaultdict

def solution(genres, plays):
    genre_total_play = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total_play[g] += p
        genre_songs[g].append((p, i))

    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    
    answer = []

    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in sorted_songs[:2]])
    
    return answer
