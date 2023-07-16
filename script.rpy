# The game starts here.

label start:

    "We're going to quickly run an example."
    $ Achievement.add(achievement_name['welcome'])
    "Hey look an achievement."
    "This achievement should now appear in the 'Achievement' screen."
    "It should also be permanent and not disappear even when you exit/restart the game."
    "It should also remain even when you return to the main menu."

    menu try_achievement:
        "Here. Try it out."

        "Grant: Welcome Achievement":
            if achievement.has(achievement_name['welcome'].name):
                "You already have this."
                jump try_achievement
            else:
                $ Achievement.add(achievement_name['welcome'])

        "Grant: Secret Achievement":
            if achievement.has(achievement_name['secret'].name):
                "You already have this."
                jump try_achievement
            else:
                $ Achievement.add(achievement_name['secret'])

        "Clear Achievements":
            $ achievements.purge()
            "Achievements cleared."
            jump try_achievement

        "(Skip)":
            pass

    "Well, that's all."
    "I hope you enjoyed this quick demo."
    "If you have any questions feel free to ask on the forums."
    "Ciao!"

    return
