import random


def f(words, type):
    k = 0
    a = len(words)
    left_w = []
    
    for i in range(len(words)):
        r1 = random.randint(0, len(words)-1)
        print(words[r1][type])
        w1 = input("Ваш ответ: ")
        print(words[r1][0])
        q1 = int(input('Совпало? Да(1) нет(0)'))
        if q1 == 1:
            k += 1
        else:
            left_w.append(words[r1])
        words.pop(r1)
    print(k, 'из', a,'%',round(k/a,2))
    print(*left_w)


words_1 = [['adventurous', 'Смелый, отважный'], ['ambitious', 'Амбициозный, целеустремлённый'], [
    'assertive', 'настойчивый'], ['bossy', 'властный'], ['cautious', 'осторожный'], ['creative', 'творческий'], [' easy-going', 'Лёгкий на подъём'], [
    'energetic', 'энергичный'], ['enthusiastic', 'восторженный, увлеченный'], ['even-tempered', 'сдеражанный'], ['generous', 'щедрый'], [' hard-working', 'трудолюбивый'], [' level-headed', 'уравновешенный'], [
    'likeable', 'приятный'], ['moody', 'угрюмый, грустный'], ['open-minded', 'Восприимчивый, открыт ко всему новому'],[
    'organized', 'организованный'], ['quiet', 'quiet'], ['reliable', 'надежный'], ['reserved', 'сдержанный'], ['self-confident', 'самоуверенный'], ['sensible', 'здравомыслящий,разумный'], [
    'sensitive', 'чувствительный'], ['serious', 'серьезный'], ['shy', 'застенчивый'], ['sociable', 'общительный'],[' strong-willed', 'сильный духом'], ['talkative', 'разговорчивый'], ['thoughtful','задумчивый'], ['warm-hearted','добросердечный(Добрый, отзывчивый)'], [
    'bilingual','двуязычный'],['ex-tycoon','бывший магнат'] ,['misbehave','плохо себя вести'] ,['misuse','злоупотребление'] ,['outperform','превосходить'] ,['outrun','опережать'] ,['overconfident','слишком самоуверенный'] ,[
    'overshadowed','омраченный']  ,['redefine','переопределить']  ,[' redo','переделывать']  ,['semicircle','полукруг']  ,['underrated','недооцененный'],['underuse','недоиспользование']]
a = int(input('Выбери тип -'))

print(f(words_1, a,))
