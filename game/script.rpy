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
define syl = Character('Сильф')
define tree = Character('Древний энт')
define boss = Character('Повелитель Пустоши')

init python:
    pet_choise = 0
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

    def show_pet(pos=[]):
        if pet_choise == 1:
             renpy.show("whitewolf", pos)
        if pet_choise == 2:
            renpy.show("phoenix", pos)
        if pet_choise == 3:
            renpy.show("unicorn", pos)
        if pet_choise == 4:
            renpy.show("rigen", pos)

    def hide_pet():
        if pet_choise == 1:
            renpy.hide("whitewolf")
        if pet_choise == 2:
            renpy.hide("phoenix")
        if pet_choise == 3:
            renpy.hide("unicorn")
        if pet_choise == 4:
            renpy.hide("rigen")

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

    $phoenix_choise = 0
    $rigen_choise = 0
    $whitewolf_choise = 10
    $unicorn_choise = 0

    $no1 = "???"
    $no2 = "?????"
    $petname = "Фамильяр"

    nn "Очередной эксперимент не удался, только материалы пошли насмарку…"

    non "Интересно, сколько еще он будет пробовать?"

    nn "Не болтай лишнего! Лучше сбрасывай!"

    stop sound fadeout 1
    play sound 'audio/hum_falling.mp3'
    play music "audio/dunF.mp3" fadeout 1 volume 0.6

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
        "Воин":
            jump get_character1

        "Водный маг":
            jump get_character2

        "Копейщик":
            jump get_character3

        "Темный колдун":
            jump get_character4

        "Огненная ведьма":
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
    play music "audio/maze.mp3" fadeout 1 volume 0.6

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

                play sound "audio/victory.mp3" volume 0.1
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

                play sound "audio/victory.mp3" volume 0.1
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

                play sound "audio/victory.mp3" volume 0.1
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
                scene snakes:
                    zoom 1.2
                    xalign 0.5
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
                scene clouds:
                    zoom 2.4
                    xalign 0.5
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
                play sound "audio/victory.mp3" volume 0.1
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
                scene roots:
                    zoom 1.4
                    xalign 0.5
                    yalign 0.35
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
                scene live_mountain:
                    zoom 2.0
                    xalign 0.5
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
                scene spider:
                    zoom 3.5
                    xalign 0.5
                    yalign 0.5
                $show_torch()
                "Вы умерли от укуса ядовитого паука."
                jump death

    label room7:
    #отображение подсказок
    scene frozen_maze
    show runa at center_door
    show runa1 at right_door
    show runa2 at left_door
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
                scene jungle:
                    zoom 2.5
                    xalign 0.5
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
                scene live_mountain:
                    zoom 2.0
                    xalign 0.5
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
                scene lava:
                    zoom 2.5
                    xalign 0.5
                    yalign 0.4
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
                play sound "audio/victory.mp3" volume 0.1
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
                play sound "audio/victory.mp3" volume 0.1
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

                play sound "audio/victory.mp3" volume 0.1
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
                scene black
                show boom:
                    xalign 0.5
                    yalign 0.5
                    zoom 1.5
                $show_torch()
                "Вы были взорваны зельем."
                jump death

            "Направо":
                "За дверью слышится утробное бульканье."
                scene lava:
                    zoom 2.5
                    xalign 0.5
                    yalign 0.4
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
                scene jungle:
                    zoom 2.5
                    xalign 0.5
                $show_torch()
                "Вы заблудились в джунглях и умерли от жажды."
                jump death

    label room12:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "За дверью слышится утробное бульканье."
                scene lava:
                    zoom 2.5
                    xalign 0.5
                    yalign 0.4
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
                show foxman at truecenter:
                    zoom 3.0
                    yalign 0.65
                "Странное существо выскочило на вас, а после наступила темнота."
                jump death

    label room13:
    #отображение подсказок
    menu:
            "Подозрительная комната"
            "Налево":
                "За дверью слышен тихий смех."
                show foxman at truecenter:
                    zoom 3.0
                    yalign 0.65
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
    play music "audio/forest_m.mp3" fadeout 1 volume 0.6
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

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    play sound "audio/victory.mp3" volume 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
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
    play sound '<from 0 to 3>audio/ogre_steps.mp3'

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
    stop music
    play music "audio/water.mp3" fadeout 1
    $show_torch()
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

    stop music
    play music "audio/forest_m.mp3" fadeout 1 volume 0.6
    scene forest_card:
        zoom 1.5
        xalign 0.5
    $show_torch()
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
    $show_torch()
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
    gg "Кажется, пора зажечь факел."
    $hide_torch()
    $torch_lit = True
    $show_torch()
    stop music
    play music "audio/necropolis.mp3" fadeout 1
    "Среди деревьев вы видите какие-то строения и решаете идти ближе к ним."
    scene graveyard:
        zoom 1.5
        xalign 0.5
    $show_torch()
    "Строения оказываются могилами, а все это место - кладбищем."
    show catcharpicture at left
    cat "Как-то здесь очень неуютно...Ой!"
    cat "А что это там? За надгробиями!"
    #бой в рамках квеста с zombie и/или werewolf

    "Из-за каменной плиты выходит зомби."
    label zombie_fight:
        $in_fight = True
        $hide_torch()
        hide catcharpicture
        $show_character([middle_left()])
        show zombie at middle_right
        $your_health = 3
        $zombie_health = 4
        if character_option == 4:
            "C помощью своей темной магии вы смогли подчинить зомби и упокоить его"
            $whitewolf_choise += 1
            jump .fight_end
        label .fight_start:
            "Зомби медленно прибижается к вам"
            menu:
                "Выберите действие"
                "Атаковать":
                    if character_option == 5:
                        "Огонь сжигает зомби и он очень быстро погибает"
                        $phoenix_choise += 1
                        jump .fight_end
                    $zombie_health-=1
                    if zombie_health<=0:
                        "Зомби наконец умирает окончательно"
                        jump .fight_end
                    "Вы раните зомби, но он похоже не обращает внимания на раны и хватает вас"

                    jump .zombie_close
                "Защититься":
                    "Зомби пытается отгрызть вам руку!"
                    $your_health-=1
                    if your_health <=0:
                        "Вы окончательно обессилели от накопившихся ран."
                        jump death
                    jump .zombie_close
                "Увернуться":
                    "Вы без труда отдаляетесь от него"
                    jump .zombie_far

        label .zombie_close:
            "Зомби держит вас и пытается перегрызть вам шею"
            menu:
                "Выберите действие"
                "Атаковать":
                    if character_option == 1:
                        "Вы отрубаете голову зомби. Слепого зомби вы добили без проблем"
                        $unicorn_choise += 1
                        jump .fight_end
                    elif character_option == 3:
                        "Атака ветром отбрасывает зомби далеко"
                        $zombie_health-=1
                        jump .zombie_far
                    else:
                        $zombie_health-=1
                        "Ваша атака отбрасывает зомби"
                        jump .fight_start

                "Защититься":
                    "У вас не получилось защититься в захвате. Зомби вызвал у вас смертельное кровотечение из артерии"
                    jump death
                "Увернуться":
                    "Вы вырвались из захвата зомби, но он успел значительно вас ранить"
                    $your_health-=2
                    if your_health<=0:
                        "Получив слишком много ранений, вы истекли кровью."
                        jump death
                    jump .fight_start

        label .zombie_far:
            "Зомби далеко от вас"
            menu:
                "Выберите действие"
                "Атаковать":
                    if character_option == 1:
                        "Для атаки вам пришлось приблизиться, но она сильно ранила зомби"
                        $zombie_health-=2
                        jump .zombie_close
                    if character_option == 5:
                        "Огонь сжигает зомби и он очень быстро погибает"
                        jump .fight_end
                    "Ваша атака ранила зомби"
                    $zombie_health-=1
                    if zombie_health<=0:
                        "Зомби наконец умирает окончательно"
                        jump .fight_end
                    jump .fight_start

                "Защититься":
                    jump .fight_start
                "Бежать":
                    "Зомби был очень меделенным и вы смогли от него убежать"
                    $rigen_choise += 1
                    jump .fight_end
        label .fight_end:
            $ renpy.music.set_volume(0.00, delay=0, channel='music')
            play sound "audio/victory.mp3" volume 0.1
            $ renpy.music.set_volume(1.00, delay=0, channel='music')
            hide zombie
            $hide_character()
            $in_fight = False


    $hide_torch()
    $torch_lit = False
    $show_torch()
    "Вы погасили факел, возвращаясь в освещенную часть леса."
    stop music
    play music "audio/forest_m.mp3" fadeout 1

    #последняя часть - загадки

    scene forest1
    $show_torch()
    show catcharpicture at left
    show markus at truecenter
    "Вы выходите на уже знакомую вам поляну, где на пне сидит Маркус."
    mark "Вы быстро вернулись. Со всем справились?"
    gg "Да"
    cat "Это было не так уж и сложно!"
    mark "Вот как? В любом случае, вас ждет еще один тест, последний."
    mark "Вы должны будете ответить на мои вопросы и от них будет зависеть, получите ли вы себе союзника."
    cat "Не тяни! Лучше сразу задавай! Мы справимся."
    #сами загадки Ответ: Солнце. Ответ: Смерть. Ответ: Колибри. Ответ:человек.
    mark "Без отдыха, без сна, беззвучным шагом с холма на холм кто движется не спеша, кто холод прогнать пришел?"
    menu:
        "Каков будет ваш ответ?"
        "Шаровая молния":
            mark "Сомнительный ответ..."
            $unicorn_choise += 1
            jump rid_2
        "Солнце":
            mark "Верно, теперь следующая загадка."
            $phoenix_choise += 1
            jump rid_2
        "Огонь":
            mark "Кажется, эта загадка у вас не удалась."
            $rigen_choise += 1
            jump rid_2
    label rid_2:
        mark "Прячься в тени иль при свете дня: время придет - ты встретишь меня. Я уловлю малейший вздох, тебя обхитрю, застану врасплох."
        menu:
            "Как думаете, что это?"
            "Смерть":
                mark "Вы правы. Мрачноватые загадки хорошо вам даются.."
                $whitewolf_choise += 1
                jump rid_3
            "Болезнь":
                mark "Это неверный ответ."
                $rigen_choise += 1
                jump rid_3
            "Страх":
                mark "Видимо, загадка оказалась слишком сложной.."
                $whitewolf_choise += 1
                jump rid_3
    label rid_3:
        mark "Мала как песчинка, лечу как пушинка. Сначала услышишь, потом лишь заметишь."
        menu:
            "Каков правильный ответ на ваш взгляд?"
            "Комар":
                mark "Вы правы. Мрачноватые загадки хорошо вам даются.."
                $phoenix_choise += 1
                jump rid_4
            "Колибри":
                mark "Да, именно эта милая птичка.."
                $unicorn_choise += 1
                jump rid_4
            "Мошка":
                mark "Видимо, загадка оказалась слишком сложной.."
                $rigen_choise += 1
                jump rid_4
    label rid_4:
        mark "Что за существо ходит на четырех ногах утром, на двух днем и на трех вечером?"
        menu:
            "Что вы думаете?"
            "Гоблин":
                mark "Гоблины редко доживают до старости... Вы не правы."
                $whitewolf_choise += 1
                jump rid_end
            "Куропатка":
                mark "Странный выбор. И он неверный."
                $unicorn_choise += 1
                jump rid_end
            "Человек":
                mark "Это верный ответ."
                $rigen_choise += 1
                jump rid_end
    label rid_end:

        mark "Что же, все испытания закончены. А это значит, что сейчас к вам выйдет то существо, что сочтет вас достойным."
        cat "Интригующе!"


        if (whitewolf_choise > phoenix_choise) and (whitewolf_choise > unicorn_choise) and (whitewolf_choise > rigen_choise):
            $pet_choise = 1 #whitewolf

        elif (phoenix_choise > whitewolf_choise) and (phoenix_choise > unicorn_choise) and (phoenix_choise > rigen_choise):
            $pet_choise = 2 #phoenix

        elif (unicorn_choise > whitewolf_choise) and (unicorn_choise > phoenix_choise) and (unicorn_choise > rigen_choise):
            $pet_choise = 3 #unicorn
        else:
            $pet_choise = 4 #rigen


    #после квеста на питомца
    scene forest1
    $show_torch()
    show catcharpicture at left
    show markus at middle_right
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

    if pet_choise == 1:
        jump pet_whitewolf
    if pet_choise == 2:
        jump pet_phoenix
    if pet_choise == 3:
        jump pet_unicorn
    if pet_choise == 4:
        jump pet_rigen

    label pet_whitewolf:
        $show_pet([truecenter])
        pet "У меня очень чуткий нюх."
        pet "Я чую след этого огра, еще не прошло так много времени, чтобы запах пропал."
        cat "Тогда отправляемся! До встречи, Маркус."
        "Юноша, сидящий на пне, кивает вам в знак прощания и вновь погружается в книгу. Вы же устремляетесь вслед за волком."
        "[petnam] приводит вас в сырую пещеру."
        stop music
        play music "audio/rcave.mp3" fadeout 1
        scene rockcave
        "Не успеваете вы сделать и пары шагов, как из темноты на вас выскакивает оборотень."

        menu:
            "Вы хотите сражаться сами или отпустить [petnam] сражаться за вас?"
            "Сражаться самому":
                $show_character([middle_left()])
                show werewolf at middle_right
                $in_fight = True
                $wounded = False
                jump start_fight_2
            "Дать возможность проявить себя питомцу":
                jump whitewolf_werewolf

        label start_fight_2:
            "Оборотень быстро приближается к вам"
            menu:
                "Выберите действие"
                "Атаковать":
                    if character_option == 1:
                        "Ваш топор врезался в грудь оборотня, застревая там, на что тот заревел и откинул вас в сторону."
                        if wounded:
                            "Последнее, что вы почувствовали - смыкание клыков оборотня на вашей шее."
                            jump death
                        $wounded = True
                    if character_option == 2:
                        "Поток воды ненадолго замедлил оборотня"
                    if character_option == 3:
                        "Быстрый укол воздушным копьем оставил оборотню рану."
                    if character_option == 4:
                        "Оборотень отпрянул назад после вашего сильного заклинания."
                    if character_option == 5:
                        "Огонь изрядно опалил шкуру оборотня."
                    jump .werewolf_dmg
                "Защититься":
                    "Вы принимаете защитную стойку."
                    if wounded:
                        "Из-за невовремя открывшейся раны вы теряете последние остатки сил. Падая, вы видите как оборотень прыгает на вас..."
                        jump death
                    $wounded = True
                    jump start_fight_2

            label .werewolf_dmg:
                menu:
                    "После вашей атаки оборотень замер."
                    "Атаковать":
                        "Оборотень, пошатнувшись, издает свой последний протяжный вой и падает на землю."
                    "Защититься":
                        "Собравшись с силами, оборотень совершает молниеносный рывок, обходящий вашу защиту."
                        "Перед вашими глазами все меркнет."
                        jump death
            hide werewolf
            $hide_character()
            $in_fight = False
            jump after_win


        label whitewolf_werewolf:
            $show_pet([middle_left()])
            show werewolf at middle_right
            "Волки начинают медленно кружить друг возле друга, присматриваясь к слабым местам."
            "Вдруг оборотень не выдерживает и нападает, но [petnam] проворным движением уклоняется и наносит сокрушительный удар лапой со спины"
            "Оборотень, пошатнувшись, издает свой последний протяжный вой и падает на землю."
            hide werewolf
            $hide_pet()


        # После победы
        label after_win:
        show catcharpicture at left
        cat "Фух, пронесло!"
        cat "[petnam], ну и куда ты нас завел? Здесь ведь нет того огра!"
        pet "Не спешите с выводами."
        "Продвинувшись вглубь пещеры вы и впрямь всречаете [no1] и [no2]."
        show ogre at truecenter:
            zoom 2.5
        cat "Бежать вам некуда, а значит, рассказывайте все подобру-поздорову!"
        jump search_completed




    label pet_phoenix:
        $show_pet([truecenter])
        pet "У меня зоркий взгляд, однако ветви и листва деревьев мешают мне увидеть огра."
        pet "В лесу я бессилен, но если придется поискать кого-то в поле или в горах, то с этим я легко справлюсь."
        mark "Вы можете попробовать найти Древнего энта, вероятно, он сможет помочь."
        cat "Спасибо, Маркус! До свидания!"
        "Юноша, сидящий на пне, кивает вам в знак прощания и вновь погружается в книгу."
        pet "Я взлечу повыше и найду самое большое дерево здесь."
        "[petnam] улетает, но вскоре возвращается, указывая вам дорогу. Вы отправляетесь вслед за фениксом."

        scene giant_tree
        show catcharpicture at left
        $show_pet([right])
        "Вы выходите к огромному, кажется, спящему дереву."
        "Однако, не успеваете вы ничего сделать, как раздается звучный голос"
        tree "Путники, что вы хотите узнать?"
        cat "А что вы можете нам рассказать, уважаемое дерево?"
        tree "Я чувствую весь этот лес и могу рассказать о чем угодно, что находится здесь."
        cat "Тогда расскажите о том, где находится один огр!"
        tree "Не так быстро... Чтобы я ответил на ваш вопрос, вы должны ответить на мой."
        tree "Все ему покорится: зверь, цвет, лист, птица; железо, прочный меч - ничто не уберечь. Пойми: наша доля - принять его волю."

        python:
            answer = renpy.input("Отвечайте, не задерживайте меня!")
            answer = answer.lower()
        if answer != "время":
            "Древнее дерево грозно зашелестело ветвями."
            tree "Как вы посмели прийти сюда и просить моей помощи, если не знаете даже таких банальных вещей?"
            "Разозленный энт выпивает из вас все жизненные силы"
            jump death

        "Шелест ветвей дерева походит на тихий добродушный смех."
        tree "Верно. Теперь задавайте свой вопрос."
        cat "Подскажи нам, Древний Энт, где сейчас находится огр [no1] и [no2]?"
        "Дерево, кажется, еще сильнее зажмуривает глаза, после чего над лесом раздается его голос, гулким эхом отлетающий от деревьев."
        tree "Вы найдете их у того, что высоких деревьев длинней, травиночки маленькой ниже, с чем дали становятся ближе."
        "Энт замолкает и больше не отвечает на ваши расспросы."
        cat "Эй! Ну разве обязательно было и тут загадкой говорить? [name], у тебя есть идеи, что это может быть?"
        menu:
            "На какое место намекет загадка энта?"
            "Река":
                cat "Тогда направляемся к ней!"
                label riv:
                    "[petnam] улетает в поисках реки, а вернувшись, указывает вам дорогу."
                    "Однако, идя по лесу, вы натыкаетесь на тропинку, за поворотом которой замечаете какое-то движение."
                    jump ogre_path
            "Ручей":
                cat "Странное предположение. Да и как мы его найдем? Он же маленький!"
                cat "Лучше направимся к реке!"
                jump riv
            "Дорога":
                cat "Отлично! Думаю, [petnam] с легкостью ее найдет!"
                "Феникс и правда быстро выводит вас на лесную тропу. За ее поворотом вы замечаете какое-то движение."
                jump ogre_path

        label ogre_path:
            scene forestpath
            show catcharpicture at left
            $show_pet([right])
            show ogre at truecenter:
                zoom 2.5
            "Пройдя чуть дальше по дороге вы находите того самого огра."
            cat "Вы пойманы! И теперь никуда не сбежите! Рассказывайте, что вам известно!"
            jump search_completed



    label pet_unicorn:
        $show_pet([truecenter])
        pet "Я не обладаю навыками для поиска существ, однако умею быстро бегать."
        pet "Мы быстро догоним огра, если сумеем понять, где он."
        mark "Вы можете попробовать найти Древнего энта, вероятно, он сможет помочь."
        mark "Сильф поможет вам найти энта."
        show sylph at middle_left
        cat "Спасибо, Маркус! До свидания!"
        "Юноша, сидящий на пне, кивает вам в знак прощания и вновь погружается в книгу."
        pet "Забирайтесь ко мне на спину, домчимся с ветерком."
        "Забравшись на спину единорогу, вы быстро следуете за летящим перед вами Сильфом."

        scene giant_tree
        show catcharpicture at left
        $show_pet([right])
        show sylph at middle_left
        syl "Мне пора, удачи вам. Не обижайте дедушку-энта.."
        cat "До встречи, не обидим!"
        hide sylph
        "Сильф улетает, а вы выходите к огромному, кажется, спящему дереву."
        "Однако, не успеваете вы ничего сделать, как раздается звучный голос"
        tree "Путники, что вы хотите узнать?"
        cat "А что вы можете нам рассказать, уважаемое дерево?"
        tree "Я чувствую весь этот лес и могу рассказать о чем угодно, что находится здесь."
        cat "Тогда расскажите о том, где находится один огр!"
        tree "Не так быстро... Чтобы я ответил на ваш вопрос, вы должны ответить на мой."
        tree "Кто новым может быть и старым; кто может и расти и убывать; кто полон может быть, но не бывает пуст, кто виден лишь когда почти у всех глаза закрыты?"
        python:
            answer = renpy.input("Отвечайте, не задерживайте меня!")
            answer = answer.lower()
        if answer != "луна":
            "Древнее дерево грозно зашелестело ветвями."
            tree "Как вы посмели прийти сюда и просить моей помощи, если не знаете даже таких банальных вещей?"
            "Разозленный энт выпивает из вас все жизненные силы"
            jump death

        #правильный ответ на загадку
        "Шелест ветвей дерева походит на тихий добродушный смех."
        tree "Верно. Теперь задавайте свой вопрос."
        cat "Подскажи нам, Древний Энт, где сейчас находится огр [no1] и [no2]?"
        "Дерево, кажется, еще сильнее зажмуривает глаза, после чего над лесом раздается его голос, гулким эхом отлетающий от деревьев."
        tree "Вы найдете их у того, что высоких деревьев длинней, травиночки маленькой ниже, с чем дали становятся ближе."
        "Энт замолкает и больше не отвечает на ваши расспросы."
        cat "Эй! Ну разве обязательно было и тут загадкой говорить? [name], у тебя есть идеи, что это может быть?"
        menu:
            "На какое место намекет загадка энта?"
            "Река":
                cat "Тогда направляемся к ней!"
                label riv1:
                    "Забравшись на [petnam] вы быстро направляетесь в сторону реки."
                    "Однако, спеша, вы натыкаетесь на тропинку, за поворотом которой замечаете какое-то движение."
                    jump ogre_path1
            "Ручей":
                cat "Странное предположение. Да и как мы его найдем? Он же маленький!"
                cat "Лучше направимся к реке!"
                jump riv1
            "Дорога":
                cat "Отлично! Думаю, с помощью [petnam] мы с легкостью ее отыщем!"
                "На единороге вы и правда быстро выезжаете на лесную. За ее поворотом вы замечаете какое-то движение."
                jump ogre_path1

        label ogre_path1:
            scene forestpath
            show catcharpicture at left
            $show_pet([right])
            show ogre at truecenter:
                zoom 2.5
            "Пройдя чуть дальше по дороге вы находите того самого огра."
            cat "Вы пойманы! И теперь никуда не сбежите! Рассказывайте, что вам известно!"
            jump search_completed


    label pet_rigen:
        $show_pet([truecenter])
        pet "У меня очень чуткий слух."
        pet "Я слышу грузные шаги этого существа за много миль."
        cat "Значит, мы сможем найти его по звуку! Выдвигаемся!"
        mark "Думаю, вам стоит взять еще одного маленького помощника для навигации по лесу."
        show sylph at middle_left
        mark "Познакомьтесь с Сильфом. Он поможет вам не заплутать среди деревьев."
        "Поблагодарив Маркуса, вы все вместе отправляетесь туда, куда указывает [petnam]."
        stop music
        play music "audio/grass.mp3" fadeout 1
        scene ruin1
        "Шаг за шагом вы выходите к лесным руинам."
        show catcharpicture at left
        $show_pet([truecenter])
        show sylph at middle_left
        cat "Что это за место? Здесь раньше был город?"
        syl "Да, но довольно давно. Сейчас тут пусто. И может быть опасно, так что будьте осмотрительнее."
        "Все вместе вы осторожно продвигаетесь по заброшенному городу в поисках огра-беглеца."
        "Неожиданно из-за зданий выходит гигант. С диким ревом он кидается на вас."
        menu:
            "Вы хотите сражаться сами или отпустить [petnam] сражаться за вас?"
            "Сражаться самому":
                scene ruin1
                $show_character([middle_left()])
                hide catcharpicture
                show giant at middle_right
                $in_fight = True
                $wounded = False
                jump start_fight_1
            "Дать возможность проявить себя питомцу":
                jump rigen_ogre

        label start_fight_1:
            "C дубиной на плече гигант приближается к вам."
            menu:
                "Выберите действие"
                "Атаковать":
                    if character_option == 1:
                        "Ваш топор врезался в грудь гиганта, застревая там, на что тот заревел и откинул вас в сторону."
                        if wounded:
                            "Последнее, что вы услышали в темноте - смех двух голов огра."
                            jump death
                        $wounded = True
                    if character_option == 2:
                        "Водяной пузырь обернулся вокруг головы гиганта. Нехватка воздуха тому явно не понравилась, но дубиной он лопнул пузырь."
                    if character_option == 3:
                        "Быстрый укол воздушным копьем оставил гиганту рану."
                    if character_option == 4:
                        "Темной магией удалось открыть множетсво ран на теле гиганта, заметно ослабив его."
                    if character_option == 5:
                        "Огненный штор оставил гиганту ожоги."
                    jump .giant_dmg
                "Защититься":
                    "Размахнувшись дубиной, ударом гигант снес вас вместе с вашей защитой."
                    if wounded:
                        "Удар дубины пришелся в голову и она лопнула, как арбуз."
                        jump death
                    $wounded = True
                    jump start_fight_1
                "Увернуться":
                    "Вы не смогли увернуться от огромной дубины гиганта."
                    if wounded:
                        "Удар оказался таким сильным, что ваши кости не выдержали."
                        jump death
                    $wounded = True
                    jump start_fight_1

            label .giant_dmg:
                menu:
                    "После вашей атаки гигант на мгновение остановился."
                    "Атаковать":
                        "Гигант грузно падает на землю, дыхания его больше не слышно."
                    "Защититься":
                        "Собравшись с силами, гигант наносит сокрушающий удар, пробивающий вашу защиту."
                        "Перед вашими глазами все меркнет."
                        jump death
                    "Увернуться":
                        "Заметив ваш маневр, гигант хватает вас и сжимает в кулаке. Ваше тело не выдерживает давления."
                        jump death

            hide giant
            $hide_character()
            $in_fight = False
            jump giant_fight_end

            label rigen_ogre:
                $show_pet([middle_left()])
                show giant at middle_right
                "Огр замахивается дубиной, однако ваш питомец быстро уворачивается, отпрыгивая в сторону, словно кролик."
                "Таким же ловким прыжком [petnam] оказывается на спине огра, сбивая его на землю."
                "Зубы ригена оказываются достаточно остры, чтобы закончить жизнь огра."
                hide giant
                $hide_pet()

        label giant_fight_end:
        show catcharpicture at left
        $show_pet([truecenter])
        show sylph at middle_left
        cat "У нас вышло победить этого гиганта!"
        syl "Боюсь, мне пора возвращаться.. Мне неуютно в этих руинах, ведь я дух леса."
        cat "Спасибо за помощь, было приятно иметь с тобой дело!"
        "Сильф скрывается среди деревьев."
        hide sylph
        pet "Я слышу еще шаги, прямо за этим зданием."
        show ogre at middle_right:
            zoom 2.5
        "Из-за здания появляется огр."
        nn "Вы все-таки нашли нас!"
        non "Как вам это удалось?"
        "[petnam] задержал огра-беглеца, прижав того к стене"
        cat "Сбежать больше не получится! Рассказывайте все, что знаете!"
        jump search_completed

    #после поиска огра

    label search_completed:
        stop music
        play music "audio/completesearch.mp3" fadeout 1
        nn "А что мы знаем?"
        non "Мы ничего не знаем!"
        gg "Вы знаете, кто приказал сбросить меня в те пещеры!"
        nn "Да, знаем.."
        non "Но не скажем!"
        nn "Нет, не скажем"
        cat "У вас не осталось выбора!"

        non "Ладно, мы отведем вас в замок нашего Господина, и ты узнаешь, зачем он сбросил тебя в то подземелье."
        "Вслед за огром вы идете через лес и выходите к дверям старинного особняка."
        scene mansion
        show catcharpicture at left
        cat "Ого, какой особняк!"
        "Пока вы с восторгом рассматриваете строение, огр с мерзким хохотом сбегает."
        "Однако смысла ловить его вы не видите, ведь дверь особняка со скрипом приоткрывается."
        "Зайдя внутрь, вы попадаете в лишенное света помещение."
        scene dark
        boss "И вот ты, герой, снова пришел в мои владения попытать удачу."
        "Постепенно в зале становится светлее. Наконец вам удается рассмотреть своего собеседника."
        scene zal
       
        $show_pet([middle_left])
        show catcharpicture at left
        show lich at middle_right
        cat "Так это ты скинул [name] в ту пещеру?!"
        "Вы слышите скрежещущий смех существа, представшего перед вами."
        boss "И да, и нет."
        gg "Как это понимать?!"
        boss "Я приказал скинуть, а не кидал собственноручно."
        boss "И, более того, ты должен был быть мертв."

        if character_option == 4:
            boss "Но раз ты все-таки выжил... Ты не такой уж слабый темный маг."
            boss "Разве тебе не хочется стать моим последователем? Ощутить вкус силы? Захватить этот бренный мир вместе со мной?"
            boss "Я готов принять тебя к себе в ученики."
            cat "Не нужно, [name], он же злодей! Он убивает даже невинных!"
            boss "Так что скажешь?"
            menu:
                "Сделайте ваш выбор"
                "Встать на сторону Повелителя":
                    gg "Я согласен"
                    boss "Отлично. Тогда первое твое задание: избавься от кошки и закопай ее где-нибудь."
                    cat "Нет, постой! Не надо!"
                    "Не слушая мольбы Клары, вы пронзаете ее черной стрелой. Бездыханное тело падает замертво."
                    "Подхватив его, вы отправляетесь на кладбище."
                    scene graveyard
                    stop music
                    play music "audio/evil.mp3" fadeout 1
                    "В этом месте вы осознаете, что теперь никогда не станете прежним."
                    "Убив Клару, своего друга, вы перешли черту и стали на сторону зла."
                    "Ваш путь будет полон крови и смерти."
                    "Что же.. Вы теперь счастливы?"
                    "Так восславьте своего нового Господина! Повелителя Пустоши!"
                    return
                "Остаться верным добру":
                    gg "Это смешно. Ты убийца, злодей, унесший множество жизней ради забавы."
                    gg "Я никогда не стану на твою сторону."
                    jump thelast_fight


        label thelast_fight:
            boss "Что же, раз так... Упокоим тебя заново!"
            boss "Ты станешь первым, а после весь мир захлебнется в крови!"
            stop music
            play music "audio/thelastfight.mp3" fadeout 1
            scene zal
            $show_character([middle_left()])
            $show_pet([truecenter])
            show lich at middle_right

            "Повелитель Пустоши с усмешкой наблюдает за вами, пока, кажется, не собираясь атаковать."
            $in_fight = True
            $boss_health = 5
            $your_health = 4
            $dead_pet = False
            label thelast_start:
                play sound "audio/batstar.mp3"
                menu:
                    "Что же вы предпримете?"
                    "Атаковать":
                        if character_option == 1:
                            "Ваш топор с трудом смог задеть изворотливого лича."
                            $boss_health -= 1
                        if character_option == 2:
                            "Кажется, попытка утопить Повелителя прошла успешно."
                            $boss_health -= 2
                        if character_option == 3:
                            "Воздушное копье из-за своей скорости смогло нанести значительный урон."
                            $boss_health -= 2
                        if character_option == 4:
                            boss "Да ты смешон. А ведь мог бы присоединиться ко мне и стать сильнейшим."
                            $boss_health -= 1
                        else:
                            $boss_health -= 1
                        jump magic_attack
                    "Защититься":
                        "Монстр заметил вас"
                        jump magic_attack
                    "Увернуться":
                        "Монстр заметил вас"
                        jump magic_attack
                    "Атака питомца":
                        if pet_choise == 1:
                            "Волк прыгнул на Повелителя и, вцепившись зубами в его руку, отгрыз часть его кости."
                            boss "Да как ты посмел! Верни мою кость!"
                            $boss_health -= 2
                        if pet_choise == 2:
                            "Феникс выпустил столб пламени в сторону Повелителя Пустоши."
                            boss "А этот огонь погорячее, чем у людских колдунишек!"
                            "Вы замечаете, что кости лича чуть подплавились."
                            $boss_health -= 2
                        if pet_choise == 3:
                            "Единорог с разбега вонзает рог в вашего врага, после чего, фыркая, отступает обратно."
                            boss "Ах, значит так... Обзавелся светлым существом на мою голову."
                            $boss_health -= 2
                        if pet_choise == 4:
                            "Риген прыгает и мощным ударом задних лап ломает Повелителю пару костей."
                            boss "Какая милая зверюшка... Так и хочется сожрать."
                            $boss_health -= 2
                        jump magic_attack

            label magic_attack:
                "В руках Повелителя Пустоши накапливаются фиолетовые сгустки темной энергии."
                menu:
                    "Выберите действие"
                    "Атаковать":
                        if character_option == 4:
                            "Ваша темная энергия отразила энергию лича и нанесла ему урон."
                            boss "Да как ты смеешь?!"
                            $boss_health -= 1
                            if boss_health <=0:
                                jump the_end
                            jump attack
                        "Вы не успели атаковать, лич оказался быстрее и ранил вас."
                        $your_health -=2
                        if your_health <=0:
                            "Вы умерли под смех Повелителя, на этот раз окончательно."
                            jump death
                        jump attack
                    "Защититься":
                        "Щит частично выдержал, но боль вы все равно ощутили."
                        $your_health -=1
                        if your_health <=0:
                            "Вы умерли под смех Повелителя, на этот раз окончательно."
                            jump death
                        jump prepares
                    "Увернуться":
                        "Вам удалось увернуться."
                        boss "Какой юркий... Ну ничго, без ног не поскачешь!"
                        jump prepares
                    "Атака питомца":
                        if pet_choise == 1:
                            "Волк прыгнул на Повелителя и отгрыз ему ногу, однако темное заклинание попало прямо в него."
                            "Ваш питомец упал на землю и больше не очнется."
                            boss "Вот так погибают блохастые псины!"
                            $boss_health -= 2
                        if pet_choise == 2:
                            "Феникс окутал вашего врага пламенем, однако это не спасло его от заклинания."
                            "Огонь птицы потух и она, посеревшая, упала на землю, заснув вечным сном."
                            boss "Можно считать, что из него вышла неплохая жареная курица, ха-ха!"
                            "Вы замечаете, что кости лича оплавились."
                            $boss_health -= 2
                        if pet_choise == 3:
                            "Единорог с разбега вонзает рог в вашего врага, врезаясь вместе с ним в стену."
                            "Однако, темная энергия попадает прямо в [petnam]. Ваш питомец упал на землю и больше не очнется."
                            boss "Не долго прожило мифическое создание."
                            $boss_health -= 2
                        if pet_choise == 4:
                            "Риген прыгает и, кусая врага за шею, продолжает бить его мощными лапами."
                            "Увы, энергия все же срывается с рук поврежденного Повелителя, и ваш питомец уходит в мир иной."
                            boss "Вот и прекрасно. На ужин будет жаркое."
                            $boss_health -= 2
                        jump without_pet

            label prepares:
                "Повелитель Пустоши потирает руки и хохочет, готовясь к следующей атаке."
                menu:
                    "Что же вы предпримите?"
                    "Атаковать":
                        "Вы атаковали монстра"
                        if character_option == 5:
                            "Огонь смог хорошенько поджарить несобранного лича."
                            if boss_health <=0:
                                "Вы жгли вашего врага до тла."
                                jump the_end
                            $monster_health -= 2
                        else:
                            $monster_health -= 1
                        if monster_health <=0:
                            "Лич умер, рассыпавшись прахом."
                            jump the_end
                        jump attack
                    "Защититься":
                        jump attack
                    "Увернуться":
                        jump attack

            label attack:
                "Повелитель направляет в вас волну ужасающей темной энергии."
                menu:
                    "Что же вы сделаете в такой опасной ситуации?"
                    "Атаковать":
                        if character_option == 3:
                            "Атака ветром рассеяла тьму и нанесла урон"
                            $monster_health -= 1
                            if monster_health <=0:
                                "Лич умер, рассыпавшись прахом."
                                jump the_end
                            jump magic_attack
                        "Атака ранила вас"
                        if character_option == 4:
                            "Тьма не сильно вам вредит"
                            $your_health -=1
                            if your_health <=0:
                                "Вы умерли, истлев, словно тысячелетняя мумия."
                                jump death
                            jump prepares_m
                        $your_health -=2
                        if your_health <=0:
                            "Вы умерли, истлев, словно тысячелетняя мумия."
                            jump death
                        jump magic_attack
                    "Защититься":
                        "Атака нанесла небольшой урон"
                        $your_health -=1
                        if your_health <=0:
                            "Вы умерли, истлев, словно тысячелетняя мумия."
                            jump death
                        jump prepares_m
                    "Увернуться":
                        "Вы не смогли увернуться от волны тьмы, она покрыла слишком значительную площадь."
                        $your_health -=2
                        if your_health <=0:
                            "Вы умерли, истлев, словно тысячелетняя мумия."
                            jump death
                        jump magic_attack

            label prepares_m:
                "Повелитель собирается колдовать что-то еще."
                menu:
                    "Что вы сделаете?"
                    "Атаковать":
                        if character_option == 2:
                            "У вас получилось устроить личу нехватку воздуха своим водяным пузырем."
                            $monster_health -= 2
                        else:
                            "У вас вышло застать Повелителя врасплох!"
                            boss "Надоедливый комар."
                            $monster_health -= 1
                        if monster_health <=0:
                            "Лич умер, рассыпавшись прахом."
                            jump the_end
                        jump magic_attack
                    "Защититься":
                        jump attack
                    "Увернуться":
                        jump attack

            label without_pet:
                $dead_pet = True
                boss "Теперь ты остался один, посмотрим, на что ты способен!"
                menu:
                    "Атаковать":
                        "Из-за смерти питомца вы срываетесь в яростную атаку и уничтожаете Повелителя Пустоши."
                    "Защититься":
                        "Не забывая об осторожности, вы защищаетесь."
                        boss "Боишься? И правильно!"
                        "Повелитель швыряет шторм тьмы в ваш щит, однако тот отражается и убивает самого Повелителя Пустоши."
                        jump the_end

            label the_end:
            play sound "audio/victory.mp3" volume 0.1
            "У вас вышло одолеть Повелителя Пустоши."
            hide lich
            $hide_character()
            $in_fight = False
            show catcharpicture at left

            if dead_pet == False:
                $show_pet([truecenter])

            cat "Ура! Победа за нами! И замок теперь наш!"
            cat "Предлагаю выйти и передохнуть."

            scene twilight
            stop music
            play music "audio/goodend.mp3" fadeout 1
            show catcharpicture at left

            if dead_pet == False:
                $show_pet([middle_right])
                pet "Мы выиграли и теперь можем жить свободно и счастливо."

            cat "Итак, мы ведь можем теперь направиться в путешествие? Куда именно?"
            gg "Туда, куда нам укажет солнце."
            "Вы еще долго любовались открывшейся перед вами картиной."
            "Преодолев сложное испытание вы открыли для себя еще более невероятный будущий путь."

    return


    label death:
    scene death_screen
    "*Вы погибли*"
    return
