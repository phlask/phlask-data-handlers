import React, { useState, useEffect } from "react";
import TimeConfig from "./TimeConfig";
import { Tap } from "./Tap";
import { DAY_NAMES } from "./TimeConfig";
import './TapForm.css';


const { getHourOptions, formatTime } = TimeConfig;


export interface TapFormProps {
  onSubmit: (data: Tap) => Promise<void>;
  editingTap?: Tap;
  toggleTapForm?: () => void;
  tap?: Tap;
}

const TapForm: React.FC<TapFormProps> = ({ onSubmit, editingTap }) => {
  const [formData, setFormData] = useState<Tap>(() => {
    if (editingTap) {
      // console.log(Object.values(editingTap));
      return editingTap;
    } else {
      return {
        access: "",
        address: "",
        city: "",
        description: "",
        filtration: "",
        gp_id: "",
        handicap: "",
        hours: [
          { open: { day: 0, time: "" }, close: { day: 0, time: "" } },
          { open: { day: 1, time: "" }, close: { day: 1, time: "" } },
          { open: { day: 2, time: "" }, close: { day: 2, time: "" } },
          { open: { day: 3, time: "" }, close: { day: 3, time: "" } },
          { open: { day: 4, time: "" }, close: { day: 4, time: "" } },
          { open: { day: 5, time: "" }, close: { day: 5, time: "" } },
          { open: { day: 6, time: "" }, close: { day: 6, time: "" } },
        ],
        lat: 0,
        lon: 0,
        norms_rules: "",
        organization: "",
        permanently_closed: false,
        phone: "",
        quality: "",
        service: "",
        statement: "",
        status: "",
        tap_type: "",
        tapnum: 0,
        vessel: "",
        zip_code: "",
      };
    }
  });

  const [showHoursForm, setShowHoursForm] = useState(false);
  const [startTime, setStartTime] = useState(0);
  const [endTime, setEndTime] = useState(23);


  useEffect(() => {
    if (editingTap) {
      setFormData(editingTap);
    }
  }, [editingTap]);

  const handleHourChange = (value: any) => {
    const { open, close } = JSON.parse(value);
    console.log(open, close);
  };
  
  

  const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const target = event.target as HTMLInputElement;
    const { name, value, type, checked } = target;
    setFormData({ ...formData, [name]: type === "checkbox" ? checked : value });
  };
  

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    onSubmit(formData);
    if (!editingTap) {
      setFormData({
        access: "",
        address: "",
        city: "",
        description: "",
        filtration: "",
        gp_id: "",
        handicap: "",
        hours: [
          { open: { day: 0, time: "" }, close: { day: 0, time: "" } },
          { open: { day: 1, time: "" }, close: { day: 1, time: "" } },
          { open: { day: 2, time: "" }, close: { day: 2, time: "" } },
          { open: { day: 3, time: "" }, close: { day: 3, time: "" } },
          { open: { day: 4, time: "" }, close: { day: 4, time: "" } },
          { open: { day: 5, time: "" }, close: { day: 5, time: "" } },
          { open: { day: 6, time: "" }, close: { day: 6, time: "" } },
        ],
        lat: 0,
        lon: 0,
        norms_rules: "",
        organization: "",
        permanently_closed: false,
        phone: "",
        quality: "",
        service: "",
        statement: "",
        status: "",
        tap_type: "",
        tapnum: 0,
        vessel: "",
        zip_code: "",
      });
    }
  };

  const handleHoursFormSubmit = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.preventDefault();
    const updatedHours = [
      { open: { day: 0, time: "" }, close: { day: 0, time: "" } },
      { open: { day: 1, time: "" }, close: { day: 1, time: "" } },
      { open: { day: 2, time: "" }, close: { day: 2, time: "" } },
      { open: { day: 3, time: "" }, close: { day: 3, time: "" } },
      { open: { day: 4, time: "" }, close: { day: 4, time: "" } },
      { open: { day: 5, time: "" }, close: { day: 5, time: "" } },
      { open: { day: 6, time: "" }, close: { day: 6, time: "" } },
    ];
    const form = e.currentTarget;
    for (let i: number =0 ; i < 7; i++) {
      console.log(`[name="day-${i}"]`);
      const checkbox = (form.querySelector(`[name="day-${i}"]`) as HTMLInputElement);
      
      console.log(checkbox);
      // const checkbox = form.elements[`day-${i}`] as HTMLInputElement;
      // const startTime = (form.querySelector(`[name="start-time-${i}"]`) as HTMLInputElement)?.value;
      // const endTime = (form.querySelector(`[name="end-time-${i}"]`) as HTMLInputElement)?.value;
      if (checkbox.checked) {
        const startFormatted = formatTime(`${startTime}:00`);
        const endFormatted = formatTime(`${endTime}:00`);
        updatedHours[i] = {
          open: { day: i, time: startFormatted },
          close: { day: i, time: endFormatted },
        };
      }
    }
    setFormData({ ...formData, hours: updatedHours });
    setShowHoursForm(false);
  };
  
  
  return (
    <form onSubmit={handleSubmit}>
      {/* Add all the fields from the Tap object */}
      <label>
        Access:
        <input name="access" value={formData.access} onChange={handleChange} required />
      </label>
      <label>
        Address:
        <input name="address" value={formData.address} onChange={handleChange} required />
      </label>
      <label>
        City:
        <input name="city" value={formData.city} onChange={handleChange} required />
      </label>
      <label>
        Description:
        <input name="description" value={formData.description} onChange={handleChange} required />
      </label>
      <label>
        Filtration:
        <input name="filtration" value={formData.filtration} onChange={handleChange} required />
      </label>
      <label>
        GP ID:
        <input name="gp_id" value={formData.gp_id} onChange={handleChange} required />
      </label>
      <label>
        Handicap:
        <input name="handicap" value={formData.handicap} onChange={handleChange} required />
      </label>
      <label>
        Hours:
        <button type="button" onClick={() => setShowHoursForm(true)}>Edit Hours</button>
      </label>
      <div>
        <select name="hours" onChange={handleHourChange}>
          {formData.hours.map((day, index) => {
            const dayHours = day.open.day === index ? `${formatTime(day.open.time)} - ${formatTime(day.close.time)}` : 'Closed';
            const dayName = DAY_NAMES[index];
            return (
              <option value={dayHours} key={index}>
                {`${dayName}: ${dayHours}`}
              </option>
            );
          })}
        </select>
        {showHoursForm && (
          <div>
            {formData.hours.map((day, index) => {
              const checkboxId = `day-${index}`;
              const startId = `start-time-${index}`;
              const endId = `end-time-${index}`;
              return (
                <div key={index}>
                  <label>
                    {DAY_NAMES[index]}
                    <input
                      type="checkbox"
                      name={`day-${index}`}
                      id={`day-${index}`}
                      checked={day.open.day === index}
                      onChange={() => {
                        const updatedHours = [...formData.hours];
                        const newDay = {
                          ...day,
                          open: { ...day.open, day: index },
                          close: { ...day.close, day: index },
                        };
                        updatedHours[index] = newDay;
                        setFormData({ ...formData, hours: updatedHours });
                      }}
                    />

                  </label>
                  {day.open.day === index && (
                    <>
                      <label htmlFor={startId}>Start Time:</label>
                      <input
                        type="range"
                        name={startId}
                        id={startId}
                        min={0}
                        max={23}
                        onChange={(e) => setStartTime(parseInt(e.target.value))}
                      />
                      <output htmlFor={startId}>{`${startTime}:00`}</output>
                      <br />
                      <label htmlFor={endId}>End Time:</label>
                      <input
                        type="range"
                        name={endId}
                        id={endId}
                        min={0}
                        max={23}
                        onChange={(e) => setEndTime(parseInt(e.target.value))}
                      />
                      <output htmlFor={endId}>{`${endTime}:00`}</output>
                    </>
                  )}
                </div>
              );
            })}
            <button type="button" onClick={handleHoursFormSubmit}>Save</button>
          </div>
        )}
      </div>


      <label>
        Lat:
        <input name="lat" value={formData.lat} onChange={handleChange} required />
      </label>
      <label>
        Lon:
        <input name="lon" value={formData.lon} onChange={handleChange} required />
      </label>
      <label>
        Norms Rules:
        <input name="norms_rules" value={formData.norms_rules} onChange={handleChange} required />
      </label>
      <label>
        Organization:
        <input name="organization" value={formData.organization} onChange={handleChange} required />
      </label>
      <label>
        Permanently Closed:
      <input
        type="checkbox"
        name="permanently_closed"
        checked={formData.permanently_closed}
        onChange={handleChange}
        // required
      />
      </label>
      <label>
        Phone:
        <input name="phone" value={formData.phone} onChange={handleChange} required />
      </label>
      <label>
        Quality:
        <input name="quality" value={formData.quality} onChange={handleChange} required />
      </label>
      <label>
        Service:
        <input name="service" value={formData.service} onChange={handleChange} required />
      </label>
      <label>
        Statement:
        <input name="statement" value={formData.statement} onChange={handleChange} required />
      </label>
      <label>
        Status:
        <input name="status" value={formData.status} onChange={handleChange} required />
      </label>
      <label>
        Tap Type:
        <input name="tap_type" value={formData.tap_type} onChange={handleChange} required />
      </label>
      <label>
        Tapnum:
        <input name="tapnum" value={formData.tapnum} onChange={handleChange} required />
      </label>
      <label>
        Vessel:
        <input name="vessel" value={formData.vessel} onChange={handleChange} required />
      </label>
      <label>
        Zip Code:
        <input name="zip_code" value={formData.zip_code} onChange={handleChange} required />
      </label>

      <button type="submit">{editingTap ? "Update Tap" : "Add Tap"}</button>
    </form>
  );
};

export default TapForm;
