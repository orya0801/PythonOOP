from overall_task.Desepticon import Desepticon
from overall_task.Autobot import Autobot
from overall_task.Gun import Gun
from overall_task.Game import Game


def main():
    desepticon = Desepticon(0, 0, Gun(), Gun())
    autobot = Autobot(100, 70, Gun(), Gun())

    game = Game(autobot, desepticon)

    game.start()


if __name__ == "__main__":
    main()



