# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character('???', color="#c8ffc8")
define non = Character('?????', color="#c8ffc8")
define gg = Character('YOU')
define cat = Character('Клара')
define sys = Character('System')

init python:
    character_option = 0
    def show_character():                   #функция просто размещает персонажа на экране,
        if character_option == 1:           #для более детального размещения необходимо добавить параметры функиции
            renpy.show("character1")      #и потом передать в renpy show
        if character_option == 2:           #надо переделать когда определимся с размещением персонажа на экране
            renpy.show("character2")
        if character_option == 3:
            renpy.show("character3")
        if character_option == 4:
            renpy.show("character4")
        if character_option == 5:
            renpy.show("character5")

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
        show character1
        "*Описание персонажа1 или какая-нибудь фраза или что-нибудь по сюжету*"
        show character1
        menu:
            "Подтвердить":
                $character_option = 1
                jump character_selected

            "Выбрать другого":
                hide character1
                jump character_choise


    label get_character2:
        show character2
        "*Описание персонажа2 или какая-нибудь фраза или что-нибудь по сюжету*"
        hide character2
        menu:
            "Подтвердить":
                $character_option = 2
                jump character_selected

            "Выбрать другого":
                hide character2
                jump character_choise


    label get_character3:
        show character3
        "*Описание персонажа3 или какая-нибудь фраза или что-нибудь по сюжету*"
        hide character3
        menu:
            "Подтвердить":
                $character_option = 3
                jump character_selected

            "Выбрать другого":
                hide character3
                jump character_choise


    label get_character4:
        show character4
        "*Описание персонажа4 или какая-нибудь фраза или что-нибудь по сюжету*"
        hide character4
        menu:
            "Подтвердить":
                $character_option = 4
                jump character_selected

            "Выбрать другого":
                jump character_choise


    label get_character5:
        show character5
        "*Описание персонажа5 или какая-нибудь фраза или что-нибудь по сюжету*"
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
    sys "Введите ваше имя"

    $show_character()
    gg "*Образец работы с персонажем*"
    $hide_character()
    "*Персонаж убран*"



    return
