import React, { useState, useEffect } from "react";
import Tooltip from "../../components/Tooltip";
import RealtimeChart from "../../charts/RealtimeChart";
import data2 from "../../../../container_stats.json";
// Import utilities
import { tailwindConfig, hexToRGB } from "../../utils/Utils";

function DashboardCard05() {
  // IMPORTANT:
  // Code below is for demo purpose only, and it's not covered by support.
  // If you need to replace dummy data with real data,
  // refer to Chart.js documentation: https://www.chartjs.org/docs/latest

  // Fake real-time data
  const [counter, setCounter] = useState(0);
  const [increment, setIncrement] = useState(0);
  const [range, setRange] = useState(35);

  // Dummy data to be looped
  const data = [
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_1"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_2"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_3"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_4"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_5"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_6"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_7"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_8"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_9"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_10"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_11"]["total_usage"] / 10000000,
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "cpu_stats"
    ]["per_process"]["CPU_12"]["total_usage"] / 10000000,
  ];
  const datamem = [
    data2["ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"][
      "memory_stats"
    ]["total_usage"] / 10000000,
  ];

  const [slicedData, setSlicedData] = useState(data.slice(0, range));

  // Generate fake dates from now to back in time
  const generateDates = () => {
    const now = new Date();
    const dates = [];
    data.forEach((v, i) => {
      dates.push(new Date(now - 2000 - i * 2000));
    });
    return dates;
  };

  const [slicedLabels, setSlicedLabels] = useState(
    generateDates().slice(0, range).reverse()
  );

  // Fake update every 2 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      setCounter(counter + 1);
    }, 2000);
    return () => clearInterval(interval);
  }, [counter]);

  // Loop through data array and update
  useEffect(() => {
    setIncrement(increment + 1);
    if (increment + range < data.length) {
      setSlicedData(([x, ...slicedData]) => [
        ...slicedData,
        data[increment + range],
      ]);
    } else {
      setIncrement(0);
      setRange(0);
    }
    setSlicedLabels(([x, ...slicedLabels]) => [...slicedLabels, new Date()]);
    return () => setIncrement(0);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [counter]);

  const chartData = {
    labels: slicedLabels,
    datasets: [
      // Indigo line
      {
        data: slicedData,
        fill: true,
        backgroundColor: `rgba(${hexToRGB(
          tailwindConfig().theme.colors.blue[500]
        )}, 0.08)`,
        borderColor: tailwindConfig().theme.colors.indigo[500],
        borderWidth: 2,
        tension: 0,
        pointRadius: 0,
        pointHoverRadius: 3,
        pointBackgroundColor: tailwindConfig().theme.colors.indigo[500],
        pointHoverBackgroundColor: tailwindConfig().theme.colors.indigo[500],
        pointBorderWidth: 0,
        pointHoverBorderWidth: 0,
        clip: 20,
      },
    ],
  };

  return (
    <div className="flex flex-col col-span-full sm:col-span-6 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
      <header className="px-5 py-4 border-b border-slate-100 dark:border-slate-700 flex items-center">
        <h2 className="font-semibold text-slate-800 dark:text-slate-100">
          {
            data2[
              "ab8165b5037922caa1193e0a41c4fad9165164d1a65e60a51a476f1f6f5c6185"
            ]["name"]
          }
        </h2>
        <Tooltip className="ml-2">
          <div className="text-xs text-center whitespace-nowrap">
            Built with{" "}
            <a
              className="underline"
              href="https://www.chartjs.org/"
              target="_blank"
              rel="noreferrer"
            >
              Chart.js
            </a>
          </div>
        </Tooltip>
      </header>
      {/* Chart built with Chart.js 3 */}
      {/* Change the height attribute to adjust the chart height */}
      <RealtimeChart data={chartData} width={595} height={248} />
    </div>
  );
}

export default DashboardCard05;
