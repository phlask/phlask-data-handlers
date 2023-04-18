
import { useState, useMemo } from 'react';
import { HourOption } from './TimeConfig';

interface DropdownProps {
  options: HourOption[];
  value: any;
  onChange: (value: any) => void;
}

const Dropdown = ({ options, value, onChange }: DropdownProps) => {
  const [selectValue, setSelectValue] = useState(value);

  const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    setSelectValue(value);
    onChange(JSON.parse(value));
  };

  

  const formattedOptions = useMemo(() => {
    return options.map(({ label, value }) => ({
      label,
      value: JSON.parse(value),
    }));
  }, [options]);

  return (
    <select value={selectValue} onChange={handleSelectChange}>
      <option value="">View Operating Hours...</option>
      {formattedOptions.map(({ label, value }) => (
        <option key={label} value={JSON.stringify(value)}>
          {label}
        </option>
      ))}
    </select>
  );
};

export default Dropdown;
