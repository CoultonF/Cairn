import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Header from './components/Header'
import Hikes from './components/Hikes'
import SearchBar from './components/SearchBar'
import Container from '@material-ui/core/Container';

function App() {
    const [hikes, setHikes] = useState([])

    const getHikes=(arg)=>{
      fetch('/api/trip_reports?search=' + arg
      ,{
        headers : { 
          'Content-Type': 'application/json',
          'Accept': 'application/json'
         }
      }
      )
        .then(function(response){
          return response.json();
        })
        .then(function(myJson) {
          setHikes(myJson)
        });
    }
  

    const [input, setInput] = useState('');
  
    const updateInput = async (input) => {
       setInput(input);
    }

    const updateHikes = async (e) => {
      e.preventDefault();
      getHikes(input);
      console.log(input);
   }

  return (
    <Container maxWidth="sm">
      <Header></Header>
      <SearchBar input={input} onChange={updateInput} submit={updateHikes} ></SearchBar>
      <br></br>
      <Hikes hikes={hikes}></Hikes>
    </Container>
  );
}

export default App;
