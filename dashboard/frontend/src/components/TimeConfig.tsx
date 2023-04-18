import { useMemo } from "react";
import { Tap } from "./Tap";

const DAY_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

type HourOption = {
  label: string;
  value: string;
};

const formatTime = (time: string) => {
  const hours = parseInt(time.slice(0, 2));
  const minutes = parseInt(time.slice(2, 4));
  const ampm = hours >= 12 ? 'pm' : 'am';
  const formattedHours = hours % 12 || 12;
  const formattedMinutes = minutes < 10 ? '0' + minutes : minutes;
  return formattedHours + ':' + formattedMinutes + ' ' + ampm;
};

const getHourOptions = (hours: Tap["hours"]): HourOption[] => {
  const options: HourOption[] = [];

  for (let day = 0; day < 7; day++) {
    const dayHours = hours.find((h: any) => h.open.day === day);

    if (dayHours) {
      const { open, close } = dayHours;
      const openTime = open.time ? formatTime(open.time) : '';
      const closeTime = close && close.time ? formatTime(close.time) : '';
      const label = `${DAY_NAMES[day]}: ${openTime} - ${closeTime}`;
      const value = JSON.stringify({ open, close });
      options.push({ label, value });
    }
  }

  return options;
};

const TimeConfig = {
  getHourOptions,
  formatTime,
};

export default TimeConfig;

export type { HourOption };

export { DAY_NAMES };