import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"/",
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>

    //     {/* new line start*/}
    //     <p>To get your profile details: </p><button onClick={getData}>Click me</button>
    //     {profileData && <div>
    //           <p>Profile name: {profileData.profile_name}</p>
    //           <p>About me: {profileData.about_me}</p>
    //         </div>
    //     }
    //      {/* end of new line */}
    //   </header>
    // </div>

    <div>
    <center>
    <h1>BFFR</h1><br></br>
    <ul>
	    <li><a href="https://bffr.atlassian.net/wiki/spaces/BFFR/pages/1671170/BFFR+Documentation">User Guide</a></li>
	    <li><a href="/profile.html">Profile</a></li>
	    <li><a href="/feed.html">Feed</a></li>
    </ul>
    <p>Hello World!</p>
    <input placeholder="Email"></input><br></br>
    <input placeholder="Password"></input><br></br>
    <button>Sign Up!</button>
    <br></br>
    <p>Already have an account? Log in</p></center>
    </div>


  );
}

export default App;
