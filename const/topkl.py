import json
import pickle as pkl

# 基础变量
with open("../default/game-values.json",mode="r",encoding="utf-8") as f:
    data = json.load(f)

res = {}
for i in data:
    if data[i].get("desc",0):
        res[i] = data[i]["desc"]
    else:
        res[i] = "-"
with open("game-values.pkl",mode="wb") as f:
    pkl.dump(res,f)

# towerNameZh
towerNameZh = [
                "基础塔",
                "狙击塔",
                "加农炮",
                "寒冰塔",
                "防空塔",
                "溅射塔",
                "爆破塔",
                "散射塔",
                "机枪塔",
                "毒液塔",
                "特斯拉",
                "导弹",
                "火焰塔",
                "激光塔",
                "电磁炮",
                "破碎机",
            ]
with open("towerNameZh.pkl",mode="wb") as f:
    pkl.dump(towerNameZh,f)

# AbilityNameZh
AbilityNameZh = [
                "火球",
                "暴风雪",
                "火焰风暴",
                "雷",
                "烟雾弹",
                "风暴",
                "磁铁",
                "子弹墙",
                "球状闪电",
                "LOIC",
                "核武器",
                "超载",
            ]
with open("AbilityNameZh.pkl",mode="wb") as f:
    pkl.dump(AbilityNameZh,f)

selectKeywordDict = {
            "基础塔": "BASIC",
            "狙击塔": "SNIPER",
            "加农炮": "CANNON",
            "寒冰塔": "FREEZING",
            "防空塔": "AIR",
            "溅射塔": "SPLASH",
            "爆破塔": "BLAST",
            "散射塔": "MULTISHOT",
            "机枪塔": "MINIGUN",
            "毒液塔": "VENOM",
            "特斯拉": "TESLA",
            "导弹": "MISSILE",
            "火焰塔": "FLAME",
            "激光塔": "LASER",
            "电磁炮": "GAUSS",
            "破碎机": "CRUSHER",
            "火球": "ABILITY_FIREBALL",
            "暴风雪": "ABILITY_BLIZZARD",
            "火焰风暴": "ABILITY_FIRESTORM",
            "雷": "ABILITY_THUNDER",
            "烟雾弹": "ABILITY_SMOKE",
            "风暴": "ABILITY_WINDSTORM",
            "磁铁": "ABILITY_MAGNET",
            "子弹墙": "ABILITY_BULLET_WALL",
            "球状闪电": "ABILITY_BALL_LIGHTNING",
            "LOIC": "ABILITY_LOIC",
            "核武器": "ABILITY_NUKE",
            "超载": "ABILITY_OVERLOAD",
            "矿机": "MINER",
            "积分": "SCORE",
        }
with open("selectKeywordDict.pkl",mode="wb") as f:
    pkl.dump(selectKeywordDict,f)

attributesZh = {
            'prices': '价格',
            'RANGE': '射程',
            'DAMAGE': '伤害',
            'ATTACK_SPEED': '攻击速度',
            'ROTATION_SPEED': '旋转速度',
            'PROJECTILE_SPEED': '子弹速度',
            'U_BURN_CHANCE': '燃烧机率',
            'U_BURNING_TIME': '燃烧时间',
            'U_DAMAGE_MULTIPLY': '伤害加成',
            'STUN_CHANCE': '眩晕机率',
            'U_STUN_DURATION': '眩晕时间',
            'U_EXPLOSION_RANGE': '爆炸范围',
            'FREEZE_PERCENT': '冰冻机率',
            'FREEZE_SPEED': '冰冻速度',
            'U_POISON_DURATION_BONUS': '中毒时间',
            'U_CHAIN_LIGHTNING_BONUS_LENGTH': '链电长度',
            'U_BATTERIES_CAPACITY': '电池容量',
            'U_ACCELERATION': '加速度',
            'U_PROJECTILE_COUNT': '子弹数量',
            'U_SHOOT_ANGLE': '射击角度',
            'AIM_SPEED': '瞄准速度',
            'U_CRIT_CHANCE': '暴击机率',
            'U_CRIT_MULTIPLIER': '暴击加成',
            'ACCURACY': '精准度',
            'CHAIN_LIGHTNING_DAMAGE': '链电伤害',
            'U_CHAIN_LIGHTNING_LENGTH': '链电长度',
            'U_POISON_DURATION': '中毒时间',
            'RESOURCE_CONSUMPTION': '资源消耗',
            'CHARGING_SPEED': '充能速度',
            'DURATION': '持续时间',
            'U_BONUS_EXPERIENCE': '经验加成',
            'U_LRM_AIM_SPEED': '瞄准速度',
        }
with open("attributesZh.pkl",mode="wb") as f:
    pkl.dump(attributesZh,f)

attributesEn = {
            "价格": "prices",
            "射程": "RANGE",
            "伤害": "DAMAGE",
            "攻击速度": "ATTACK_SPEED",
            "旋转速度": "ROTATION_SPEED",
            "子弹速度": "PROJECTILE_SPEED",
            "燃烧机率": "U_BURN_CHANCE",
            "燃烧时间": "U_BURNING_TIME",
            "伤害加成": "U_DAMAGE_MULTIPLY",
            "眩晕机率": "STUN_CHANCE",
            "眩晕时间": "U_STUN_DURATION",
            "爆炸范围": "U_EXPLOSION_RANGE",
            "冰冻机率": "FREEZE_PERCENT",
            "冰冻速度": "FREEZE_SPEED",
            "中毒时间": "U_POISON_DURATION_BONUS",
            "链电长度": "U_CHAIN_LIGHTNING_BONUS_LENGTH",
            "电池容量": "U_BATTERIES_CAPACITY",
            "加速度": "U_ACCELERATION",
            "子弹数量": "U_PROJECTILE_COUNT",
            "射击角度": "U_SHOOT_ANGLE",
            "瞄准速度": "AIM_SPEED",
            "暴击机率": "U_CRIT_CHANCE",
            "暴击加成": "U_CRIT_MULTIPLIER",
            "精准度": "ACCURACY",
            "链电伤害": "CHAIN_LIGHTNING_DAMAGE",
            "链电长度": "U_CHAIN_LIGHTNING_LENGTH",
            "中毒时间": "U_POISON_DURATION",
            "资源消耗": "RESOURCE_CONSUMPTION",
            "充能速度": "CHARGING_SPEED",
            "持续时间": "DURATION",
            "经验加成": "U_BONUS_EXPERIENCE",
            "瞄准速度": "U_LRM_AIM_SPEED",
        }
with open("attributesEn.pkl",mode="wb") as f:
    pkl.dump(attributesEn,f)
