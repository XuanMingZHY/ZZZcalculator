# import numpy as np
# import random
import psycopg2
import execute_sql
import W_Engine

#设定好的基础攻击力和防御力
BASE_ATK = 2000
BASE_DEF = 1500

#假定抗性穿透值
resPenetration = 0.1

#敌方基础防御力
ENERMY_DEF = 200




def printMenu():
    print("1. ZZZ Expectation Calculator")
    print("2. ZZZ psql -U postgres Calculator")
    choice = str(input("Please make your choice[1/2]: "))
    if choice == "1":
        return Judgement
    elif choice == "2":
        return 0
         




def Judgement(CRIT_RATE:float, CRIT_DMG:float, character_level:int): 
 
#暴击/爆伤区期望值计算
    CRITresult = BASE_ATK * ((1 + CRIT_DMG) * CRIT_RATE + (1-CRIT_RATE))
    
    
# 抗性乘区判断/计算
    isResistance = input("\nWhether the enemy has resistant or vulnerable?\n Please make your choice: [0] for resistant | [1] for vulnerable | [-] for neither\n >>>")
    if isResistance == "0":
        resistance = 0.2
    elif isResistance == "1":
        resistance = -0.2
    else:
        resistance = 0
        
    #我方角色抗性穿透率
    RESpenetration = float(input("\nWhether the enemy has resistance penetration? If so, enter the value. If not, enter 0\n >>>"))
    #我方角色是否含有固定穿透值
    STABLE_RESP = int(input("\nCharacter has stable resistance penetration value? If so, enter the value. If not, enter 0. \n >>>"))
    #计算结果
    RESresult = 1 - resistance + RESpenetration
    
        
# 防御乘区判断/计算
    #受击方（敌人）防御加成/减益
    isDefence = input("\nWhether the enemy has effect of increasing or decreasing DEF?\n Please make your choice: [0] for increase | [1] for decrease | [-] for neither\n >>>")
    if isDefence == "0":
        changableDefence = float(input("Please enter the value of the defence increasing:"))
    elif isDefence == "1":
        changableDefence = float(input("Please enter the value of the defence decreasing:"))
    else:
        changableDefence = 0
    
    #敌人是否含有固定防御力/计算受击方防御
    STABLE_DEF = int(input("\nEnemy has stable defence? If so, enter the value. If not, enter 0. \n >>>"))
    TEMP_DEF = ENERMY_DEF * (1 - changableDefence) + STABLE_DEF
    
    #数据库中获取攻击基数
    attack_base_value = execute_sql.get_attack_base_value(execute_sql.config, character_level)
    print(f"Got it! The base attack value at the level {character_level} is {attack_base_value}!")
    
    #计算受击方有效防御
    validDEF = TEMP_DEF * (1 - RESpenetration) - STABLE_RESP
    
    #防御区计算结果
    DEF = attack_base_value / (attack_base_value + validDEF)
    
        
        
    
    FINALresult = CRITresult * RESresult * DEF
    return FINALresult

        
            
def main():
    while(True):
        character_level = int(input("Please enter the character's level[0~60]: ")) 
        if not isinstance(character_level, (int,float)) or character_level < 0 or character_level > 60:
            print("Error! The level of the agent must be an integer and between 0 and 60!")
        else:
            break
        
    W_Engine.searchEngine()
    execute_sql.get_WEngine_value(execute_sql.config, )
        
    while(True):
        try:          
            CRIT_RATE = float(input("Please enter the Critical Rate of the character: "))
            if CRIT_RATE < 0:
                print("\nError! The CRIT_RATE must be greater than 0!")
            else:
                print(f"\nGot it! Your Critical Rate is {CRIT_RATE * 100}%!")
                break
        except:
            print("\nError! The CRIT_RATE must be a number!")
            
        
    while(True):
        try:          
            CRIT_DMG = float(input("Please enter the Critical Rate of the character: "))
            if CRIT_DMG < 0:
                print("\nError! The CRIT_DMG must be greater than 0!")
            else:
                print(f"\nGot it! Your Critical Damage is {CRIT_DMG * 100}%!")
                break
        except:
            print("\nError! The CRIT_DMG must be a number!")
            
    
            
    
    input("Press ENTER to choose calculators!\n")
    handle = printMenu()
    result = handle(CRIT_RATE, CRIT_DMG, character_level)
    print(f"The variant of your character's damage is {result}.")

    
           
if __name__ == '__main__':
    main()
    