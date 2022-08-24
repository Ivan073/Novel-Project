init 15:
    $cursor_pos = 100
    $fish_pos = renpy.random.randint(50,150)
init -5 python:
    style.FishingBar = Style(style.default)
    style.FishingBar.left_bar = Solid("#46eb34")
    style.FishingBar.right_bar = Solid("#46eb34")
    style.FishingBar.thumb = "runa.png"
    style.FishingBar.thumb_offset = 25
    style.FishingBar.left_gutter = 25
    style.FishingBar.right_gutter = 25
    style.FishingBar.xmaximum = 700
    style.FishingBar.ymaximum = 40

    style.FishBar = Style(style.default)
    style.FishBar.thumb = Solid("#fcfc00")      #деление пекрывает курсор
    #style.FishBar.thumb = HBox(Solid("#fcfc00"),Solid("#fff"),Solid("#fcfc00"))
    style.FishBar.thumb_offset = 50
    style.FishBar.xmaximum = 700
    style.FishBar.ymaximum = 40



screen MiniGameFish:
    
    #значения могут уходить за пределы шкалы
    key [ 'K_LEFT', 'repeat_K_LEFT' ] action [SetVariable("cursor_pos", cursor_pos - 2)]
    key [ 'K_RIGHT', 'repeat_K_RIGHT' ] action [SetVariable("cursor_pos", cursor_pos + 2)]
    key 'K_RETURN' action [Jump("YouWin")]

    bar:
        style "FishingBar"
        range 200
        value cursor_pos
        align(0.5,0.7)

    bar:
        style "FishBar"
        range 200
        value fish_pos
        align(0.5,0.7)

screen Fish_Up:
    timer 0.02 repeat True action SetVariable("fish_pos", fish_pos + renpy.random.randint(-1,1))    #курсор просто хаотично изменяется, а не движется


label YouLose:
    "Lose"
    jump end_fishing

label YouWin:
    "Win"
    jump end_fishing
