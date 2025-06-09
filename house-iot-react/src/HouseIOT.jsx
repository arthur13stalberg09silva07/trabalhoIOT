import { useState, useEffect } from 'react';

export default function HouseIOT() {
  const [sensorData, setSensorData] = useState({
    temperatura: 25,
    luminosidade: 300,
    presenca: false,
  });

  const [atuadores, setAtuadores] = useState({
    ar_condicionado: false,
    lampada: false,
    fechadura: true,
  });

  useEffect(() => {
    const intervalo = setInterval(() => {
      const novaTemperatura = Math.floor(Math.random() * (35 - 20 + 1)) + 20;
      const novaLuminosidade = Math.floor(Math.random() * (500 - 100 + 1)) + 100;
      const novaPresenca = Math.random() < 0.5;

      const novosSensores = {
        temperatura: novaTemperatura,
        luminosidade: novaLuminosidade,
        presenca: novaPresenca,
      };

      setSensorData(novosSensores);

      setAtuadores((prev) => ({
        ...prev,
        ar_condicionado: novaTemperatura > 28,
        lampada: novaLuminosidade < 200 || novaPresenca,
      }));
    }, 2000);

    return () => clearInterval(intervalo);
  }, []);

  const alternarFechadura = () => {
    setAtuadores((prev) => ({
      ...prev,
      fechadura: !prev.fechadura,
    }));
  };

  return (
    <div style={{ fontFamily: 'sans-serif', maxWidth: 400, margin: '0 auto' }}>
      <h2>Sensores</h2>
      <p>Temperatura: {sensorData.temperatura} °C</p>
      <p>Luminosidade: {sensorData.luminosidade} lux</p>
      <p>Presença: {sensorData.presenca ? 'Sim' : 'Não'}</p>

      <h2>Atuadores</h2>
      <p>Ar-condicionado: {atuadores.ar_condicionado ? 'Ligado' : 'Desligado'}</p>
      <p>Lâmpada: {atuadores.lampada ? 'Ligada' : 'Desligada'}</p>
      <p>Fechadura: {atuadores.fechadura ? 'Fechada' : 'Aberta'}</p>

      <button onClick={alternarFechadura}>Alternar Fechadura</button>
    </div>
  );
}
