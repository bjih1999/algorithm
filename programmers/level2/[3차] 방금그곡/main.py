import datetime

def solution(m, musicinfos):
    answer = ''

    m = replaceShop(m)
    musics = []
    for musicinfo in musicinfos:
        splitted = musicinfo.split(',')
        start = datetime.datetime.strptime(splitted[0],'%H:%M')
        end = datetime.datetime.strptime(splitted[1],'%H:%M')
        duration = end - start
        minute = duration.seconds
        hour = minute // 60
        replaced = replaceShop(splitted[3])
        title = splitted[2]

        melody_count = len(replaced)

        div = hour // melody_count
        mod = hour % melody_count

        musics.append([title, replaced * div + replaced[:mod]])

    sorted_musics = sorted(musics, key = lambda x: -len(x[1]))
    print(sorted_musics)

    for title, melody in sorted_musics:
        if m in melody:
            return title
    return "(None)"

def replaceShop(m):
    replaced = m.replace('C#', '3')
    replaced = replaced.replace('D#', '4')
    replaced = replaced.replace('F#', '6')
    replaced = replaced.replace('G#', '7')
    replaced = replaced.replace('A#', '8')

    return replaced
    

    

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "12:00,12:14,TEST,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))