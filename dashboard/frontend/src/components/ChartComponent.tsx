import React, { useEffect, useState } from "react";
import Chart, { ChartData, ChartOptions } from "chart.js/auto";
import axios from "axios";
import "./ChartComponent.css";

interface ChartDataResponse {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    fill: boolean;
    backgroundColor: string;
  }[];
}

const ChartComponent: React.FC = () => {
  const [chartData, setChartData] = useState<ChartDataResponse | null>(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/chart-data").then((response) => setChartData(response.data));
  }, []);

  useEffect(() => {
    if (chartData) {
      const ctx = document.getElementById("myChart") as HTMLCanvasElement;
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: chartData.labels,
          datasets: chartData.datasets.map((dataset) => ({
            label: dataset.label,
            data: dataset.data,
            fill: dataset.fill,
            backgroundColor: dataset.backgroundColor,
          })),
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: "Example Chart",
            },
          },
          scales: {
            y: {
              min: 0,
              stacked: false,
            },
          },
          indexAxis: 'x',
          barPercentage: 5.0,
          categoryPercentage: 0.5,
        } as ChartOptions,
      });
    }
  }, [chartData]);

  return (
    <div className="chart-container">
      {chartData ? (
        <canvas id="myChart" width="400" height="400"></canvas>
      ) : (
        <p>Loading chart data...</p>
      )}
    </div>
  );
};

export default ChartComponent;
