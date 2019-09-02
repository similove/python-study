if __name__ == '__main__':
    print('-' * 20, '欢迎光临<孙悟空大战白骨精>', '-' * 20)
    print('请选择您的身份:')
    print('\t1. 孙悟空')
    print('\t2. 白骨精')
    player_role = input('请选择:[1-2]: ')
    print('-' * 66)
    if player_role == '1':
        print('您选择了1, 您将以孙悟空的角色进行游戏!')
    elif player_role == '2':
        print('你太不要脸了, 居然选择白骨精, 系统将默认分配孙悟空角色!')
    else:
        print('您的输入有误, 系统默认为您分配了孙悟空角色!')

    boss_life = 12
    player_life = 2
    player_attack = 2
    boss_attack = 6
    while True:
        print('-' * 66)
        print('请选择您的技能: ')
        print('\t1. 练级')
        print('\t2. 打BOSS')
        print('\t3. 逃跑')
        game_choose = input('请选择[1-3]: ')
        print('-' * 66)
        if game_choose == '1':
            player_life += 2
            player_attack += 2
            print(f"恭喜您升级了, 现在的生命值为{player_life}, 攻击力为{player_attack}")
        elif game_choose == '2':
            boss_life -= player_attack
            if boss_life <= 0:
                print(f'->白骨精<-受到了{player_attack}点伤害, 重伤不治死了, ->孙悟空<-获胜')
                break
            else:
                print(f"现在的生命值为{player_life}, 攻击力为{player_attack}")
            player_life -= boss_attack
            print('->白骨精<-反击了->孙悟空<-')
            if player_life <= 0:
                print(f'您受到了{boss_attack}点伤害, 重伤不治死亡! GAME OVER')
                break
            else:
                print(f"现在的生命值为{player_life}, 攻击力为{player_attack}")
        elif game_choose == '3':
            print('->孙悟空<-扭头就跑, GAME OVER')
            break
        else:

            print('您的输入有误!')
