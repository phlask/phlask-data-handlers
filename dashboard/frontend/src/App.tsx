import { useState } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import NavBar from './components/NavBar';
import TapForm, {TapFormProps} from './components/TapForm';
import { Tap } from './components/Tap';


const App = () => {
  const [dashboardVisible, setDashboardVisible] = useState(true);
  const [tapFormVisible, setTapFormVisible] = useState(false);

  const toggleDashboard = () => {
    setDashboardVisible(!dashboardVisible);
    setTapFormVisible(false);
  };

  const toggleTapForm = () => {
    setTapFormVisible(!tapFormVisible);
    setDashboardVisible(false);
  };
  const handleSubmit = async (data: Tap) => {
    // your code to handle form submission
  };

  return (
    <div className="App">
      <header className="App-header">
        <NavBar toggleDashboard={toggleDashboard} toggleTapForm={toggleTapForm} />
      </header>
      {dashboardVisible && <Dashboard />}
      {tapFormVisible && <TapForm onSubmit={handleSubmit} toggleTapForm={toggleTapForm} />}
    </div>
  );
};

export default App;
