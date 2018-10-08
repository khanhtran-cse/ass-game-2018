from const import *
from team import Team
from flag import Flag
from basetank import BaseTank
from util import *

def main():
    clock = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    background = pygame.image.load('./images/background.jpg')
    background = pygame.transform.scale(background, WINDOW_SIZE)

    # flag
    posFlagEnemy = (40, 60)
    flagEnemy = Flag(posFlagEnemy, True)

    # flag
    posFlagAlly = (WINDOW_WIDTH- 40, WINDOW_HEIGHT-60)
    flagAlly = Flag(posFlagAlly, False)

    # init team , (260, 150), (212, 212), (150, 260), (78,  290)
    posEnemy = [(290, 78), (260, 150), (212, 212), (150, 260), (78,  290)]
    angleEnemy = [255, 240, 225, 210, 195, 180]

    teamEnemyGroup = pygame.sprite.Group()
    Team(teamEnemyGroup,posEnemy, angleEnemy, False, flagEnemy, flagAlly, ENEMY_RANDOM_ATTACK)

    # ally team
    posAlly = [(WINDOW_WIDTH- 290, WINDOW_HEIGHT- 78), (WINDOW_WIDTH- 260, WINDOW_HEIGHT- 150), (WINDOW_WIDTH- 150,  WINDOW_HEIGHT-260), (WINDOW_WIDTH- 78,  WINDOW_HEIGHT- 290)]
    angleAlly = [75, 60, 30, 15]

    teamAllyGroup = pygame.sprite.Group()
    Team(teamAllyGroup, posAlly, angleAlly, True, flagAlly, flagEnemy, ALLY_RANDOM_ATTACK)



    #player 
    playerTank = BaseTank( (WINDOW_WIDTH- 212, WINDOW_HEIGHT- 212), 45, True)
    teamAllyGroup.add(playerTank)

    flagGroup = pygame.sprite.Group()
    flagGroup.add(flagEnemy)
    flagGroup.add(flagAlly)

    bulletGroup = pygame.sprite.Group()
    bulletEnemyGroup = pygame.sprite.Group()
    # all tank to 
    allTankGroup = pygame.sprite.Group()
    allTankGroup.add(teamAllyGroup.sprites())
    allTankGroup.add(teamEnemyGroup.sprites())
    # print(allTankGroup.sprites())
    exit = False
    gameover = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                exit = True

        keystate = pygame.key.get_pressed()
        if gameover == False:
            #handle player 2 input
            if(keystate[pygame.K_w]):
                playerTank.move('head')
            elif(keystate[pygame.K_s]):
                playerTank.move('back')
            elif(keystate[pygame.K_a]):
                playerTank.move('left')
            elif(keystate[pygame.K_d]):
                playerTank.move('right')
            elif(keystate[pygame.K_SPACE]):
                newBullet = playerTank.shot()
                if newBullet:
                    bulletGroup.add(newBullet)

            screen.blit(background, (0,0))

            flagGroup.update()
            flagGroup.draw(screen)
            teamEnemyGroup.update()
            teamEnemyGroup.draw(screen)
            teamAllyGroup.update()
            teamAllyGroup.draw(screen)

            pygame.draw.circle(screen, BLUE, (int(playerTank.position[0]), int(playerTank.position[1])), 5)

            bulletGroup.update()
            bulletGroup.draw(screen)
            # print(bulletGroup.sprites())
            # print(playerTank.rect)
            # print(allTankGroup.rect)
            # factor
            # if 
                # pass  
            for i in allTankGroup.sprites():
                if i in teamAllyGroup:
                    if i != playerTank:
                        i.AI(teamEnemyGroup,bulletGroup, flagEnemy,flagAlly)
                else:
                    i.AI(teamAllyGroup,bulletGroup, flagAlly, flagEnemy)
                    # print("ENEMY: ", state)

            # for i in teamAllyGroup:
            #     print(i.initState)

            for i in allTankGroup.sprites():
                if(collisionTankWithBullets(i,bulletGroup)):
                    #animation fire...
                    i.isShoted(BULLET_DAMAGE)

            for i in flagGroup.sprites():
                if(collisionTankWithBullets(i, bulletGroup)):
                    i.isShoted(BULLET_DAMAGE)

            # for i in allTankGroup.sprites():
            #     tmp = collisionTankWithTank(i, allTankGroup)
            #     if (tmp != None):
            #         tmp.isShoted(TANK_RAM)
            #         i.isShoted(TANK_RAM)
            #         print("hp tank orther ",tmp.hp)
            #         print("hp tank i ",i.hp)
                    #animation
                    

            for i in flagGroup.sprites():
                if i.lose:
                    gameover = True;
        else:
            showEndGame(screen, flagEnemy.lose)
        # screen.blit(playerTank.image, playerTank.position)

        pygame.display.flip()
        clock.tick(FPS)

def showEndGame(screen, enemyLose):

    hintFont = pygame.font.SysFont("helvetica", 30)
    if enemyLose:
        score = hintFont.render('Your Win', True, (244, 66, 66))
    else:
        score = hintFont.render('Game Over', True, (244, 66, 66))
    screen.blit(score, (WINDOW_WIDTH/2-50, WINDOW_HEIGHT/2- 10))

if __name__ == '__main__':
    main()
    