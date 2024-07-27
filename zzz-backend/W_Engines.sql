CREATE DATABASE "W_Engines";


CREATE TABLE WEngine_status (
    id SERIAL PRIMARY KEY,
    WEngineName VARCHAR(50) NOT NULL,
    ATTACK INT NOT NULL CHECK (ATTACK >= 0),
    CRIT_RATE FLOAT NOT NULL CHECK (CRIT_RATE >= 0),
    CRIT_DMG FLOAT NOT NULL CHECK (CRIT_DMG >= 0),
    ATTACK_PERCENT FLOAT NOT NULL CHECK (ATTACK_PERCENT >= 0),
    Impact FLOAT NOT NULL CHECK (Impact >= 0),
    AttributeDamageBonus FLOAT NOT NULL CHECK (AttributeDamageBonus >= 0),
    DamageBonus FLOAT NOT NULL CHECK (DamageBonus >= 0)
);

-- 插入数据
INSERT INTO WEngine_status (WEngineName, ATTACK, CRIT_RATE, CRIT_DMG, ATTACK_PERCENT, Impact, AttributeDamageBonus, DamageBonus) VALUES

-- Attack 强攻
-- Deep Sea Visitor 深海访客(Ellen 艾莲)
('DeepSeaVisitor', 713, 0.44, 0, 0, 0, 0.25, 0),

-- Steel Cushion 钢铁肉垫（Nekomiya Mana 猫宫又奈）
('SteelCushion', 684, 0.24, 0, 0, 0, 0.2, 0.25),

-- The Brimstone 硫磺石（Soldier 11 11号）
('TheBrimstone', 684, 0, 0, 0.46, 0, 0.2, 0),

-- Starlight Engine 星徽引擎（Billy 比利）
('StarlightEngine', 594, 0, 0, 0.41, 0, 0, 0),

-- Starlight Engine Replice 仿制星徽引擎（Billy 比利）
('StarlightEngineReplice', 594, 0, 0, 0.41, 0, 0, 0),

-- Housekeeper 家政员（Corin 可琳）
('Housekeeper', 624, 0, 0.4, 0, 0, 0.45, 0),

-- Drill Rig - Red Axis 旋钻机-赤轴（Anton 安东）
('DrillRigRedAxis', 624, 0, 0.4, 0, 0, 0.5, 0),

-- Kaboon the Canoon 加农转子
('KaboontheCanoon', 594, 0.2, 0, 0.075, 0, 0, 0);