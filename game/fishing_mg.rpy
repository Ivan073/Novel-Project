init 15:
    $cursor_pos = 500
    $fish_pos = renpy.random.randint(300,700)
    $progress = 200
    $fish_speed = renpy.random.random()*1.6-0.8
init -5 python:
    style.ProgressBar = Style(style.default)
    style.ProgressBar.left_bar = Solid("#fc2803")
    style.ProgressBar.xmaximum = 800
    style.ProgressBar.ymaximum = 15

    style.FishingBar = Style(style.default)
    style.FishingBar.left_bar = Solid("#46eb34")
    style.FishingBar.right_bar = Solid("#46eb34")
    style.FishingBar.thumb = "runa.png"
    style.FishingBar.thumb_offset = 25
    style.FishingBar.left_gutter = 25
    style.FishingBar.right_gutter = 25
    style.FishingBar.xmaximum = 800
    style.FishingBar.ymaximum = 50

    style.FishBar = Style(style.default)
    style.FishBar.thumb = HBox(Solid("#fcfc00",xsize=3),Null(width=150),Solid("#fcfc00",xsize=3))
    style.FishBar.thumb_offset = 50
    style.FishBar.xmaximum = 800
    style.FishBar.ymaximum = 50



screen Fishing:
    
    key [ 'K_LEFT', 'repeat_K_LEFT' ] action If(cursor_pos > 0, true=SetVariable("cursor_pos", cursor_pos - 10))
    key [ 'K_RIGHT', 'repeat_K_RIGHT' ] action If(cursor_pos < 1000, true=SetVariable("cursor_pos", cursor_pos + 10))
    key 'K_RETURN' action [Jump("YouWin")]

    bar:
        style "ProgressBar"
        range 1000
        value progress
        align(0.5,0.67)

    bar:
        style "FishingBar"
        range 1000
        value cursor_pos
        align(0.5,0.7)

    bar:
        style "FishBar"
        range 1000
        value fish_pos
        align(0.5,0.7)

    timer 0.02 repeat True action If(fish_pos + fish_speed<930 and fish_pos + fish_speed>70, true=SetVariable("fish_pos", fish_pos + fish_speed))    #положение рыбы меняется
    timer 1 repeat True action SetVariable("fish_speed", renpy.random.random()*12-6) #скорость рыбы меняется
    timer 0.02 repeat True action If(abs(cursor_pos-fish_pos)< 85, true=SetVariable("progress", progress + 1.4), false=SetVariable("progress", progress - 1.2))
    if progress<=0:
        timer 0.01 action Jump("fishing_lose")
    if progress >=1000:
        timer 0.01 action Jump("fishing_win")

label fishing_lose:
    "Вы упустили рыбу. Придется попробовать еще раз"
    $cursor_pos = 500
    $fish_pos = renpy.random.randint(300,700)
    $progress = 200
    $fish_speed = renpy.random.random()*1.6-0.8
    jump fishing

label fishing_win:
    "Вы поймали рыбу"
    jump end_fishing
