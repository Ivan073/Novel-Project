screen CardScreen:
    grid 4 4:
        align (.5, .5)
        spacing 20
        for card in card_list:
            button:
                xsize 180
                ysize 240
                if card ["value"] != 'empty':
                    if card ["chosen"]:
                        if card ["value"] == 'R' or card ["value"] == 'WR':
                            background '#ff0000'
                        if card ["value"] == 'G' or card ["value"] == 'WG':
                            background '#1aff00'
                        if card ["value"] == 'B' or card ["value"] == 'WB':
                            background '#0f07eb'
                        if card ["value"] == 'Y' or card ["value"] == 'WY':
                            background '#ffff00'
                        if card ["value"] == 'C' or card ["value"] == 'WC':
                            background '#03fcca'
                        if card ["value"] == 'P' or card ["value"] == 'WP':
                            background '#b503fc'
                    else:
                        background '#fac984'
                action If ((not card ["chosen"] and can_click), [SetDict (card, "chosen", True), Return (card)] ) #нажатие на карту
    text str (turns) xalign 1.0 yalign 0.0 size 48


label CardGame:
    python:
        turns=15
        open_cards = []
        can_click = True
        card_values = ['R','R','G','G','Y','Y','B','B','C','C','P','P','W','W','W']
        cards_left = 15
        card_list = []
        renpy.random.shuffle (card_values)
        card_values.append('empty')
        for i in range (0, len (card_values)):
            if card_values [i] == 'empty':
                card_list.append ({"value": card_values[i], "chosen": True})
            else:
                card_list.append ({"value": card_values[i], "chosen": False})

    show screen CardScreen
   
    label .game_cycle:
        $can_click = True
        if len(open_cards) <2:
            $card = ui.interact()
            if card["value"] == 'W':
                $rand = renpy.random.randint(1,6)
                if rand == 1:
                    $card["value"] = 'WR'
                if rand == 2:
                    $card["value"] = 'WG'
                if rand == 3:
                    $card["value"] = 'WY'
                if rand == 4:
                    $card["value"] = 'WB'
                if rand == 5:
                    $card["value"] = 'WC'
                if rand == 6:
                    $card["value"] = 'WP'
            $open_cards.append(card)
            jump .game_cycle
        $can_click = False
        $turns-=1
        $renpy.pause (0.3, hard = True)
        if len(open_cards) == 2:
            python:
                if open_cards [0] ["value"] == 'WR' or open_cards [0] ["value"] == 'WG' or open_cards [0] ["value"] == 'WY' or open_cards [0] ["value"] == 'WB' or open_cards [0] ["value"] == 'WC' or open_cards [0] ["value"] == 'WP':
                    open_cards [0] ["value"] = 'W'
                if open_cards [1] ["value"] == 'WR' or open_cards [1] ["value"] == 'WG' or open_cards [1] ["value"] == 'WY' or open_cards [1] ["value"] == 'WB' or open_cards [1] ["value"] == 'WC' or open_cards [1] ["value"] == 'WP':
                    open_cards [1] ["value"] = 'W'
                if open_cards [0] ["value"] == open_cards [1] ["value"] and open_cards [0] ["value"] != 'W':
                    open_cards [0] ["value"] = 'empty'
                    open_cards [1] ["value"] = 'empty'
                    cards_left-=2
                open_cards [0] ["chosen"] = False
                open_cards [1] ["chosen"] = False
                open_cards.clear()
        if cards_left == 3:
            jump .win
        if turns == 0:
            jump .lose
        jump .game_cycle


    label .win:
        hide screen CardScreen
        return
    
    label .lose:
        window show
        "Вы проиграли. Попробуйте еще раз"
        jump card_game
        return