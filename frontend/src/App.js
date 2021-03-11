import { useState } from 'react'
import Header from './components/Header'
import Hikes from './components/Hikes'
function App() {
    const [hikes, setHikes] = useState([
        {
            id: 1,
            text: 'South Lawson',
            date: ' Feb 5th 2019'
    
        },
        {
            id: 2,
            text: 'Mount Sarrail',
            date: ' May 5th 2019'
    
        },
        {
            id: 3,
            text: 'Mount Temple',
            date: ' Sep 5th 2015'
    
        },
    ])
  return (
    <div className="container">
      <Header title='Cairn' />
      <Hikes hikes={hikes}></Hikes>
    </div>
  );
}

export default App;
