from const import *
from team import Team
from flag import Flag
from basetank import BaseTank
from util import *
from Explosion import Explosion
from health import Health
import time

def getSpriteByPosition(position,group):
    for index,spr in enumerate(group):
        if (index == position):
            return spr
    return False

def deactiveGroup(group):
    for index,spr in enumerate(group):
        spr.setActive(False)

def main():
    clock = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    background = pygame.image.load('./data/background.png')
    background = pygame.transform.scale(background, WINDOW_SIZE)

    #sound
    if pygame.mixer:
        # music = os.path.join(Util.main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load('./data/house_lo.wav')
        pygame.mixer.music.play(-1)


    exit = False
    while not exit:
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
        posAlly = [(WINDOW_WIDTH- 290, WINDOW_HEIGHT- 78), (WINDOW_WIDTH- 260, WINDOW_HEIGHT- 150),(WINDOW_WIDTH- 212, WINDOW_HEIGHT- 212), (WINDOW_WIDTH- 150,  WINDOW_HEIGHT-260), (WINDOW_WIDTH- 78,  WINDOW_HEIGHT- 290)]
        angleAlly = [75, 60,45, 30, 15]

        teamAllyGroup = pygame.sprite.Group()
        Team(teamAllyGroup, posAlly, angleAlly, True, flagAlly, flagEnemy, ALLY_RANDOM_ATTACK)

        #load explosion image
        img = pygame.image.load('./data/explosion1.gif')
        Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
        explosionGroup = pygame.sprite.Group()
        Explosion.containers = explosionGroup

        Health.screen = screen

        #player 
        playerControlGroup = pygame.sprite.Group()
        playerControlGroup.add(teamAllyGroup.sprites()[2])

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
        gameover = False
        # activeALock = 0
        # activeBLock = 0
        # activeAIndex = 0
        
        playAgain=False
        countDown = 6000 # ms

        while not (playAgain or exit):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    exit = True
            keystate = pygame.key.get_pressed()
            if gameover == False:

                #handle player 2 input
                if(keystate[pygame.K_w]):
                    for i in playerControlGroup:
                        i.move('head')
                if(keystate[pygame.K_s]):
                    for i in playerControlGroup:
                        i.move('back')
                if(keystate[pygame.K_a]):
                    for i in playerControlGroup:
                        i.move('left')
                if(keystate[pygame.K_d]):
                    for i in playerControlGroup:
                        i.move('right')
                if(keystate[pygame.K_SPACE]):
                    for i in playerControlGroup:
                        newBullet = i.shot()
                        if newBullet:
                            bulletGroup.add(newBullet)

                if(keystate[pygame.K_1]):
                    allySprites = teamAllyGroup.sprites()
                    if allySprites[0] in playerControlGroup:
                        playerControlGroup.remove(allySprites[0])
                        print('remove')
                    else:
                        playerControlGroup.add(allySprites[0])
                        print('add')
                elif(keystate[pygame.K_2] and len(teamAllyGroup)> 1):
                    allySprites = teamAllyGroup.sprites()
                    if allySprites[1] in playerControlGroup:
                        playerControlGroup.remove(allySprites[1])
                    else:
                        playerControlGroup.add(allySprites[1])
                elif(keystate[pygame.K_3] and len(teamAllyGroup)> 2):
                    allySprites = teamAllyGroup.sprites()
                    if allySprites[2] in playerControlGroup:
                        playerControlGroup.remove(allySprites[2])
                    else:
                        playerControlGroup.add(allySprites[2])
                elif(keystate[pygame.K_4] and len(teamAllyGroup)> 3):
                    allySprites = teamAllyGroup.sprites()
                    if allySprites[3] in playerControlGroup:
                        playerControlGroup.remove(allySprites[3])
                    else:
                        playerControlGroup.add(allySprites[3])
                elif(keystate[pygame.K_5] and len(teamAllyGroup)> 4):
                    allySprites = teamAllyGroup.sprites()
                    if allySprites[4] in playerControlGroup:
                        playerControlGroup.remove(allySprites[4])
                    else:
                        playerControlGroup.add(allySprites[4])
                screen.blit(background, (0,0))

                # count 5->0 to begin playe
                if countDown >= 0:
                    hintFont = pygame.font.SysFont("helvetica", 50)

                    score = hintFont.render(str(countDown//1000), True, (244, 66, 66))
                    screen.blit(score, (WINDOW_WIDTH/2-50, WINDOW_HEIGHT/2- 10))
                    countDown = 6000 - pygame.time.get_ticks()
                else:

                    # currentTime = time.time()
                    # if(keystate[K_PERIOD] and currentTime > activeALock):
                    #     #change active of A
                    #     activeALock = currentTime + LOCK_TIME

                    #     activeAIndex += 1
                    #     deactiveGroup(teamAllyGroup)
                    #     if(activeAIndex >= len(teamAllyGroup)):
                    #         activeAIndex = 0

                    #     if(len(teamAllyGroup) > 0):
                    #         playerTank = getSpriteByPosition(activeAIndex,teamAllyGroup)
                    #         playerTank.setActive(True)



                    # print(bulletGroup.sprites())
                    # print(playerTank.rect)
                    # print(allTankGroup.rect)
                    # factor
                    # if 
                        # pass  
                    for i in allTankGroup.sprites():
                        if i in teamAllyGroup:
                            if i not in playerControlGroup:
                                i.AI(teamEnemyGroup,bulletGroup, flagEnemy,flagAlly)
                        else:
                            i.AI(teamAllyGroup,bulletGroup, flagAlly, flagEnemy)

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
                        
                    if not teamEnemyGroup:
                        gameover = 'win'
                    elif not teamAllyGroup:
                        gameover = 'lose'

                    for i in flagGroup.sprites():
                        if i.lose:
                            if i == flagEnemy:
                                gameover = 'win'
                            else:
                                gameover = 'lose'

                flagGroup.update()
                flagGroup.draw(screen)
                teamEnemyGroup.update()
                teamEnemyGroup.draw(screen)
                teamAllyGroup.update()
                teamAllyGroup.draw(screen)
                explosionGroup.update()
                explosionGroup.draw(screen)

                for i in playerControlGroup:
                    pygame.draw.circle(screen, BLUE, (int(i.position[0]), int(i.position[1])), 5)

                bulletGroup.update()
                bulletGroup.draw(screen)
            else:
                showEndGame(screen, gameover)
                if(keystate[pygame.K_SPACE]):
                    playAgain = True
            # screen.blit(playerTank.image, playerTank.position)
            pygame.display.flip()
            clock.tick(FPS)
        print(exit)

def showEndGame(screen, state):
    hintFont = pygame.font.SysFont("helvetica", 30)

    if state =='win':
        score = hintFont.render('Your Win', True, (244, 66, 66))
    elif state == 'lose':
        score = hintFont.render('Your lose', True, (244, 66, 66))
    screen.blit(score, (WINDOW_WIDTH/2-50, WINDOW_HEIGHT/2- 10))

if __name__ == '__main__':
    main()
    