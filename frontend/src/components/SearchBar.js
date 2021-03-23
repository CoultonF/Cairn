import { Button } from '@material-ui/core';
import { styled } from '@material-ui/core/styles';
import { useState } from 'react'

const SearchBar = ({input:keyword, onChange:setKeyword, submit:handleSubmit}) => {
    const BarStyling = {height:'auto',width:"20rem",background:"#F2F1F9", border:"none", padding:"0.5rem", textalign:"left", display:"inline-block",margin:'0 auto 1rem auto'};
    const InlineStyling = {border:"none", display:"inline-block",  width:"100%", textalign:"center"};
    const OuterStyle = {textAlign:"center"};

    const MyButton = styled(Button)({
      background: 'linear-gradient(45deg, #32ab3e 30%, #169164 90%)',
      border: 0,
      color: 'white',
      height: '31px',
      padding: '0 30px'

    });

    return (
      <form onSubmit={handleSubmit} style={OuterStyle}>
      <input 
       style={BarStyling}
       key="random1"
       refs="searchBox"
       value={keyword}
       placeholder={"Search Trip Reports"}
       onChange={(e) => setKeyword(e.target.value)}
      />
      <MyButton onClick={handleSubmit}>Search</MyButton>
      </form>
    );
}

export default SearchBar