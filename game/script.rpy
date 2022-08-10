# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character('???', color="#c8ffc8")
define non = Character('?????', color="#c8ffc8")
define gg = Character('YOU')
define cat = Character('Клара')
define sys = Character('System')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    play sound 'audio/wagon_creak.mp3' fadeout 1

    nn "Очередной эксперимент не удался, только материалы пошли насмарку…"

    non "Интересно, сколько еще он будет пробовать?"

    nn "Не болтай лишнего! Лучше сбрасывай!"

    stop sound fadeout 1
    play sound 'audio/hum_falling.mp3'
    play music "audio/dunF.mp3" fadeout 1

    scene dungeon

    show catcharpicture

    #stop music fadeout1

    cat "Ого! А ты еще кто? И как здесь оказался?"

    cat "Что-то тут темно... Дай-ка рассмотреть себя получше."

    scene dungeon

    show 33:
        xalign 0.5
        yalign 0.5
    sys "Выберите свою внешность"


    return
