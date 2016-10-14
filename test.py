
import game
import buzzwords


def main():
    G = game.Game()
    B = G.generate()

    print("Here!\n")
    B.draw()
    for w in buzzwords.buzzwords:
        print "Claiming", w
        B.claim(w)
        B.draw()
        if B.winner():
            break
main()
