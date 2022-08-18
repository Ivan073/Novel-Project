# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character('???', color="#c8ffc8")
define non = Character('?????', color="#c8ffc8")
define gg = Character('YOU')
define cat = Character("[nc]")
define sys = Character('System')
define sphinx = Character('Великий Сфинкс')
define min = Character('Минос, Король Лабиринта')

init python:
    character_option = 0
    in_fight = False           #эта переменная используется в screens.rpy для изменения стиля менб=ю выбора
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


transform middle_left:
    xalign 0.0
    yalign 0.5

transform middle_right:
    xalign 1.0
    yalign 0.5

transform left_door:
    xalign 0.05
    yalign 0.05

transform center_door:
    xalign 0.5
    yalign 0

transform right_door:
    xalign 0.75
    yalign 0.25

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
    stop music
    play music "audio/maze.mp3" fadeout 1

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
    #нужны символы, бои, ловушки, сундуки, реплики
    label room1:
    #отображение подсказок
    scene frozen_maze
    show catcharpicture at left
    show runa at left_door
    menu:
            "Куда идем?"
            "Налево":
                "Шаги отдаются эхом от стен ледяной пещеры"
                #бой
                hide catcharpicture
                scene frozen_cave
                $show_character([middle_left()])
                show slime at middle_right
                "Вы встретили слизня. Он ничего не делает"
                $in_fight = True
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы победили слизня"
                        "Защититься":
                            "Слизень вас игнорирует"
                            jump .fight_start
                        "Увернуться":
                            "Слизень вас игнорирует"
                            jump .fight_start

                hide slime
                $hide_character()
                $in_fight = False
                scene frozen_maze
                show catcharpicture at left
                jump room2

            "Вперед":
                "С каждым сделанным шагом становится теплее. Что же так нагревает воздух?"
                scene fire
                "За дверью разверзлось адское пламя, поглощающее все вокруг"
                if character_option == 5:
                    $show_character([truecenter()])
                    gg "Огонь не причинит мне вреда, это моя стихия. Возвращаемся обратно."
                    jump room1
                jump death

            "Направо":
                "*Идет направо*"
                #бой
                hide catcharpicture
                scene dirt_cave:
                    zoom 2.5
                $show_character([middle_left()])
                show slime2 at middle_right
                "Вы встретили слизня. Он ничего не делает"
                $in_fight = True
                label .fight2_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы победили слизня"
                        "Защититься":
                            "Слизень вас игнорирует"
                            jump .fight2_start
                        "Увернуться":
                            "Слизень вас игнорирует"
                            jump .fight2_start

                hide slime2
                $hide_character()
                $in_fight = False
                scene frozen_maze
                show catcharpicture at left
                jump room6

    label room2:
    #отображение подсказок
    scene frozen_maze
    show catcharpicture at left
    show runa at right_door
    menu:
            "Куда идем?"
            "Налево":
                "С потолка на вас капает вода, но вы продолжаете идти"
                scene water_cave:
                    zoom 2.5
                "Вы оказались в подводной пещере. Дверь за вами сразу закрылась"
                if character_option == 2:
                    $show_character([truecenter()])
                    gg "Воду получится отодвинуть, но нужно поторапливаться и возвращаться. "
                    jump room2
                jump death

            "Вперед":
                "Чем дальше вы продвигаетесь по пещере, тем отчетливее виднеются чьи-то тени."
                #бой
                hide catcharpicture
                $show_character([middle_left()])
                show goblin at middle_right:
                    zoom 1.3
                "Вы встретили гоблина. Он быстро к вам приближается"
                $in_fight = True
                $wounded = False
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Гоблин был быстрее и ранил вас"
                            if wounded:
                                "Гоблин нанес смертельное ранение"
                                jump death
                            $wounded = True
                            jump .fight_start
                        "Защититься":
                            "Атака была не сильной и вы смогли ее блокировать, оглушив гоблина"
                            jump .goblin_staggered
                        "Увернуться":
                            "Гоблин оказался проворным и смог ранить вас"
                            if wounded:
                                "Гоблин нанес смертельное ранение"
                                jump death
                            $wounded = True
                            jump .fight_start

                label .goblin_staggered:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы успели добить гоблина"
                        "Защититься":
                            "Гоблин оправился от удара"
                            jump .fight_start
                        "Увернуться":
                            "Гоблин оправился от удара"
                            jump .fight_start

                hide goblin
                $hide_character()
                $in_fight = False
                show catcharpicture at left
                jump room8

            "Направо":
                "На полу местами лежит песок, что хрустит под ногами с каждым шагом"
                #сделать загадку
                scene sphinks
                show catcharpicture at left
                sphinx "Что за жалкие смертные пожаловали в мою обитель?"
                cat "Мы случайно дверью ошиблись! Сейчас уже уходим.."
                sphinx "Теперь вам дороги назад нет, сперва отгадайте загадку."
                sphinx "Кто не дышит, но живет; хоть не нужно - много пьет; и в жизни, и в смерти тело как лед."
                #ответ: рыба
                python:
                    answer = renpy.input("Каков ответ?")
                    answer = answer.lower()
                if answer == "рыба":
                    sphinx "Верно"
                    jump room3
                else:
                    sphinx "Неверно"
                    jump death

    label room3:
    #отображение подсказок
    scene frozen_maze
    show catcharpicture at left
    show runa at center_door
    menu:
            "Куда идем?"
            "Налево":
                "Эта дверь сразу кажется подозрительной, но вы все равно открываете ее"
                scene snakes
                "В ваших глазах темнеет после множественных змеиных укусов."
                jump death

            "Вперед":
                "За дверью виден блеск монет."
                scene gold:
                    zoom 2.4
                    xalign 0.5
                gg "Сокровище!"
                #здесь получить сокровище
                scene frozen_maze
                jump room4

            "Направо":
                "Из-за двери веет свежим ветром. Может, это выход?"
                scene clouds
                if character_option == 3:
                    $show_character([truecenter()])
                    gg "Поток воздуха из копья надолго нас не удержит. Клара, нам стоит быстрее вернуться."
                    jump room3
                "Полет был красивым, как у птицы, но недолгим: слишком скоро случилось столкновение с землей."
                jump death

    label room4:
    #отображение подсказок
    scene frozen_maze
    show catcharpicture at left
    show runa at right_door
    menu:
            "Куда идем?"
            "Налево":
                "Кажется, за дверью слышится карканье воронов."
                scene put_stone
                show catcharpicture at left
                cat "Как думаешь, в какую сторону нам повернуть?"
                menu:
                    "Налево":
                        jump death
                    "Направо":
                        jump room13
                #сделать загадку

            "Вперед":
                "За дверью оказывается лесная поляна. Неужели это выход?"
                scene pit
                "Вы угодили в волчью яму."
                jump death

            "Направо":
                "*Идет направо*"
                #бой

                hide catcharpicture
                $show_character([middle_left()])
                show hakutaku at middle_right:
                    zoom 1.3
                "Вы встретили огненного монстра. Он вас еще не заметил"
                $in_fight = True
                $monster_health = 3
                $your_health = 4
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            jump .paw_attack
                        "Защититься":
                            "Монстр заметил вас"
                            jump .paw_attack
                        "Увернуться":
                            "Монстр заметил вас"
                            jump .paw_attack

                label .paw_attack:
                    "Монстр замахивается своей лапой"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            if character_option == 1:
                                "Атака топором остановила лапу и ранила чудовище"
                                $monster_health -= 1
                                if monster_health <=0:
                                    jump .end_fight
                                jump .fire_attack
                            "Атака ранила вас"
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .fire_attack
                        "Защититься":
                            "Атака нанесла небольшой урон"
                            $your_health -=1
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .monster_prepares_fire
                        "Увернуться":
                            "Вы успешно увернулись"
                            jump .monster_prepares_fire

                label .monster_prepares_fire:
                    "Монстр готовится к следущей атаке"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            if monster_health <=0:
                                jump .end_fight    
                            jump .fire_attack
                        "Защититься":
                            jump .fire_attack
                        "Увернуться":
                            jump .fire_attack

                label .fire_attack:
                    "Монстр пускает в вас волну огня"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            if character_option == 3:
                                "Атака ветром рассеяла огонь и нанесла урон"
                                $monster_health -= 1
                                if monster_health <=0:
                                    jump .end_fight
                                jump .paw_attack
                            "Атака ранила вас"
                            if character_option == 5:
                                "Огонь не сильно вам вредит"
                                $your_health -=1
                                if your_health <=0:
                                    "Эта атака добила вас"
                                    jump death
                                jump .monster_prepares_paw
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .paw_attack
                        "Защититься":
                            "Атака нанесла небольшой урон"
                            $your_health -=1
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .monster_prepares_paw
                        "Увернуться":
                            "Вы не смогли увернуться от волны огня"
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .paw_attack

                label .monster_prepares_paw:
                    "Монстр готовится к следущей атаке"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            if monster_health <=0:
                                jump .end_fight
                            jump .paw_attack
                        "Защититься":
                            jump .fire_attack
                        "Увернуться":
                            jump .fire_attack

                label .end_fight:
                "Вы победили"
                hide hakutaku
                $hide_character()
                $in_fight = False
                show catcharpicture at left

                jump room5

    label room5:
    #отображение подсказок
    show runa at left_door
    menu:
            "Кажется выход близко"
            "Налево":
                "Шагая, вы слышите чье-то тяжелое дыхание"
                #сделать загадку
                show minotaur at truecenter
                min "Так значит, у вас получилось преодолеть большую часть моего лабиринта."
                min "Так просто вы не уйдете. Сначала отгадайте загадку."
                min "Мертвых оживляет. Нас смешит, а порой - печалит. Рождается вмиг. Гибнет, когда ты - старик."
                #ответ: память
                python:
                    answer = renpy.input("Каков ответ?")
                    answer = answer.lower()
                if answer == "память":
                    min "Верно"
                    jump lab_exit
                else:
                    min "Неверно"
                    jump death
                

            "Вперед":
                "За дверью слышится звон монет."
                scene gold:
                    zoom 2.4
                    xalign 0.5
                gg "Сокровище!"
                scene frozen_cave
                show mimic at truecenter:
                    zoom 4.0
                gg "Это еще что за существо?!"
                jump death

            "Направо":
                "Вы слышите тихое поскрипывание, раздающееся словно от старого дерева."
                scene roots
                if character_option == 1:
                    $show_character([truecenter()])
                    gg "Топором можно разрубать корни, но долго мне не продержаться. Нужно убираться отсюда."
                    jump room5
                "Корни оплетают вас и вы задыхаетесь."
                jump death

    label room6:
    #отображение подсказок
    show runa at center_door
    menu:
            "Кажется свернули не туда"
            "Налево":
                "*Идет налево*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Вперед":
                "*Идет вперед*"
                #сделать загадку
                jump room7

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти-ловушка*"
                jump death

    label room7:
    #отображение подсказок
    show runa at center_door
    show runa at right_door
    show runa at left_door
    menu:
            "Подозрительная комната"
            "Налево":
                "*Идет налево*"
                #бой
                hide catcharpicture
                $show_character([middle_left()])
                show hakutaku at middle_right:
                    zoom 2.5
                "Вы встретили огромное чудовище. Кажется оно недовольно"
                $in_fight = True
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Ваша атака не нанесла никакого урона. Вас раздавили лапой насмерть"
                            jump death
                        "Защититься":
                            "Монстр разбил вашу защиту одним ударом и добил вас вторым"
                            jump death
                        "Бежать":
                            "Только вы обернулись чтобы убежать, как стены лабиринта растаяли. Вместе с вами"
                            jump death

                hide hakutaku
                $hide_character()
                $in_fight = False
                show catcharpicture at left
                jump death

            "Вперед":
                "*Идет вперед*"
                "*Какая-нибудь причина смерти-ловушка*"
                jump death

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label room8:
    #отображение подсказок
    show runa at right_door
    show runa at left_door                  #отображается только одна руна
    menu:
            "Кажется свернули не туда"
            "Налево":
                "*Идет налево*"
                gg "Сокровище!"
                scene gold:
                    zoom 2.4
                    xalign 0.5
                gg "Сокровище!"
                scene frozen_cave
                show mimic at truecenter:
                    zoom 4.0
                gg "Не сокровище..."
                jump death

            "Вперед":
                "*Идет вперед*"
                #сделать загадку
                jump room9

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label room9:
    #отображение подсказок
    show runa at center_door
    menu:
            "Куда идем?"
            "Налево":
                "*Идет налево*"
                #бой

                hide catcharpicture
                $show_character([middle_left()])
                show hakutaku at middle_right:
                    zoom 1.3
                "Вы встретили огненного монстра. Он вас еще не заметил"
                $in_fight = True
                $monster_health = 3
                $your_health = 4
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            jump .paw_attack
                        "Защититься":
                            "Монстр заметил вас"
                            jump .paw_attack
                        "Увернуться":
                            "Монстр заметил вас"
                            jump .paw_attack

                label .paw_attack:
                    "Монстр замахивается своей лапой"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            if character_option == 1:
                                "Атака топором остановила лапу и ранила чудовище"
                                $monster_health -= 1
                                if monster_health <=0:
                                    jump .end_fight
                                jump .fire_attack
                            "Атака ранила вас"
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .fire_attack
                        "Защититься":
                            "Атака нанесла небольшой урон"
                            $your_health -=1
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .monster_prepares_fire
                        "Увернуться":
                            "Вы успешно увернулись"
                            jump .monster_prepares_fire

                label .monster_prepares_fire:
                    "Монстр готовится к следущей атаке"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            if monster_health <=0:
                                jump .end_fight    
                            jump .fire_attack
                        "Защититься":
                            jump .fire_attack
                        "Увернуться":
                            jump .fire_attack

                label .fire_attack:
                    "Монстр пускает в вас волну огня"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            if character_option == 3:
                                "Атака ветром рассеяла огонь и нанесла урон"
                                $monster_health -= 1
                                if monster_health <=0:
                                    jump .end_fight
                                jump .paw_attack
                            "Атака ранила вас"
                            if character_option == 5:
                                "Огонь не сильно вам вредит"
                                $your_health -=1
                                if your_health <=0:
                                    "Эта атака добила вас"
                                    jump death
                                jump .monster_prepares_paw
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .paw_attack
                        "Защититься":
                            "Атака нанесла небольшой урон"
                            $your_health -=1
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .monster_prepares_paw
                        "Увернуться":
                            "Вы не смогли увернуться от волны огня"
                            $your_health -=2
                            if your_health <=0:
                                "Эта атака добила вас"
                                jump death
                            jump .paw_attack

                label .monster_prepares_paw:
                    "Монстр готовится к следущей атаке"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы атаковали монстра"
                            if character_option == 2:
                                "Ваша водная атака нанесла значительный урон"
                                $monster_health -= 2
                            else:
                                $monster_health -= 1
                            if monster_health <=0:
                                jump .end_fight
                            jump .paw_attack
                        "Защититься":
                            jump .fire_attack
                        "Увернуться":
                            jump .fire_attack

                label .end_fight:
                "Вы победили"
                hide hakutaku
                $hide_character()
                $in_fight = False
                show catcharpicture at left

                jump room10

            "Вперед":
                "*Идет вперед*"
                #сделать бой
                jump room11

            "Направо":
                "*Идет направо*"
                #сделать бой
                jump room12

    label room10:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "*Идет налево*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Вперед":
                "*Идет вперед*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label room11:
    #отображение подсказок
    show runa at center_door
    menu:
            "Кажется выход близко"
            "Налево":
                "*Идет налево*"
                #сделать загадку
                "*Какая-нибудь причина смерти-загадка*"
                jump death

            "Вперед":
                "*Идет вперед*"
                #сделать загадку
                jump lab_exit

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label room12:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "*Идет налево*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Вперед":
                "*Идет вперед*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label room13:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "*Идет налево*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Вперед":
                "*Идет вперед*"
                "*Какая-нибудь причина смерти*"
                jump death

            "Направо":
                "*Идет направо*"
                "*Какая-нибудь причина смерти*"
                jump death

    label lab_exit:
    "*Вышли из лабиринта*"

    #конец лабиринта

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


    label death:
    scene death_screen
    "*Вы погибли*"
    return
