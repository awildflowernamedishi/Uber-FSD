import './App.css';
import Login from './components/Login';
import NavBar from './components/NavBar';

function App() {
  const app_var = "App variable"
  return ( 
    
    <div className="app">
        <NavBar/>
        <Login />
    </div>
  );
}

export default App;