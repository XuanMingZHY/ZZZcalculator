import React, { useState } from 'react';
import axios from 'axios';
import './zzzCalculator.css';

const DamageCalculator = () => {
  const [level, setLevel] = useState('');
  const [critRate, setCritRate] = useState('');
  const [critDmg, setCritDmg] = useState('');
  const [wEngine, setWEngine] = useState('');
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const response = await axios.post('/calculate', { level, critRate, critDmg, wEngine });
      // 处理后端返回的数据
      setResult(response.data)
    } 
    catch (error) {
      console.error('Error:', error);
      if(error.response && error.response.data && error.response.data.error){
        setError(error.response.data.error);
      }
      else{
        setError('出错啦，请重试！Error! Please try again!');
      }
    }
    finally{
      setLoading(false);
    }
  
  };

  return (
    <div className="damage-calculator">
      <div className="calculator-container">
        <h2>欢迎来到绝区零伤害计算器</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="level">等级:</label>
            <input type="number" id="level" value={level} onChange={(e) => setLevel(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="critRate">暴击率 (CRIT_RATE):</label>
            <input type="number" id="critRate" step="0.01" value={critRate} onChange={(e) => setCritRate(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="critDmg">暴击伤害 (CRIT_DMG):</label>
            <input type="number" id="critDmg" step="0.01" value={critDmg} onChange={(e) => setCritDmg(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="wEngine">音擎:</label>
            <select id="wEngine" value={wEngine} onChange={(e) => setWEngine(e.target.value)} required>
              <option value="">选择音擎</option>
              <option value="deepSeaVisitor">深海访客 (Ellen 艾莲)</option>
              <option value="steelCushion">钢铁肉垫 (Nekomiya Mana 猫宫又奈)</option>
              <option value="brimstone">硫磺石 (Soldier 11 11号)</option>
              <option value="starlightEngine">星徽引擎 (Billy 比利)</option>
              <option value="starlightEngineReplica">仿制星徽引擎 (Billy 比利)</option>
              <option value="housekeeper">家政员 (Corin 可琳)</option>
              <option value="drillRigRedAxis">旋钻机-赤轴 (Anton 安东)</option>
              <option value="kaboonTheCanoon">加农转子</option>
            </select>
          </div>
          <div style={{ textAlign: 'center' }}>
            <button type="submit" className="calculate-button">计算伤害</button>
          </div>
          <div className='form-group'>
            <lable htmlFor="result">计算结果：</lable>
            <input type="number" id="result" step="0.01" value={result} onChange={(e) => setResult(e.target.value)} required />
          </div>
        </form>
      </div>
    </div>
  );
};

export default DamageCalculator;
