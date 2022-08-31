# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nn = Character("[no1]", color="#c8ffc8")
define non = Character("[no2]", color="#c8ffc8")
define gg = Character('YOU')
define cat = Character("[nc]")
define sys = Character('System')
define sphinx = Character('Великий Сфинкс')
define min = Character('Минос, Король Лабиринта')
define mount = Character('Живая гора')
define mark = Character('Маркус')
define pet = Character('[petname]')

init python:
    torch_lit = False
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

    def show_torch():
        if torch_flag:
            if torch_lit:
                renpy.show("torch", [topright()])
            else:
                renpy.show("ext_torch", [topright()])

    def hide_torch():
        if torch_lit:
            renpy.hide("torch")
        else:
            renpy.hide("ext_torch")


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

    $no1 = "???"
    $no2 = "?????"
    $petname = "Фамильяр"

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
        $show_torch()
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
            scene frozen_cave
            $torch_lit = True
            $show_torch()
            show catcharpicture at left
            jump choi_done
        label cho:
            $show_torch()
            cat "Боишься увидеть что-то страшное? Ха!"
            jump choi_done


        label choi_done:
            cat "Я в любом случае хорошо вижу в темноте..."



    cat "Ого, да тут же ледяная пещера! А там вдалеке, кажется, свет."
    cat "Обычный ледяной пол сменился узорчатыми плитками..."
    scene frozen_maze
    stop music
    play music "audio/maze.mp3" fadeout 1

    $show_torch()
    show catcharpicture at left
    cat "А чтобы выйти отсюда, придется постараться.."
    cat "Левая дверь кажется самой интересной. Может, сперва пойдем туда?"
    if torch_flag == True:
        if torch_lit == True:
            gg "Может, стоит потушить факел?"
            cat "Не нужно, он может пригодиться в этом месте. Не факт, что во всех комнатах так светло."


    #Здесь мини-игра лабиринт
    #нужны символы, бои, ловушки, сундуки, реплики
    label room1:
    #отображение подсказок
    scene frozen_maze
    $show_torch()
    show catcharpicture at left
    show runa at left_door
    menu:
            "Куда идем?"
            "Налево":
                "Шаги отдаются эхом от стен ледяной пещеры"
                #бой
                $hide_torch()
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
                $show_torch()
                show catcharpicture at left
                jump room2

            "Вперед":
                "С каждым сделанным шагом становится теплее. Что же так нагревает воздух?"
                scene fire
                $show_torch()
                "За дверью разверзлось адское пламя, поглощающее все вокруг"
                if character_option == 5:
                    $show_character([truecenter()])
                    gg "Огонь не причинит мне вреда, это моя стихия. Возвращаемся обратно."
                    jump room1
                jump death

            "Направо":
                "*Идет направо*"
                #бой
                $hide_torch()
                hide catcharpicture
                scene dirt_cave:
                    zoom 2.5
                $show_torch()
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
                $show_torch()
                show catcharpicture at left
                jump room6

    label room2:
    #отображение подсказок
    scene frozen_maze
    $show_torch()
    show catcharpicture at left
    show runa at right_door
    menu:
            "Куда идем?"
            "Налево":
                "С потолка на вас капает вода, но вы продолжаете идти"
                scene water_cave:
                    zoom 2.5
                $show_torch()
                "Вы оказались в подводной пещере. Дверь за вами сразу закрылась"
                if character_option == 2:
                    $show_character([truecenter()])
                    gg "Воду получится отодвинуть, но нужно поторапливаться и возвращаться. "
                    jump room2
                jump death

            "Вперед":
                "Чем дальше вы продвигаетесь по пещере, тем отчетливее виднеются чьи-то тени."
                #бой
                $hide_torch()
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

                scene sphinks
                $show_torch()
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
                    sphinx "У вас вышло разгадать загадку и спасти свои жалкие жизни."
                    jump room3
                else:
                    sphinx "Не верно. Теперь вы будете погребены под песком."
                    jump death

    label room3:
    #отображение подсказок
    scene frozen_maze
    $show_torch()
    show catcharpicture at left
    show runa at center_door
    menu:
            "Куда идем?"
            "Налево":
                "Эта дверь сразу кажется подозрительной, но вы все равно открываете ее"
                scene snakes
                $show_torch()
                "В ваших глазах темнеет после множественных змеиных укусов."
                jump death

            "Вперед":
                "За дверью виден блеск монет."
                scene gold:
                    zoom 2.4
                    xalign 0.5
                $show_torch()
                gg "Сокровище!"
                "Хотя в сундуке было много золота, единственной полезной вещью оказался факел"
                if torch_flag:
                    "Но он у вас уже был"
                $torch_flag = True
                scene frozen_maze
                $show_torch()
                jump room4

            "Направо":
                "Из-за двери веет свежим ветром. Может, это выход?"
                scene clouds
                $show_torch()
                if character_option == 3:
                    $show_character([truecenter()])
                    gg "Поток воздуха из копья надолго нас не удержит. Клара, нам стоит быстрее вернуться."
                    jump room3
                "Полет был красивым, как у птицы, но недолгим: слишком скоро случилось столкновение с землей."
                jump death

    label room4:
    #отображение подсказок
    scene frozen_maze
    $show_torch()
    show catcharpicture at left
    show runa at right_door
    menu:
            "Куда идем?"
            "Налево":
                "Кажется, за дверью слышится карканье воронов."
                scene put_stone
                $show_torch()
                show catcharpicture at left
                cat "Как думаешь, в какую сторону нам повернуть?"
                menu:
                    "Налево":
                        jump death
                    "Направо":
                        jump room13


            "Вперед":
                "За дверью оказывается лесная поляна. Неужели это выход?"
                scene pit
                $show_torch()
                "Вы угодили в волчью яму."
                jump death

            "Направо":
                "*Идет направо*"
                #бой
                $hide_torch()
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
                                "Ваша атака водяным пузырем нанесла значительный урон"
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
                                "Ваша атака водным пузырем нанесла значительный урон"
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
                                "Огонь практически не вредит вам"
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
            "Кажется, выход близко"
            "Налево":
                "Шагая, вы слышите чье-то тяжелое дыхание"

                show minotaur at truecenter
                min "Так значит, у вас получилось преодолеть большую часть моего лабиринта."
                min "Так просто вы не уйдете. Сначала отгадайте загадку."
                min "Мертвых оживляет. Нас смешит, а порой - печалит. Рождается вмиг. Гибнет, когда ты - старик."
                #ответ: память
                python:
                    answer = renpy.input("Каков ответ?")
                    answer = answer.lower()
                if answer == "память":
                    min "У вас вышло отгадать мою загадку. Так и быть, вы свободны."
                    jump lab_exit
                else:
                    min "Как я и ожидал, вы не справились. Наградой за это будет смерть."
                    jump death


            "Вперед":
                "За дверью слышится звон монет."
                scene gold:
                    zoom 2.4
                    xalign 0.5
                $show_torch()
                gg "Сокровище!"
                scene frozen_cave
                $show_torch()
                show mimic at truecenter:
                    zoom 4.0
                gg "Это еще что за существо?!"
                jump death

            "Направо":
                "Вы слышите тихое поскрипывание, раздающееся словно от старого дерева."
                scene roots
                $show_torch()
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
            "Кажется, свернули не туда"
            "Налево":
                "Постепенно вы начинаете ступать по песку."
                scene zsand
                $show_torch()
                "Вы задохнулись в зыбучих песках."
                jump death

            "Вперед":
                "За дверью свистит ветер и слышен негромкий стук перекатывающихся камней."
                scene live_mountain
                $show_torch()
                mount "Ого! Путники! А разгадайте-ка мою загадку!"
                mount "Ввысь идет, но не растет. На деревья сверху взирает, но корни свои скрывает."
            #ответ: гора
                python:
                    answer = renpy.input("Давайте отвечайте!")
                    answer = answer.lower()
                if answer == "гора":
                    mount "Как вы так легко отгадали?? Ладно, проходите."
                    jump room7
                else:
                    mount "Ха-ха-ха-ха!!"
                    "Живая гора не сдерживает смеха, пораженная вашим ответом."
                    "Вас придавило камнем, упавшим с живой хохочущей горы."
                    jump death



            "Направо":
                "Вы чувствуете паутину, попадающую вам на лицо."
                scene spider
                $show_torch()
                "Вы умерли от укуса ядовитого паука."
                jump death

    label room7:
    #отображение подсказок
    show runa at center_door
    show runa at right_door
    show runa at left_door
    menu:
            "Эта комната кажется подозрительной."
            "Налево":
                "*Идет налево*"
                #бой
                $hide_torch()
                hide catcharpicture
                $show_character([middle_left()])
                show hakutaku at middle_right:
                    zoom 2.5
                "Вы встретили огромное чудовище. Оно выглядит недовольным."
                $in_fight = True
                label .fight_start:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Ваша атака не нанесла никакого урона. Последнее, что вы увидели перед смертью - огромная лапа, давящая на вашу голову."
                            jump death
                        "Защититься":
                            "Монстр разбил вашу защиту лапой, а его пасть сомкнулась на вашем горле."
                            jump death
                        "Бежать":
                            "Только вы обернулись чтобы убежать, как стены лабиринта растаяли вместе с вами"
                            jump death

                hide hakutaku
                $hide_character()
                $in_fight = False
                show catcharpicture at left
                jump death

            "Вперед":
                "*Идет вперед*"
                scene iron_lady
                $show_torch()
                "В этом месте вы видите две странные статуи. Неожиданно они оживают и заключают вас внутри себя."
                jump death

            "Направо":
                "Кажется, за дверью слышно пение птиц."
                scene Jungle
                $show_torch()
                "Вы заблудились в джунглях и умерли от жажды."
                jump death

    label room8:
    #отображение подсказок
    show runa at right_door
    show runa1 at left_door                  #отображается только одна руна/ исправлено, проверить, помогло ли!
    menu:
            "Кажется, свернули не туда"
            "Налево":
                "Шаги эхом раздаются по коридору."
                scene gold:
                    zoom 2.4
                    xalign 0.5
                $show_torch()
                gg "Мы нашли сокровище!"
                scene frozen_cave
                $show_torch()
                show mimic at truecenter:
                    zoom 4.0
                gg "Монстр?!"
                jump death

            "Вперед":
                "За дверью свистит ветер и слышен негромкий стук перекатывающихся камней."
                scene live_mountain
                $show_torch()
                mount "Ого! Путники! А разгадайте-ка мою загадку!"
                mount "Кто новым может быть и старым; кто может и расти и убывать; кто полон может быть, но не бывает пуст, кто виден лишь когда почти у всех глаза закрыты?"
            #ответ: луна
                python:
                    answer = renpy.input("Давайте отвечайте!")
                    answer = answer.lower()
                if answer == "луна":
                    mount "Как вы так легко отгадали?? Ладно, проходите."
                    scene frozen_maze
                    $show_torch()
                    jump room9
                else:
                    mount "Ха-ха-ха-ха!!"
                    "Живая гора не сдерживает смеха, пораженная вашим ответом."
                    "Вас придавило камнем, упавшим с живой хохочущей горы."
                    jump death


            "Направо":
                "За дверью слышится утробное бульканье."
                scene lava
                $show_torch()
                "Вы решили поплавать в лаве."
                jump death

    label room9:
    #отображение подсказок
    show runa at center_door
    menu:
            "Куда идем?"
            "Налево":
                "Вы стараетесь тихо прокрасться в нужную вам дверь."
                #бой
                $hide_torch()
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
                #бой
                $hide_torch()
                hide catcharpicture
                $show_character([middle_left()])
                show foxman at middle_right:
                    zoom 1.3
                "Кто-то похожий на лиса виднеется вдалеке."

                $in_fight = True
                $wounded = False

                label .fight_start2:
                    "В вас летит ледяной снаряд!"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            if character_option == 5:
                                "Огненная атака расплавила снаряд, но не достала противника"
                                "Вы смогли приблизится"
                                jump .closer
                            if character_option == 3:
                                "Ветер отразил снаряд, но не достал противника"
                                "Вы смогли приблизится"
                                jump .closer
                            "Снаряд попал в вас"
                            if wounded:
                                "Этот снаряд пробил вас насквозь"
                                jump death
                            $wounded = True
                            jump .fight_start2
                        "Защититься":
                            "Снаряд оказался очень мощным и ранил вас"
                            if wounded:
                                "Этот снаряд пробил вас насквозь"
                                jump death
                            $wounded = True
                            jump .fight_start2
                        "Увернуться":
                            "На большой дистанции увернуться было просто"
                            "У вас было достаточно времени чтобы сократить дистанцию"
                            jump .closer

                label .closer:
                    "Лис выпускает волну ледяных шипов вокруг себя"
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы разбиваете шипы и приближаетесь еще ближе"
                            jump .closest
                        "Защититься":
                            menu:
                                "Шипы не ранят вас но вы покрываетесь льдом"
                                "Разбивать лед":
                                    "Вы разбиваете лед, но лис уже готовит новую атаку"
                                    jump .closer
                                "Попытаться вырваться":
                                    "Вы делаете рывок изо льда в сторону лиса. Лед оказывается недостаточно прочным внутри и легко слетает с вас"
                                    jump .closest
                        "Увернуться":
                            "Вы успешно уворачиваетесь отступая назад"
                            jump .fight_start2

                label .closest:
                    "Лис достаточно близок для атаки, но теперь он сам готовится прыгнуть на вас"
                    "Выберите действие"
                    menu:
                        "Атаковать":
                            if character_option == 1:
                                "Ваш топор был достаточно быстр чтобы попасть по лису. Вы разрубили его напополам"
                                jump .end_fight2
                            "Атака лиса была очень быстрой и вы не смогли по нему попасть"
                            "Лис кусает вас в прыжке и заходит вам за спину"
                            if wounded:
                                "Это было смертельное ранение"
                                jump death
                            $wounded = True
                            jump .closest
                        "Защититься":
                            if wounded:
                                "Резкая атака окончательно вас ослабила и лис смог вас добить"
                                jump death
                            "Лис повалил вас на землю и серьезно ранил, но у вас появилась возможность нанести удар"
                            "Он оказался довольно уязвимым и вы смогли его убить"
                            jump .end_fight2
                        "Увернуться":
                            "Во время уворота вы толкаете лиса и он теряет равновесие, но все еще готовится к прыжку"
                            menu:
                                "Выберите действие"
                                "Атаковать":
                                    "Вы смогли попасть в лиса в его неуклюжей атаке и убить его "
                                    jump .end_fight2
                                "Защититься":
                                    "После еще одной неудачной атаки лис окончательно потерял равновесие и открылся для удара"
                                    "Он оказался довольно уязвимым и вы смогли его убить"
                                    jump .end_fight2
                                "Увернуться":
                                    "Вы пытаетесь повторить маневр, но в этот раз лис был готов и откусил вам руку"
                                    "Следущая атака лиса была смертельной"
                                    jump death

                label .end_fight2:
                hide foxman
                $hide_character()
                $in_fight = False
                show catcharpicture at left

                "Вы заметили что у лиса был факел и забрали его"
                $torch_flag = True
                jump room11

            "Направо":
                "*Идет направо*"
                #бой

                "Заглянув в дверь, вы быстро зашли туда, заметив какое-то движение."
                $hide_torch()
                hide catcharpicture
                $show_character([middle_left()])
                show goblin at middle_right:
                    zoom 1.3
                "Вы встретили гоблина. Он быстро к вам приближается"
                $in_fight = True
                $wounded = False
                label .fight_start3:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Гоблин был быстрее и ранил вас"
                            if wounded:
                                "Гоблин нанес смертельное ранение"
                                jump death
                            $wounded = True
                            jump .fight_start3
                        "Защититься":
                            "Атака была не сильной и вы смогли ее блокировать, оглушив гоблина"
                            jump .goblin_staggered
                        "Увернуться":
                            "Гоблин оказался проворным и смог ранить вас"
                            if wounded:
                                "Гоблин нанес смертельное ранение"
                                jump death
                            $wounded = True
                            jump .fight_start3

                label .goblin_staggered:
                    menu:
                        "Выберите действие"
                        "Атаковать":
                            "Вы успели добить гоблина"
                        "Защититься":
                            "Гоблин оправился от удара"
                            jump .fight_start3
                        "Увернуться":
                            "Гоблин оправился от удара"
                            jump .fight_start3

                hide goblin
                $hide_character()
                $in_fight = False
                show catcharpicture at left
                jump room12

    label room10:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "С каждым шагом вы чувствуете, что что-то не так."
                scene wp
                $show_torch()
                "Вы стали жертвой жестоких правил игры."
                jump death

            "Вперед":
                "Вы слышите подозрительное шипение."
                scene boom
                $show_torch()
                "Вы были взорваны зельем."
                jump death

            "Направо":
                "За дверью слышится утробное бульканье."
                scene lava
                $show_torch()
                "Вы решили поплавать в лаве."
                jump death

    label room11:
    #отображение подсказок
    show runa at center_door
    menu:
            "Кажется выход близко"
            "Налево":
                "На полу местами лежит песок, что хрустит под ногами с каждым шагом"
                #загадка
                scene sphinks
                $show_torch()
                show catcharpicture at left
                sphinx "Что за жалкие смертные пожаловали в мою обитель?"
                cat "Мы случайно дверью ошиблись! Сейчас уже уходим.."
                sphinx "Теперь вам дороги назад нет, сперва отгадайте загадку."
                sphinx "Какой мой любимый цвет?"
                cat "Да он издевается!"
                sphinx "Отвечай на вопрос, иначе умрешь еще раньше."
                #ответа нет
                python:
                    answer = renpy.input("Так какой цвет?")
                    answer = answer.lower()
                sphinx "Не верно. Теперь вы будете погребены под песком."
                jump death


            "Вперед":
                "За дверью слышится негромкий то ли рык, то ли смех."
                show minotaur at truecenter
                min "Жалкие смертные смогут выйти из лабиринта только если разгадают загадку."
                min "Без отдыха, без сна, беззвучным шагом с холма на холм кто движется не спеша, кто холод прогнать пришел?"
                #ответ: солнце
                python:
                    answer = renpy.input("Ну что, додумался?")
                    answer = answer.lower()
                if answer == "солнце":
                    min "У вас вышло отгадать мою загадку. Так и быть, вы свободны."
                    jump lab_exit
                else:
                    min "Как я и ожидал, вы не справились. Наградой за это будет смерть."
                    jump death


            "Направо":
                "Кажется, за дверью слышно пение птиц."
                scene Jungle
                $show_torch()
                "Вы заблудились в джунглях и умерли от жажды."
                jump death

    label room12:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "За дверью слышится утробное бульканье."
                scene lava
                $show_torch()
                "Вы решили поплавать в лаве."
                jump death

            "Вперед":
                "Вы слышите грохот."
                scene dark
                $show_torch()
                "На вас обвалился потолок."
                jump death

            "Направо":
                "За дверью слышен тихий смех."
                show foxman at truecenter
                "Странное существо выскочило на вас, а после наступила темнота."
                jump death

    label room13:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "За дверью слышен тихий смех."
                show foxman at truecenter
                "Странное существо выскочило на вас, а после наступила темнота."
                jump death

            "Вперед":
                "С каждым шагом вы чувствуете, что что-то не так."
                scene wp
                $show_torch()
                "Вы стали жертвой жестоких правил игры."
                jump death

            "Направо":
                "За дверью слышен тихий смех."
                show foxman at truecenter
                "Странное существо выскочило на вас, а после наступила темнота."
                jump death

    label lab_exit:
        scene canyon
        $show_torch()
        show catcharpicture at left
        cat "Наконец-то мы выбрались! Ура!"

    #конец лабиринта
    "Вы погасили факел"
    $hide_torch()
    $torch_lit = False
    $show_torch()
    cat "Прекрасный вид! Предлагаю спускаться вниз и заходить в лес. Вдруг там будет что-то интересное?"
    gg "Верно, ведь нам все равно нужно куда-то идти."
    "Вы спускаетесь с горы."
    scene forest1
    "Постепенно вы ступаете во владения деревьев, где со всех сторон слышатся лесные звуки"
    stop music
    play music "audio/forest_m.mp3" fadeout 1
    $show_torch()
    show catcharpicture at left
    cat "Какой густой лес... Погоди-ка.."
    cat "Тебе не кажется, что вот то дерево как-то странно на нас смотрит?"
    #бой с treant

    $hide_torch()
    hide catcharpicture
    $show_character([middle_left()])
    show treant at middle_right:
        zoom 1.3
    $in_fight = True
    $wounded = False
    label .fight_start_tre:
        menu:
            "Выберите действие"
            "Атаковать":
                "Вы успели нанести атаку до того, как энт что-то предпринял."
                jump .tre_dmg
            "Защититься":
                "Корни ударили вас из-под земли, но вы успели защититься, получив небольшой урон."
                if wounded:
                    "Корни оплели вас за руки и ноги, разрывая на куски."
                    jump death
                $wounded = True
                jump .fight_start_tre
            "Увернуться":
                "Огромные корни схватили, чем вы смогли увернуться."
                if wounded:
                    "Корни обвили вас, сильно передавливая, словно змеи."
                    jump death
                $wounded = True
                jump .fight_start_tre

    label .tre_dmg:
        menu:
            "Корни начинают оплетать энта."
            "Атаковать":
                "Вы успели добить энта."
            "Защититься":
                "Энт восстановил себя с помощью корней."
                jump .fight_start_tre
            "Увернуться":
                "Энт восстановил себя с помощью корней."
                jump .fight_start_tre

    hide treant
    $hide_character()
    $in_fight = False


    #после победы в бою:
    scene forest1
    $show_torch()
    show catcharpicture at left
    cat "Фух! Наконец мы справились. Это же ужас какой-то!"
    gg "Неприятно то, что мы подняли много шума. Как бы сюда кто-то не сбежался.."

    #добавлен звук тяжелых шагов
    play sound 'audio/ogre_steps.mp3'

    cat "Что это такое?"
    show ogr at middle_right
    nn "Снова вы?"
    non "Но этого быть не может!"
    nn "Мы же вас скинули!"
    gg "Клара, что за странное существо с нами говорит? Онао может разругаться с самим собой?"
    cat "Этого огра я уже видела! Тогда, в пещере, у лабиринта"
    cat "Думаю, это они скинули тебя вниз с телеги"
    "Огр резко замолкает, словно не желает разглашать великую ценнейшую тайну"
    gg "А давайте вы хотя бы представитесь для начала..?"
    nn "Наши имена лучшие на всем свете! Краснонос и Зубокрыл!"
    $no1 = "Краснонос"
    $no2 = "Зубокрыл"
    cat "Какие же вы все-таки смешные.. хи-хи.."
    gg "Зачем вы скинули меня вниз?"
    non "Нам было приказано.."
    gg "Кем приказано?"
    nn "Так мы тебе и сказали! И вообще.."
    non "Надо закончить начатое!"
    "На вас нападает огр."
    #бой с огром

    $hide_torch()
    hide catcharpicture
    $show_character([middle_left()])
    show ogr at middle_right:
        zoom 1.3
    $in_fight = True
    $wounded = False
    label .fight_start_ogr:
        "[no1] и [no2] яростно закричали, направляясь прямо на вас и замахиваясь дубиной."
        menu:
            "Выберите действие"
            "Атаковать":
                if character_option == 1:
                    "Ваш топор оказался быстрее огра."
                if character_option == 2:
                    "Водяной пузырь успешно захватил огра, но вскоре лопнул."
                if character_option == 3:
                    "Быстрый укол воздушным копьем успел нанести огру урон."
                if character_option == 4:
                    "Темная магия на мгновение ослепила огра, вызывая кровотечение."
                if character_option == 5:
                    "Огненный шар оставил огру несколько ожогов."
                jump .ogr_dmg
            "Защититься":
                "Защита не помогла вам - огр своей тяжелой дубиной пробил её."
                if wounded:
                    "Последнее, что вы услышали в темноте - смех двух голов огра."
                    jump death
                $wounded = True
                jump .fight_start_ogr
            "Увернуться":
                "Огр ударил наотмашь, все равно попадая по вам."
                if wounded:
                    "Атака оказалась такой сильной, что ваши кости не выдержали."
                    jump death
                $wounded = True
                jump .fight_start_ogr

    label .ogr_dmg:
        menu:
            "Огр перехватывает дубину поудобнее."
            "Атаковать":
                "Огр ругается и убегает, вы не успеваете его догнать."
            "Защититься":
                "Огр со смехом разминается, оправляясь от ударов."
                jump .fight_start_ogr
            "Увернуться":
                "Огр со смехом разминается, оправляясь от ударов."
                jump .fight_start_ogr

    hide ogr
    $hide_character()
    $in_fight = False

    $show_torch()
    show catcharpicture at left
    cat "Жаль, что они успели сбежать в лес! Ух, мы бы их допросили!"
    "Ваш поход по лесу продолжается и вскоре вы ввидите странного мальчика, сидящего на пне и читающего книгу."
    show markus at truecenter

    cat "Привет! Мы очень рады с тобой познакомиться!"
    gg "Не подскажешь, где выход отсюда?"
    mark "C местоположенем выхода я вряд ли смогу помочь, зато у меня для вас есть другое предложение. "
    gg "Какое?"
    mark "Вы сможете получить питомца-фамильяра по истечению этих мелких поручений."
    mark "Первым вашим заданием станет ловля рыбы. Недалеко отсюда вы найдете выход к озеру."
    mark "Без победы не возвращайтесь."
    #миниигра-квест на получение фамильяра (варианты: phoenix, rigen, whitewolf,unicorn)
    $phoenix_choise = 0
    $rigen_choise = 0
    $whitewolf_choise = 0
    $unicorn_choise = 0

    #миниигра рыбалка
    scene shore
    label fishing:
        show catcharpicture at left
        cat "Что ж, я уверена, что у нас получится что-то словить!"
        hide catcharpicture
        sys "Для управления используйте стрелочки <- ->"
        call screen Fishing
    label end_fishing:
        if fishing_fails == 0:
            show one at truecenter
            gg "Кажется, мы словили гуппи..!"
            $whitewolf_choise += 1
        if fishing_fails == 1:
            show two at truecenter
            gg "Кажется, мы словили золотую рыбку!"
            $phoenix_choise += 1
        if fishing_fails == 2:
            show three at truecenter
            gg "Кажется, мы словили... Рыбу-клоуна?"
            $rigen_choise += 1
        if fishing_fails >= 3:
            show four at truecenter
            gg "Кажется, мы словили... очень красивую полупрозрачную рыбку!"
            $unicorn_choise += 1
    show catcharpicture at left
    cat "Интересно, хорошо это или плохо? Ладно, пойдем дальше."

    scene forest_card
    show catcharpicture at left
    cat "Ого, да там же карты на пне лежат! Кажется, это следующая часть задания!"
    hide catcharpicture

    #миниигра карты
    "Карточная игра"
    $card_firstwin=True
    label card_game:
    window hide
    scene black
    jump CardGame

    label card_game_end:
    window show
    scene forest1
    "Вы победили!"
    show catcharpicture at left
    cat "Не ясно, засчиталось ли нам что-то... Может, Маркус и вовсе нас обманул?"
    gg "Посмотрим, думаю, мы делаем все это не просто так."

    if card_firstwin:
        $whitewolf_choise += 1
        $unicorn_choise += 1
    else:
        $phoenix_choise += 1
        $rigen_choise += 1


    "Вы заходите дальше в лес, постепенно становится все темнее."
    #добавить зажигание факела
    stop music
    play music "audio/necropolis.mp3" fadeout 1
    "Среди деревьев вы видите какие-то строения и решаете идти ближе к ним."
    scene graveyard
    "Строения оказываются могилами, а все это место - кладбищем."
    show catcharpicture at left
    cat "Как-то здесь очень неуютно...Ой!"
    cat "А что это там? За надгробиями!"
    #бой в рамках квеста с zombie и/или werewolf



    #последняя часть - загадки
    scene forest1
    $show_torch()
    show catcharpicture at left
    show markus at truecenter
    "Вы выходите на уже знакомую вам поляну, где на пне сидит Маркус."
    mark "Вы быстро вернулись. Со всем справились?"
    gg "Да"
    cat "Это было не так уж и сложно!"
    mark "Вот как? В любом случае, ваш ждет еще один тест, последний."
    mark "Вы должны будете ответить на мои вопросы и от них будет зависеть, получите ли вы себе союзника."
    cat "Не тяни! Лучше сразу задавай! Мы справимся."
    #сами загадки Ответ: Солнце. Ответ: Смерть. Ответ: Колибри. Ответ:человек.
    mark "Без отдыха, без сна, беззвучным шагом с холма на холм кто движется не спеша, кто холод прогнать пришел?"
    mark "Прячься в тени иль при свете дня: время придет - ты встретишь меня. Я уловлю малейший вздох, тебя обхитрю, застану врасплох."
    mark "Мала как песчинка, лечу как пушинка. Сначала услышишь, потом лишь заметишь."
    mark "Что за существо ходит на четырех ногах утром, на двух днем и на трех вечером?"

    #после квеста на питомца
    $show_torch()
    show catcharpicture at left
    show markus at truecenter
    mark "Поздравляю, теперь у вас есть новый друг. Он сможет помочь вам в дальнейших странствиях."
    mark "Правда, вам придется дать ему имя. Обычным лесным жителям они ни к чему."
    mark "Уже придумали, как назовете?"
    python:
        petnam = renpy.input("Дайте имя своему фамильяру.")
        petnam = petnam.strip() or "Фамильяр"

    $petname = petnam
    cat "Как думаешь, [petnam] поможет нам отыскать того огра?"
    gg "Не знаю, Клара, но стоит попробовать. А ты что думаешь, [petnam]?"

    #в зависимости от попавшегося питомца будут разные поиски огра

    label pet_rigen:
        pet "У меня очень чуткий слух."
        pet "Я слышу грузные шаги этого существа за много миль."

    label pet_whitewolf:
        pet "У меня очень чуткий нюх."
        pet "Я чую след этого огра, еще не прошло так много времени, чтобы запах пропал."

    label pet_phoenix:
        pet "У меня зоркий взгляд, однако ветви и листва деревьев мешают мне увидеть огра."
        pet "В лесу я бессилен, но если придется поискать кого-то в поле или в горах, то с этим я легко справлюсь."

    label pet_unicorn:
        pet "Я не обладаю навыками для поиска существ, однако умею быстро бегать."
        pet "Мы быстро догоним огра, если сумеем понять, где он."



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
