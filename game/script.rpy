# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character('???', color="#c8ffc8")
define non = Character('?????', color="#c8ffc8")
define gg = Character('YOU')
define cat = Character("[nc]")
define sys = Character('System')

init python:
    character_option = 0
    def show_character(pos=[]):             #функция принимает массив трансформаций которые флияют на размещение персонажа
        if character_option == 1:           #трансформации это функции
            renpy.show("character1", pos)   #трансформации уже прописанные в renPy перечислены здесь https://www.renpy.org/doc/html/transforms.html
        if character_option == 2:           #если понадобится можно добавить свои кастомные функции-трансформации
            renpy.show("character2", pos)
        if character_option == 3:
            renpy.show("character3", pos)
        if character_option == 4:
            renpy.show("character4", pos)
        if character_option == 5:
            renpy.show("character5", pos)

    def hide_character():
        if character_option == 1:
            renpy.hide("character1")
        if character_option == 2:
            renpy.hide("character2")
        if character_option == 3:
            renpy.hide("character3")
        if character_option == 4:
            renpy.hide("character4")
        if character_option == 5:
            renpy.hide("character5")


# Игра начинается здесь:
label start:

    play sound 'audio/wagon_creak.mp3' fadeout 1

    nn "Очередной эксперимент не удался, только материалы пошли насмарку…"

    non "Интересно, сколько еще он будет пробовать?"

    nn "Не болтай лишнего! Лучше сбрасывай!"

    stop sound fadeout 1
    play sound 'audio/hum_falling.mp3'
    play music "audio/dunF.mp3" fadeout 1

    $nc = "Пушистое нечто"
    scene dungeon

    show catcharpicture

    #stop music fadeout1

    cat "Ого! А ты еще кто? И как здесь оказался?"

    cat "Что-то тут темно... Дай-ка рассмотреть себя получше."

    scene dungeon

    #show character1:
    #    xalign 0.5
    #    yalign 0.7
    sys "Выберите свою внешность"




    label character_choise:
    menu:
        "*вариант1*":
            jump get_character1

        "*вариант2*":
            jump get_character2

        "*вариант3*":
            jump get_character3

        "*вариант4*":
            jump get_character4

        "*вариант5*":
            jump get_character5


    label get_character1:
        show character1 at truecenter
        "*Воин, боевой топор которого рассечет любого врага, а задорная улыбка рассеет все сомнения*"
        hide character1
        menu:
            "Подтвердить":
                $character_option = 1
                jump character_selected

            "Выбрать другого":
                hide character1
                jump character_choise


    label get_character2:
        show character2 at truecenter
        "*Астролог призывает бушующие волны и создает отражение звездного неба, заключая врагов в теневые пузыри*"
        hide character2
        menu:
            "Подтвердить":
                $character_option = 2
                jump character_selected

            "Выбрать другого":
                hide character2
                jump character_choise


    label get_character3:
        show character3 at truecenter
        "*Владелец копья, выкованного для борьбы с чудовищами доисторических горных хребтов, что поможет ему обуздать воздушную стихию*"
        hide character3
        menu:
            "Подтвердить":
                $character_option = 3
                jump character_selected

            "Выбрать другого":
                hide character3
                jump character_choise


    label get_character4:
        show character4 at truecenter
        "*Некогда волшебник, практикующий тайную магию, который в погоне за источниками магической мощи отказался от своих учений в пользу тёмной магии*"
        hide character4
        menu:
            "Подтвердить":
                $character_option = 4
                jump character_selected

            "Выбрать другого":
                jump character_choise


    label get_character5:
        show character5 at truecenter
        "*Алая ведьма, мечтающая сжечь всех демонов мира. Языки пламени вегда ласково касаются ее рук, а широкие поля шляпы прячут взгляд*"
        hide character5
        menu:
            "Подтвердить":
                $character_option = 5
                jump character_selected

            "Выбрать другого":
                hide character5
                jump character_choise


    label character_selected:
    $hide_character()
    sys "*Выбор закончен*"
    show catcharpicture:
            xalign 0.5
            yalign 0.7

    cat "Как-то ты странно одет для этого подземелья.."
    cat "А как, говоришь, тебя зовут?"

    python:
        name = renpy.input("Как вас зовут?")
        name = name.strip() or "Пустота"


    cat "[name], значит? Хм, где-то я это слышала."
    $nc = "Клара"
    cat "Мое имя Клара, приятно познакомиться"
    cat "Так что привело тебя сюда?"

    hide catcharpicture
    show catcharpicture:
        xalign 0
        yalign 0.7

    menu:

        "Не знаю, я здесь совершенно случайно.":
            jump choice1_1

        "Меня сбросили сюда с телеги какие-то люди. Больше ничего не помню.":
            jump choice1_2

    label choice1_1:

        $ torch_flag = False

        cat "Правда? Ну ладно, будем выбираться."

        jump choice1_done

    label choice1_2:

        $ torch_flag = True

        cat "Люди? Я здесь видела только огра. И он как раз обронил вот тот факел, который может нам пригодиться."

        show ext_torch at truecenter

        cat "А теперь можем выбираться отсюда."
        hide ext_torch
        show ext_torch at topright
        jump choice1_done

    label choice1_done:

    # Сделать постепенное затемнение экрана (?)
    cat "С каждым шагом становится все темнее"

    scene dark

    if torch_flag == True:
        cat "Как раз пригодиться факел, который мы нашли! Зажжем?"
        menu:

            "Да.":
                jump choic

            "Нет.":
                jump cho

        label choic:
            $ on_flag = True
            scene frozen_cave
            show torch at topright
            show catcharpicture at left
            jump choi_done
        label cho:
            $ on_flag = False
            cat "Боишься увидеть что-то страшное? Ха!"
            jump choi_done


        label choi_done:
            cat "Я в любом случае хорошо вижу в темноте..."

      

    cat "Ого, да тут же ледяная пещера! А там вдалеке, кажется, свет."
    cat "Обычный ледяной пол сменился узорчатыми плитками..."
    scene frozen_maze
    if torch_flag == True:
        show ext_torch at topright
        if on_flag == True:
            hide ext_torch
            show torch at topright
    show catcharpicture at left
    cat "А чтобы выйти отсюда, придется постараться.."
    cat "Левая дверь кажется самой интересной. Может, сперва пойдем туда?"
    if torch_flag == True:
        if on_flag == True:
            gg "Может, стоит потушить факел?"
            cat "Не нужно, он может пригодиться в этом месте. Не факт, что во всех комнатах так светло."

    #Здесь мини-игра лабиринт

    $show_character()
    gg "*Образец работы с персонажем*"
    $show_character([right()])
    gg "*Справа*"
    $show_character([left()])
    gg "*Слева*"
    $show_character([topleft()])
    gg "*Слева сверху*"
    $hide_character()
    "*Персонаж убран*"



    return
