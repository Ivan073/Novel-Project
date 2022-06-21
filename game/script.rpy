# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character('???', color="#c8ffc8")
define non = Character('?????', color="#c8ffc8")
define gg = Character('YOU')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    nn "Очередной эксперимент не удался, только материалы пошли насмарку…"

    non "Интересно, сколько еще он будет пробовать?"

    nn "Не болтай лишнего! Лучше сбрасывай!"

    play music "audio/dunF.mp3" fadeout 1

    scene dungeon

    show dar

    gg "Мое имя…  Где я?"

    #stop music fadeout1

    return
